-- CREATES THE TRIGGER FOR ALL TRANSFER TRANSACTIONS TO RECORD INTO THE DATABASE

drop trigger if exists deposit_transfer_transactions;

delimiter //
create trigger deposit_transfer_transactions
	before insert on transaction
	for each row
BEGIN
	declare from_accountName varchar(10);
    declare from_accttype int;
    declare to_accountName varchar(10);
    declare to_accttype int;
    
    
    
    select AccountType_ID into from_accttype from customer_accounts_account where AccountNumber = new.FromAccountNumber;
    select Name into from_accountName from AccountType where ID = from_accttype;
    select AccountType_ID into to_accttype from customer_accounts_account where AccountNumber = new.ToAccountNumber;
    select Name into to_accountName from AccountType where ID = to_accttype;
    
    
    
    
	if new.Type = 'T_DEPOSIT' THEN
        set new.Status = 'SUCCESSFUL';
        set new.DateAndTime = current_timestamp();
        set new.ToBankName = 'INTERNAL';
        set new.FromBankName = 'INTERNAL';
        set new.FromName = from_accountName;
        set new.ToName = to_accountName;
	end if;
    
   
END //

delimiter ;