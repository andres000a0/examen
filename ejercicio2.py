cuentas_cersei = [
    {"numero_cuenta": 1, "saldo": 0},
    {"numero_cuenta": 2, "saldo": 0},
    {"numero_cuenta": 3, "saldo": 0},
    {"numero_cuenta": 4, "saldo": 0},
    {"numero_cuenta": 5, "saldo": 0},
    {"numero_cuenta": 6, "saldo": 0},
    {"numero_cuenta": 7, "saldo": 0},
    {"numero_cuenta": 8, "saldo": 0},
    {"numero_cuenta": 9, "saldo": 0},
    {"numero_cuenta": 10, "saldo": 0}
]

for cuenta in cuentas_cersei:
    saldo = float(
        input(f"Ingrese el saldo de la cuenta {cuenta['numero_cuenta']}: "))
    cuenta["saldo"] = saldo

cuentas_ordenadas = sorted(
    cuentas_cersei, key=lambda k: k["saldo"], reverse=True)

print("Cuentas ordenadas de mayor a menor saldo:")
for i, cuenta in enumerate(cuentas_ordenadas):
    print(f"{i+1}. Cuenta {cuenta['numero_cuenta']}: ${cuenta['saldo']:.2f}")
