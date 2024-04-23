use `pet-set-vet`;

drop trigger if exists before_insert_invproc;

delimiter //

create trigger before_insert_invproc
	before insert on invoiceprocedure
    for each row
begin
	declare invoice_total decimal(8,2);
    declare proc_cost decimal(8,2);
    
    select balanceDue into invoice_total from invoice where id = new.invoiceId;
    select fee into proc_cost from `procedure` where procCode = new.procId;
    set invoice_total = invoice_total + proc_cost;
    update invoice set balanceDue = invoice_total where id = new.invoiceId;
end//

delimiter ;

insert into invoiceprocedure values(2,3,1001);