INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('aturing', 'b93727798b520dc10d145b53909c061f082ff14cd5f8cb4ab24c3b71bfa57d7e12e1296029be74c06a0d91ba32756f9fc978047fbe7232be67f94dfc1de9ced9', 'alan@enigma.com', 'Alan', 'Turing');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('dritchie', '67aff785bd17ac24448d491926ff7aadd8fa75e51a2f7a9bfc31889bad0adcd2989061a27ccd9eff9e5e31f2bc14b5c193727e116dc8dc48259acb3919171cd4', 'dennis@unix.com', 'Dennis', 'Ritchie');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('llamport', '9171d14954eeda4e70777c23d98e349818125cdaeb884ff97ebf8cc0a9c7778f54ce394256588148132a03ebea891e44077c659e6c0132fa87a8cf77e436ae11', 'leslie@paxos.com', 'Leslie', 'Lamport');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('bliskov', '1e4b9ae956cad1385cfa6fffd8323dd16c3fe18c54e6447e49bddef2138d042e84e1505a541c6ef19a5026e684b2559efd366145870a0a8d4d4173c0877f6cd2', 'barbara@thor.com', 'Barbara', 'Liskov');

INSERT into `inventory` (`item_name`, `info`, `image_url`, `category`, 'item_file')
VALUES ('Lab 0', 'Syntax Review', 'static/images/lab0.jpg', 'labs', 'static/labs/lab0.zip');

INSERT into `inventory` (`item_name`, `info`, `image_url`, `category`, 'item_file')
VALUES ('Lab 1', 'Basic Development Environment Setup', 'static/images/lab1.jpg', 'labs', 'static/labs/lab1.zip');

INSERT into `inventory` (`item_name`, `info`, `image_url`, `category`, 'item_file')
VALUES ('Lab 2', 'Types and Built-in Functions in Python', 'static/images/lab2.jpg', 'labs', 'static/labs/lab2.zip');

INSERT into `inventory` (`item_name`, `info`, `image_url`, `category`, 'item_file')
VALUES ('Lab 3', 'Polygon Visualizer',  'static/images/lab3.jpg', 'labs', 'static/labs/lab3.zip');

INSERT into `inventory` (`item_name`, `info`, `image_url`, `category`, 'item_file')
VALUES ('Lab 4', 'Git and Paired Programming', 'static/images/lab4.jpg', 'labs', 'static/labs/lab4.zip');

INSERT into `inventory` (`item_name`, `info`, `image_url`, `category`, 'item_file')
VALUES ('Lab 5', 'Test-Driven Development', 'static/images/lab5.jpg', 'labs', 'static/labs/lab5.zip');

INSERT into `inventory` (`item_name`, `info`, `image_url`, `category`, 'item_file')
VALUES ('Lab 6', 'Building a Flask Web Server', 'static/images/lab6.jpg', 'labs', 'static/labs/lab6.zip');

INSERT into `inventory` (`item_name`, `info`, `image_url`, `category`, 'item_file')
VALUES ('Lab 7', 'Automated Web Interactions with Selenium', 'static/images/lab7.jpg', 'labs', 'static/labs/lab7.zip');

INSERT into `inventory` (`item_name`, `info`, `image_url`, `category`, 'item_file')
VALUES ('Lab 8', 'Data Formats and Flow', 'static/images/lab8.jpg', 'labs', 'static/labs/lab8.zip');

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('1', 'aturing', '1', 10, '2022-12-21 7:30:30', 5.50);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('2', 'dritchie', '2', 10, '2022-12-21 7:30:30', 5.50);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('3', 'llamport', '3', 10, '2022-12-21 7:30:30', 5.50);
