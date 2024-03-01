create database if not exists Veterinary_Clinic_Database;

use Veterinary_Clinic_Database;

drop table if exists appointment;
drop table if exists pet;
drop table if exists client;
drop table if exists employee;

create table employee (
	firstName varchar(20),
    lastName varchar(20),
    role varchar(20),
    phone varchar(15),
    ext int,
    office varchar(10),
    constraint emp_pk primary key (phone, ext)
);

create table client (
	firstName varchar(20),
    lastName varchar(20),
    phone varchar(15),
    altPhone varchar(15),
    sms varchar(15),
    email varchar(45),
    prefContact varchar(45),
    constraint client_pk primary key (phone)
);

create table pet (
	id int,
    name varchar(20),
    species varchar(20),
    sex varchar(1),
    dob date,
    chipped int,
    owner varchar(15),
    constraint pet_pk primary key (id),
    constraint pet_client_fk foreign key (owner) references client (phone)
);

create table if not exists appointment (
	`start` datetime,
    room varchar(15),
    petId int,
    vetPhone varchar(15),
    vetExt int,
    constraint app_pk primary key (start, petId),
    constraint app_pet_fk foreign key (petId) references pet (id),
    constraint app_emp_fk foreign key (vetPhone, vetExt) references employee (phone, ext)
);

create table if not exists account (
	id int not null primary key,
    `client` varchar(15),
    `status` int,
    balance decimal(8,2),
    dueDate date,
    lastReminder date,
    constraint acc_client_fk foreign key (client) references client(phone)
);

create table if not exists `procedure` (
	procCode int not null primary key,
    description varchar(255),
    fee decimal(8,2)
);

create table if not exists invoice (
	id int not null primary key,
    account int not null,
    procTotal decimal(8,2),
    taxRate decimal(5,2),
    balanceDue decimal(8,2),
    invoiceDate date,
    constraint inv_acc_fk foreign key (account) references account(id)

);

create table if not exists invoiceprocedure (
	id int not null primary key,
    invoiceId int,
    procId int,
    constraint invproc_inv_fk foreign key (invoiceId) references invoice(id),
    constraint invproc_proc foreign key (procId) references `procedure`(procCode)
);


create table if not exists procedurepet (
	id int not null primary key,
    procId int,
    petID int,
    invoiceID int,
    appointmentTime datetime,
    constraint proc_pet_fk foreign key (petID) references pet(id),
    constraint proc_app_fk foreign key (appointmentTime) references appointment(start),
    constraint proc_inv_fk foreign key (invoiceID) references invoice(id),
    constraint proc_procd_fk foreign key (procId) references `procedure`(procCode)
);






