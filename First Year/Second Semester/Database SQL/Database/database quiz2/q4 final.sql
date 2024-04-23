USE College_Enrollment_System;

DROP TRIGGER IF EXISTS AFTER_INSERT_ENROLL;

DELIMITER //

CREATE TRIGGER AFTER_INSERT_ENROLL
    AFTER INSERT ON enrollment
    FOR EACH ROW
BEGIN
	DECLARE student_ID INT;
    DECLARE current_balance DECIMAL(10,0);
    DECLARE enroll_fee DECIMAL(10,2);
    DECLARE offering_id INT;
    
    SELECT offeringId INTO offering_id from enrollment where id = new.id;
	SELECT studentID INTO student_ID FROM enrollment WHERE id = new.id ;
    SELECT balance INTO current_balance FROM `account` WHERE studentID = student_ID;
    SELECT fee INTO enroll_fee FROM offering where id = offering_id;
    
    SET current_balance = current_balance + enroll_fee;
    
    UPDATE `account` SET balance = current_balance WHERE studentID = studentID ;
END//

DELIMITER ;