use ap;

delimiter //

create trigger invoices_before_update
	before update on invoices
    for each row
begin 
	declare sum_line_item_ammount decimal (9,2);
    declare mysql_error tinyint default false;
    select sum(line_item_amount)
    into sum_line_item_ammount
    from invoice_line_items
    where invoice_id = new.invoice_id;
    
    if sum_line_item_ammount != new.invoice_total then
		signal sqlstate 'error'
			set message_text = 'invalid';
	end if;
end//
delimiter ;
        