use `pet-set-vet`;
delete from invoice;
delete from account;
delete from employee;
delete from `procedure`;
delete from pet;
delete from client;

insert into client values ("Alfred", "Aimes", "709-555-1235", "709-123-5678", "709-123-5678", "al.aimes@hotmail.com", "email"),
("Brian", "Bowes", "709-555-1236", "709-123-6789", "709-123-6789", "brian.bowes@hotmail.com", "email"),
("Charles", "Chu", "709-555-1237", "709-123-7890", "709-123-7890", "chuck.chu@hotmail.com", "phone"),
("David", "Duchamps", "709-555-1238", "709-123-8901", "709-123-8901", "dave.duchamps@hotmail.com", "phone"),
("Eric", "Elferson", "709-555-1239", "709-123-9012", "709-123-9012", "dave.duchamps@hotmail.com", "sms"),
("Zoey", "Zahn", "709-555-9876", "709-123-9876", "709-123-9876", "zoey.zahn@hotmail.com", "sms"),
("Paul", "Drover", "709-555-1234", "709-123-9876", "709-123-9876", "paul.drover@hotmail.com", "sms");

insert into `pet` values 
(NULL, "Alfie", "feline", "f", "2022-07-15", 0, "709-555-1234"),
(NULL, "Barney", "feline", "f", "2022-07-15", 0, "709-555-1234"),
(NULL, "Champ", "canine", "m", "2021-08-14", 56764, "709-555-1236"),
(NULL, "Droog", "canine", "m", "2020-09-13", 0, "709-555-1235"),
(NULL, "Ernie", "feline", "m", "2023-10-12", 0, "709-555-1237");

insert into `procedure` values 
(1001, "Spay", 300.00),
(1002, "Neuter", 100.00),
(1003, "Flea treatment", 45.00),
(1004, "Mat removal", 30.00),
(1005, "Check-up", 30.00),
(1006, "Complex Laceration requiring stiches", 25.00),
(1007, "Simple Laceration", 10.00),
(1008, "labour & Delivery", 500.00),
(1009, "Bone splint", 40.00),
(1010, "Surgery", 1000.00);

insert into employee values
("William", "Wonka", "Receptionist", "709-222-2221", 10, "M101"),
("William", "Shatner", "Captain", "709-222-2221", 11, "M102"),
("William", "Wallace", "Leader", "709-222-2221", 12, "M103"),
("William", "Henry", "King", "709-222-2221", 13, "M104"),
("William", "Calmer", "Vet", "709-222-2221", 14, "M105");

insert into account values
(NULL, "709-555-1234", 3, 0.0, "2024-03-15", "2024-04-01"),
(NULL, "709-555-1235", 0, 0.0, NULL, NULL);

insert into invoice values 
(NULL, (select id from account where client="709-555-1234"), 1234.50, 0.15, 1419.68, "2024-03-01");
