# Création d'un tuple de plusieurs éléments

mon_tuple = (1,2,4,5)
print(mon_tuple)

# Création d'un tuple mixte contenant de plusieurs types variés

tuple_mixte = (1,"Python",True,False,2.16)
print(tuple_mixte)

# Créaton d'un tuple sans parenthèse

tuple_sans_parenthese = 12,35,87
print(tuple_sans_parenthese)

#Création d'un tuple sans virgule

tuple_seul_element = (35,)
print(tuple_seul_element)
tuple_seul_element_sans_virgule = (35) #ceci n'est pas un tuple
print(tuple_seul_element_sans_virgule) 

#Creatiin d'un tuple à partir d'une chaine de caractères et une liste

liste_exemple = [12,13,14,15]
tuple_a_partir_liste = tuple(liste_exemple)
print(tuple_a_partir_liste)

chaine = "Python"
tuple_a_partir_chaine = tuple(chaine)
print(tuple_a_partir_chaine)

#Accéder aux éléments d’un tuple

mon_tuple = (10, 20, 30, 40, 50)
print(mon_tuple[3])
print(mon_tuple[-1])

#Extraction de sous-tuples (slicing)

#Concaténation de tuples
tuple_1 = (1,2,3,4,5,6)
tuple_2 = (7,8,9,10,11)

concatenation_tuple = tuple_1 + tuple_2
print(concatenation_tuple)

#Utilisation des fonctions intégrées len(), min() et max()

mon_tuple = (10, 20, 30, 40)
print(len(mon_tuple))
print(min(mon_tuple))
print(max(mon_tuple))

#Trouver l’index d’un élément avec index()
tuple_index = (10, 20, 30, 40)
print(tuple_index.index(30))  # Output : 2

#Les tuples nommés (namedtuples)