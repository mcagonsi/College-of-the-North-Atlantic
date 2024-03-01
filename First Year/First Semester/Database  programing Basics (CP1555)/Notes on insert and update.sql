use ap;

-- Question 5
insert into invoices 
values(invoice_id,32,'AX-014-027', '2018-08-01',434.58,0.00,0.00,2,'2018-08-31', Null);

-- Question 6

insert into invoice_line_items 
(invoice_id,invoice_sequence,account_number, line_item_amount,line_item_description)
values
(115,1,160,180.23,'Hard drive'),
(115,2,527,254.35,'Exchange Server update');

-- Question 7
update invoices
set credit_total = round(0.1 * invoice_total),
	payment_total = invoice_total - credit_total
where invoice_id =115;

-- Question 8
update vendors
set default_account_number = 403
where vendor_id = 44;

-- Question 9
update invoices
set terms_id = 2
where vendor_id in (select vendor_id from vendors
							where default_terms_id =2);
 
-- Question 10
delete from invoice_line_items
where invoice_id in (select invoice_id from invoices where invoice_number ='AX-014-027');
delete from invoices
where invoice_number = 'AX-014-027';




