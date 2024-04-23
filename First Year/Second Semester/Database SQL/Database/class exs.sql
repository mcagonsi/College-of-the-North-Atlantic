-- This creates the employee table
CREATE TABLE IF NOT EXISTS employee (
    FirstName VARCHAR(20) NOT NULL,
    LastName VARCHAR(20) NOT NULL,
    Role VARCHAR(20) NOT NULL,
    Phone VARCHAR(15) NOT NULL PRIMARY KEY,
    Office VARCHAR(10),
    Ext INT NOT NULL PRIMARY KEY
    
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
    FOREIGN KEY (PetId) REFERENCES pet(ID),
    FOREIGN KEY (VetPhone) REFERENCES employee(Phone),
    FOREIGN KEY (VetExt) REFERENCES employee(Ext)
);

drop database Quiz;