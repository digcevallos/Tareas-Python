# Ejercicio 1: Definir una Clase
class Animal:
    
    def __init__(self, raza, genero):
        self.raza = raza
        self.genero = genero
                
    def informacion(self):
        print(f"El animal, es: {self.raza}, y tiene de género: {self.genero}")

p1 = Animal("Leopardo", "Masculino")
p1.informacion()

print()

p2 = Animal("Capibara", "Femenino")
p2.informacion()

print()

# Ejercicio 2: Trabajar con Atributos y Métodos
class Coche:
    def __init__(self, marca, acelerar):
        self.marca = marca
        self.acelerar = acelerar
    
    def mi_vehiculo(self):
        print('Acelera el vehiculo a: ')


mi_auto = Coche('Kia', 150)
print(mi_auto.marca)
mi_auto.mi_vehiculo()
print()

mi_auto2 = Coche ('BD', 200)
print(mi_auto2.acelerar)
print()

# Ejercicio 3: Crear una Clase con Múltiples Métodos
class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        self.resultado = 0

    def sumar(self):
        return self.numero1 + self.numero2

    def restar(self):
        return self.numero1 - self.numero2

s = Calculadora (10, 5)
print("El resultado de la suma es: ", s.sumar())

r = Calculadora (10, 5)
print("El resultado de la resta es: ", r.restar())
