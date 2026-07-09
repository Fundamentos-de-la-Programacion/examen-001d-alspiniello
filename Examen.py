def menu_print():
    print("""
        ========== MENÚ PRINCIPAL ==========
        1. Copias por género
        2. Búsqueda de libros por rango de multa
        3. Actualizar multa de libro
        4. Agregar libro
        5. Eliminar libro
        6. Salir
        =====================================
    """)

def leer_opcion():
    try:
        menu=int(input("\n:"))
    except ValueError:
        return -1
    if 6>=menu>=1:
        return menu
    
    return -1
def leer_str():
    inpu=input(":")
    return inpu.lower()

#si sobra tiempo
def generos_disp():
    pass

def opcion1_copiasgenero(loc,cant_prestamos):
    total=0
    num=1
    print("Genero:")
    genderinp=leer_str()
    for sylphy in loc:
        if genderinp==loc[sylphy][2]:
            total=cant_prestamos[sylphy][1]+total
    print(f"hay: {total} libros de {genderinp}")

def opcion2_multarang(lib,mult):
    #AÑADIR seguros si sobra tiemposulio
    num=1
    print("\nValor Maximo de multa: ")
    maxi=int(input(": "))
    print("\nValor Minimo de multa: ")
    mino=int(input(": "))
    print(f"LIBROS EN RANGO DE {mino} a {maxi}")

    for sylphy in mult:
        if maxi>=mult[sylphy][0]>=mino:
            print(f"{num}. {lib[sylphy][0]}")
            num=1+num        

def search(where,find):
    for sylphy in where:
        if find==sylphy:
            return True
        else:
            return False
    return False

def adicion(code):
    try:
        new=int(input("Nueva multa: "))
    except ValueError:
        return False
    
    return new

def opcion3_actmulta(multas):
    info=False
    print("Codigos disponibles: ")
    for sylphy in multas:
        print(sylphy)
    
    while info == False:
        code=input("Ingresar el codigo de multa a actualizar:")
        info=search(multas,code)
    return code

def opcion5_del(eliminar,lib,prest):
    pass

def main():
    libros = {
    'L001': ['Sombras del Sur', 'A. Rojas', 'novela', 2019, 'AndesPress', False],
    'L002': ['Python en Ruta', 'M. Diaz', 'tecnología', 2023, 'CodeBooks', True],
    'L003': ['Mar y Viento', 'C. Silva', 'poesía', 2017, 'Litoral', False],
    'L004': ['Historia Breve', 'J. Pérez', 'historia', 2015, 'Cronos', False],
    'L005': ['Mundos Lejanos', 'L. Torres', 'ciencia ficción', 2021, 'Orión', True],
    'L006': ['Cocina Simple', 'R. Soto', 'cocina', 2018, 'Sabores', False],
    }
    prestamos = {
    'L001': [500, 4],
    'L002': [700, 0],
    'L003': [300, 10],
    'L004': [400, 2],
    'L005': [600, 1],
    'L006': [350, 6],
    }   
    menu_print()
    menu=leer_opcion()
    match menu:
        case 1:
            opcion1_copiasgenero(libros,prestamos)
        case 2:
            opcion2_multarang(libros,prestamos)
        case 3:
            ifo=opcion3_actmulta(prestamos)
            nuevo=adicion(ifo)
            prestamos[ifo]=[nuevo,prestamos[ifo][1]]
            print(nuevo,ifo,prestamos)
        
        case 4:
            test=False
            while test==False:
                code=input("codigo DE libro a añadir: ")
                test=search(libros,code)
            print(libros)
            

        case 5:
            test=False
            while test==False:
                code=input("codigo DE libro a eliminar: ")
                test=search(libros,code)
            print(libros)

        case -1:
            print("Solo numeros del 1-6 enteros")
        case 6:
            return menu
num=0 
while num!=6:
    num=main()
print("PROGRAMA FINALIZADO")

