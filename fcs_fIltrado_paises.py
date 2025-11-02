import csv
import unicodedata

RUTA_ARCHIVO = "ARCHIVO_PAISES\\paises.csv"

def quitar_tildes(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

#------------------------------------------
#FILTROS
#------------------------------------------

def filtrado_continente():
    
    continentes_validos = ["america","europa","asia","africa","oceania","antartida"]
    
    continente = input("Ingrese el contiente con el que desea filtrar: ").strip()
    
    #Verificaciones de continente
    if not continente:
        print("\n" + "=" * 30)
        print("Entrada vacia. Intentelo de nuevo...")
        return
    
    if continente.isdigit():
        print("\n" + "=" * 30)
        print("No puede ingresar numero. Intentelo de nuevo...")
        return
    
    if continente not in continentes_validos:
        print("\n" + "=" * 30)
        print("El continente ingresado no existe. Intentelo de nuevo...")
        return
    
    
    cont_sin_tildes = quitar_tildes(continente.lower())
    
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            encontrados = []
            
            for fila in lector:
                if quitar_tildes(fila["continente"].lower()) == cont_sin_tildes:
                    encontrados.append(fila)
            
            if encontrados:
                print(f"\nPaises del continente de {continente}: \n")
                    
                print("-" * 70)
                print(f"{'Nombre':<20} {'Población':<17} {'Superficie':<10} {'Continente':>15}")
                print("-" * 70)

                    
                for pais in encontrados:
                        nombre = pais["nombre"]
                        poblacion = int(pais["poblacion"])
                        superficie = float(pais["superficie"])
                        continente = pais["continente"]

                        print(f"{nombre:<20} | {poblacion:>12} | {superficie:>14} | {continente:>15} |")
                
    except FileNotFoundError:
        print(" El archivo no existe. Creando uno nuevo...")
        inicializar_archivo()

def filtrado_rango_poblacion():
    try:
        
        #Entrada de usuario y validaciones
        pobl_min = int(input("Ingrese la poblacion minima: "))
        
        if not pobl_min:
            print("\n" + "=" * 30)
            print("Entrada vacia. Intentelo de nuevo...")
            return
        
        pobl_max = int(input("Ingrese la poblacion maxima: "))
        
        if not pobl_max:
            print("\n" + "=" * 30)
            print("Entrada vacia. Intentelo de nuevo...")
            return
        
        
    except ValueError:
        print("\n" + "=" * 30)
        print("No puede ingresar letras. Intentelo de nuevo...")
        return
    
    try:
        
        #Apertura de archivo
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            encontrados = []
            
            #Busqueda de las poblacion solicitadas
            for fila in lector:
                try:
                    poblacion = int(fila["poblacion"])
                    
                    if pobl_min <= poblacion <= pobl_max:
                        encontrados.append(fila)
                    
                except ValueError:
                    continue
            
            #Escritura de la poblacion solicitadas
            if encontrados:
                
                print("\n" + "=" * 30)
                print(f"|Paises con poblacion entre {pobl_min} y {pobl_max} de habitantes: \n")
                
                print("-" * 70)
                print(f"{'Nombre':<20} {'Población':<17} {'Superficie':<10} {'Continente':>15}")
                print("-" * 70)
                    
                for pais in encontrados:
                    nombre = pais["nombre"]
                    poblacion = int(pais["poblacion"])
                    superficie = float(pais["superficie"])
                    continente = pais["continente"]

                    print(f"{nombre:<20} | {poblacion:<17} | {superficie:<10} | {continente:>15}")
    except FileNotFoundError:
        print(" El archivo no existe. Creando uno nuevo...")
        inicializar_archivo()

def filtrado_superficie():
    
    try:
        
        #Entrada de usuario y validaciones.
        sup_min = int(input("Ingrese la superficie minima: "))
        
        if not sup_min:
            print("\n" + "=" * 30)
            print("Entrada vacia. Intentelo de nuevo...")
            return
        
        sup_max = int(input("Ingrese la superficie maxima: "))
        
        if not sup_max:
            print("\n" + "=" * 30)
            print("Entrada vacia. Intentelo de nuevo...")
            return
        
    except ValueError:
        print("\n" + "=" * 30)
        print("No puede ingresar letras. Intentelo de nuevo...")
        return

    try:
        
        #Apertura de archivo
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            encontrados = []
            
            
            #Busqueda de las superficies solicitadas
            for fila in lector:
                try:
                    superficie = float(fila["superficie"])
                    
                    if sup_min <= superficie <= sup_max:
                        encontrados.append(fila)
                    
                except ValueError:
                    continue
            
            
            #Escritura de las superficies solicitadas
            if encontrados:
                
                print(f"\n|Paises con superficie entre {sup_min} y {sup_max} \n")
                
                print("-" * 70)
                print(f"{'Nombre':<20} {'Población':<17} {'Superficie':<10} {'Continente':>15}")
                print("-" * 70)
                    
                for pais in encontrados:
                    nombre = pais["nombre"]
                    poblacion = int(pais["poblacion"])
                    superficie = float(pais["superficie"])
                    continente = pais["continente"]

                    print(f"{nombre:<20} | {poblacion:<17} | {superficie:<10} | {continente:>15}")
                print("-" * 70)
                
    except FileNotFoundError:
        inicializar_archivo()

#------------------------------------------
#ORDENAMIENTOS
#------------------------------------------

def buscar_nombre(pais):
    return pais["nombre"].lower()
def ordenamiento_nombre():
    try:
        
        #Apertura de archivo
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            paises = list(lector)
            
            if not paises:
                print("\n" + "=" * 30)
                print("El archivo esta vacio. No hay paises para ordenar.")
            
            paises_ordenados = sorted(paises, key=buscar_nombre)

            #Se sobrescribe el CSV original por el nuevo ordenado
            with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
                encabezado = ["nombre", "poblacion","superficie","continente"]
                escritor = csv.DictWriter(archivo, fieldnames=encabezado)
                escritor.writeheader()
                escritor.writerows(paises_ordenados)
            print("\n" + "=" * 30)
            print("Paises ordenado correctamente.")
            
    except FileNotFoundError:
        print(" El archivo no existe. Creando uno nuevo...")
        inicializar_archivo()

def obtener_poblacion(pais):
    return int(pais["poblacion"])
def ordenamiento_poblacion(opcion):
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            paises = list(lector)
            
            if not paises:
                print("\n" + "=" * 30)
                print("El archivo esta vacio. No hay paises para ordenar.")
            
            #Ordenamiento Ascendente y Descendente (a/d)
            if opcion == "a":
                ordenados_poblacion = sorted(paises, key=obtener_poblacion)
                print("\n" + "=" * 30)
                print("- Paises ordenados ascendentemente -.")
                
            elif opcion == "d":
                ordenados_poblacion = sorted(paises, key=obtener_poblacion, reverse=True)
                print("\n" + "=" * 30)
                print("- Paises ordenados descendentemente - .")
            
            #Se sobreescribe el CSV original por el nuevo ordenado
            with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
                encabezado = ["nombre","poblacion","superficie","continente"]
                escritor = csv.DictWriter(archivo, fieldnames=encabezado)
                escritor.writeheader()
                escritor.writerows(ordenados_poblacion)
            
            
    except FileNotFoundError:
        print(" El archivo no existe. Creando uno nuevo...")
        inicializar_archivo()

def obtener_superficie(pais):
    return float(pais["superficie"])
def ordenamiento_superficie(opcion):
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            paises = list(lector)
            
            if not paises:
                print("\n" + "=" * 30)
                print("El archivo esta vacio. No hay paises para ordenar.")
            
            #Ordenamiento Ascendente o Descendente (a/d)
            if opcion == "a":
                ordenados_superficie = sorted(paises, key=obtener_superficie)
                print("- Paises ordenados ascendentemente -.")
                
            elif opcion == "d":
                ordenados_superficie = sorted(paises, key=obtener_superficie, reverse=True)
                print("- Paises ordenados descendentemente - .")
            
            #Sobreescribo el CSV original por el nuevo ordenado
            with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
                encabezado = ["nombre","poblacion","superficie","continente"]
                escritor = csv.DictWriter(archivo, fieldnames=encabezado)
                escritor.writeheader()
                escritor.writerows(ordenados_superficie)
            
            
    except FileNotFoundError:
        print(" El archivo no existe. Creando uno nuevo...")
        inicializar_archivo()

#------------------------------------------
#ESTADISTICAS
#------------------------------------------

def pais_menor_mayor():
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            
            primera = True
            nombre_mayor = nombre_menor = None
            may_poblacion = None
            men_poblacion = None

            for fila in lector:
                try:
                    pobl = int(fila["poblacion"])
                except (ValueError, KeyError):
                    continue
                
                if primera:
                    may_poblacion = men_poblacion = pobl
                    nombre_mayor = nombre_menor = fila["nombre"]
                    primera = False
                    
                else:
                    if pobl > may_poblacion:
                        may_poblacion = pobl
                        nombre_mayor = fila["nombre"]
                        
                    if pobl < men_poblacion:
                        men_poblacion = pobl
                        nombre_menor = fila["nombre"]

            if primera:
                print("No hay paises con poblacion valida.")
                return

            print(f"|Pais con mayor poblacion: {nombre_mayor} |Poblacion: {may_poblacion}")
            print(f"|Pais con menor poblacion: {nombre_menor} |Poblacion: {men_poblacion}")

    except FileNotFoundError:
        inicializar_archivo()

def promedio_poblacion():
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            paises = list(lector)
            
            suma_poblacion = 0
            
            #Suma de la poblacion de cada pais.
            for fila in paises:
                try:
                    suma_poblacion += int(fila["poblacion"])
                except ValueError:
                    continue
            
            #Promedio total
            
            try:
                prom_poblacion = suma_poblacion / len(paises)
            except ZeroDivisionError:
                print("ERROR. Valor invalido para division..")
            
            print("\n" + "=" * 30)
            print(f"|El promedio de poblacion mundial es de: {prom_poblacion}")
            
    except FileNotFoundError:
        print(" El archivo no existe. Creando uno nuevo...")
        inicializar_archivo()

def promedio_superficie():
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            paises = list(lector)
            
            suma_superficie = 0
            
            #Suma de la superficie de cada pais
            for fila in paises:
                try:
                    suma_superficie += float(fila["superficie"])
                except ValueError:
                    continue
            
            #Promedio total
            prom_superficie = suma_superficie / len(paises)
            
            print("\n" + "=" * 30)
            print(f"|El promedio de la superficie mundial es de: {round(prom_superficie,2)}")
            
    except FileNotFoundError:
        print(" El archivo no existe. Creando uno nuevo...")
        inicializar_archivo()

def paises_por_continente():
    try:
        with open(RUTA_ARCHIVO, "r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)
            paises = list(lector)
            
            #Diccionario de continentes vacio
            conteo_continentes = {}

            for pais in paises:
                
                #Asignacion de continente
                continente = pais["continente"].strip().capitalize()
                
                #Verificacion si suma al contador del continente
                if continente in conteo_continentes:
                    conteo_continentes[continente] += 1
                    
                #Verificacion si ingresa un nuevo continente
                else:
                    conteo_continentes[continente] = 1
                
            for continente, cantidad in conteo_continentes.items():
                print(f"|Continente {continente} | Cantidad de paises: {cantidad}")
                
                
    except FileNotFoundError:
        print(" El archivo no existe. Creando uno nuevo...")
        inicializar_archivo()
