ma_liste = list(range(10))
print(ma_liste)

ma_Liste = [10,15,20,25,30]
print(ma_Liste[0])
print(ma_Liste[-1])

sous_liste = ma_Liste[1:4]
print(sous_liste)
sous_maliste = ma_Liste
print(sous_maliste)
sous_maliste.append(800)
print(sous_maliste)
sous_maliste.insert(1, 100)
print(sous_maliste)
sous_maliste.extend([5, 8, 9, 400])
print(sous_maliste)
sous_maliste.remove(8)
print(sous_maliste)
sous_maliste.pop()
print(sous_maliste)
sous_maliste[1:8] = [15 ,20 ,45 ,90 ,100 ,39 ,56]
print(sous_maliste)

del ma_Liste[0]
print(ma_Liste)
del ma_Liste[0]
print(ma_Liste)
print(100 in ma_Liste)

position = ma_Liste.index(56)
print(position)

ne_liste = [10,2020,25,10,13,27,884,27,2,2,1,3,2]
print(ne_liste.count(2))

ne_liste.sort()
ma_Liste.sort()
ma_liste.sort
sous_maliste.sort()

print(f"{ma_liste}, {ne_liste}, {ma_Liste}, {sous_maliste}")

# for element in ne_liste:
#     # print(element)
    
#     for index, element in enumerate(ma_liste):
#         print(f"Index {index} : {element}")
print('\n')
thrue_liste = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(thrue_liste[0])
# print(thrue_liste[0][1])
# print(thrue_liste)

copier_liste = thrue_liste.copy()

ma_liste = [1, 2, 3]
carres = list(map(lambda x: x ** 2, ma_liste))
pairs = list(filter(lambda x: x % 2 == 0, ma_liste))