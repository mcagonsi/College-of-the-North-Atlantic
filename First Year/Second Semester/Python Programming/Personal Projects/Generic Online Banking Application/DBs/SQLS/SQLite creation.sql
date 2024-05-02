BEGIN TRANSACTION;
DROP TABLE IF EXISTS "AccountType";
CREATE TABLE IF NOT EXISTS "AccountType" (
	"ID"	INT NOT NULL,
	"Name"	VARCHAR(45) NOT NULL,
	PRIMARY KEY("ID")
);
DROP TABLE IF EXISTS "Account";
CREATE TABLE IF NOT EXISTS "Account" (
	"AccountNumber"	INTEGER NOT NULL,
	"Balance"	INT NOT NULL,
	"Active"	TINYINT NOT NULL,
	"AccountType_ID"	INT NOT NULL,
	"Accounts_ID"	INT NOT NULL,
	CONSTRAINT "fk_Account_AccountType1" FOREIGN KEY("AccountType_ID") REFERENCES "AccountType"("ID"),
	CONSTRAINT "fk_Account_Accounts1" FOREIGN KEY("Accounts_ID") REFERENCES "Accounts"("ID"),
	PRIMARY KEY("AccountNumber" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "Transaction";
CREATE TABLE IF NOT EXISTS "Transaction" (
	"ID"	INTEGER NOT NULL,
	"accountID"	INT NOT NULL,
	"type"	VARCHAR(10) NOT NULL,
	"Amount"	INT NOT NULL,
	"DateAndTime"	DATE NOT NULL,
	"FromBankName"	VARCHAR(45) NOT NULL,
	"FromName"	VARCHAR(45) NOT NULL,
	"FromAccountNumber"	VARCHAR(45) NOT NULL,
	"ToBankName"	VARCHAR(45) NOT NULL,
	"ToName"	VARCHAR(45) NOT NULL,
	"ToAccountNumber"	VARCHAR(45) NOT NULL,
	"Status"	VARCHAR(45) NOT NULL,
	"Account_AccountNumber"	INT NOT NULL,
	CONSTRAINT "fk_Transaction_Account1" FOREIGN KEY("Account_AccountNumber") REFERENCES "Account"("AccountNumber"),
	PRIMARY KEY("ID" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "OnlineBankingAcct";
CREATE TABLE IF NOT EXISTS "OnlineBankingAcct" (
	"ID"	INTEGER NOT NULL,
	"Email"	VARCHAR(40) NOT NULL,
	"Password"	VARCHAR(100) NOT NULL,
	"customerID"	INT NOT NULL,
	CONSTRAINT "cust_onlinebankID_fk" FOREIGN KEY("customerID") REFERENCES "Customer"("ID"),
	PRIMARY KEY("ID" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "Accounts";
CREATE TABLE IF NOT EXISTS "Accounts" (
	"ID"	INTEGER,
	"OnlineBankingAcct_ID"	INT,
	"Customer_ID"	INT NOT NULL,
	CONSTRAINT "fk_Accounts_Customer1" FOREIGN KEY("Customer_ID") REFERENCES "Customer"("ID"),
	CONSTRAINT "fk_Accounts_OnlineBankingAcct1" FOREIGN KEY("OnlineBankingAcct_ID") REFERENCES "OnlineBankingAcct"("ID"),
	PRIMARY KEY("ID" AUTOINCREMENT)
);
DROP TABLE IF EXISTS "Customer";
CREATE TABLE IF NOT EXISTS "Customer" (
	"ID"	INTEGER NOT NULL,
	"FirstName"	VARCHAR(45) NOT NULL,
	"LastName"	VARCHAR(45) NOT NULL,
	"Gender"	TEXT NOT NULL,
	"DOB"	DATE NOT NULL,
	"RelationshipStatus"	VARCHAR(45) NOT NULL,
	"PhoneNumber"	VARCHAR(45) NOT NULL,
	"StateOfOrigin"	VARCHAR(45) NOT NULL,
	"CountryOfOrigin"	VARCHAR(45) NOT NULL,
	"HouseAddress"	VARCHAR(45) NOT NULL,
	"Town_City"	VARCHAR(45) NOT NULL,
	"CountryOfResidence"	VARCHAR(45) NOT NULL,
	"PostalCode"	VARCHAR(45) NOT NULL,
	"OnlineBankingAcct_ID"	INT,
	PRIMARY KEY("ID" AUTOINCREMENT)
);
INSERT INTO "AccountType" VALUES (1,'CHEQUING');
INSERT INTO "AccountType" VALUES (2,'SAVINGS');
INSERT INTO "AccountType" VALUES (3,'INVESTMENT');
COMMIT;
