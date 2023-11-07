valores = []
numeros_impares = []
numeros_pares = []

for i in range(10):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    valores.append(valor)
    if valor % 2 == 0:
        numeros_pares.append(valor)
    else:
        numeros_impares.append(valor)

tupla_pares = (len(numeros_pares), sum(numeros_pares))
tupla_impares = (len(numeros_impares), sum(numeros_impares))

print("Números pares:", tuple(numeros_pares))
print("Números ímpares:", tuple(numeros_impares))
print("Quantidade e Soma de números pares:", tupla_pares)
print("Quantidade e Soma de números ímpares:", tupla_impares)
