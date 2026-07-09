peliculas_db = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False]
}  

cartelera_db = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3]
}    

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

def cupos_genero(genero, peliculas, cartelera):
    total_cupos = 0
    genero_buscado = genero.strip().lower()
    
    for cod, datos in peliculas.items():
        if datos[1].lower() == genero_buscado:
            if cod in cartelera:
                total_cupos += cartelera[cod][1]
                
    print(f"El total de cupos disponibles es: {total_cupos}")

def busqueda_precio(p_min, p_max, peliculas, cartelera):
    resultados = []
    for cod, datos_cartelera in cartelera.items():
        precio = datos_cartelera[0]
        cupos = datos_cartelera[1]
        
        if p_min <= precio <= p_max and cupos > 0:
            if cod in peliculas:
                titulo = peliculas[cod][0]
                resultados.append(f"{titulo}--{cod}")
                
    if resultados:
        resultados.sort()
        print(f"Las películas encontradas son: {resultados}")
    else:
        print("No hay películas en ese rango de precios.")

def buscar_codigo(codigo, cartelera):
    cod_buscado = codigo.strip().upper()
    for cod in cartelera.keys():
        if cod.upper() == cod_buscado:
            return True
    return False

def obtener_clave_real(codigo, cartelera):
    cod_buscado = codigo.strip().upper()
    for cod in cartelera.keys():
        if cod.upper() == cod_buscado:
            return cod
    return codigo

def actualizar_precio(codigo, nuevo_precio, cartelera):
    if buscar_codigo(codigo, cartelera):
        clave_real = obtener_clave_real(codigo, cartelera)
        cartelera[clave_real][0] = nuevo_precio
        return True
    return False

def validar_codigo(codigo, cartelera):
    if not codigo.strip():
        return False
    if buscar_codigo(codigo, cartelera):
        return False
    return True

def validar_titulo(titulo):
    return bool(titulo.strip())

def validar_genero(genero):
    return bool(genero.strip())

def validar_duracion(duracion):
    try:
        val = int(duracion)
        return val > 0
    except ValueError:
        return False

def validar_clasificacion(clasificacion):
    return clasificacion.strip().upper() in ['A', 'B', 'C']

def validar_idioma(idioma):
    return bool(idioma.strip())

def validar_es_3d(es_3d):
    return es_3d.strip().lower() in ['s', 'n']

def validar_precio(precio):
    try:
        val = int(precio)
        return val > 0
    except ValueError:
        return False

def validar_cupos(cupos):
    try:
        val = int(cupos)
        return val >= 0
    except ValueError:
        return False
    
def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos, peliculas, cartelera):
    if buscar_codigo(codigo, cartelera):
        return False
    cod_upper = codigo.strip().upper()

    bool_3d = True if es_3d.strip().lower() == 's' else False
    
    peliculas[cod_upper] = [titulo.strip(), genero.strip(), int(duracion), clasificacion.strip().upper(), idioma.strip(), bool_3d]

    cartelera[cod_upper] = [int(precio), int(cupos)]
    return True

def eliminar_pelicula(codigo, peliculas, cartelera):
    if buscar_codigo(codigo, cartelera):
        clave_real = obtener_clave_real(codigo, cartelera)
        if clave_real in peliculas:
            del peliculas[clave_real]
        if clave_real in cartelera:
            del cartelera[clave_real]
        return True
    return False
def main():
    while True:
        print("\n========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por género")
        print("2. Búsqueda de películas por rango de precio")
        print("3. Actualizar precio de película")
        print("4. Agregar película")
        print("5. Eliminar película")
        print("6. Salir")
        print("=====================================")
        
        opc = leer_opcion()
        
        if opc == 1:
            gen = input("Ingrese género a consultar: ")
            cupos_genero(gen, peliculas_db, cartelera_db)
            
        elif opc == 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))
                    if p_min <= p_max and p_min >= 0:
                        break
                    else:
                        print("El precio mínimo debe ser menor o igual al máximo y mayores a cero.")
                except ValueError:
                    print("Debe ingresar valores enteros")
            busqueda_precio(p_min, p_max, peliculas_db, cartelera_db)
            
        elif opc == 3:
            while True:
                cod = input("Ingrese código de película: ")
                try:
                    precio_nuevo = int(input("Ingrese nuevo precio: "))
                    if precio_nuevo <= 0:
                        print("El precio debe ser un valor entero positivo.")
                        continue
                except ValueError:
                    print("Debe ingresar un valor entero.")
                    continue
                
                if actualizar_precio(cod, precio_nuevo, cartelera_db):
                    print("Precio actualizado")
                else:
                    print("El código no existe")
                    
                resp = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
                if resp != 's':
                    break
        elif opc == 4:
            cod = input("Ingrese código de película: ")
            tit = input("Ingrese título: ")
            gen = input("Ingrese género: ")
            dur = input("Ingrese duración (minutos): ")
            cla = input("Ingrese clasificación: ")
            idi = input("Ingrese idioma: ")
            f3d = input("¿Es 3D? (s/n): ")
            pre = input("Ingrese precio: ")
            cup = input("Ingrese cupos: ")
            
            if not validar_codigo(cod, cartelera_db):
                print("Error: Código inválido o ya existente.")
            elif not validar_titulo(tit):
                print("Error: Título inválido.")
            elif not validar_genero(gen):
                print("Error: Género inválido.")
            elif not validar_duracion(dur):
                print("Error: Duración inválida.")
            elif not validar_clasificacion(cla):
                print("Error: Clasificación inválida (Debe ser A, B o C).")
            elif not validar_idioma(idi):
                print("Error: Idioma inválido.")
            elif not validar_es_3d(f3d):
                print("Error: Formato 3D inválido (s/n).")
            elif not validar_precio(pre):
                print("Error: Precio inválido.")
            elif not validar_cupos(cup):
                print("Error: Cupos inválidos.")
            else:
                if agregar_pelicula(cod, tit, gen, dur, cla, idi, f3d, pre, cup, peliculas_db, cartelera_db):
                    print("Película agregada")
                else:
                    print("El código ya existe")
        elif opc == 5:
            cod = input("Ingrese código de película: ")
            if eliminar_pelicula(cod, peliculas_db, cartelera_db):
                print("Película eliminada")
            else:
                print("El código no existe")
                
        elif opc == 6:
            print("Programa finalizado.")
            break
if __name__ == "__main__":
    main()