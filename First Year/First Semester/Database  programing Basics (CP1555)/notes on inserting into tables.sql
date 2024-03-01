use bookstore;

-- Question 1
insert into author(first_name, last_name, birth_date)
values('Michael', 'Agonsi', '2000-04-19');

insert into book (isbn,title,category,published)
values (183787, 'The Importance of Database', 'Computers', '2023-11-20');

insert into book_author( isbn, author_id)
values(183787, 4);
 
 
 -- Question 2
insert into book (isbn, title, category, published)
value (183780, 'Cooking by Numbers', 'cooking', '2023-11-19');

insert into book_author(isbn,author_id)
values (183780,1);


-- Question  3
update book
set title = 'Bicycle Racing (2nd Edition)', published = '2023-11-19'
where isbn = 111512 ;



-- Question 4
delete from book
where isbn = 111745;

delete from book_author
where book_author_id = 5;


-- Question 5
insert into author (first_name, last_name, birth_date)
values ('Joel', 'Murach', '1968-05-23');
insert into book (isbn, title, category, published) VALUES
(1943872368, 'Murach''s MySQL (3rd Edition)','computers', '2019-03-22');
insert into book_author(isbn,author_id)
values (1943872368,5);