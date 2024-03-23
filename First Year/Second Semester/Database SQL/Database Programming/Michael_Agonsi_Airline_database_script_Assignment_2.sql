-- Create the database
CREATE DATABASE IF NOT EXISTS airline_database;

USE airline_database;

-- This creates the pilot table --
CREATE TABLE IF NOT EXISTS Pilot (
    FirstName VARCHAR(45) NOT NULL,
    LastName VARCHAR(45) NOT NULL,
    Passport VARCHAR(45) PRIMARY KEY,
    StreetNumber VARCHAR(10),
    StreetName VARCHAR(40),
    City VARCHAR(45),
    ProvOrState VARCHAR(45),
    Country VARCHAR(45),
    Code VARCHAR(10),
    DOB DATE
    
);

-- This create the airframe
CREATE TABLE IF NOT EXISTS Airframe (
    ID VARCHAR(10) NOT NULL PRIMARY KEY,
    AirRange INT NOT NULL,
    Seats INT NOT NULL,
    FuelCapacity INT NOT NULL,
    Make VARCHAR(45) NOT NULL,
    Model VARCHAR(45) NOT NULL,
    LastMaintenance DATE NOT NULL
);

-- This creates the route table
CREATE TABLE IF NOT EXISTS Route (
    ID VARCHAR(45) NOT NULL PRIMARY KEY,
    Depart VARCHAR(45) NOT NULL,
    Destination VARCHAR(45) NOT NULL
);

-- This creates the pilotcert table
CREATE TABLE IF NOT EXISTS PilotCert (
    ID INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    PilotID VARCHAR(45),
    AirframeID VARCHAR(10),
    FOREIGN KEY (PilotID) REFERENCES Pilot(Passport),
    FOREIGN KEY (AirframeID) REFERENCES Airframe(ID)
);


-- this creates the flight table
CREATE TABLE IF NOT EXISTS Flight (
    ID VARCHAR(10) NOT NULL PRIMARY KEY,
    RouteID VARCHAR(10),
    AirframeID VARCHAR(10),
    Depart DATETIME NOT NULL,
    Duration TIME NOT NULL,
    PilotID VARCHAR(45),
    FuelAtDep VARCHAR(45) NOT NULL,
    FOREIGN KEY (RouteID) REFERENCES Route(ID),
    FOREIGN KEY (AirframeID) REFERENCES Airframe(ID),
    FOREIGN KEY (PilotID) REFERENCES Pilot(Passport)
);


-- this creates the passenger table
CREATE TABLE IF NOT EXISTS Passenger (
    FirstName VARCHAR(45) NOT NULL,
    LastName VARCHAR(45) NOT NULL,
    Passport VARCHAR(45) NOT NULL PRIMARY KEY,
    StreetNumber VARCHAR(10),
    StreetName VARCHAR(45),
    City VARCHAR(45),
    ProvOrState VARCHAR(45),
    Country VARCHAR(45),
    Code VARCHAR(10),
    DOB DATE,
    FlightID VARCHAR(10),
    FOREIGN KEY (FlightID) REFERENCES Flight(ID)
);


-- The code below inserts all the required data for the assignment--
insert into Pilot values 
('Emi', 'Misdirected', 'CA00001', '20', 'Polina Road', "St. John's", 'NL','CA', '403','1988-04-19');

insert into Airframe values 
('PAL241',20000,245, 40000, 'Boeing', '737 Max', '2014-09-23'),
('PAL242',45000,350, 70000, 'Airbus', 'A340', '2019-10-11');

insert into PilotCert values 
(1, 'CA00001', 'PAL241');

insert into Route values
('YYT-YYZ', "St. John's International Airport", "Toronto-Pearson Airport");

insert into Flight values
('A1', 'YYT-YYZ', 'PAL241', '2024-04-01 06:00', '04:30', 'CA00001', '38000');

insert into Passenger values
('Michael', 'Agonsi', 'A3410567', '30', 'Diana Road', "St. John's", 'NL', 'CA', '709', '2000-04-19', 'A1');



