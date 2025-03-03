import numpy as np
import random

#Se definiran 5 carreras, 11=Sistemas, 12=Industrial, 13=Civil, 14=Electrica, 15= Electronica

class estudiante:
    def __init__(self, codigo, nombre, promAc, programa):
        self.codigo = codigo
        self.nombre = nombre
        self.promAc = promAc
        self.programa = programa
    
    def mensaje(self):
        print(f"Estudiante {self.codigo}, nombre: {self.nombre}")
        
totalEstudiantes = np.empty(6500, dtype=object)

nombres = ["Juan", "Roberto", "Ximena", "Juana", "Marisela", "Camilo"]

for i in range(6500):
    totalEstudiantes[i] = estudiante(random.randint(1960000, 2259999), random.choice(nombres), random.uniform(0.0,5.0), random.randint(11,15))
#Formato "Viejo" 1961XX 1961=1961, Formato "Nuevo" 225XXXX 225=2025 

arregloOrdenado = np.argsort([estudiante.promAc for estudiante in totalEstudiantes])[::-1]
arregloOrdenado = totalEstudiantes[arregloOrdenado]

print("***PARTE 1***")
print("Ingrese la carrera que desea elegir para verificar --> 11=Sistemas, 12=Industrial, 13=Civil, 14=Electrica, 15= Electronica")
carrera = int(input())
while (carrera < 11 and carrera >15):
    print("Porfavor ingrese un valor adecuado --> 11=Sistemas, 12=Industrial, 13=Civil, 14=Electrica, 15= Electronica")
    carrera = int(input())
acumuladora = 0
for i in totalEstudiantes:
    if(i.promAc >= 4.0 and i.programa == carrera):
        acumuladora = acumuladora + 1
        i.mensaje()

print("******************************************************************")
print(f"Fueron {acumuladora} estudiantes que cumplieron con la condición")
print("******************************************************************")

print()
print("***PARTE 2***")
acumuladora = 0
for i in totalEstudiantes:
    if(i.promAc >= 2.7 and i.promAc <3.2):
        temp = str(i.codigo)
        temp = temp[:3]
        if(int(temp)<=198):
            acumuladora = acumuladora + 1
            i.mensaje()

print("******************************************************************")
print(f"Fueron {acumuladora} estudiantes que cumplieron con la condición")
print("******************************************************************")
