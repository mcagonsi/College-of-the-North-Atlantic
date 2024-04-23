use `pet-set-vet`;
set global event_scheduler = on
delimiter //

create event expire_appointment on schedule at '2024-4-11 15:32:40'
do begin
	delete from employee where role= 'Captain';
end//

delimiter ;

show events;