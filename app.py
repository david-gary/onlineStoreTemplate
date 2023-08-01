#!/usr/bin/env python3

from authentication.auth_tools import login_pipeline, update_passwords, hash_password
from database.db import Database
from flask import Flask, render_template, request
from core.session import Sessions

app = Flask(__name__)
HOST, PORT = 'localhost', 8080
global username, products, db, sessions
username = 'default'
db = Database('database/store_records.db')
products = db.get_full_inventory()
sessions = Sessions()
sessions.add_new_session(username, db)
wallets = db.get_all_wallets()

@app.route('/')
def index_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
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
    return render_template('login.html')


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
    global username
    username = request.form['username']
    password = request.form['password']
    if login_pipeline(username, password):
        sessions.add_new_session(username, db)
        db.create_wallet(username, 0)
        return render_template('home.html', products=products, sessions=sessions, username=username)
    else:
        print(f"Incorrect username ({username}) or password ({password}).")
        username = 'default'
        return render_template('index.html', products=products, sessions=sessions, username=username)

@app.route('/home', methods=['GET'])
def home():
    return render_template("home.html",products=products, sessions=sessions, username=username)

@app.route('/register')
def register_page():
    """
    Renders the register page when the user is at the `/register` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('register.html')


@app.route('/admin')
def admin_page():
    """
    Renders the admin page when the user is at the `/admin` endpoint.

    args:
        - None

    returns:
        - None
    """
    auth_level = sessions.get_session(username).auth_level
    auth_level = 1 # Not good security
    if auth_level == 0: #The user does not have admin privelages
        return render_template('admin.html', message = "Access Denied. Not authorized to access this page.", username=username, products=[], sessions=sessions, auth_level=auth_level)
    elif auth_level == 1:
        return render_template("admin.html", message = "Product Management", username=username, products=products, sessions=sessions, auth_level=auth_level)

@app.route('/admin',methods=['POST'])
def admin():
    """
    Sets the price of the products after price selection
    """
    
    global products
    
    for product in products:
        price_string = request.form[str(product['id'])]
        try:
            new_price = float(price_string)
            db.set_item_price(product['id'], new_price)
        except ValueError: #No new value was passed
            pass
        
    products = db.get_full_inventory()
    return render_template('admin.html', message='Your changes have been saved.')
        

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
    password = request.form['password']
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    salt, key = hash_password(password)
    update_passwords(username, key, salt)
    if db.get_email_by_username(username) != None: # A user does not already exist with that username
        db.insert_user(username, key, email, first_name, last_name)
    else:
        print(f"A user already exists with the username {username}")
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
        print(f"item ID: {item['id']}")
        if request.form[str(item['id'])] > '0':
            count = request.form[str(item['id'])]
            order[item['item_name']] = count
            user_session.add_new_item(
                item['id'], item['item_name'], item['price'], count)

    if db.get_wallet_amount_username(username)[0]['amount'] > user_session.total_cost:
        user_session.submit_cart()
        db.increment_wallet_by_username(username, -1 * user_session.total_cost)
        return render_template('checkout.html', order=order, sessions=sessions, total_cost=user_session.total_cost)
    else:
        return render_template('checkout.html', order=order, sessions=sessions, total_cost="  - Purchase failed due to not enough funds.") 

@app.route("/wallet", methods=['GET'])
def wallet():
    """
    Renders the wallet page when the user is at the `/wallet` endpoint with a GET request.

    args:
        - None

    returns:
        - None

    modifies:
        - None

    """
    # Add wallet logic here
    wallet_amount_json = db.get_wallet_amount_username(username)
    if len(wallet_amount_json) > 0:
        wallet_amount = wallet_amount_json[0]['amount']
    else:
        wallet_amount=0
    # Render wallet.html
    return render_template('wallet.html',balance=wallet_amount, username=username)

@app.route("/wallet", methods=['POST'])
def wallet_increment():
    db.increment_wallet_by_username(username, 10)
    wallet_amount_json = db.get_wallet_amount_username(username)
    wallet_amount = wallet_amount_json[0]['amount']
    return render_template('wallet.html',balance=wallet_amount, username=username)

if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
