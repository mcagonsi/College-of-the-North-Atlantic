use bankdb;
drop trigger if exists transfer_transactions;

delimiter //
create trigger transfer_transactions
	before insert on transaction
	for each row
BEGIN
	declare from_accountName varchar(10);
    declare from_accttype int;
    declare to_accountName varchar(10);
    declare to_accttype int;
    declare from_balance Decimal(9,2);
    declare to_balance Decimal(9,2);
    
    
    select AccountType_ID into from_accttype from customer_accounts_account where AccountNumber = new.FromAccountNumber;
    select Name into from_accountName from AccountType where ID = from_accttype;
    select AccountType_ID into to_accttype from customer_accounts_account where AccountNumber = new.ToAccountNumber;
    select Name into to_accountName from AccountType where ID = to_accttype;
    
    select balance into from_balance from account where AccountNumber=new.FromAccountNumber;
    select balance into to_balance from account where AccountNumber = new.ToAccountNumber;
    
    
    
    
	if new.Type = 'TRANSFER' THEN
        set new.Status = 'SUCCESSFUL';
        set new.DateAndTime = current_timestamp();
        set new.ToBankName = 'N/A';
        set new.FromBankName = 'N/A';
        set new.FromName = from_accountName;
        set new.ToName = to_accountName;
        update account set balance = from_balance - new.amount where AccountNumber = new.FromAccountNumber;
		update account set balance = to_balance + new.amount where AccountNumber = new.ToAccountNumber;
	end if;
    
   
END //

delimiter ;

insert into transaction(ID,accountID,type,amount,FromAccountNumber,ToAccountNumber,Status) values
 (default,2588,'TRANSFER', 100 ,25887257,25889591,Status);