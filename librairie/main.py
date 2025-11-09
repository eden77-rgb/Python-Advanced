"""
Module principal de gestion de la bibliothèque.

Ce module permet de :
- charger les données
- nettoyer les données
- typer les données

Scénario à tester :
- afficher le nombre total de livres disponibles
- emprunter un livre
- tenter d'emprunter un livre déjà emprunté (gérer l'erreur via try/except)
- rendre un livre
- réafficher le nombre total de livres disponibles

Référence du sujet :
https://github.com/Antoine07/python_expert/blob/main/Slides/TP_bibliotheque.md
"""

from book import Book
from category import Category
from library import Library
from exception import BookAvailableError

# Charger les données
try:
    with open("../data/book.csv", "r", encoding="utf-8") as file:
        data = file.readlines()

except FileNotFoundError:
    print("Fichier introuvable")


# Netoyage des data
data = [line.strip() for line in data if line.strip() != ""]
data = [line.split(";") for line in data]

headers = data.pop(0)


# Extraction des data + typage
data_clean = []
for line in data:
    try:
        if all(line):
            try:
                categorie, titre, auteur, annee, disponible = line
                annee = int(annee)
                disponible = disponible == "yes"

                data_clean.append([categorie, titre, auteur, annee, disponible])

            except ValueError:
                print(f"[ERREUR] Ligne ignorée (donée invalide) : {line}")

        else:
            raise ValueError(f"[ERREUR]: Ligne ignoré (champ vide) : {line}")

    except ValueError as e:
        print(e)


# Ajout des Livres et Categories a la Librairies
library = Library()

try:
    for line in data_clean:
        categorie, titre, auteur, annee, disponible = line

        category = library.find_category(categorie)
        if category:
            category.add_book(Book(titre, auteur, annee, disponible))

        else:
            library.add_category(Category(categorie, [Book(titre, auteur, annee, disponible)]))

except TypeError as e:
    print(e)


# Afficher le nombre total de livres disponibles
print(f"\nNombre total de livres disponibles : {library.total_available()}\n")


# Emprunter un livre
try:
    succes = library.borrow_book("Théâtre", "Dom Juan")
    if succes:
        print("Livre emprunté avec succès")

except LookupError as e:
    print(e)

except BookAvailableError as e:
    print(e)


print(f"Nombre total de livres disponibles : {library.total_available()}\n")


# Tenter d'emprunter un livre déjà emprunté (gérer l'erreur via try/except)
try:
    succes = library.borrow_book("Théâtre", "Dom Juan")
    if succes:
        print("Livre emprunté avec succès\n")

except LookupError as e:
    print(e)

except BookAvailableError as e:
    print(e)


# Rendre un livre
try:
    library.return_book("Théâtre", "Dom Juan")

except LookupError as e:
    print(e)


# Réafficher le nombre total disponible
print(f"\nNombre total de livres disponibles : {library.total_available()}\n")
