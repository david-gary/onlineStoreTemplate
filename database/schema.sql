CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name VARCHAR(255) NOT NULL,
    info VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    stock INTEGER NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(255) PRIMARY KEY NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_id VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    item_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    sale_date DATETIME NOT NULL,
    cost DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username),
    FOREIGN KEY (item_id) REFERENCES inventory(id)
);

CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY,
    sale_id INTEGER NOT NULL,
    payment_status TEXT NOT NULL,
    amount REAL NOT NULL,
    payment_date DATE NOT NULL,
    FOREIGN KEY (sale_id) REFERENCES sales (sale_id)
);

