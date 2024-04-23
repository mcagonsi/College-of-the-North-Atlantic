create database if not exists Dealer_Order;

use Dealer_Order;

create table if not exists Invoices (
invoiceid integer not null primary key,
make varchar(30) not null,
model varchar(30) not null,
maker varchar(20) not null,
dealer varchar(20) not null,
quantity integer not null,
order_date date not null,
sales_rep varchar(10) not null
);

alter table Invoices
add constraint dealer_invoice_fk foreign key (dealer) references Dealer(id),
add constraint maker_invoice_fk foreign key (maker) references Maker(id),
add constraint salesrep_invoice_fk foreign key (sales_rep) references Employee(id);

