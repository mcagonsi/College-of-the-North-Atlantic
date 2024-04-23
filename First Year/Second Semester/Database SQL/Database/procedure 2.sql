USE ap;

DROP PROCEDURE IF EXISTS Factorial;
DELIMITER //

CREATE PROCEDURE Factorial()
BEGIN 
    DECLARE num INTEGER DEFAULT 8;
    DECLARE count INTEGER;
    DECLARE result INTEGER DEFAULT 1;
    
    SET count = num;
    
    WHILE count > 1 DO
        SET result = result * count;
        SET count = count - 1;
    END WHILE;
    
    SELECT CONCAT('The factorial of ', num, ' is: ', result) AS Result;
END //
DELIMITER ;

call Factorial();