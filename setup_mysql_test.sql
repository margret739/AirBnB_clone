-- Creates a MySQL server with:
-- Database hbnb_test_db.
-- User hbnb_test with password hbnb_test on hbnb_test_db
-- GRANT all privileges for hbnb_test on hbnb_test_db.
-- GRANT SELECT privilege for hbnb_test on performance_schema.


-- Create the databse if it doesn't exist
CREATE DATABSE IF NOT EXISTS hbnb_test_db;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on hbnb_test_db to hbnb_test
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

--Flush privileges to apply changes
FLUSH PRIVILEGES;
