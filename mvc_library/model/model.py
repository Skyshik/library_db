from mysql import connector

class Model:
    """
    *******************************************
    * A data model with MySQL for a library DB*
    *******************************************
    """
    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    """
    **************************
    *Zip methods             *
    **************************
    """
    def create_zip(self, zip, city, state):
        try:
            sql = 'INSERT INTO zips (`zip`, `z_city`, `z_state`) VALUES (%s, %s, %s)'
            vals = (zip, city, state)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_zip(self, zip):
        try:
            sql = 'SELECT * FROM zips WHERE zip = %s'
            vals = (zip,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_zips(self):
        try:
            sql = 'SELECT * FROM zips'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_zips_city(self, city):
        try:
            sql = 'SELECT * FROM zips WHERE z_city = %s'
            vals = (city,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_zip(self, fields, vals):
        try:
            sql = 'UPDATE zips SET '+','.join(fields)+' WHERE zip = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err 

    def delete_zip(self, zip):
        try: 
            sql = 'DELETE FROM zips WHERE zip = %s'
            vals = (zip,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    """
    **************************
    *Authors methods          *
    **************************
    """

    def create_author(self, fname, lname1, lname2, nationality):
        try: 
            sql = 'INSERT INTO authors (`a_fname`, `a_lname1`, `a_lname2`, `a_nationality`) VALUES (%s, %s, %s, %s)'
            vals = (fname, lname1, lname2, nationality)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_author(self, id_author):
        try:
            sql = 'SELECT * FROM authors WHERE id_author = %s'
            vals = (id_author,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_authors(self):
        try:
            sql = 'SELECT * FROM authors'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_authors_fname(self, fname):
        try:
            sql = 'SELECT * FROM authors WHERE a_fname = %s'
            vals = (fname,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_authors_lname1(self, lname1):
        try:
            sql = 'SELECT * FROM authors WHERE a_lname1 = %s'
            vals = (lname1,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_authors_nationality(self, nationality):                              
        try:
            sql = 'SELECT * FROM authors WHERE a_nationality = %s'
            vals = (nationality,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_author(self, fields, vals):
        try: 
            sql = 'UPDATE authors SET '+','.join(fields)+' WHERE id_author = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_author(self, id_author):
        try:
            sql = 'DELETE FROM authors WHERE id_author = %s'
            vals = (id_author,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    **************************
    *Users methods           *
    **************************
    """

    def create_user(self, fname, lname1, lname2, street, noexte, noint, col, zip, email, phone):
        try:
            sql = 'INSERT INTO users (`u_fname`, `u_lname1`, `u_lname2`, `u_street`, `u_noexte`, `u_noint`, `u_col`, `u_zip`, `u_email`, `u_phone`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
            vals = (fname, lname1, lname2, street, noexte, noint, col, zip, email, phone)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_user(self, id_user):
        try: 
            sql = 'SELECT users.*,zips.z_city,zips.z_state FROM users JOIN zips ON users.u_zip = zips.zip and users.id_user = %s'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_users(self):
        try:
            sql = 'SELECT users.*,zips.z_city,zips.z_state FROM users JOIN zips ON users.u_zip = zips.zip'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_users_zip(self, zip):
        try:
            sql = 'SELECT users.*,zips.z_city,zips.z_state FROM users JOIN zips ON users.u_zip = zips.zip and users.u_zip = %s'
            vals = (zip,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_user(self, fields, vals):
        try:
            sql = 'UPDATE users SET '+','.join(fields)+' WHERE id_user = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_user(self, id_user):
        try:
            sql = 'DELETE FROM users WHERE id_user = %s'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    """
    **************************
    *Books methods            *
    **************************
    """

    def create_book(self, title, genre, edition, editorial, author):
        try:
            sql = 'INSERT INTO books (`b_title`, `b_genre`, `b_edition`, `b_editorial`, `id_author`) VALUES (%s, %s, %s, %s, %s)'
            vals = (title, genre, edition, editorial, author)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_book(self, id_book):
        try:
            sql = 'SELECT books.*,authors.a_fname,authors.a_lname1 FROM books JOIN authors ON books.id_author = authors.id_author and books.id_book = %s'
            vals = (id_book,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_books(self):
        try:
            sql = 'SELECT books.*,authors.a_fname,authors.a_lname1 FROM books JOIN authors ON books.id_author = authors.id_author'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_book_title(self, title):
        try:
            sql = 'SELECT books.*,authors.a_fname,authors.a_lname1 FROM books JOIN authors ON books.id_author = authors.id_author and books.b_title = %s'
            vals = (title,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_book(self, fields, vals):
        try:
            sql = 'UPDATE books SET '+','.join(fields)+'WHERE id_book = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_book(self, id_book):
        try:
            sql = 'DELETE FROM books WHERE id_book = %s'
            vals = (id_book,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err 
    
    """
    **************************
    *Borrowings methods       *
    **************************
    """

    def create_borrowing(self, id_user, id_book, loanDate, returnDate):
        try:
            sql = 'INSERT INTO borrowings (`id_user`, `id_book`, `b_loanDate`,`b_returnDate`) VALUES (%s, %s, %s, %s)'
            vals = (id_user, id_book, loanDate, returnDate)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_borrowing(self, id_borrowing):
        try:
            sql = 'SELECT borrowings.*, users.*, books.* FROM borrowings JOIN users ON users.id_user = borrowings.id_user and borrowings.id_borrowing = %s JOIN books ON books.id_book = borrowings.id_book'
            vals = (id_borrowing,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_borrowings(self):
        try:
            sql = 'SELECT borrowings.*, users.*, books.* FROM borrowings JOIN users ON users.id_user = borrowings.id_user JOIN books ON books.id_book = borrowings.id_book'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_borrowing_loanDate(self, loanDate):
        try:
            sql = 'SELECT borrowings.*, users.*, books.* FROM borrowings JOIN users ON users.id_user = borrowings.id_user and borrowings.b_loanDate = %s JOIN books ON books.id_book = borrowings.id_book'
            vals = (loanDate,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_borrowing(self, fields, vals):
        try:
            sql = 'UPDATE borrowings SET '+','.join(fields)+' WHERE id_borrowing = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_borrowing(self, id_borrowing):
        try:
            sql = 'DELETE FROM borrowings WHERE id_borrowing = %s'
            vals = (id_borrowing,)
            self.cursor.execute(sql, vals) 
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err