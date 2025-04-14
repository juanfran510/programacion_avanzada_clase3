

class Libro:
    class Persona:
        def __init__(self,nombre,apellido):
                self.nombre = nombre
                self.apellido = apellido
        def get_nombre_completo(self):
                return f"{self.nombre} {self.apellido}"
        def set_nombre(self,nuevo_nombre):
                self.nombre = nuevo_nombre
        def set_apellido(self,nuevo_apellido):
                self.apellido = nuevo_apellido
    def __init__(self,titulo,nombre_autor,apellido_autor,ISBN,paginas,edicion,ciudad,pais,editorial,fecha_de_edicion):
        self.titulo = titulo
        self.ISBN = ISBN
        self.paginas = paginas
        self.edicion = edicion
        self.lugar = f"{ciudad} ({pais})"
        self.editorial = editorial
        self.fecha_de_edicion = fecha_de_edicion
        self.autor = self.Persona(nombre_autor,apellido_autor)


    
    def get_libro(self):
        print(f"Título: {self.titulo} {self.edicion}")
        print(f"Autor: {self.autor.get_nombre_completo()}")
        print(f"ISBN: {self.ISBN}")
        print(f"{self.editorial}, {self.lugar}")
        print(f"{self.fecha_de_edicion}")
        print(f"{self.paginas} páginas")

    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def set_autor(self, nuevo_autor):
        self.autor = nuevo_autor

    def set_ISBN(self, nuevo_ISBN):
        self.ISBN = nuevo_ISBN

    def set_paginas(self, nuevas_paginas):
        self.paginas = nuevas_paginas

    def set_edicion(self, nueva_edicion):
        self.edicion = nueva_edicion

    def set_editorial(self, nueva_editorial):
        self.editorial = nueva_editorial

    def set_lugar(self, nueva_ciudad, nuevo_pais):
        self.lugar = f"{nueva_ciudad} ({nuevo_pais})"

    def set_fecha_de_edicion(self, nueva_fecha):
        self.fecha_de_edicion = nueva_fecha