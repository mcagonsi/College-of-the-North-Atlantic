create database if not exists Quiz;

use Quiz;

-- This creates the client table
CREATE TABLE IF NOT EXISTS client (
    FirstName VARCHAR(20) NOT NULL ,
    LastName VARCHAR(20) NOT NULL,
    Phone VARCHAR(15) NOT NULL PRIMARY KEY,
    Email VARCHAR(45)
);


-- This creates the employee table
CREATE TABLE IF NOT EXISTS employee (
	Ext INT UNIQUE NOT NULL ,
    Phone VARCHAR(15) NOT NULL,
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    Role VARCHAR(20) NOT NULL,
    Office VARCHAR(10),
    CONSTRAINT employee_pk PRIMARY KEY (Ext,Phone)
    
    
);

-- this creates the pet table
CREATE TABLE IF NOT EXISTS pet(
    Name VARCHAR(20) NOT NULL,
    Species VARCHAR(20) NOT NULL,
    DOB DATE NOT NULL,
    Chipped INT,
    Owner VARCHAR(15),
    ID INT NOT NULL PRIMARY KEY,
    FOREIGN KEY (Owner) REFERENCES client(Phone)

);


-- this creates the appointment table
CREATE TABLE IF NOT EXISTS appointment (
    Start DATETIME NOT NULL PRIMARY KEY,
    Room VARCHAR(15) NOT NULL,
    PetId INT NOT NULL,
    VetPhone VARCHAR(15),
    VetExt INT,
    CONSTRAINT Pet_App_FK FOREIGN KEY (PetId) REFERENCES pet(ID),
    FOREIGN KEY (VetExt,VetPhone) REFERENCES employee(Ext,Phone)
	

);







