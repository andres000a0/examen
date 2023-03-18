listas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

opcion = 1

while opcion != 0:
    print('Seleciona la cuenta')
    print('Opción 1 = Lista de cuentas')
    print('Opción 0 = salir')
    opcion = int(input('ingresa una opción: '))
    
    if opcion == 1:
        print('Opción 1 = Cuenta de Impuestos 1')
        print('Opción 2 = Cuenta de Impuestos 1')
        print('Opción 3 = Cuenta de Impuestos 2')
        print('Opción 4 = Cuenta de Impuestos 3')
        print('Opción 5 = Cuenta de Impuestos 4')
        print('Opción 6 = Cuenta de Impuestos 5')
        print('Opción 7 = Cuenta de Impuestos 6')
        print('Opción 8 = Cuenta de Impuestos 7')
        print('Opción 9 = Cuesta de Recaudos')
        print('Opción 10 = Cuenta Familiar')
        lista = {
        }
        lista[1] = 'El saldo es: 10000'
        lista[2] = 'El saldo es: 20000'
        lista[3] = 'El saldo es: 30000'
        lista[4]= 'El saldo es: 40000'
        lista[5] = 'El saldo es: 50000'
        lista[6] = 'El saldo es: 60000'
        lista[7] = 'El saldo es: 70000'
        lista[8] = 'El saldo es: 80000'
        lista[9] = 'El saldo es: 90000'
        lista[10] = 'El saldo es: 100000'
        print(lista)
    elif (opcion == 2):
        CuentaBuscar = int(input('Ingrese el Numero de la cuenta: '))
        for lista in listas:
            if lista == CuentaBuscar:
                print(lista)
            else:
                print(f'Ciclista no existe')
        
