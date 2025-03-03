import numpy as np
import random

class aspiranteCSU:
    def __init__(self, numero, votos=0):
        self.numero = numero
        self.votos = votos
    
    def impresion(self):
        print(f"Aspirante con el id: {self.numero} posee {self.votos} de votos")
    
vectorAspirantes = np.empty(30, dtype=object)

for i in range(30):
    vectorAspirantes[i] = aspiranteCSU(i+1)
votantes = 5000

for i in range(30):
    temp = random.randint(0,votantes)
    votantes = votantes-temp
    vectorAspirantes[i].votos = temp

arregloOrdenado = np.argsort([aspirante.votos for aspirante in vectorAspirantes])[::-1]
arregloOrdenado = vectorAspirantes[arregloOrdenado]

print("***A CONTINUACION SE PRESENTAN LOS DATOS ORDENADOS DE MANERA DESCENDENTE***")
for i in range(30):
    arregloOrdenado[i].impresion()