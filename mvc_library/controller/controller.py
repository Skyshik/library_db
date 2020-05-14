from model.model import Model
from view.view import View
from datetime import date

class Controller:
    """
    *******************************
    * A controller for library DB *
    *******************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def start(self):
        self.view.start()
        self.main_menu()
    
    """
    ***********************
    * General Controllers *
    ***********************
    """
    def main_menu(self):
        o = '0'
        while o != '6':
            self.view.main_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.zips_menu()
            elif o == '2':
                self.authors_menu()
            elif o == '3':
                self.users_menu()
            elif o == '4':
                self.books_menu()
            elif o == '5':
                self.borrowings_menu()
            elif o == '6':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def update_list(self, fs, vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v != '':
                fields.append(f+' =%s')
                vals.append(v)
        return fields,vals

    """
    ************************
    * Controllers for zips *
    ************************
    """
    def zips_menu(self):
        o = '0'
        while o != '7':
            self.view.zips_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_zip()
            elif o == '2':
                self.read_zip()
            elif o == '3':
                self.read_all_zips()
            elif o == '4':
                self.read_zips_city()
            elif o == '5':
                self.update_zip()
            elif o == '6':
                self.delete_zip()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return
 
    def ask_zip(self):
        self.view.ask('Ciudad: ')
        city = input()
        self.view.ask('Estado: ')
        state = input()
        return [city,state]

    def create_zip(self):
        self.view.ask('CP: ')
        i_zip = input()
        city, state = self.ask_zip()
        out = self.model.create_zip(i_zip, city, state)
        if out == True:
            self.view.ok(i_zip, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL CP ESTA REPETIDO')
            else:
                self.view.error('NO SE PUDO AGREGAR EL CP. REVISA.')
        return

    def read_zip(self):
        self.view.ask('CP: ')
        i_zip = input()
        zip = self.model.read_zip(i_zip)
        if type(zip) == tuple:
            self.view.show_zip_header('Datos del CP '+i_zip+' ')
            self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            if zip == None:
                self.view.error('EL CP NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL CP. REVISA.')
        return

    def read_all_zips(self):
        zips = self.model.read_all_zips()
        if type(zips) == list:
            self.view.show_zip_header('Todos los CPs')
            for zip in zips:
                self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            self.view.error('PROBLEMA AL LEER TODOS LOS CPs. REVISA.')
        return

    def read_zips_city(self):
        self.view.ask('Ciudad: ')
        city = input()
        zips = self.model.read_zips_city(city)
        if type(zips) == list:
            self.view.show_zip_header(' CPs para la ciudad de '+city+' ')
            for zip in zips:
                self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else: 
            self.view.error('PROBLEMA AL LEER LOS CPs. REVISA')
        return

    def update_zip(self):
        self.view.ask('CP a modificar: ')
        i_zip = input()
        zip = self.model.read_zip(i_zip)
        if type(zip) == tuple:
            self.view.show_zip_header('Datos del CP '+i_zip+' ')
            self.view.show_a_zip(zip)
            self.view.show_zip_midder()
            self.view.show_zip_footer()
        else:
            if zip == None:
                self.view.error('EL CP NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL CP. REVISA.')
            return
        self.view.msg('Ingrese los valores a modificar(vacio para dejarlo igual):')
        whole_vals = self.ask_zip()
        fields, vals = self.update_list(['z_city','z_state'], whole_vals)
        vals.append(i_zip)
        vals = tuple(vals)
        out = self.model.update_zip(fields, vals)
        if out == True:
            self.view.ok(i_zip, 'actualizado')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL CP. REVISA')
        return

    def delete_zip(self):
        self.view.ask('CP a borrar: ')
        i_zip = input()
        count = self.model.delete_zip(i_zip)
        if count != 0:
            self.view.ok(i_zip, 'borro')
        else:
            if count == 0:
                self.view.error('EL CP NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR EL CP. REVISA.')
        return

    """
    **************************
    * Controllers for authors *
    **************************
    """
    def authors_menu(self):
        o = '0'
        while o != '9':
            self.view.authors_menu()
            self.view.option('9')
            o = input()
            if o == '1':
                self.create_author()
            elif o == '2':
                self.read_an_author()
            elif o == '3':
                self.read_all_authors()
            elif o == '4':
                self.read_authors_fname()
            elif o == '5':
                self.read_authors_lname1()
            elif o == '6':
                self.read_authors_nationality()
            elif o == '7':
                self.update_author()
            elif o == '8':
                self.delete_author()
            else:
                self.view.not_valid_option()
        return

    def ask_author(self):
        self.view.ask('Nombre: ')
        fname = input()
        self.view.ask('Apellido paterno: ')
        lname1 = input()
        self.view.ask('Apellido materno: ')
        lname2 = input()
        self.view.ask('Nacionalidad: ')
        nationality = input()
        return[fname,lname1,lname2,nationality]

    def create_author(self):
        fname, lname1, lname2, nationality = self.ask_author()
        out = self.model.create_author(fname, lname1, lname2, nationality)
        if out == True:
            self.view.ok(fname+' '+lname1+' '+lname2, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL AUTOR. REVISA')
        return

    def read_an_author(self):
        self.view.ask('ID del autor: ')
        id_author = input()
        author = self.model.read_author(id_author)
        if type(author) == tuple:
            self.view.show_author_header('Datos del autor '+id_author+' ')
            self.view.show_author(author)
            self.view.show_author_midder()
            self.view.show_author_footer()
        else:
            if author == None:
                self.view.error('EL AUTOR NO EXISTE')
            else:
                self.view.error('PROBLEMAS AL LEER EL AUTOR. REVISA')
        return

    def read_all_authors(self):
        authors = self.model.read_all_authors()
        if type(authors) == list:
            self.view.show_author_header('Todos los autores ')
            for author in authors:
                self.view.show_author(author)
                self.view.show_author_midder()
            self.view.show_author_footer()
        else:
            self.view.error('PROBLEMAS AL LEER TODOS LOS AUTORES. REVISA.')
        return

    def read_authors_fname(self):
        self.view.ask('Nombre del autor: ')
        fname = input()
        authors = self.model.read_authors_fname(fname)
        if type(authors) == list:
            self.view.show_author_header('Autores con el nombre '+fname+' ')
            for author in authors:
                self.view.show_author(author)
                self.view.show_author_midder()
            self.view.show_author_footer()
        else:
            self.view.error('PROBLEMAS AL LEER LOS AUTORES. REVISA.')
        return

    def read_authors_lname1(self):
        self.view.ask('Apellido paterno del autor: ')
        lname1 = input()
        authors = self.model.read_authors_lname1(lname1)
        if type(authors) == list:
            self.view.show_author_header('Autores con el apellido '+lname1+' ')
            for author in authors:
                self.view.show_author(author)
                self.view.show_author_midder()
            self.view.show_author_footer()
        else:
            self.view.error('PROBLEMAS AL LEER LOS AUTORES. REVISA.')
        return

    def read_authors_nationality(self):
        self.view.ask('Nacionalidad del autor: ')
        nationality = input()
        authors = self.model.read_authors_nationality(nationality)
        if type(authors) == list:
            self.view.show_author_header('Autores de nacionalidad '+nationality+' ')
            for author in authors:
                self.view.show_author(author)
                self.view.show_author_midder()
            self.view.show_author_footer()
        else:
            self.view.error('PROBLEMAS AL LEER LOS AUTORES. REVISA.')
        return

    def update_author(self):
        self.view.ask('ID del autor a modificar: ')
        id_author = input()
        author = self.model.read_author(id_author)
        if type(author) == tuple:
            self.view.show_author_header('Datos del autor '+id_author+' ')
            self.view.show_author(author)
            self.view.show_author_midder()
            self.view.show_author_footer()
        else:
            if author == None:
                self.view.error('EL AUTOR NO EXISTE')
            else:
                self.view.error('PROBLEMAS AL LEER EL AUTOR. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar(vacio para dejarlo igual):')
        whole_vals = self.ask_author()
        fields, vals = self.update_list(['a_fname','a_lname1','a_lname2','a_nationality'], whole_vals)
        vals.append(id_author)
        vals = tuple(vals)
        out = self.model.update_author(fields, vals)
        if out == True:
            self.view.ok(id_author, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL AUTOR. REVISA')
        return

    def delete_author(self):
        self.view.ask('ID del autor a eliminar: ')
        id_author = input()
        count = self.model.delete_author(id_author)
        if count != 0:
            self.view.ok(id_author, 'borro')
        else:
            if count == 0:
                self.view.error('EL AUTOR NO EXISTE.')
            else:
                self.view.error('PROBLEMAS AL BORRAR EL AUTOR. REVISA')
        return

    """
    *************************
    * Controllers for users *
    *************************
    """
    def users_menu(self):
        o = '0'
        while o != '7':
            self.view.users_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_user()
            elif o == '2':
                self.read_user()
            elif o == '3':
                self.read_all_users()
            elif o == '4':
                self.read_users_zip()
            elif o == '5':
                self.update_user()
            elif o == '6':
                self.delete_user()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_user(self):
        self.view.ask('Nombre: ')
        fname = input()
        self.view.ask('Apellido paterno: ')
        lname1 = input()
        self.view.ask('Apellido materno: ')
        lname2 = input()
        self.view.ask('Calle: ')
        street = input()
        self.view.ask('No exterior: ')
        noexte = input()
        self.view.ask('No interior: ')
        noint = input()
        self.view.ask('Colonia: ')
        col = input()
        self.view.ask('CP: ')
        zip = input()
        self.view.ask('Email: ')
        email = input()
        self.view.ask('Telefono: ')
        phone = input()
        return [fname,lname1,lname2,street,noexte,noint,col,zip,email,phone]

    def create_user(self):
        fname, lname1, lname2, street, noexte, noint, col, zip, email, phone = self.ask_user()
        out = self.model.create_user(fname, lname1, lname2, street, noexte, noint, col, zip, email, phone)
        if out == True:
            self.view.ok(fname+' '+lname1+' '+lname2, 'agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR EL USUARIO. REVISA.')
        return
    
    def read_user(self):
        self.view.ask('ID usuario: ')
        id_user = input()
        user = self.model.read_user(id_user)
        if type(user) == tuple:
            self.view.show_user_header('Datos del usuario '+id_user+' ')
            self.view.show_a_user(user)
            self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            if user == None:
                self.view.error('EL USUARIO NO EXISTE')
            else:
                self.view.error('PROBLEMAS AL LEER EL USUARIO. REVISA.')
        return
    
    def read_all_users(self):
        users = self.model.read_all_users()
        if type(users) == list:
            self.view.show_user_header('Todos los clientes')
            for user in users:
                self.view.show_a_user(user)
                self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            self.view.error('PROBLEMAS AL LEER TODOS LOS USUARIOS. REVISA.')
        return

    def read_users_zip(self):
        self.view.ask('CP: ')
        zip = input()
        users = self.model.read_users_zip(zip)
        if type(users) == list:
            self.view.show_user_header('Usuarios en el CP '+zip+' ')
            for user in users:
                self.view.show_a_user(user)
                self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            self.view.error('PROBLEMAS AL LEER LOS USUARIOS. REVISA.')
        return

    def update_user(self):
        self.view.ask('Usuario a actualizar: ')
        id_user = input()
        user = self.model.read_user(id_user)
        if type(user) == tuple:
            self.view.show_user_header('Datos del usuario '+id_user+' ')
            self.view.show_a_user(user)
            self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            if user == None:
                self.view.error('EL USUARIO NO EXISTE')
            else:
                self.view.error('PROBLEMAS AL LEER EL USUARIO. REVISA.')
            return
        self.view.msg('Ingresa los datos a modificar(vacio para dejarlo igual):')
        whole_vals = self.ask_user()
        fields, vals = self.update_list(['u_fname', 'u_lname1', 'u_lname2', 'u_street', 'u_noexte', 'u_noint', 'u_zip', 'u_email', 'u_phone'], whole_vals)
        vals.append(id_user)
        vals = tuple(vals)
        out = self.model.update_user(fields, vals)
        if out == True:
            self.view.ok(id_user,'actualizo')
        else:
            self.view.error('PROBLEMAS AL ACTUALIZAR EL USUARIO. REVISA.')
        return

    def delete_user(self):
        self.view.ask('ID del usuario a borrar: ')
        id_user = input()
        count = self.model.delete_user(id_user)
        if count != 0:
            self.view.ok(id_user, 'borro')
        else:
            if count == 0:
                self.view.error('EL USUARIO NO EXISTE')
            else:
                self.view.error('PROBLEMAS AL BORRAR EL USUARIO. REVISA.')
        return

    """
    *************************
    * Controllers for books *
    *************************
    """

    def books_menu(self):
        o = '0'
        while o != '7':
            self.view.books_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_book()
            elif o == '2':
                self.read_book()
            elif o == '3':
                self.read_all_books()
            elif o == '4':
                self.read_book_title()
            elif o == '5':
                self.update_book()
            elif o == '6':
                self.delete_book()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_book(self):
        self.view.ask('Nombre de Libro: ')
        book = input()
        self.view.ask('Genero: ')
        genre = input()
        self.view.ask('Edicion: ')
        edition = input()
        self.view.ask('Editorial: ')
        editorial = input()
        self.view.ask('Autor: ')
        author = input()
        return [book,genre,edition,editorial,author]

    def create_book(self):
        book, genre, edition, editorial, author = self.ask_book()
        out = self.model.create_book(book, genre, edition, editorial, author)
        if out == True:
            self.view.ok(book, 'agrego')    
        else:
            self.view.error('NO SE PUDO AGREGAR EL LIBRO. REVISA.')
        return

    def read_book(self):
        self.view.ask('ID del libro: ')
        id_book = input()
        book = self.model.read_book(id_book)
        if type(book) == tuple:
            self.view.show_book_header('Datos del libro'+id_book+' ')
            self.view.show_a_book(book)
            self.view.show_book_midder()
            self.view.show_book_footer()
        else:
            if book == None:
                self.view.error('EL LIBRO NO EXISTE.')
            else:
                self.view.error('PROBLEMA AL LEER EL LIBRO. REVISA.')
        return

    def read_all_books(self):
        books = self.model.read_all_books()
        if type(books) == list:
            self.view.show_book_header('TODOS LOS LIBROS')
            for book in books:
                self.view.show_a_book(book)
                self.view.show_book_midder()
            self.view.show_book_footer()
        else:
            self.view.error('PROBLEMA AL LEER TODOS LOS LIBROS. REVISA')
        return

    def read_book_title(self):
        self.view.ask('Nombre del libro:')
        title = input()
        books = self.model.read_book_title(title)
        if type(books) == list:
            self.view.show_book_header('Datos del libro '+title+' ')
            for book in books:
                self.view.show_a_book(book)
                self.view.show_book_midder()
            self.view.show_book_footer()
        else:
            self.view.error('PROBLEMAS AL LEER LOS LIBROS. REVISA')
        return

    def update_book(self):
        self.view.ask('ID del libro a modificar: ')
        id_book = input()
        book = self.model.read_book(id_book)
        if type(book) == tuple:
            self.view.show_book_header('Datos del libro'+id_book+' ')
            self.view.show_a_book(book)
            self.view.show_book_midder()
            self.view.show_book_footer()
        else:
            if book == None:
                self.view.error('EL LIBRO NO EXISTE')
            else:
                self.view.error('PROBLEMAS AL LEER EL LIBRO. REVISA')
            return
        self.view.msg('Ingresa los valores a modificar(vacio para dejarlo igual):')
        whole_vals = self.ask_book()
        fields, vals = self.update_list(['b_title', 'b_genre', 'b_edition', 'b_editorial', 'id_author'], whole_vals)
        vals.append(id_book)
        vals = tuple(vals)
        out = self.model.update_book(fields, vals)
        if out == True:
            self.view.ok(id_book, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL PRODUCTO. REVISA')
        return

    def delete_book(self):
        self.view.ask('Id del libro a borrar: ')
        id_book = input()
        count = self.model.delete_book(id_book)
        if count != 0:
            self.view.ok(id_book, 'borro')
        else:
            self.view.error('PROBLEMA AL BORRAR EL LIBRO. REVISA')
        return

    """
    ******************************
    * Controllers for borrowings *
    ******************************
    """
    def borrowings_menu(self):
        o = '0'
        while o != '7':
            self.view.borrowings_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_borrowing()
            elif o == '2':
                self.read_borrowing()
            elif o == '3':
                self.read_all_borrowings()
            elif o == '4':
                self.read_borrowing_loanDate()
            elif o == '5':
                self.update_borrowing()
            elif o == '6':
                self.delete_borrowing()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_borrowing(self):
        self.view.ask('ID usuario: ')
        id_user = input()
        self.view.ask('ID libro: ')
        id_book = input()
        today = date.today()
        loanDate = today.strftime('%d-%m-%y')
        self.view.ask('Fecha de devolucion: ')
        returnDate = input()
        return [id_user, id_book, loanDate, returnDate]

    def create_borrowing(self):
        id_user, id_book, loanDate, returnDate = self.ask_borrowing()
        out = self.model.create_borrowing(id_user, id_book, loanDate, returnDate)
        if out == True:
            self.view.ok(id_user+' '+id_book, 'agrego')
        else:
            self.view.error('NO SE PUDO CREAR EL PRESTAMO. REVISA.')
        return
        
    def read_borrowing(self):
        self.view.ask('ID de prestamo: ')
        id_borrowing = input()
        borrowing = self.model.read_borrowing(id_borrowing)
        if type(borrowing) == tuple:
            self.view.show_borrowing_header('Datos del prestamo '+id_borrowing+' ')
            self.view.show_a_borrowing(borrowing)
            self.view.show_borrowing_midder()
            self.view.show_borrowing_footer()
        else:
            if borrowing == None:
                self.view.error('EL PRESTAMO NO EXISTE.')
            else:
                self.view.error('PROBLEMAS AL LEER EL PRESTAMO. REVISA.')
        return  

    def read_all_borrowings(self):
        borrowings = self.model.read_all_borrowings()
        if type(borrowings) == list:
            self.view.show_borrowing_header('Todos los prestamos')
            for borrowing in borrowings:
                self.view.show_a_borrowing(borrowing)
                self.view.show_borrowing_midder()
            self.view.show_borrowing_footer()
        else:
            self.view.error('PROBLEMAS AL LEER TODOS LOS PRESTAMOS. REVISA')
        return  

    def read_borrowing_loanDate(self):
        self.view.ask('Fecha de solicitud: ')
        loanDate = input()
        borrowings = self.model.read_borrowing_loanDate(loanDate)
        if type(borrowings) == list:
            self.view.show_borrowing_header('Todos los prestamos del dia '+loanDate+' ')
            for borrowing in borrowings:
                self.view.show_a_borrowing(borrowing)
                self.view.show_borrowing_midder()
            self.view.show_borrowing_footer()
        else:
            self.view.error('PROBLEMAS AL LEER LOS PRESTAMOS. REVISA')
        return
    
    def update_borrowing(self):
        self.view.ask('ID del prestamo a modificar: ')
        id_borrowing = input()
        borrowing = self.model.read_borrowing(id_borrowing)
        if type(borrowing) == tuple:
            self.view.show_borrowing_header('Datos del prestamo '+id_borrowing+' ')
            self.view.show_a_borrowing(borrowing)
            self.view.show_borrowing_midder()
            self.view.show_borrowing_footer()
        else:
            if borrowing == None:
                self.view.error('EL PRESTAMO NO EXISTE.')
            else:
                self.view.error('PROBLEMAS AL LEER EL PRESTAMO. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar(vacio para dejarlo igual):')
        whole_vals = self.ask_borrowing()
        fields, vals = self.update_list(['id_user', 'id_book', 'b_loanDate', 'b_returnDate'], whole_vals)
        vals.append(id_borrowing)
        vals = tuple(vals)
        out = self.model.update_borrowing(fields, vals)
        if out == True:
            self.view.ok(id_borrowing, 'actualizo')
        else:
            self.view.error('NO SE PUDO MODIFICAR EL PRESTAMO. REVISA.')
        return

    def delete_borrowing(self):
        self.view.ask('ID del prestamo a eliminar: ')
        id_borrowing = input()
        count = self.model.delete_borrowing(id_borrowing)
        if count != 0:
            self.view.ok(id_borrowing, 'borro')
        else:
            if count == 0:
                self.view.error('EL PRESTAMO NO EXISTE')
            else:
                self.view.error('PROBLEMAS AL BORRAR EL PRESTAMO. REVISA.')
        return