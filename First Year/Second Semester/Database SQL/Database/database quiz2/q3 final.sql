USE College_Enrollment_System;

DROP TABLE IF EXISTS  contact;
DROP TRIGGER IF EXISTS BEFORE_INSERT_CONTACT;
DROP TRIGGER IF EXISTS AFTER_UPDATE_CONTACT;


CREATE TABLE IF NOT EXISTS contact (
	contactID		INT NOT NULL AUTO_INCREMENT,
	firstName 		VARCHAR(40) NOT NULL,
    lastName 		VARCHAR(40) NOT NULL,
    studentID		INT NULL,
    mailing_address	VARCHAR(50) NOT NULL,
    phone			VARCHAR(50) NOT NULL,
    email 			VARCHAR(25) NOT NULL,
    created_updated	DATE NULL,
    
    
    CONSTRAINT contact_student_pk PRIMARY KEY (contactID),
    CONSTRAINT student_contact_fk FOREIGN KEY (firstname,lastName,studentID) REFERENCES student (firstName,LastName,id)
    
    );

DELIMITER //

CREATE TRIGGER BEFORE_INSERT_CONTACT
    BEFORE INSERT ON contact
    FOR EACH ROW
BEGIN
	DECLARE student_ID INT;
    DECLARE date_created DATE;
    DECLARE fName VARCHAR(40);
    DECLARE lName VARCHAR(40);
    
    SET date_created = NOW();
    
	SELECT id INTO student_ID FROM student WHERE firstName = new.firstName AND lastName = new.lastName;
    
    UPDATE contact SET studentID = student_ID;
    UPDATE contact SET created_updated = date_created;
END//

DELIMITER ;
DELIMITER //

CREATE TRIGGER AFTER_UPDATE_CONTACT
    AFTER UPDATE ON contact
    FOR EACH ROW
BEGIN
	DECLARE student_ID INT;
    DECLARE date_created DATE;
    DECLARE fName VARCHAR(40);
    DECLARE lName VARCHAR(40);
    
    SET date_created = NOW();
    
    SELECT firstName into fName from contact;
    SELECT lastName into lName from contact;
    
	SELECT id INTO student_ID FROM student WHERE firstName = fName AND lastName = lName;
    
    UPDATE contact SET studentID = student_ID;
    UPDATE contact SET created_updated = date_created;
END//

DELIMITER ;

INSERT INTO contact(firstName, lastName, mailing_address, phone, email) VALUES 
	('Dave','Dive','45 Brandon Street, St.Johns','+17096748765','Dave@gmail.com'),
    ('Earl','Ernst','45 Fraude Street, St.Johns','+17096748893','Earl@gmail.com'),
    ('Fred','Flintstone','45 Diana Street, St.Johns','+17096742345','Fred@gmail.com');
    
    

