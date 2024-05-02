


DROP TABLE IF EXISTS `Customer` ;

CREATE TABLE IF NOT EXISTS `Customer` (
  `ID` INT NOT NULL AUTO_INCREMENT,
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
  PRIMARY KEY (`ID`)
  )
ENGINE = InnoDB;

CREATE INDEX `fk_Customer_OnlineBankingAcct_idx` ON `Customer` (`OnlineBankingAcct_ID` ASC) VISIBLE;

CREATE UNIQUE INDEX `ID_UNIQUE` ON `Customer` (`ID` ASC) VISIBLE;




DROP TABLE IF EXISTS `AccountType` ;

CREATE TABLE IF NOT EXISTS `AccountType` (
  `ID` INT NOT NULL,
  `Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;





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





DROP TABLE IF EXISTS `Accounts` ;

CREATE TABLE IF NOT EXISTS `Accounts` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `OnlineBankingAcct_ID` INT NOT NULL,
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


