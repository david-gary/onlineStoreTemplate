# P3 Implementation Changelog

## **Changes by Alberto**
### Website:

- **REQ-1:** Added Homepage navbar with home button to redirect to homepage - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/18caea8cbcf944fd41e9b9a98fd1623d5565908e) - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/370521892db1ca19dc27f95c0b657920d2da17db) - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/0208311f4df315586c961a88ccda8a430d727032)
- **REQ-2:** Users can register account into the database and login - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/9072eacd0b405eebb15afbdb7c6357a643ff2616) - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/9072eacd0b405eebb15afbdb7c6357a643ff2616)
- **REQ-3:** Users have their cart saved even after logging out - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/1d6dc85768a670a6f7f3af8e7404e2b336209318)
- **REQ-4:** Customers can now add products to the shopping cart and view the content - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/238ba64e30c9bc58f8ff03d8792e8e08b91e144f)
- **REQ-5:** `Admin Panel` added to manage some database functions. Only accessible through admin login - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/7696795c4466f83ee2be3e97e6510c5d14c7202d) - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/9f6f53fca778f01a1dee26c16d15a982e1f17028) - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/07e4b425f239c1ac5c1d221a535feda6e2512cfc) - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/7696795c4466f83ee2be3e97e6510c5d14c7202d)
- **REQ-6:** Customers can checkout product in the index page, but needs to have an account to checkout - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/b96975418ae36ef286ce214c9c54ddfb7066cafc)
- **REQ-7:** Items are displayed neatly with name, image, info and price - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/a9f203fced50599f64ee3ad2aa8e51ccc65529a1) - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/441ed3288de037ea8bcedc3eafb43a85aafa807f) - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/441ed3288de037ea8bcedc3eafb43a85aafa807f)
- **REQ-8:** Database storing inventory, sales and users' informations - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/545671b11dc075284acd5c714f931c56a2249de1) - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/a9f203fced50599f64ee3ad2aa8e51ccc65529a1) - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/0a0933441cafe76ac1258b12cb1671568431b363)
- **REQ-9:** Added items stock function to keep track of items available, can't buy items if not enough in stock warning - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/789a41d5e2b3bb15d3d537a150a13fb8eeba81dc) 
- **REQ-10:** Checkout page will now show total cost of the order - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/238ba64e30c9bc58f8ff03d8792e8e08b91e144f) - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/b76f8b0f67809ad985299cf0dce4e4e627a1d05f)
- **REQ-11:** Admin Panel will now allow admin to update products information - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/07e4b425f239c1ac5c1d221a535feda6e2512cfc)
- **REQ-12:** Admin Panel will now allow admin to add products to database  - [COMMIT](https://github.com/olivialba/onlineStoreTemplate/commit/7696795c4466f83ee2be3e97e6510c5d14c7202d)
- Added Header
- Added Logout
- Added Order Page table to see a user's past orders
- Added Users can update quantity of items at checkout
- Changed overall CSS style of the Website
- Changed Login and Register buttons

### Admin Panel:
- Bookstoremanager login will show an Admin panel, the panel is defined in 'admin_panel.html' and 'admin_panel.py'
- Bookstoremanager login info: 
  - Username: `Admin`
  - Password: `Admin`

### Fixed Bugs:
- Prevent: users can't register with 'default' or 'admin' in their username, to prevent bugs
- Fixed: login users didn't change session to their new login
- Fixed: customers can't login if username or password invalid
- Fixed: incorrect and uneven css style for login and register .html pages
- Fixed: Incorrect backend for login-logout
- Fixed: Users now keep their cart saved even after logging out
