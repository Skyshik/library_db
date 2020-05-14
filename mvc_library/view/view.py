class View:
    """
    ***************************
    * A view for a library DB *
    ***************************
    """
    def start(self):
        print('********************************')
        print('* ¡Bienvenido a la biblioteca! *')
        print('********************************')

    def end(self):
        print('********************************')
        print('*       ¡Nos vemos! :)         *')
        print('********************************')

    def main_menu(self):
        print('************************')
        print('* -- Menu Principal -- *')
        print('************************')
        print('1. CPs')
        print('2. Autores')
        print('3. Usuarios')
        print('4. Libros')
        print('5. Prestamos')
        print('6. Salir')

    def option(self, last):    
        print('Selecciona una opcion (1-'+last+'): ', end = '')

    def not_valid_option(self):
        print('¡Opcion no valida!\nIntenta de nuevo')
    
    def ask(self, output):
        print(output, end = '')

    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))

    def error(self, err):
        print(' ¡Error! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

    """
    **************************
    * Views for zips         *
    **************************
    """

    def zips_menu(self):
        print('********************')
        print('* -- Submenu CPs --*')
        print('********************')
        print('1. Agregar un CP')
        print('2. Mostrar un CP')
        print('3. Mostrar todos los CPs')
        print('4. Mostrar CPs de una ciudad')
        print('5. Actualizar un CP')
        print('6. Borrar un CP')
        print('7. Regresar')

    def show_a_zip(self, record):
        print(f'{record[0]:<6}|{record[1]:<35}|{record[2]:<35}')

    def show_zip_header(self, header):
        print(header.center(80,'*'))
        print('CP'.ljust(6)+'|'+'Ciudad'.ljust(35)+'|'+'Estado'.ljust(35))
        print('-'*80)

    def show_zip_midder(self):
        print('-'*80)

    def show_zip_footer(self):
        print('*'*80)
        
    """
    **************************
    * Views for author       *
    **************************
    """  

    def authors_menu(self):
        print('***********************')
        print('* -- Submenu Autor --*')
        print('***********************')
        print('1. Agregar un autor')
        print('2. Mostrar un autor')
        print('3. Mostrar todos los autores')
        print('4. Mostrar un autor por nombre')
        print('5. Mostrar un autor por apellido paterno')
        print('6. Mostrar autores por nacionalidad')
        print('7. Actualizar un autor')
        print('8. Borrar un autor')
        print('9. Regresar')

    def show_author(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Apellido Paterno:', record[2])
        print('Apellido Materno', record[3])
        print('Nacionalidad:', record[4])

    def show_author_brief(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1]+' '+record[2]+' '+record[3])

    def show_author_header(self, header):
        print(header.center(54,'+'))

    def show_author_midder(self):
        print('-'*54)

    def show_author_footer(self):
        print('*'*54)

    """
    **************************
    * Views for users         *
    **************************
    """

    def users_menu(self):
        print('*************************')
        print('* -- Submenu Usuarios --*')
        print('*************************')
        print('1. Agregar un usuario')
        print('2. Mostrar un usuario')
        print('3. Mostrar todos los usuarios')
        print('4. Mostrar usuarios por ciudad')
        print('5. Actualizar un usuario')
        print('6. Borrar un usuario')
        print('7. Regresar')

    def show_a_user(self,record):
        print('ID:', record[0])
        print('Nombre:', record[1])
        print('Apellido Paterno:', record[2])
        print('Apellido Materno:', record[3])
        print('Calle:', record[4])
        print('No. Exterior:', record[5])
        print('No. Interior:', record[6])
        print('Colonia:', record[7])
        print('Ciudad:', record[11])
        print('Estado:', record[12])
        print('Codigo Postal:', record[8])
        print('Email:', record[9])
        print('Telefono:', record[10])

    def show_a_user_brief(self, record):
        print('ID:', record[0])
        print('Nombre:', record[1]+' '+record[2]+' '+record[3])
        print('Direccion:', record[4]+' '+record[5]+' - '+record[6]+', '+record[7])
        print(record[11]+', '+record[12]+', '+record[8])
        print('Email:', record[9])
        print('Telefono:', record[10])

    def show_user_header(self, header):
        print(header.center(54,'*'))
        print('-'*54)

    def show_user_midder(self):
        print('-'*54)

    def show_user_footer(self):
        print('*'*54)

    """
    **************************
    * Views for books         *
    **************************
    """    

    def books_menu(self):
        print('***********************')
        print('* -- Submenu Libros --*')
        print('***********************')
        print('1. Agregar un libro')
        print('2. Mostrar un libro')
        print('3. Mostrar todos los libros')
        print('4. Mostrar un libro por titulo')
        print('5. Actualizar un libro')
        print('6. Borrar un libro')
        print('7. Regresar')

    def show_a_book(self, record):
        print('ID:', record[0])
        print('Titulo:', record[1])
        print('Genero:', record[2])
        print('Edicion:', record[3])
        print('Editorial:', record[4])
        print('Nombre del autor:', record[6])
        print('Apellido del autor:', record[7])

    def show_book_brief(self,record):
        print('ID:', record[0])
        print('Titulo:', record[1])

    def show_book_header(self, header):
        print(header.center(53,'*'))
        print('-'*53)

    def show_book_midder(self):
        print('-'*53)

    def show_book_footer(self):
        print('*'*53)

    """
    **************************
    * Views for borrowings    *
    **************************
    """  

    def borrowings_menu(self):
        print('**************************')
        print('* -- Submenu Prestamos --*')
        print('**************************')
        print('1. Agregar un prestamo')
        print('2. Mostrar un prestamo')
        print('3. Mostrar todos los prestamos')
        print('4. Mostrar los prestamos de un dia')
        print('5. Actualizar un prestamo')
        print('6. Borrar un prestamo')
        print('7. Regresar')

    def show_a_borrowing(self, record):
        print('ID Prestamo: ',record[0])
        print('ID Libro: ', record[2])
        print('Titulo: ', record[17])
        print('ID Usuario: ', record[1])
        print('Nombre: ', record[6])
        print('Apellido paterno: ', record[7])
        print('Apellido materno: ', record[8])
        print('Fecha de solicitud: ', record[3])
        print('Fecha de devolucion: ', record[4])

    def show_borrowing_header(self, header):
        print(header.center(55,'*'))
        print('-'*55)

    def show_borrowing_midder(self):
        print('-'*55)

    def show_borrowing_footer(self):
        print('*'*55)