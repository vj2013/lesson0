class Caja:
    """Clase Caja para la realizar la operación de Volumen"""
    def __init__(self, largo, alto, ancho):
        self.largo = largo
        self.alto = alto
        self.ancho = ancho
    
    def caculaVolumen(self):
        """Se realiza la operación con los atributos de la clase"""
        return self.largo*self.alto*self.ancho

#Creamos dos objetos
caja = Caja(2,3,4)
caja2 = Caja(5,5,2)

print("El volumen es: ", caja.caculaVolumen())
print("El volumen2 es: ", caja2.caculaVolumen())