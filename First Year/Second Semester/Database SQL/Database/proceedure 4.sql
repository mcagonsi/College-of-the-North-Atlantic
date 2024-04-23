use ap;

DROP PROCEDURE IF EXISTS VendorFilter;
DELIMITER //

CREATE PROCEDURE VendorFilter()


BEGIN 
	
	DECLARE VendorName varchar(50) default null;
    DECLARE InvoiceNumber varchar(20) default null;
    DECLARE BalanceDue varchar(20) default null;
    DECLARE OUTPUT varchar(200);
    DECLARE row_not_found TINYINT DEFAULT FALSE;
    DECLARE update_count INT DEFAULT 0;
    
    
    DECLARE INVOICE_VENDOR_CURSOR CURSOR FOR
		SELECT vendor_name, invoice_number, (invoice_total - payment_total - credit_total) as balance_due FROM invoices
        inner join vendors on vendors.vendor_id = invoices.vendor_id
        WHERE (invoice_total - payment_total - credit_total) >= 5000;
        
	DECLARE CONTINUE HANDLER FOR NOT FOUND
		SET row_not_found = True;
        
	OPEN INVOICE_VENDOR_CURSOR;
    
    
    SET OUTPUT = '';
	WHILE row_not_found = FALSE DO
		FETCH INVOICE_VENDOR_CURSOR INTO VendorName, InvoiceNumber, BalanceDue;
        
		if BalanceDue = null THEN
			SELECT 'NO RECORDS FOUND';
		ELSE 
			SET update_count = update_count +1;
			SET OUTPUT = concat(OUTPUT, BalanceDue,' | ', InvoiceNumber,' | ', VendorName,' // ');
	
			

			end if;
		end while;
	select OUTPUT as result;
    
END //
DELIMITER ;

CALL VendorFilter();