create table Customer (
 `ID` INT NOT NULL ,
  `FirstName` VARCHAR(45) NOT NULL,
  `LastName` VARCHAR(45) NOT NULL,
  `DOB` DATE NOT NULL,
  `RelationshipStatus` VARCHAR(45) NOT NULL,
  `PhoneNumber` VARCHAR(45) NOT NULL,
  `StateOfOrigin` VARCHAR(45) NOT NULL,
  `CountryOfOrigin` VARCHAR(45) NOT NULL,
  `HouseAddress` VARCHAR(45) NOT NULL,
  `Town_City` VARCHAR(45) NOT NULL,
  `CountryOfResidence` VARCHAR(45) NOT NULL,
  `PostalCode` VARCHAR(45) NOT NULL,
  `OnlineBankingAcct_ID` INT NOT NULL,
  PRIMARY KEY (`ID`));
  
  create table AccountType (
  `ID` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`));
  
  create table OnlineBankingAcct (
  `ID` INT NOT NULL ,
  `Email` VARCHAR(40) NOT NULL,
  `Password` VARCHAR(100) NOT NULL,
  `customerID`INT NOT NULL,
  
  PRIMARY KEY (`ID`),
  CONSTRAINT cust_onlinebankID_fk 
  foreign key (`customerID`) references `Customer`(`ID`));
  
  create table Accounts (
   `ID` INT NOT NULL,
  `OnlineBankingAcct_ID` INT NOT NULL,
  `Customer_ID` INT NOT NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `fk_Accounts_OnlineBankingAcct1`
    FOREIGN KEY (`OnlineBankingAcct_ID`)
    REFERENCES `OnlineBankingAcct` (`ID`),
  CONSTRAINT `fk_Accounts_Customer1`
    FOREIGN KEY (`Customer_ID`) REFERENCES `Customer` (`ID`));
	
create table Account (
  `AccountNumber` INT NOT NULL,
  `Balance` INT NOT NULL,
  `Active` TINYINT NOT NULL,
  `AccountType_ID` INT NOT NULL,
  `Accounts_ID` INT NOT NULL,
  PRIMARY KEY (`AccountNumber`),
  CONSTRAINT `fk_Account_AccountType1`
    FOREIGN KEY (`AccountType_ID`)
    REFERENCES `AccountType` (`ID`),
  CONSTRAINT `fk_Account_Accounts1`
    FOREIGN KEY (`Accounts_ID`) REFERENCES `Accounts` (`ID`));
	
	
	create table `Transaction`(
	`ID` INT NOT NULL ,
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
    REFERENCES `Account` (`AccountNumber`));