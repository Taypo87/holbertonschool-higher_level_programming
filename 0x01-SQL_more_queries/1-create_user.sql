-- creates new user, sets password and privileges

CREATE USER IF NOT EXISTS 'user-0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
