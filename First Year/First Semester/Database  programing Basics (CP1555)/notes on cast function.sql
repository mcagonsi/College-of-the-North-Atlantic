use ap;

-- Question 1
select invoice_total,
	format(invoice_total,1) as invoice_total_1dec,
    convert(invoice_total , signed) as invoice_total_int,
    cast(invoice_total as signed) as invoice_total_cast_int
from invoices;

select invoice_date from invoices;

-- Question 2
select invoice_date,
	cast(invoice_date as datetime), 
    cast(invoice_date as char(7))
from invoices;

-- Question 3

create table class_schedule(
	course_code varchar(10) not null primary key,
    week_days enum('Monday','Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'));

insert into class_schedule (course_code, week_days) values
('CP1850','Monday'),
('CP1555', 'Tuesday'),
('CP1420', 'Tuesday'),
('CM1400', 'Wednesday'),
('MA1900', 'Thursday'),
('CP1461', 'Tuesday'),
('CR1130', 'Monday');

select * from class_schedule
where week_days = 'Tuesday';


-- Question 4
create table color_pallate(
	secondary_color varchar(15) primary key not null,
    primary_color set ('red','yellow','blue'));


insert into color_pallate(secondary_color, primary_color) values
	('green', ("yellow,blue")),
    ('purple', ("blue,red")),
    ('orange', ("yellow,red"));
select * from color_pallate
where primary_color like "%red%";
    
    