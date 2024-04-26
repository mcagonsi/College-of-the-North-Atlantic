use `pet-set-vet-solution`;
-- alter table pet modify column id int auto_increment;

DROP PROCEDURE IF EXISTS ClientPetIns;
DELIMITER //
CREATE PROCEDURE ClientPetIns (
	pet_id_param int,
    pet_name_param varchar(20),
    species_param varchar(20),
    sex_param varchar(1),
    dob_param date,
    chipped_param int,
    client_Fname_param varchar(20),
    client_Lname_param varchar(20),
    phone_param varchar(15),
    altphone_param varchar(15),
    sms_param varchar(15),
    email_param varchar(45),
    pref_Contact_param varchar(45)
)

BEGIN
	DECLARE count int;
	declare mysql_error tinyint default false;
	
        
    SET count = 0;

    
    -- validate data PET inputs
    IF pet_id_param is null then
		SIGNAL SQLSTATE 'ERROR'
			SET message_text = 'Must Enter Pet Info',
				MYSQL_ERRNO = 1407;
	ELSEIF pet_name_param is null then
		SIGNAL SQLSTATE 'ERROR'
			SET MESSAGE_TEXT = 'NULL NOT ACCEPTED';
	ELSEIF species_param is null then
		SIGNAL SQLSTATE 'ERROR'
			SET MESSAGE_TEXT = 'NULL NOT ACCEPTED';
	ELSEIF sex_param is null then
		SIGNAL SQLSTATE 'ERROR'
			SET MESSAGE_TEXT = 'NULL NOT ACCEPTED';
	ELSEIF dob_param is null then
		SIGNAL SQLSTATE 'ERROR'
			SET MESSAGE_TEXT = 'NULL NOT ACCEPTED';
	ELSEIF chipped_param is null then
		SIGNAL SQLSTATE 'ERROR'
			SET MESSAGE_TEXT = 'NULL NOT ACCEPTED';
	ELSEIF client_Fname_param is null  then
		SIGNAL SQLSTATE 'ERROR'
				SET message_text = 'Must Enter CLIENT INFO',
					MYSQL_ERRNO = 2235;
	ELSEIF client_Lname_param is null then
		SIGNAL SQLSTATE 'ERROR'
			SET MESSAGE_TEXT = 'NULL NOT ACCEPTED';
	ELSEIF phone_param is null then
		SIGNAL SQLSTATE 'ERROR'
			SET MESSAGE_TEXT = 'NULL NOT ACCEPTED';
	ELSEIF sex_param != 'm' and sex_param != 'f' THEN 
		SIGNAL SQLSTATE 'ERROR'
			SET message_text = 'SEX INVALID',
				MYSQL_ERRNO = 2233;
	END IF;
    

       
    
    
    
START TRANSACTION;
	INSERT INTO `client` values (client_Fname_param, client_Lname_param , phone_param , altphone_param , sms_param , email_param, pref_Contact_param);
	INSERT INTO pet values (pet_id_param, pet_name_param, species_param, sex_param, dob_param, chipped_param, phone_param);
    
    
	
	if mysql_error = false then
		SET count = count + 1;
        SELECT concat(count,' was inserted into table') as success_message;
	ELSE 
		ROLLBACK;
	END IF;
END//
DELIMITER ;

CALL ClientPetIns (104, 'Jack', 'German Shepherd', 'm', '2005-4-19', 2, 'Michael', 'Agonsi','7098625352','0','0','0','0');

	