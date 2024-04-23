use `pet-set-vet`;

DROP PROCEDURE IF EXISTS newAppointment;


DELIMITER //
CREATE PROCEDURE newAppointment (
	client_phone_param varchar(15),
    pet_name_param varchar(20),
    date_time_param datetime,
    doctor_phone_param varchar(15),
    doctor_ext_param int
    
)

BEGIN
	
    
    
        
    DECLARE sql_error TINYINT DEFAULT FALSE;
	DECLARE CONTINUE HANDLER FOR SQLEXCEPTION
		SET sql_error = TRUE;
	
   
	
    IF client_phone_param = 0 then
		SIGNAL SQLSTATE '22003'
		SET MESSAGE_TEXT = 'Failed! Null value not allowed';
	end if;			
	
    
	
	
    
END//
DELIMITER ;

call newAppointment(0,NULL,NULL,NULL,NULL)