use ap;

DROP PROCEDURE IF EXISTS VendorFilter;
DELIMITER //

CREATE PROCEDURE VendorFilter()


BEGIN 
	
	DECLARE City varchar(20);
    DECLARE Zipcode varchar(20);
    DECLARE row_not_found TINYINT DEFAULT FALSE;
    DECLARE update_count INT DEFAULT 0;
    
    
    DECLARE VENDOR_CURSOR CURSOR FOR
		SELECT vendor_city, vendor_zip_code FROM vendors
        WHERE vendor_state = 'CA';
        
	DECLARE CONTINUE HANDLER FOR NOT FOUND
		SET row_not_found = True;
        
	OPEN VENDOR_CURSOR;
    drop table if exists location;
	create table  location (info varchar(50) );
	WHILE row_not_found = FALSE DO
		FETCH VENDOR_CURSOR INTO City, Zipcode;
        
		if City = null and Zipcode = null THEN
			SELECT 'NO RECORDS FOUND';
		ELSE 
			SET update_count = update_count +1;
			insert into Location values (concat(City,',', Zipcode));
	
			

			end if;
		end while;
	select * from location;
    
END //
DELIMITER ;

CALL VendorFilter();