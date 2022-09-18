Arr = [10, 2, 5, 8, 6]
ArrOrdenado = sorted(Arr)
ValorMinimo = 0
ValorMaximo = 0

n = len(ArrOrdenado) -1
k = 0

for i in range(n):
    ValorMinimo += ArrOrdenado[i]
    k = i + 1
    ValorMaximo += ArrOrdenado [k]

print("Valor Maximo: ", ValorMaximo,'\n', "Valor Minimo: ", ValorMinimo)