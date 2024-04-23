USE College_Enrollment_System;

DROP PROCEDURE IF EXISTS CreateStudentAccount;

DELIMITER //

CREATE PROCEDURE CreateStudentAccount ()
BEGIN
   DECLARE student_id INT;
   DECLARE acct_balance DECIMAL(10,0);
   DECLARE accStatus INT;
   DECLARE update_count INT DEFAULT 0;

   DECLARE ACCOUNT_CREATE_CURSOR CURSOR FOR
		SELECT id, arrears, `status` from student
        WHERE arrears > 0;
        
	DECLARE CONTINUE HANDLER FOR NOT FOUND
		SET row_not_found = True;
	
    OPEN ACCOUNT_CREATE_CURSOR;
    
    WHILE row_not_found = FALSE DO
		FETCH ACCOUNT_CREATE_CURSOR INTO student_id, acct_balance, acctStatus;
			if student_id = NULL AND acct_balance = NULL and acctStatus = NULL THEN
				SELECT 'NO RECORDS FOUND';
			ELSE
				SET update_count = update_count +1;
                INSERT INTO `account` (studentID, balance, accountStatus) VALUES (student_id, acct_balance, acctStatus);
			END IF;
		END WHILE;
        
	ALTER TABLE student DROP COLUMN arrears;

END //

DELIMITER ;

CALL CreateStudentAccount();
	
        
    


