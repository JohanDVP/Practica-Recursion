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
    secuencias.append(nueva_secuencia)

    otra = input("¿Desea registrar otra?: (si/no)")

    if otra.lower() == "si":
        return registrar_secuencias(secuencias)

    return secuencias

#Punto 2

def contar_patrones(secuencia, patron, pos = 0, cont = 0):
    if pos > len(secuencia) - len(patron):
        return cont

    if secuencia[pos:pos + len(patron)] == patron:
        cont += 1

    return contar_patrones(secuencia, patron, pos + 1, cont)

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

def generar_subcadena(secuencia, longitud, pos = 0, resultado = None):
    if resultado is None:
        resultado = []

    if longitud <= 0 or longitud > len(secuencia):
        return resultado

    if pos > len(secuencia) - longitud:
        return resultado

    subcadena = secuencia[pos:pos + longitud]
    resultado.append(subcadena)

    return generar_subcadena(secuencia, longitud, pos + 1, resultado)

def generar_subcadena_lista(secuencias, longitud, pos = 0):
    if pos == len(secuencias):
        return

    current = secuencias[pos]

    subcadenas = generar_subcadena(current.secuencia, longitud)

    print(f"Muestra: {current.nombre} | Subcadenas: {subcadenas}")

    return generar_subcadena_lista(secuencias, longitud, pos + 1)

#Punto 5

def nucleotidos_a_t(secuencia, pos = 0):
    if pos == len(secuencia):
        return (0,0)

    cantidad_a, cantidad_t = nucleotidos_a_t(secuencia, pos + 1)

    if secuencia[pos] == "A":
        cantidad_a += 1

    elif secuencia[pos] == "T":
        cantidad_t += 1

    return cantidad_a, cantidad_t

def comparar_a_t(secuencia):
    a, t = nucleotidos_a_t(secuencia)

    if a > t:
        return "Tiene mas A que T."
    elif t > a:
        return "Tiene mas T que A."
    else:
        return "Tiene igual cantidad de A y T."

#Punto 6

def mutar_secuencia(secuencia, pos = 0):
    if pos == len(secuencia):
        return "", 0

    mutada, cantidad = mutar_secuencia(secuencia, pos + 1)

    if secuencia[pos] == "A":
        mutada = "T" + mutada
        cantidad += 1

    elif secuencia[pos] == "T":
        mutada = "A" + mutada
        cantidad += 1

    else:
        mutada = secuencia[pos] + mutada

    return mutada, cantidad

def print_mutaciones(secuencia):
    mutada, cantidad = mutar_secuencia(secuencia)

    print(f"Original: {secuencia} | Mutada: {mutada} | Mutaciones: {cantidad}")

#Punto 7

def buscar_patron(secuencia, patron, pos=0):
    if pos > len(secuencia) - len(patron):
        return False

    if secuencia[pos:pos + len(patron)] == patron:
        return True

    return buscar_patron(secuencia, patron, pos + 1)

def encontrar_secuencia(secuencias, riesgo_minimo, longitud_minima, patron, pos=0):
    if pos == len(secuencias):
        return None

    current = secuencias[pos]

    if current.riesgo >= riesgo_minimo and len(current.secuencia) >= longitud_minima and buscar_patron(current.secuencia, patron):
        return current.nombre

    return encontrar_secuencia(secuencias, riesgo_minimo, longitud_minima, patron, pos + 1)

def imprimir_secuencia_encontrada(secuencias, riesgo_minimo, longitud_minima, patron):
    resultado = encontrar_secuencia(secuencias, riesgo_minimo, longitud_minima, patron)

    if resultado is not None:
        print("Muestra encontrada:", resultado)
    else:
        print("No se encontró ninguna secuencia.")

#Punto 8

def eliminar_por_riesgo(secuencias, riesgo_minimo, pos = 0):
    if pos == len(secuencias):
        return

    if secuencias[pos].riesgo < riesgo_minimo:
        del secuencias[pos]
        return eliminar_por_riesgo(secuencias, riesgo_minimo, pos)

    return eliminar_por_riesgo(secuencias, riesgo_minimo, pos + 1)

def mostrar_secuencias(secuencias, pos=0):
    if pos == len(secuencias):
        return

    actual = secuencias[pos]

    print(f"ID: {actual.id}")
    print(f"Nombre: {actual.nombre}")
    print(f"Secuencia: {actual.secuencia}")
    print(f"Riesgo: {actual.riesgo}")
    print("--------------------")

    return mostrar_secuencias(secuencias, pos + 1)


def menu():
    print("\n===== SISTEMA DE ANALISIS DE ADN =====")
    print("1. Registrar secuencias")
    print("2. Contar patrones")
    print("3. Calcular riesgo promedio")
    print("4. Generar subcadenas")
    print("5. Comparar nucleotidos A y T")
    print("6. Simular mutacion genetica")
    print("7. Buscar secuencia por criterios")
    print("8. Eliminar secuencias de bajo riesgo")
    print("9. Mostrar todas las secuencias")
    print("0. Salir")
    print("======================================")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        registrar_secuencias(secuencias)

    elif opcion == "2":
        patron = input("Ingrese el patron que desea buscar: ")
        contar_patrones_lista(secuencias, patron)

    elif opcion == "3":
        if len(secuencias) == 0:
            print("No hay secuencias registradas.")
        else:
            promedio = calcular_riesgo(secuencias)
            print("El riesgo promedio es:", promedio)

    elif opcion == "4":
        longitud = int(input("Ingrese la longitud de las subcadenas: "))
        generar_subcadena_lista(secuencias, longitud)

    elif opcion == "5":
        secuencia = input("Ingrese la secuencia de ADN: ")
        print(comparar_a_t(secuencia))

    elif opcion == "6":
        secuencia = input("Ingrese la secuencia de ADN: ")
        print_mutaciones(secuencia)

    elif opcion == "7":
        riesgo = int(input("Ingrese el riesgo minimo: "))
        longitud = int(input("Ingrese la longitud minima: "))
        patron = input("Ingrese el patron que debe contener: ")

        imprimir_secuencia_encontrada(
            secuencias, riesgo, longitud, patron
        )

    elif opcion == "8":
        riesgo = int(input("Eliminar secuencias con riesgo menor a: "))
        eliminar_por_riesgo(secuencias, riesgo)
        print("Eliminacion completada.")

    elif opcion == "9":
        if len(secuencias) == 0:
            print("No hay secuencias registradas.")
        else:
            mostrar_secuencias(secuencias)

    elif opcion == "0":
        print("Saliendo del sistema.")
        return

    else:
        print("Opcion no valida.")

    return menu()


menu()

