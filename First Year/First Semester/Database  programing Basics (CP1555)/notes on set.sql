CREATE TABLE route (
    route_id integer not null auto_increment primary key,
    route_name varchar(40),
    stops SET("St. John's", 'Whitbourne', 'Avondale', 'Brigus', 'Bay Roberts', 'Harbour Grace', 'Carbonear', 'Come by Chance', 'Clarenville', 'Bay Verte', 'Fogo', 'Twillingate', "Morton's Harbour")
    );
    
insert into route (route_name, stops) values
    ('direct', ("St. John's,Clarenville")),
    ('TCH', ("St. John's,Whitbourne,Come by Chance,Clarenville")),
    ('CBN', ("St. John's,Bay Roberts,Harbour Grace,Carbonear")),
    ('Stix', ("St. John's,Clarenville,Fogo")),
    ('Jig', ("Fogo,Twillingate,Morton's Harbour"));
    
select * from route where stops like "%Clarenville%";
select * from route where FIND_IN_SET('Clarenville', stops)>0;

insert into route (route_name, stops) values ('airports', ("St. John's"));

select * from route where route_name = 'airports';

alter table route modify stops set (
    "St. John's", 'Whitbourne', 'Avondale', 'Brigus', 'Bay Roberts', 'Harbour Grace', 'Carbonear',
    'Come by Chance', 'Clarenville', 'Bay Verte', 'Fogo', 'Twillingate', "Morton's Harbour",
    "Gander", "Dearlake", "Cornerbrook", "Stephenville", "Port aux Basque");
    
update route set stops = CONCAT(stops, ",Gander,Dearlake,Stephenville") where route_name = 'airports';
select * from route where route_name = 'airports';

select * from route where stops like "%,Gander%";