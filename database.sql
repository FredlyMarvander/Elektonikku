CREATE DATABASE elektronikku

CREATE TABLE Users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255),
  email VARCHAR(255),
  password VARCHAR(255),
  role VARCHAR(255),
  balance INT
);

CREATE TABLE Carts (
  id INT AUTO_INCREMENT PRIMARY KEY,
  transactionDate DATE,
  userId INT,

  CONSTRAINT fk_cart_user
    FOREIGN KEY (userId)
    REFERENCES Users(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE CartDetails (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  price INT,
  quantity INT,
  cartId INT,

  CONSTRAINT fk_cart_details_cart
    FOREIGN KEY (cartId)
    REFERENCES Carts(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);


CREATE TABLE Products (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  description VARCHAR(255),
  price INT,
  stock INT,
  user_id INT,

  CONSTRAINT fk_user
    FOREIGN KEY (user_id)
    REFERENCES Users(id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);



###########################################################
INSERT INTO Users (username, email, password, role, balance)
VALUES
(
  'admin',
  'admin@gmail.com',
  'admin123',
  'admin',
  0
);


INSERT INTO Users (username, email, password, role, balance)
VALUES
  (
    'farhan92',
    'farhan92@gmail.com',
    'farhan2007',
    'customer',
    150000
  );
######################################################