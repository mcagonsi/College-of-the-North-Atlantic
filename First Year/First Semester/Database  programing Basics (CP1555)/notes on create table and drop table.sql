use bookstore;
create table student_records (
	id int primary key auto_increment  not null,
    f_name varchar(20) not null,
    l_name varchar(20) not null,
    init varchar(5),
    dob varchar(10) default null,
    start_year int not null,
    start_semester int not null,
    homeroom varchar(10) not null,
    gpa int not null);
    
drop table student_records;
    
    insert into student_records(id, f_name, l_name, init, dob, start_year, start_semester, homeroom, gpa) values
    (12345, 'Paul', 'Drover', 'X', null, 2000, 1, 'k205', 2),
    (default, 'Joe', 'Jones', 'J', null, 2022, 1, 'k205', 3),
    (default, 'Abby', 'Angel', 'A', null, 2023, 2, 'k207', 3);