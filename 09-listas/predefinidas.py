cantantes  =  ['2pac', 'Drake', 'Bunbury', 'Badbunny']
numeros = [1,2,5,8,3,9]


#ordenar
# print(numeros)
numeros.sort()
# print(numeros)

#añadir elementos 
cantantes.append('Wisin')
cantantes.insert(1,"David")
# print(cantantes)

#eliminar elementos 
cantantes.pop(1)
cantantes.remove('Badbunny')
# print(cantantes)

# print(numeros)
numeros.reverse()
# print(numeros)

#Buscar dentro de una lista 
# print('Drake' in cantantes)

#Contar elementos 
# print(cantantes)
# print(len(cantantes))

#Cuantas veces aparece un elemento 
numeros.append(5)
print(numeros.count(5))

#Conseguir indice 
print(cantantes.index("Drake"))

#Unir listas 
cantantes.extend(numeros)
print(cantantes)