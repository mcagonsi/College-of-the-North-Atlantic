use `pet-set-vet`;

drop trigger if exists before_insert_account;

delimiter //
create trigger before_insert_account
	before insert on invoice
    for each row
begin
	declare account_balance decimal(8,2);
    
    select balance into account_balance from `account` where id = new.account;
    set account_balance = account_balance + new.balanceDue;
    update account set balance = account_balance where id = new.account;
    
end//

delimiter ;

insert into invoice value (2,1,null,null,139,now());
insert into invoice value (3,1,null,null,500,now());

