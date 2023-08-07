#!/usr/bin/env python3

from authentication.auth_tools import login_pipeline, update_passwords, hash_password
from flask import Flask, render_template, request
from admin_panel import admin_panel_bp
from core_info import sessions, db # Sessions and Database

app = Flask(__name__)
app.register_blueprint(admin_panel_bp) # Register blueprint to connect 'app.py' to 'admin_panel.py'
HOST, PORT = 'localhost', 8080
global username, products, db, sessions
username = 'default'
products = db.get_full_inventory()
sessions.add_new_session(username, db)


@app.route('/')
def index_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
    products = db.get_full_inventory() # Reload Inventory in case a new product was just added
    if username != 'default': # If a user is logged in, re-route to show home.html
        return render_template('home.html', username=username, products=products, sessions=sessions)
    return render_template('index.html', username=username, products=products, sessions=sessions)

@app.route('/about_us')
def about_us():
    """
    Renders the about us page when the user is at the `/about_us` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('about_us.html', username=username)


@app.route('/logout')
def logout():
    """
    Logout of an account and renders the index page

    args:
        - None

    returns:
        - None
    """
    global username
    products = db.get_full_inventory() # Reload Inventory in case a new product was just added
    if username == 'default':
        return render_template('index.html', username=username, products=products, sessions=sessions)
    else:
        username = 'default'
    return render_template('index.html', username=username, products=products, sessions=sessions)


@app.route('/login')
def login_page():
    """
    Renders the login page when the user is at the `/login` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('login.html', username=username)


@app.route('/home', methods=['POST'])
def login():
    """
    Renders the home page when the user is at the `/home` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds a new session to the sessions object

    """
    user = request.form['username']
    password = request.form['password']
    if login_pipeline(user, password):
        global username
        if (user not in sessions.get_all_sessions()): # Add new session only if session didn't already exist, to keep cart items even after log out 
            sessions.add_new_session(user, db)
        username = user # Set global username of new session

        if user == 'Admin':
            print(f"Special username logged in: {user}")
        return render_template('home.html', username=username, products=products, sessions=sessions)
    else:
        print(f"Incorrect username ({user}) or password ({password}).")
        return render_template('login.html', username=username, login_error=True)


@app.route('/register')
def register_page():
    """
    Renders the register page when the user is at the `/register` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('register.html', username=username)


@app.route('/register', methods=['POST'])
def register():
    """
    Renders the index page when the user is at the `/register` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - passwords.txt: adds a new username and password combination to the file
        - database/store_records.db: adds a new user to the database
    """
    username = request.form['username']
    # ERROR: Customers can't have 'admin' or 'default' in their username
    if 'admin' in username.lower() or 'default' in username.lower():
        return render_template('register.html', register_error=True)
    
    password = request.form['password']
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    salt, key = hash_password(password)
    update_passwords(username, key, salt)
    db.insert_user(username, key, email, first_name, last_name)
    return render_template('index.html')


@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Renders the checkout page when the user is at the `/checkout` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds items to the user's cart
    """
    order = {}
    user_session = sessions.get_session(username)
    for item in products:
        if request.form[str(item['id'])] > '0':
            count = request.form[str(item['id'])] # Get quantity inputted. Quantity text-bar: name={{product.id}}
            order[item['item_name']] = count
            user_session.add_new_item(
                item['id'], item['item_name'], item['price'], count)

    user_session.submit_cart()
    return render_template('checkout.html', sessions=sessions, total_cost=user_session.total_cost, cart=user_session.get_cart_with_quantity())


@app.route('/checkout-update', methods=['POST'])
def reload_checkout_page():
    """
    Renders the checkout page when the user is at the `/checkout` endpoint with a POST request.
    Update cart quantity or create a new sale, and renders the checkout page with new information.

    args:
        - None

    returns:
        - None

    modifies:
        - Update: Update quantity of an item in the user session's cart
        - New Sale: Create a new sale in the database and empties cart
    """
    user_session = sessions.get_session(username)
    cart = user_session.get_cart_with_quantity()
    if 'update_checkout' in request.form: # Updating quantity of product in checkout - button
        for item_id, item_info in cart.items():
            new_quantity = int(request.form[str(item_id)])
            user_session.update_item_quantity(item_id, new_quantity)
        print('Quantity updated')
        
    elif 'send_checkout' in request.form: # Create new sale - button
        transaction_id = db.get_new_sale_transaction_id()
        user_session.update_date()
        for item_id, item_info in cart.items():
            item_stock = db.get_item_stock_by_id(item_id)['stock']
            remaining_stock = item_stock - int(item_info['quantity'])
            if (remaining_stock >= 0): # Check if item's stock is enough
                db.insert_new_sale(transaction_id, username, item_id, item_info['quantity'], user_session.date, item_info['subtotal'])
                db.set_item_stock(item_id, remaining_stock)
            else:
                not_enough_stock = {}
                item_name = db.get_item_name_by_id(item_id)['item_name']
                not_enough_stock[item_id] = {'item_name': item_name, 'item_stock': item_stock}
                return render_template('checkout.html', sessions=sessions, not_enough_stock=not_enough_stock, total_cost=user_session.total_cost, cart=user_session.get_cart_with_quantity())
        user_session.reset_cart() # Reset cart in user session to be empty after a sale
        if len(cart.items()) == 0:
            print("Cart is empty.")
        else:
            print("Sales added")
    user_session.submit_cart() # Reset or Get total_cost - This needs to be here regardless of if statement outcome
    return render_template('checkout.html', sessions=sessions, sale_made=True, total_cost=user_session.total_cost, cart=user_session.get_cart_with_quantity())
        

@app.route('/orders', methods=['GET'])
def orders_page():
    """
    Renders the orders page when the user is at the `/orders` endpoint with a GET request.
    Create a table with the orders of the user. Show error if no user is not logged in.

    args:
        - None

    returns:
        - None

    modifies:
        - None
    """
    if username == 'default':
        return render_template('orders.html', username=username, no_user_error=True)
    else:
        sales = db.get_sales_by_username(username)
        print(sales)
        return render_template('orders.html', username=username, sales=sales)


@app.route('/admin_panel', methods=['POST'])
def admin_panel():
    """
    Renders the admin panel when the user is at the `/admin_panel` endpoint with a POST request and 
    is using the admin account.

    args:
        - None

    returns:
        - None

    modifies:
        - None
    """
    global username
    current_session = sessions.get_session(username)
    if 'Admin' == current_session.username:
        print("Admin verified: proceeding to Admin Panel")
        return render_template('admin_panel.html', sessions=sessions)
    return render_template('index.html', username=username, products=products, sessions=sessions)

if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
