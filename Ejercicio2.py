class Punto:
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)

    def eje_x(self):
        return(self.x)
    def eje_y(self):
        return(self.y)
    def punto(self):
        return(self.punto)
    def suma_eje_x(self,f):
        self.x += float(f) 
    def resta_eje_x(self,f):
        self.x -= float(f) 
    def suma_eje_y(self,f):
        self.y += float(f)
    def resta_eje_y(self,f):
        self.y -= float(f) 
    def impresion(self):
        print(f"El punto es: {self.punto}")
    def opuesto(self):
        opuesto_x = -self.x
        opuesto_y = -self.y
        punto_opuesto = (opuesto_x,opuesto_y)
        return(punto_opuesto)
    def __str__(self):
        return f"({self.x}, {self.y})"
    


