## Conjuntos são caracterizados por {}
exemplo = {1, 2, 3, 4}

## Add elementos
exemplo.add(5)

## Removendo elemento
exemplo.discard(2)

#----------------------------------------#

conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

conjuntoUniao = conjunto.union(conjunto2)
print("ConjuntoUniao = ", conjuntoUniao)

conjuntoInter = conjunto.intersection(conjunto2)
print("conjuntoInter = ", conjuntoInter)

conjuntoDiff = conjunto.difference(conjunto2)
print("conjuntoDiff = ", conjuntoDiff)

conjuntoDiff_simetrica = conjunto.symmetric_difference(conjunto2)
print("conjuntoDiff_simetrica = ", conjuntoDiff_simetrica)

#----------------------------------------#

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)


conjunto = {10, 20, 30, 40, 50}
conjunto.discard (40)
print(conjunto)
