list_courses = []

initial_input = input("Souhaitez-vous commencer avec une liste d'articles ? (oui/non) ")
if initial_input.lower() == "oui":
     articles = input("Entrez les articles de départ, séparés par des virgules : ")
     liste_courses = articles.split(",")
     list_courses = [article.strip() for article in list_courses]
print("Liste initiale :", liste_courses)

print("Liste initiale :", liste_courses)

# Ajouter un article
def ajouter_article(liste):
    article = input("Entrez l'article à ajouter : ")
    liste.append(article)
    print(f"L'article '{article}' a été ajouté à la liste.")
    print("Liste mise à jour :", liste)
ajouter_article(list_courses)

# Supprimer un article
def supprimer_article(liste):
        article = input("Entrez l'article à supprimer : ")
        if article in liste:
            liste.remove(article)   
            print(f"L'article '{article}' a été supprimé de la liste.")
            print("Liste mise à jour :", liste)
        else :   
            print(f"L'article '{article}' n'est pas dans la liste.")

supprimer_article(liste_courses)