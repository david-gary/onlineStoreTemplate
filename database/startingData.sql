INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('aturing', 'b93727798b520dc10d145b53909c061f082ff14cd5f8cb4ab24c3b71bfa57d7e12e1296029be74c06a0d91ba32756f9fc978047fbe7232be67f94dfc1de9ced9', 'alan@enigma.com', 'Alan', 'Turing');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('dritchie', '67aff785bd17ac24448d491926ff7aadd8fa75e51a2f7a9bfc31889bad0adcd2989061a27ccd9eff9e5e31f2bc14b5c193727e116dc8dc48259acb3919171cd4', 'dennis@unix.com', 'Dennis', 'Ritchie');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('llamport', '9171d14954eeda4e70777c23d98e349818125cdaeb884ff97ebf8cc0a9c7778f54ce394256588148132a03ebea891e44077c659e6c0132fa87a8cf77e436ae11', 'leslie@paxos.com', 'Leslie', 'Lamport');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('bliskov', '1e4b9ae956cad1385cfa6fffd8323dd16c3fe18c54e6447e49bddef2138d042e84e1505a541c6ef19a5026e684b2559efd366145870a0a8d4d4173c0877f6cd2', 'barbara@thor.com', 'Barbara', 'Liskov');

INSERT into `inventory` (`item_name`, `info`, `image_url`, `category`, 'item_file', 'markdown_file', 'due_date', 'topics', 'difficulty')
VALUES ('Lab 0', 'Syntax Review', 'static/images/lab0_1.png', 'labs', 'static/labs/lab0.zip', 'static/markdown/lab0.md', 'n/a', 'Python, Java, Syntax', 'Easy');

INSERT into `inventory` (`item_name`, `info`, `image_url`, `category`, 'item_file', 'markdown_file', 'due_date', 'topics', 'difficulty')
VALUES ('Lab 1', 'Basic Development Environment Setup', 'static/images/lab1_1.png', 'labs', 'static/labs/lab1.zip', 'static/markdown/lab1.md', '01/18/2023', 'Python, Hello World, File Access', 'Easy');

INSERT into `inventory` (`item_name`, `info`, `image_url`, `category`, 'item_file', 'markdown_file', 'due_date', 'topics', 'difficulty')
VALUES ('Lab 2', 'Types and Built-in Functions in Python', 'static/images/lab2_1.jpg', 'labs', 'static/labs/lab2.zip', 'static/markdown/lab2.md', '01/25/2023', 'Python, Partner, Data Types, Hash', 'Easy');

INSERT into `inventory` (`item_name`, `info`, `image_url`, `category`, 'item_file', 'markdown_file', 'due_date', 'topics', 'difficulty')
VALUES ('Lab 3', 'Polygon Visualizer',  'static/images/lab3_1.png', 'labs', 'static/labs/lab3.zip', 'static/markdown/lab3.md', '01/26/2023', 'Python, Requirements, Graphics, pygame', 'Medium');

INSERT into `inventory` (`item_name`, `info`, `image_url`, `category`, 'item_file', 'markdown_file', 'due_date', 'topics', 'difficulty')
VALUES ('Lab 4', 'Git and Paired Programming', 'static/images/lab4_1.png', 'labs', 'static/labs/lab4.zip', 'static/markdown/lab4.md', '02/01/2023', 'Partner, Git, Github, Version Control', 'Hard');

INSERT into `inventory` (`item_name`, `info`, `image_url`, `category`, 'item_file', 'markdown_file', 'due_date', 'topics', 'difficulty')
VALUES ('Lab 5', 'Test-Driven Development', 'static/images/lab5_1.png', 'labs', 'static/labs/lab5.zip', 'static/markdown/lab5.md', '02/09/2023', 'Python, Unit Test', 'Hard');

INSERT into `inventory` (`item_name`, `info`, `image_url`, `category`, 'item_file', 'markdown_file', 'due_date', 'topics', 'difficulty')
VALUES ('Lab 6', 'Building a Flask Web Server', 'static/images/lab6_1.png', 'labs', 'static/labs/lab6.zip', 'static/markdown/lab6.md', '02/23/2023', 'Python, Flask, Web', 'Hard');

INSERT into `inventory` (`item_name`, `info`, `image_url`, `category`, 'item_file', 'markdown_file', 'due_date', 'topics', 'difficulty')
VALUES ('Lab 7', 'Automated Web Interactions with Selenium', 'static/images/lab7_1.png', 'labs', 'static/labs/lab7.zip', 'static/markdown/lab7.md', '03/09/2023', 'Python, Selenium, Web, Scraping', 'Medium');

INSERT into `inventory` (`item_name`, `info`, `image_url`, `category`, 'item_file', 'markdown_file', 'due_date', 'topics', 'difficulty')
VALUES ('Lab 8', 'Data Formats and Flow', 'static/images/lab8_1.png', 'labs', 'static/labs/lab8.zip', 'static/markdown/lab8.md', '03/23/2023', 'Python, Selenium, Web, Scraping, JSON, SQL', 'Medium');

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('1', 'aturing', '1', 10, '2022-12-21 7:30:30', 5.50);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('2', 'dritchie', '2', 10, '2022-12-21 7:30:30', 5.50);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('3', 'llamport', '3', 10, '2022-12-21 7:30:30', 5.50);
