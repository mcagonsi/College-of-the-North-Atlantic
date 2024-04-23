create database if not exists `pet-set-vet`;

use `pet-set-vet`;

drop table if exists procedurePet;
drop table if exists appointment;
drop table if exists pet;
drop table if exists invoiceProcedure;
drop table if exists `procedure`;
drop table if exists invoice;
drop table if exists account;
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

create table account (
	id int auto_increment,
    client varchar(15),
    status int,
    balance decimal(8,2),
    dueDate date,
    lastReminder date,
    constraint account_pk primary key (id),
    constraint accountClient_fk foreign key (client) references client (phone)
);

create table invoice (
	id int auto_increment,
    account int,
    procTotal decimal (8,2),
    taxRate decimal (5,2),
    balanceDue decimal(8,2),
    invoiceDate date,
    constraint invoice_pk primary key (id),
    constraint accountInvoice_fk foreign key (account) references account (id)
);

create table `procedure` (
	procCode int,
    description varchar (255),
    fee decimal(8,2),
    constraint vetProcedure_pk primary key (procCode)
);

create table invoiceProcedure (
	id int,
    invoiceId int,
    procId int,
    constraint invoiceProcedure_pk primary key (id),
    constraint ipInv_fk foreign key (invoiceId) references invoice (id),
    constraint ipProc_fk foreign key (procId) references `procedure` (procCode)
);

create table pet (
	id int auto_increment,
    name varchar(20),
    species varchar(20),
    sex varchar(1),
    dob date,
    chipped int,
    owner varchar(15),
    constraint pet_pk primary key (id),
    constraint pet_client_fk foreign key (owner) references client (phone)
);

create table appointment (
	start datetime,
    room varchar(15),
    petId int,
    vetPhone varchar(15),
    vetExt int,
    constraint app_pk primary key (start, petId),
    constraint app_pet_fk foreign key (petId) references pet (id),
    constraint app_emp_fk foreign key (vetPhone, vetExt) references employee (phone, ext)
);

create table procedurePet (
	id int auto_increment,
    procId int,
    petId int,
    invoiceId int,
    appointmentTime datetime,
    constraint procedurePet_pk primary key (id),
    constraint ppProc_fk foreign key (procId) references `procedure` (procCode),
    constraint ppPet_fk foreign key (petId) references pet (id),
    constraint ppInv_fk foreign key (invoiceId) references invoice (id),
    constraint ppApp_fk foreign key (appointmentTime, petId) references appointment (start, petId)
);