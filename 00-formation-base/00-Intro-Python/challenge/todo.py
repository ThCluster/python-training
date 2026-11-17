# Initialisation de la liste de courses
liste_courses = []

# Demande d'initialisation
initial_input = input("Souhaitez-vous commencer avec une liste d'articles ? (oui/non) ")
if initial_input.lower() == "oui":
    articles = input("Entrez les articles de départ, séparés par des virgules : ")
    liste_courses = articles.split(",")
    liste_courses = [article.strip() for article in liste_courses]  # Nettoyage des espaces

print("Liste initiale :", liste_courses)


# Ajouter un article
def ajouter_article(liste):
    article = input("Entrez l'article à ajouter : ")
    liste.append(article)
    print(f"L'article '{article}' a été ajouté à la liste.")
    print("Liste mise à jour :", liste)

ajouter_article(liste_courses)

# Afficher la liste des courses
def afficher_liste(liste):
    print("Votre liste de courses :")
    for i, article in enumerate(liste, start=1):
        print(f"{i}. {article}")

afficher_liste(liste_courses)

# Supprimer un article
def supprimer_article(liste):
    article = input("Entrez l'article à supprimer : ")
    if article in liste:
        liste.remove(article)
        print(f"L'article '{article}' a été supprimé de la liste.")
        print("Liste mise à jour :", liste)
    else:
        print(f"L'article '{article}' n'est pas dans la liste.")

supprimer_article(liste_courses)

# Modifier un article
def modifier_article(liste):
    article = input("Entrez l'article à modifier : ")
    if article in liste:
        nouvel_article = input("Entrez la nouvelle valeur : ")
        index = liste.index(article)
        liste[index] = nouvel_article
        print(f"L'article '{article}' a été modifié en '{nouvel_article}'.")
        print("Liste mise à jour :", liste)
    else:
        print(f"L'article '{article}' n'est pas dans la liste.")

modifier_article(liste_courses)

# Afficher la liste des courses
def afficher_liste(liste):
    print("Votre liste de courses :")
    for i, article in enumerate(liste, start=1):
        print(f"{i}. {article}")

afficher_liste(liste_courses)

# Menu principal
def menu():
    print("\nMenu :")
    print("1 : Afficher la liste des courses")
    print("2 : Ajouter un article")
    print("3 : Supprimer un article")
    print("4 : Modifier un article")
    print("5 : Quitter")

    choix = input("Entrez le numéro de votre choix : ")
    return choix

while True:
    choix = menu()
    if choix == "1":
        afficher_liste(liste_courses)
    elif choix == "2":
        ajouter_article(liste_courses)
    elif choix == "3":
        supprimer_article(liste_courses)
    elif choix == "4":
        modifier_article(liste_courses)
    elif choix == "5":
        print("Merci d'avoir utilisé le programme !")
        break
    else:
        print("Option invalide. Veuillez choisir une option du menu.")