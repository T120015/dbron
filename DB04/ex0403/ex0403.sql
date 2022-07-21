CREATE DATABASE if NOT EXISTS dbron04;
USE dbron04;
DROP TABLE if EXISTS meibo;
CREATE TABLE meibo(
	meiboID INT NOT NULL AUTO_INCREMENT ,
	namae VARCHAR(30),
	yomi VARCHAR(50),
	spec FLOAT,
	wcnt INT,
	lastupdate DATETIME,
	PRIMARY KEY(meiboID)
);
SHOW TABLES;
DESC meibo;
