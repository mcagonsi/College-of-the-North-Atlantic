use `bookstore-1nf`;
CREATE TABLE `the books` (
  `title` varchar(255) NOT NULL,
  `isbn` varchar(15) NOT NULL,
  `publisher-name` varchar(45) NOT NULL,
  `publisher-location` varchar(255) NOT NULL,
  `publisher-url` varchar(80) DEFAULT NULL,
  `publication-date` date NOT NULL,
  `author-name` varchar(255) NOT NULL,
  `author-birthdate` date NOT NULL,
  `author-location` varchar(255) NOT NULL,
  `pages` int DEFAULT NULL,
  `url` varchar(80) DEFAULT NULL,
  `category` varchar(45) DEFAULT NULL,
  `format` varchar(45) NOT NULL,
  `price` decimal(6,2) NOT NULL,
  `edition` varchar(45) DEFAULT NULL
);

SELECT * FROM book;