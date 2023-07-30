from database.db import Database

database = Database('database/store_records.db')

products = database.get_full_inventory()

def main():
    done = False
    while not done:
        print("""
1) List items
2) Delete item
3) Add new item
4) Quit
""")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            for product in products:
                print(f"Item id: {product['id']}, item_name: {product['item_name']}, info: {product['info']}, price: ${product['price']}, stock: {product['stock']}, image_url: {product['image_url']}")
                print("\n")
            highest_id = product['id']

        elif choice == 2:
            item_name = input("Enter the item name: ")
            item_info = input("Enter the item info: ")
            item_price = int(input("Enter the item price (No decimal points): ").replace("$",""))
            item_image_url = input("Enter the item image url (such as static/images/mango.jpeg): ")
            database.insert_new_item(item_name, item_price, item_info)
            new_id = int(database.get_all_item_ids()[len(database.get_all_item_ids())-1]['id'])
            database.set_item_image_url(new_id, item_image_url)

        elif choice == 3:
            print("Not yet implemented.")
        elif choice == 4:
            print("Quitting...")
            done = True

if __name__ == "__main__":
    main()
        
