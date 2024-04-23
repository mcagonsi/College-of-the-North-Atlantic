use College_Enrollment_System;
DROP TABLE IF EXISTS  `account`;


CREATE TABLE IF NOT EXISTS `account` (
	accountID 		INT NOT NULL,
    studentID		INT NOT NULL,
    balance 		DECIMAL(10,0) NOT NULL,
    accountStatus	INT NOT NULL,
    
    CONSTRAINT acc_pk PRIMARY KEY (accountID),
    CONSTRAINT acct_student_id_fk FOREIGN KEY (studentID) REFERENCES student (id),
    CONSTRAINT acct_student_bal_fk FOREIGN KEY (balance) REFERENCES student (arrears),
    CONSTRAINT student_status_fk FOREIGN KEY (accountStatus) REFERENCES student(`status`)
    
    )
    
	