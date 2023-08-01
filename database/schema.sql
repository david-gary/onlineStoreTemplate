CREATE TABLE food (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name VARCHAR(255) NOT NULL,
    info VARCHAR(255) NOT NULL,
    calorie INTEGER NOT NULL,
    protein INTEGER NOT NULL,
    carbs INTEGER NOT NULL,
    allergy VARCHAR(255) NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL
);

CREATE TABLE users (
    username VARCHAR(255) PRIMARY KEY NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL
);

CREATE TABLE logs (
    entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
    log_id VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    item_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    entry_date DATETIME NOT NULL,
    total_calorie INTEGER NOT NULL,
    total_protein INTEGER NOT NULL,
    total_carbs INTEGER NOT NULL,
    FOREIGN KEY (username) REFERENCES users(username),
    FOREIGN KEY (item_id) REFERENCES food(id)
);