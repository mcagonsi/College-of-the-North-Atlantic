-- Question 1 (of 1)
-- Create a stored procedure called newAppointment that will establish an 'appointment' for a 'client' that has a single 'pet'.
-- The 'appointment' will be for 8am, April 3rd, 2024 for a "check-up" 'procedure' with Dr. Calm.
-- Note that the appointment and employee tables have composite keys.
-- Also note that creating a record in the 'procedurepet' table will require creating an 'invoice' first. Make sure the invoice balanceDue and the invoice date are accurate.
-- The procedure call should be of the form newAppointment (<client's phone number>, <pet's name>, <date and time>, <dr's phone number>, <dr's ext>);
-- If any of the parameters are NULL, report an error and make sure that no tables are altered.
-- If all parameters are ok, your procedure should insert records into the appointment, procedurepet and invoices tables and update the account tables.
-- Protect the insertions and update with a transaction.
-- A continue or exit handler is requires so that the database changes can commit or rollback.
-- Then show that:
--   "call newAppointment (NULL, NULL, NULL, NULL, NULL);" fails because the client's phone number is null,
--   "call newAppointment ("709-555-1235", NULL, NULL, NULL, NULL);" fails because the pet's name is null,
--   "call newAppointment ("709-555-1235", "Alfie", NULL, NULL, NULL);" fails because Mr Aimes doesn't own Alfie,
--   "call newAppointment ("709-555-1235", "Droog", NULL, NULL, NULL);" fails because the appointment time is null,
--   "call newAppointment ("709-555-1235", "Droog", "2024-04-03 08:00:00", NULL, NULL);" fails because the dr's phone number is null,
--   "call newAppointment ("709-555-1235", "Droog", "2024-04-03 08:00:00", "709-222-2221", NULL);" fails because the dr's ext is null,
--   "call newAppointment ("709-555-1235", "Droog", "2024-04-03 08:00:00", "709-222-2221", 14);" succeeds
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

    
	DECLARE count int ;
    DECLARE pet_id int default null;
    DECLARE dr_ext int default null;
    DECLARE vet_name varchar(20) default null;
    DECLARE proc_id int default null;
    DECLARE acc_id int default null;
    DECLARE inv_id int default null;
    DECLARE inv_proc_id int default null;
    DECLARE proced_total decimal(8,2) default null;
    DECLARE tax_rate decimal(5,2);
    DECLARE balance_due decimal(8,2) default null;
    DECLARE valid_owner varchar(20) default null;
    
    
	
    select `name` 
	into valid_owner
    from pet
	where `owner` = client_phone_param;
	
    if client_phone_param is null then
		SIGNAL SQLSTATE '22003'
			SET message_text = "fails because the client's phone number is null",
				MYSQL_ERRNO = 1407;
    
	elseif pet_name_param != valid_owner then
		SIGNAL SQLSTATE '22003'
			SET message_text = "fails because Mr Aimes doesn't own Alfie",
				MYSQL_ERRNO = 1407;
	elseif pet_name_param is null then
		SIGNAL SQLSTATE '22003'
			SET message_text = "fails because the pet's name is null",
				MYSQL_ERRNO = 1407;
	elseif date_time_param is null then
		SIGNAL SQLSTATE '22003'
			SET message_text = "fails because the appointment time is null",
				MYSQL_ERRNO = 1407;
	elseif doctor_phone_param is null then
		SIGNAL SQLSTATE '22003'
			SET message_text = "fails because the dr's phone number is null",
				MYSQL_ERRNO = 1407;
	elseif doctor_ext_param is null then
		SIGNAL SQLSTATE '22003'
			SET message_text = "fails because the dr's ext is null",
				MYSQL_ERRNO = 1407;
	else
		
		
		select id into pet_id from pet where `name` = valid_owner;
    
		select max(id) into inv_id from invoice;
		if inv_id is null then
			set inv_id = 1;
		else
			set inv_id = inv_id + 1;
		end if;
		
		select max(id) into inv_proc_id from invoiceprocedure;
		
		if inv_proc_id is null then
			set inv_proc_id = 1;
		else
			set inv_proc_id = inv_id + 1;
		end if;
		
        
        select id 
		into acc_id 
		from `account` 
		where `client` = client_phone_param;
        
        select procCode 
		into proc_id 
		from `procedure` 
		where `description` = 'Check-up';
        
        select fee 
		into proced_total 
		from `procedure` 
		where `description` = 'Check-up';
        
        select lastName 
		into vet_name 
		from employee 
		where phone = doctor_phone_param and ext = doctor_ext_param;
        
		
        set tax_rate = 0.15;
        set balance_due = proced_total * tax_rate;
	
	end if;
    
    
	START TRANSACTION;
	insert into appointment values(date_time_param, 1, pet_id, doctor_phone_param, doctor_ext_param);
    
    insert into invoice values (inv_id, acc_id, proced_total, tax_rate, balance_due, '2024-04-02');
    
    insert into procedurepet values (1, proc_id, pet_id, inv_id, date_time_param);
    
    insert into invoiceprocedure values (inv_proc_id, inv_id, proc_id);
    
    update `account` 
    set `status` = 1 , balance = proced_total
    where `client` = client_phone_param;
    
	
	IF sql_error = FALSE THEN
		COMMIT;
		SET count = count + 1;
        SELECT concat(count,' appointment was scheduled') as success_message;
	ELSE 
		ROLLBACK;
	END IF;
END//
DELIMITER ;


call newAppointment ("709-555-1235", "Droog", "2024-04-03 08:00:00", "709-222-2221", 14);