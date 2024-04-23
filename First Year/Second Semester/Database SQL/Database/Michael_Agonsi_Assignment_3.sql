
-- Question 1
use ap;

DROP PROCEDURE IF EXISTS balanceGreater;
DELIMITER //

CREATE PROCEDURE balanceGreater()
BEGIN 
	DECLARE rows_count integer;
    
    SELECT count(invoice_total - payment_total - credit_total)
	INTO rows_count
	FROM invoices
	WHERE (invoice_total - payment_total - credit_total) > 7000;
    
    if rows_count > 0 THEN
		SELECT concat(rows_count, ' invoices exceed $7000') as message;
	else
		select 'No invoices exceed $7000' as message;
	end if;
		
    
END//
DELIMITER ;

CALL balanceGreater();




-- Question 2
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
    
    
    
    if total_balance >= 15000 THEN
		SELECT concat('Number of invoices: 'rows_count, ' Total balance due:', total_balance) as message;
	else
		select 'Total balance due is less than $15000' as message;
	end if;
		
    
END//
DELIMITER ;

CALL balanceLess();




-- Question 3
use ap;

DROP PROCEDURE IF EXISTS Factorial;
DELIMITER //

CREATE PROCEDURE Factorial()
BEGIN 
	DECLARE num integer ;
    DECLARE count integer;
    DECLARE result integer;
    
    set num = 8;
    set count = num;
    set result = 1;

    
    WHILE count > 1 do
		
        SET result = result * count;
        SET count = count - 1 ;
	   
	END WHILE;
	
	if result > 0 then
	select concat('The factorial of 8 is: ', result);
	END IF;
    


        
    
END//
DELIMITER ;

CALL Factorial();