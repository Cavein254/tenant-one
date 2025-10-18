-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS tenants CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'myuser'@'%' IDENTIFIED BY 'mysuperpassword';

-- Grant privileges on the database
GRANT ALL PRIVILEGES ON tenants.* TO 'myuser'@'%';

-- Apply changes
FLUSH PRIVILEGES;