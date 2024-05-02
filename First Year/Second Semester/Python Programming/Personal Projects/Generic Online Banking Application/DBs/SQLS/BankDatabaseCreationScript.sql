DROP DATABASE IF EXISTS bankdb;
-- CREATES THE BANK DATABASE
create database if not exists bankdb;

use bankdb;

-- CREATES THE CUSTOMER TABLE
DROP TABLE IF EXISTS `Customer` ;

CREATE TABLE IF NOT EXISTS `Customer` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `FirstName` VARCHAR(45) NOT NULL,
  `LastName` VARCHAR(45) NOT NULL,
  `Gender` VARCHAR(45) NOT NULL,
  `DOB` DATE NOT NULL,
  `RelationshipStatus` VARCHAR(45) NOT NULL,
  `PhoneNumber` VARCHAR(45) NOT NULL,
  `StateOfOrigin` VARCHAR(45) NOT NULL,
  `CountryOfOrigin` VARCHAR(45) NOT NULL,
  `HouseAddress` VARCHAR(45) NOT NULL,
  `Town_City` VARCHAR(45) NOT NULL,
  `CountryOfResidence` VARCHAR(45) NOT NULL,
  `PostalCode` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`)
  )
ENGINE = InnoDB;


CREATE UNIQUE INDEX `ID_UNIQUE` ON `Customer` (`ID` ASC) VISIBLE;


-- CREATES THE ACCOUNT TYPE TABLE FOR REFERENCES

DROP TABLE IF EXISTS `AccountType` ;

CREATE TABLE IF NOT EXISTS `AccountType` (
  `ID` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;



-- CREATES THE ONLINE BANKING ACCOUNT TABLE

DROP TABLE IF EXISTS `OnlineBankingAcct` ;

CREATE TABLE IF NOT EXISTS `OnlineBankingAcct` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `Email` VARCHAR(40) NOT NULL,
  `Password` VARCHAR(100) NOT NULL,
  `customerID`INT NOT NULL,
  
  PRIMARY KEY (`ID`),
  CONSTRAINT cust_onlinebankID_fk 
  foreign key (`customerID`) references `Customer`(`ID`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `Email_UNIQUE` ON `OnlineBankingAcct` (`Email` ASC) VISIBLE;


-- CREATES THE ACCOUNTS TABLE


DROP TABLE IF EXISTS `Accounts` ;

CREATE TABLE IF NOT EXISTS `Accounts` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `OnlineBankingAcct_ID` INT NULL,
  `Customer_ID` INT NOT NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `fk_Accounts_OnlineBankingAcct1`
    FOREIGN KEY (`OnlineBankingAcct_ID`)
    REFERENCES `OnlineBankingAcct` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Accounts_Customer1`
    FOREIGN KEY (`Customer_ID`)
    REFERENCES `Customer` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Accounts_OnlineBankingAcct1_idx` ON `Accounts` (`OnlineBankingAcct_ID` ASC) VISIBLE;

CREATE INDEX `fk_Accounts_Customer1_idx` ON `Accounts` (`Customer_ID` ASC) VISIBLE;



-- CREATES THE ACCOUNT TABLE

DROP TABLE IF EXISTS `Account` ;

CREATE TABLE IF NOT EXISTS `Account` (
  `AccountNumber` INT NOT NULL AUTO_INCREMENT,
  `Balance` INT NOT NULL,
  `Active` TINYINT NOT NULL,
  `AccountType_ID` INT NOT NULL,
  `Accounts_ID` INT NOT NULL,
  PRIMARY KEY (`AccountNumber`),
  CONSTRAINT `fk_Account_AccountType1`
    FOREIGN KEY (`AccountType_ID`)
    REFERENCES `AccountType` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Account_Accounts1`
    FOREIGN KEY (`Accounts_ID`)
    REFERENCES `Accounts` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Account_AccountType1_idx` ON `Account` (`AccountType_ID` ASC) VISIBLE;

CREATE INDEX `fk_Account_Accounts1_idx` ON `Account` (`Accounts_ID` ASC) VISIBLE;



-- CREATES THE TRANSACTION TABLE

DROP TABLE IF EXISTS `Transaction` ;

CREATE TABLE IF NOT EXISTS `Transaction` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `accountID` INT NOT NULL,
  `type` VARCHAR(10) NOT NULL,
  `Amount` INT NOT NULL,
  `DateAndTime` DATE NOT NULL,
  `FromBankName` VARCHAR(45) NOT NULL,
  `FromName` VARCHAR(45) NOT NULL,
  `FromAccountNumber` VARCHAR(45) NOT NULL,
  `ToBankName` VARCHAR(45) NOT NULL,
  `ToName` VARCHAR(45) NOT NULL,
  `ToAccountNumber` VARCHAR(45) NOT NULL,
  `Status` VARCHAR(45) NOT NULL,
  `Account_AccountNumber` INT NOT NULL,
  PRIMARY KEY (`ID`, `Account_AccountNumber`),
  CONSTRAINT `fk_Transaction_Account1`
    FOREIGN KEY (`Account_AccountNumber`)
    REFERENCES `Account` (`AccountNumber`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Transaction_Account1_idx` ON `Transaction` (`Account_AccountNumber` ASC) VISIBLE;


-- INSERTS REQUIRED VALUES FOR THE ACCOUNT TYPE TABLE
USE bankdb;
INSERT INTO accounttype VALUES (1,'CHEQUING');
INSERT INTO accounttype VALUES (2, 'SAVINGS');
INSERT INTO accounttype VALUES (3, 'INVESTMENT');

-- CREATES THE TRIGGER FOR CREATING FINANCIAL ACCOUNT ONCE A NEW CUSTOMER IS ADDED TO THE BANK DEFAULT IS CHEQUINGS ACCOUNT CREATION
drop trigger if exists create_financial_account;

delimiter //
create trigger create_financial_account
	after insert on Customer
	for each row
BEGIN

	declare accountsid int;
	declare customer_id int;
	declare onlinebankid int;
	declare account_number int;
	
	select ID into customer_id from Customer where ID = new.ID;
	set accountsid = FLOOR(RAND() * (9999 - 1000 + 1)) + 1000;
	set account_number = concat(accountsid,'',FLOOR(RAND() * (9999 - 1000 + 1)) + 1000);
	
	insert into Accounts (ID,OnlineBankingAcct_ID,Customer_ID) values (accountsid,Null,customer_id);
	insert into Account values (account_number,0,True,1,accountsid);
END //

delimiter ;

-- CREATES THE TRIGGER FOR CREATING ONLINE BANKING ACCOUNT ONCE A NEW ONLINE ACCOUNT INFORMATION IS INSERTED TO THE ONLINE BANK ACCOUNT TABLE

drop trigger if exists create_online_account;

delimiter //
create trigger create_online_account
	after insert on onlinebankingacct
	for each row
BEGIN

	
	declare customer_id int;
	declare onlinebankid int;
    declare accountsid int;
	
    select customerID into customer_id from onlinebankingacct where ID = new.ID;
	select ID into accountsid from accounts where Customer_ID = customer_id;
    select ID into onlinebankid from onlinebankingacct where ID = new.ID;
	
	
	
	update Accounts set OnlineBankingAcct_ID = onlinebankid where ID = accountsid;
	
END //

delimiter ;

