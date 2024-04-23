use ap;

DROP PROCEDURE IF EXISTS test:

-- Change statement delimiter from semicolon to double front slashes

DELIMITER //

CREATE PROCEDURE test()
BEGIN 
	DECLARE sum_balance_due_var DECIMAL(9,2);
    
    SELECT SUM(invoice_total - payment_total - credit_total)
	INTO sum_balance_due_var
	FROM invoices
	WHERE vendor_id = 78;
    
	IF sum_balance_due_var > 0 THEN
		SELECT CONCAT('Balance due: $', sum_balance_due_var) AS message;
	ELSE
		SELECT 'Balance paid in full' AS message;
	END IF;
    
END//

DELIMITER ;

CALL test();


use ap;

DROP PROCEDURE IF EXISTS balanceLess;
DELIMITER //

CREATE PROCEDURE balanceLess()
BEGIN 
	DECLARE rows_count integer ;
    DECLARE total_balance Decimal(9,2);
    
    SELECT count(invoice_total - payment_total - credit_total)
	INTO rows_count
	FROM invoices
	WHERE (invoice_total - payment_total - credit_total) > 0;
    
    select sum(invoice_total - payment_total - credit_total)
    into total_balance
    from invoices
    where (invoice_total - payment_total - credit_total) > 0;
    
    
    
    if total_balance > 15000 THEN
		SELECT concat('Number of invoices: ',rows_count, '    Total balance due: $', total_balance) as message;
	else
		select 'Total balance due is less than $15000' as message;
	end if;
		
    
END//
DELIMITER ;

CALL balanceLess();