SELECT * FROM account;
update account set Balance = 2000 where AccountNumber = 48483208;
select * from customer;
delete from customer where FirstName = 'MICHAEL';
SELECT * FROM ACCOUNTS;
select * from onlinebankingacct;
delete from onlinebankingacct where ID =5;
delete from account where AccountNumber = 48489762;
delete from account where AccountNumber = 25887178;
drop view if exists Accounts_Account;

select * from transaction;
insert into transaction(ID,accountID,type,amount,DateAndTime,FromBankName,FromName,FromAccountNumber,ToBankName,ToName,ToAccountNumber,Status)values
 (default,accountID,'DEBIT', amount,default,FromBankNamme,FromName,FromAcctNo,ToBankName,ToName,ToAccountNumber,Status);
select * from Customer_Accounts_Account;

insert into onlinebankingacct value (default,'agonsimisfdgchael@gmail.com','ssdadfa',5);
update accounts set OnlineBankingAcct_ID = Null where ID = 6531;
