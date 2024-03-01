create database bookstore;
use bookstore;

create table book (
	isbn int PRIMARY KEY NOT NULL,
    title varchar(255),
    category varchar(255),
    published date
);


create table author (
	author_id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    first_name varchar(255),
    last_name varchar(255),
    birth_date date
);

create table if not exists book_author (
	book_author_id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
    isbn int,
    author_id int
);

INSERT into book(isbn, title, category, published) values(111919, 'Cooking Pros', 'cooking', '2001-11-04');
INSERT into book(isbn, title, category, published) values(111512, 'Bicycle Racing', 'sports', '2002-11-03');
INSERT into book(isbn, title, category, published) values(111545, 'Database Pros', 'computers', '2001-10-13');
INSERT into book(isbn, title, category, published) values(111632, 'Python Programming', 'computers', '2000-01-02');
INSERT into book(isbn, title, category, published) values(111745, 'Space adventures', 'science-fiction', '1998-04-02');

INSERT into author(author_id, first_name, last_name, birth_date) values(1, 'Jill', 'Jones', '2000-11-04');
INSERT into author(author_id, first_name, last_name, birth_date) values(2, 'James', 'Peters', '1999-10-05');
INSERT into author(author_id, first_name, last_name, birth_date) values(3, 'Jason', 'Lang', '1997-06-08');

INSERT INTO book_author(book_author_id, isbn, author_id) VALUES(1, 111919, 1);
INSERT INTO book_author(book_author_id, isbn, author_id) VALUES(2, 111512, 2);
INSERT INTO book_author(book_author_id, isbn, author_id) VALUES(3, 111545, 1);
INSERT INTO book_author(book_author_id, isbn, author_id) VALUES(4, 111632, 1);
INSERT INTO book_author(book_author_id, isbn, author_id) VALUES(5, 111745, 3);





