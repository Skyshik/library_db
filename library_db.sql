#definicion del schema de la base de datos
#base de datos tienda
#crea db
DROP DATABASE IF EXISTS library;
CREATE DATABASE IF NOT EXISTS library;
#select the db to work with
use library;

	CREATE TABLE IF NOT EXISTS zips(
	zip VARCHAR(6) NOT NULL,
    z_city VARCHAR(35) NOT NULL,
    z_state VARCHAR(35) NOT NULL,
    PRIMARY KEY(zip)
    )ENGINE=INNODB;
	
	CREATE TABLE IF NOT EXISTS authors(
	id_author INT NOT NULL AUTO_INCREMENT,
    a_fname VARCHAR(35) NOT NULL,
	a_lname1 VARCHAR(35) NOT NULL,
	a_lname2 VARCHAR(35),
	a_nationality VARCHAR(35) NOT NULL,
	PRIMARY KEY (authorId)
    ) ENGINE= INNODB;
   
	CREATE TABLE IF NOT EXISTS users(
	id_user INT NOT NULL AUTO_INCREMENT,
    u_fname VARCHAR(35) NOT NULL,
    u_lname1 VARCHAR(35) NOT NULL,
    u_lname2 VARCHAR(35),
    u_street VARCHAR(35) NOT NULL,
    u_noexte VARCHAR(7) NOT NULL,
    u_noint VARCHAR(7),
    u_col VARCHAR(35),
    u_zip VARCHAR(6),
    u_email VARCHAR(35),
    u_phone VARCHAR(13),
    PRIMARY KEY (id_user),
    CONSTRAINT fkzip_client FOREIGN KEY(u_zip)
		REFERENCES zips(zip)
        ON DELETE SET NULL
        ON UPDATE CASCADE
) ENGINE=INNODB;
   
	CREATE TABLE IF NOT EXISTS books(
	id_book INT NOT NULL AUTO_INCREMENT,
    b_title VARCHAR(35) NOT NULL,
    b_genre VARCHAR(35) NOT NULL,
    b_edition VARCHAR(35) NOT NULL,
    b_editorial VARCHAR(35) NOT NULL,
    authorId INT NOT NULL,
	PRIMARY KEY (id_book),
    CONSTRAINT fkauthor_book FOREIGN KEY(id_author)
		REFERENCES authors(id_author)
        ON DELETE CASCADE
        ON UPDATE CASCADE
) ENGINE=INNODB;

	CREATE TABLE IF NOT EXISTS borrowings(
		id_borrowing INT NOT NULL AUTO_INCREMENT,
        id_user INT NOT NULL,
        id_book INT NOT NULL,
        b_loanDate VARCHAR(10) NOT NULL,
        b_returnDate VARCHAR(10) NOT NULL,       
        PRIMARY KEY(id_borrowing),
		CONSTRAINT fkuserId_b FOREIGN KEY(id_user)
		REFERENCES users(id_user)
			ON DELETE CASCADE
			ON UPDATE CASCADE,
		CONSTRAINT fkbookId_b FOREIGN KEY(id_book)
		REFERENCES books(id_book)
			ON DELETE CASCADE
			ON UPDATE CASCADE
)ENGINE= INNODB;

