-- a script that prepares a MySQL server for the project
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- creating the user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grabting privillages
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_test'@'localhost';
-- granting select on performance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
