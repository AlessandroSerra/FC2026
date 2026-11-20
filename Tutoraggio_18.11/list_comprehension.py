# due modi equivalenti per riempire una lista di elementi
# chiamiamo il secondo "list comprehension"

lista = []

for i in range(11):
    lista.append(i)


lista2 = [i for i in range(11)]

print(lista)
