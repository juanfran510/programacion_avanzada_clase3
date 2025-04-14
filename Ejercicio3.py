from Ejercicio2 import Punto

class Linea:
    def Linea(self,_punto_a=Punto,_punto_b=Punto):
        self._punto_a = _punto_a
        self._punto_b = _punto_b

    def mueve_derecha(self,f):
        self._punto_a.suma_eje_x(f)
        self._punto_b.suma_eje_x(f)
    def mueve_izquierda(self,f):
        self._punto_a.resta_eje_x(f)
        self._punto_b.resta_eje_x(f)
    def mueve_arriba(self,f):
        self._punto_a.suma_eje_y(f)
        self._punto_b.suma_eje_y(f)
    def mueve_abajo(self,f):
        self._punto_a.resta_eje_y(f)
        self._punto_b.resta_eje_y(f)

    def impresion(self):
        print(f'La linea va desde: "{self._punto_a}" hasta {self._punto_b}')



punto1 = Punto(2.1,8.3)
punto2 = Punto(3.5,1.1)
linea1 =Linea(punto1,punto2)
linea1.impresion()
linea1.mueve_derecha(2.3)
linea1.impresion()
