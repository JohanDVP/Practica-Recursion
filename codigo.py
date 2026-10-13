class ADN:
    def __init__(self, id, nombre, secuencia, riesgo):
        self.id = id
        self.nombre = nombre
        self.secuencia = secuencia
        self.riesgo = riesgo

secuencias = []

#Punto 1

def registrar_secuencias(secuencias):
    id = int(input("Ingrese el ID: "))
    nombre = input("Ingrese el nombre: ")
    secuencia = input("Ingrese la secuencia: ")
    riesgo = int(input("Ingrese el nivel de riesgo: "))

    nueva_secuencia = ADN(id, nombre, secuencia, riesgo)
    secuencia.append(nueva_secuencia)

    otra = input("¿Desea registrar otra?: (si/no)")

    if otra.lower() == "si":
        return registrar_secuencias(secuencias)

    return secuencias

#Punto 2

def contar_patrones(secuencia, patron, pos = 0, cont = 0):
    if pos > len(secuencia) - len(patron):
        return cont

    if secuencia[pos:pos + len(patron)] == patron:
        contador = contador + 1

    return contar_patrones(secuencia, patron, pos + 1, contador)

def contar_patrones_lista(secuencias, patron, pos = 0):
    if pos == len(secuencias):
        return

    current = secuencias[pos]

    cantidad = contar_patrones(current.secuencia, patron)

    print(current.nombre, cantidad)

    return contar_patrones_lista(secuencias, patron, pos + 1)

#Punto 3

def calcular_riesgo(secuencias, pos  = 0, suma = 0):
    if pos == len(secuencias):
        return (suma / len(secuencias))

    current = secuencias[pos]

    suma += current.riesgo

    return calcular_riesgo(secuencias, pos + 1, suma)

#Punto 4






