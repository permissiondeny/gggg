def leer(cadena):
    cadena += '$'
    aux = cadena[0]
    valor = []
    cantidad = []
    contador = 1
    for x in range(1, len(cadena)):
        if cadena[x] == aux[-1]:
            aux += cadena[x]
            contador += 1
        else:
            valor.append(aux[-1])
            cantidad.append(contador)
            aux = cadena[x]
            contador = 1
    return valor, cantidad


def main():
    # 1 - 11 - 21- 1211 - 111221 - 312211
    a = '1'
    secuencia = [a]
    for i in range(4):
        v, c = leer(a)
        a = ""
        for i in range(len(v)):
            a += str(c[i]) + v[i]
        secuencia.append(a)
    print(secuencia)


main()
