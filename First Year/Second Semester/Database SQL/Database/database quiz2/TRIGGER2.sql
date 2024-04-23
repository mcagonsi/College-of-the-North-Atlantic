use ap;
drop trigger vendors_before_update;
delimiter //
create trigger vendors_before_update
	before update on vendors
    for each row
begin
	
		set new.vendor_state = upper(new.vendor_state);
	
end//

delimiter ;

update vendors set vendor_state = 'wy' where vendor_id = 1;

select * from vendors where vendor_id = 1;



