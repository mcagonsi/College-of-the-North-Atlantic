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
  `Balance` DECIMAL(9,2) NOT NULL,
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
  `Amount` DECIMAL(9,2) NOT NULL,
  `DateAndTime` DATE NOT NULL,
  `FromBankName` VARCHAR(45) NOT NULL,
  `FromName` VARCHAR(45) NOT NULL,
  `FromAccountNumber` VARCHAR(45) NOT NULL,
  `ToBankName` VARCHAR(45) NOT NULL,
  `ToName` VARCHAR(45) NOT NULL,
  `ToAccountNumber` VARCHAR(45) NOT NULL,
  `Status` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`, `accountID`),
  CONSTRAINT `fk_Transaction_Account1`
    FOREIGN KEY (`accountID`)
    REFERENCES `Account` (`AccountNumber`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_Transaction_Account1_idx` ON `Transaction` (`accountID` ASC) VISIBLE;


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

-- CREATES THE CUSTOMER_ACCOUNTS_ACCOUNT VIEW 
drop view if exists Customer_Accounts_Account;

CREATE VIEW Customer_Accounts_Account AS
SELECT customer.ID ,customer.LastName, customer.PhoneNumber, accounts.ID as accounts_id, accounts.OnlineBankingAcct_ID, account.AccountNumber, account.AccountType_ID, account.Active
FROM accounts 
join account on accounts.id = account.Accounts_ID
join customer on accounts.Customer_ID = customer.ID;

-- CREATES THE TRIGGER TO CLOSE CUSTOMER ACCOUNT AND DELETE CUSTOMER FROM THE DATABASE IF CUSTOMER WISHES TO CLOSE ACCOUNT


drop trigger if exists close_customer_account;

delimiter //
create trigger close_customer_account
	before delete on customer
	for each row
BEGIN

	
	declare customer_id int;
	declare onlinebankid int default null;
    declare accountsid int;
    declare counter int default 1;
    declare accountNumber int;
    
	
    select ID into customer_id from customer where ID = old.ID;
	select accounts_id into accountsid from customer_accounts_account where ID = customer_id;
    select OnlineBankingAcct_ID into onlinebankid from customer_accounts_account where ID = customer_id;
    
    delete from account where Accounts_ID = accounts_id and AccountType_ID =1;
    delete from account where Accounts_ID = accounts_id and AccountType_ID =2;
    delete from account where Accounts_ID = accounts_id and AccountType_ID =3;
    
    delete from accounts where ID = accountsid;
    
    
    IF onlinebankid is not null then
		delete from onlinebankingacct where ID = onlinebankid;
	END IF;
	
END //

delimiter ;

-- CREATES A TRIGGER TO GENERATE AN ACCOUNT NUMBER WHEN A NEW FINANCE ACCOUNT(INVESTMENT OR SAVINGS) IS CREATED FOR A CUSTOMER

drop trigger if exists generate_account_number;

delimiter //
create trigger generate_account_number
	before insert on account
	for each row
BEGIN

    declare account_number int;
    
	set account_number = concat(new.accounts_id,'',FLOOR(RAND() * (9999 - 1000 + 1)) + 1000);
    set new.accountNumber = account_number;
	
END //

delimiter ;

-- CREATES THE TRIGGER FOR ALL DEPOSIT TRANSACTIONS TO RECORD INTO THE DATABASE


drop trigger if exists deposit_into_account;

delimiter //
create trigger deposit_into_account
	before insert on transaction
	for each row
BEGIN
	declare accountName varchar(10);
    declare accttype int;
    
    
    select AccountType_ID into accttype from customer_accounts_account where AccountNumber = new.ToAccountNumber;
    select Name into accountName from AccountType where ID = accttype;
    
	if new.Type = 'DEPOSIT' THEN
		set new.accountID = new.ToAccountNumber;
        set new.Status = 'SUCCESSFUL';
        set new.DateAndTime = current_timestamp();
        set new.FromBankName = 'N/A';
        set new.FromAccountNumber = 'N/A';
        set new.ToBankName = 'CUSTOMER';
        set new.ToName = accountName;
	end if;
END //

delimiter ;

-- CREATES THE TRIGGER FOR ALL WITHDRAWAL TRANSACTION TO RECORD INTO THE DATABASE

drop trigger if exists withdraw_from_account;

delimiter //
create trigger withdraw_from_account
	before insert on transaction
	for each row
BEGIN
	declare accountName varchar(10);
    declare accttype int;
    
    
    select AccountType_ID into accttype from customer_accounts_account where AccountNumber = new.FromAccountNumber;
    select Name into accountName from AccountType where ID = accttype;
    
	if new.Type = 'WITHDRAWAL' THEN
		set new.accountID = new.FromAccountNumber;
        set new.Status = 'SUCCESSFUL';
        set new.DateAndTime = current_timestamp();
        set new.ToBankName = 'N/A';
        set new.ToAccountNumber = 'N/A';
        set new.FromBankName = 'CUSTOMER';
        set new.FromName = accountName;
	end if;
END //

delimiter ;
