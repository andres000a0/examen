opcion = 1

ciclistas = []

while opcion != 0:
    print('Ciclista')
    print('Opción 1 = ingresa una Ciclista')
    print('Opción 2 = mostrar Ciclista')
    print('Opción 3 = buscar una Ciclista')
    print('Opción 4 = editar Ciclista')
    print('Opción 5 = eliminar una Ciclista')
    print('Opción 0 = salir')

    opcion = int(input('ingresa una opción: '))
    if (opcion == 1):
        Ciclista = {}
        Ciclista['id'] = int(input('Digita el id de la Ciclista: '))
        Ciclista['nombre'] = input('Digita el nombre: ')
        Ciclista['edad'] = float(input('Digita la edad: '))
        Ciclista['pais'] = (input('Digita el pais: '))
        Ciclista['equipo'] = input('Digita el equipo: ')
        Ciclista['tiempo'] = int(input('Digita el tiempo: '))
        ciclistas.append(Ciclista)
        print(f'Ciclista ingresada....')
    elif (opcion == 2):
        for Ciclista in ciclistas:
            print(Ciclista)
    elif (opcion == 3):
        CiclistaBuscar = int(input('Ingrese el id de la empadana: '))
        for Ciclista in ciclistas:
            if Ciclista['id'] == CiclistaBuscar:
                print(f'Ciclista no existe')
            else:
                print(Ciclista['precio'])
    elif (opcion == 4):
        CiclistaBuscar = int(input('Ingrese el id de la empadana: '))
        for Ciclista in ciclistas:
            if Ciclista['id'] == CiclistaBuscar:
                print(f'Ciclista no existe')
            else:
                print(f'Precio actual de la Ciclista')
                print(Ciclista['precio'])
                nuevoPrecio = float(input('Ingresa en nuevo precio'))
                Ciclista['precio'] = nuevoPrecio
    elif (opcion == 5):
        CiclistaBuscar = int(input('Ingrese el id de la empadana: '))
        for Ciclista in ciclistas:
            if Ciclista['id'] == CiclistaBuscar:
                print(f'Ciclista no existe')
            else:
                ciclistas.remove(Ciclista)
    elif (opcion == 0):
        pass
    else:
        print(f'Opción invalida')
