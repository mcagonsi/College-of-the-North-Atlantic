-- CREATES THE TRIGGER FOR ALL CREDIT TRANSACTIONS TO RECORD INTO THE DATABASE


drop trigger if exists credit_into_account;

delimiter //
create trigger credit_into_account
	before insert on transaction
	for each row
BEGIN
	declare accountName varchar(10);
    declare accttype int;
    declare accountID int;
    declare cur_bal decimal(9,2);
    declare new_bal decimal(9,2);
    
    select Accounts_ID into accountID from account where AccountNumber=new.ToAccountNumber;
    select AccountType_ID into accttype from customer_accounts_account where AccountNumber = new.ToAccountNumber;
    select Name into accountName from AccountType where ID = accttype;
    select Balance into cur_bal from account where AccountNumber = new.ToAccountNumber;
    
    
	if new.Type = 'CREDIT' THEN
        set new.Status = 'SUCCESSFUL';
        set new.DateAndTime = current_timestamp();
        set new.ToName = accountName;
        set new.accountID = accountID;
        set new_bal = cur_bal + new.amount;
        update account set Balance = new_bal where AccountNumber = new.ToAccountNumber;
        
        
	end if;
END //

delimiter ;

insert into transaction(ID,type,amount,FromBankName,FromName,FromAccountNumber,ToBankName,ToAccountNumber)values
 (default,'CREDIT', 500,'Tesla Bank','Michael Agonsi', 48483208,'ROYAL BANK OF CANADA',81356949);