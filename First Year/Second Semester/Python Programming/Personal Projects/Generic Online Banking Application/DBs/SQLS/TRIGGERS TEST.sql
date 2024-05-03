use bankdb;


drop trigger if exists close_customer_account;

delimiter //
create trigger close_customer_account
	before delete on customer
	for each row
BEGIN

	
	declare customer_id int;
	declare onlinebankid int default null;
    declare accountsid int;
    
	
    select ID into customer_id from customer where ID = old.ID;
	select accounts_id into accountsid from customer_accounts_account where ID = customer_id;
    select OnlineBankingAcct_ID into onlinebankid from customer_accounts_account where ID = customer_id;
    
    WHILE accountNumber is not null do
        delete from account where Accounts_ID = accounts_id;
	END WHILE;
    IF onlinebankid is not null then
		delete from onlinebankingacct where ID = onlinebankid;
	END IF;
	
END //

delimiter ;
