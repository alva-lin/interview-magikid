-- Create the database
CREATE DATABASE IF NOT EXISTS your_database_name;

-- Use the database
USE your_database_name;

-- Create the table
CREATE TABLE IF NOT EXISTS user (
  uid INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(255),
  gender ENUM('MALE', 'FEMALE')
);
