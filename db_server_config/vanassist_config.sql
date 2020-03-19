CREATE DATABASE vanassist;
USE vanassist;
DROP USER IF EXISTS admin;
CREATE USER 'admin'@'%' IDENTIFIED BY 'vanassist';
GRANT ALL PRIVILEGES ON vanassist.* TO 'admin'@'%';
FLUSH PRIVILEGES;