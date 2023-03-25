#multiplos
multiplos_de_2 = 0
multiplos_de_3 = 0
multiplos_de_2_y_3 = 0

for i in range(20):
    numero = int(input(f"Ingrese el número {i+1}: "))

    if numero % 2 == 0:
        multiplos_de_2 += 1

    if numero % 3 == 0:
        multiplos_de_3 += 1

    if numero % 2 == 0 and numero % 3 == 0:
        multiplos_de_2_y_3 += 1

print(f"Se ingresaron {multiplos_de_2} números múltiplos de 2.")
print(f"Se ingresaron {multiplos_de_3} números múltiplos de 3.")
print(f"Se ingresaron {multiplos_de_2_y_3} números múltiplos de 2 y 3 al mismo tiempo.")