def menor(x, y, z):
    lista = [x, y, z]
    menor = x

    for i in lista:
        if i < menor:
            menor = i
    return menor