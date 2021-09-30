# La POO es un paradigma no soportado 
# originalmente por python, python maneja 
# el paradigma imperativo. 

# Python simula POO con la declaracion de clases y 
# ha ciendo referencia a un objeto de forma circular.

# Forma 1
''' 
class <Nombre de la clase>:
      <definicion del cuerpo de la clase>
'''
# Forma 2
'''
class <nombre de la clase>(<Super clase>):
      <DEfinicion del cuerpo de la clase>  
'''

# El constructor se define siempre con el metodo __init__()
# (Doble guion bajo antes y despues de init)

# La declaracion de atributos se realiza por medio de el constructor
# Para hacer encapsulamieto de metodos.......

class Persona:
    def__init__( self , n , e , est ):
    self.nombre = n
    self.edad = e
    self.estatura = est

    def to_string( self ):
        return "Nombre: " + self.nombre + "Edad: " + str(self.edad)

per = Persona("Edgar", 19, 1.87)
print(per.to_string())


###################

Class Estudiante (Perosna):
      def__init__(self, nc, nombre, edad, est):
            self.__num_cta = nc
            super().__init__(nombre,edad,est)

      def to_string(self):
            return super().to_string() + "numero de cta.:" + self__num_cta

est = Estudiante ("318082321", "Edgar", 19, 1.87)
print(est.to_string())
