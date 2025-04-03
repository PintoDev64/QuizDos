TotalCasos = int(input())

CantidadNumeros = []

for N in range(TotalCasos):
    CantidadNumeros.append(int(input()))

def CalcularPachecos(numero):
    if (numero % 2 == 0 and numero > 0):
        return "EVEN POSITIVE"
    elif (numero % 2 == 0 and numero < 0):
        return "EVEN NEGATIVE"
    elif (numero % 2 == 1 and numero > 0):
        return "ODD POSITIVE"
    elif (numero % 2 == 1 and numero < 0):
        return "ODD NEGATIVE"
    elif (numero == 0):
        return "NULL";

for NumeroUtilizado in range(len(CantidadNumeros)):
    print(CalcularPachecos(CantidadNumeros[NumeroUtilizado]))