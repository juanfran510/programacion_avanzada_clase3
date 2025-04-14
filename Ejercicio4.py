

class Cancion:
    def cancion(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor
    def get_titulo(self):
        return self.titulo
    def get_autor(self):
        return self.autor
    def set_titulo(self,nombre):
        self.titulo = nombre
    def set_autor(self,nombre):
        self.autor = nombre