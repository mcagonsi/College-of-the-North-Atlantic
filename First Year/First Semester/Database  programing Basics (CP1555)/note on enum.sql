use ap;
create table delivery (delivery_id integer not null auto_increment primary key,invoice_id VARCHAR(40),
    method ENUM ('Canada Post', 'DHL', 'UPS', 'Courier', 'Taxi', 'Bus', 'Hand'));
    
insert into delivery (invoice_id, method) values
	(1, 'Canada Post'),
    (2, 'DHL'),
    (3, 'UPS'),
    (4, 'Hand');
    
select * from delivery;

insert into delivery (invoice_id, method) values
	(4, 'hello');