INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('aturing', 'b93727798b520dc10d145b53909c061f082ff14cd5f8cb4ab24c3b71bfa57d7e12e1296029be74c06a0d91ba32756f9fc978047fbe7232be67f94dfc1de9ced9', 'alan@enigma.com', 'Alan', 'Turing');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('dritchie', '67aff785bd17ac24448d491926ff7aadd8fa75e51a2f7a9bfc31889bad0adcd2989061a27ccd9eff9e5e31f2bc14b5c193727e116dc8dc48259acb3919171cd4', 'dennis@unix.com', 'Dennis', 'Ritchie');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('llamport', '9171d14954eeda4e70777c23d98e349818125cdaeb884ff97ebf8cc0a9c7778f54ce394256588148132a03ebea891e44077c659e6c0132fa87a8cf77e436ae11', 'leslie@paxos.com', 'Leslie', 'Lamport');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('bliskov', '1e4b9ae956cad1385cfa6fffd8323dd16c3fe18c54e6447e49bddef2138d042e84e1505a541c6ef19a5026e684b2559efd366145870a0a8d4d4173c0877f6cd2', 'barbara@thor.com', 'Barbara', 'Liskov');

INSERT into `users` (`username`, `password_hash`, `email`, `first_name`, `last_name`)
VALUES ('Admin', 'f90747b096a0bb34bcae8ed0b623367ac42aac304853f446957b37314a2c07606b7c292dfc9e1e672cec634365b02f863bfd9b9217c44f8756366da2994955a4', 'admin@gmail.com', 'Admin', 'Admin');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('A Little Life', 'A novel by Hanya Yanagihara following the lives of four friends, grappling with love, trauma, and resilience, while one carries a haunting past.', 14.99, 49, 'static/books/a_little_life.jpg', 'Literary fiction');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('American Prometheus', 'Kai Bird and Martin J. Sherwin"s biography explores the life of physicist J. Robert Oppenheimer, his scientific achievements, controversies, and tragedies.', 22.49, 26, 'static/books/american_prometheus.jpg', 'Biography');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('Archers Voice', 'Mia Sheridan"s heartwarming romance about Archer Hale, a mute man haunted by his past, and Bree Prescott, who brings healing and love into his life.', 30.00, 28, 'static/books/archers_voice.jpg', 'Romance fiction');

INSERT into `inventory` (`item_name`, `info`, `price`, `stock`, `image_url`, `category`)
VALUES ('House of Earth and Blood', 'Sarah J. Maas"s captivating fantasy follows Bryce Quinlan and Hunt Athalar as they seek justice in a city of intrigue.', 16.99, 34, 'static/books/house_of_earth_and_blood.jpg', 'Fantasy fiction');

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('c8c1d', 'aturing', '1', 2, '2022-12-27 7:30:30', 31.48);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('3f1e2', 'dritchie', '2', 3, '2021-11-17 7:30:30', 70.84);

INSERT into `sales` (`transaction_id`, `username`, `item_id`, `quantity`, `sale_date`, `cost`)
VALUES ('b4d7r', 'llamport', '3', 1, '2020-12-13 7:30:30', 31.50);
