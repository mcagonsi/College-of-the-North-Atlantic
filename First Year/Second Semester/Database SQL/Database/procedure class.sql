
use ap;
DROP PROCEDURE IF EXISTS test()
DELIMITER //

CREATE PROCEDURE test2()
BEGIN
	DECLARE terms_id_var INT;
    SELECT terms_id INTO terms_id_var
    FROM invoices WHERE invoice_id = 4;
    
    CASE terms_id_var
		WHEN 1 THEN
			SELECT 'Net due 10 days' AS Terms;
		WHEN 2 THEN
			SELECT 'Net due 20 days' AS Terms;
		WHEN 3 THEN
			SELECT 'Net due 30 days' AS Terms;
		ELSE
			SELECT 'Net due more than 30 days' AS Terms;
		END CASE;
END//

call test2()
            