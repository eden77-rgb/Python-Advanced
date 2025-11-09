"""
Module de gestion d'une librairie.

Ce module permet de :
- trouver une categorie
- ajouter une categorie
- emprunter un livre
- rendre un livre
- récupérer le nombre de livres disponibles
- récupérer tous les livres
"""

from category import Category
from book import Book

class Library:
    """
    Représente une Librairie

    Attributs :
        categories (list[Category]) : réprésente toute les catégorie de la librairie
    """

    def __init__(self, categories : list[Category] | None = None):
        if categories is None:
            self.__categories = []

        else:
            if all(isinstance(categorie, list[Category]) for categorie in categories):
                self.__categories = categories

            else:
                raise TypeError("[ERREUR]: Toutes les entrées doivent être des Category")


    def find_category(self, name : str) -> Category | None:
        """Récupère une categorie selon son nom"""
        for category in self.__categories:
            if category.get_name() == name:
                return category

        return None


    def add_category(self, category : Category):
        """"Ajoute une categorie"""
        if isinstance(category, Category):
            self.__categories.append(category)

        else:
            raise TypeError("[ERREUR]: L'objet doit être une Category")


    def borrow_book(self, category_name : str, title : str) -> bool:
        """Emprunte un livre selon sa categorie, son titre et sa disponibilité"""
        category = self.find_category(category_name)

        if not category:
            raise LookupError("[ERREUR]: Categorie introuvable")

        book = category.find_book(title)
        if not book:
            raise LookupError("[ERREUR]: Livre introuvable")

        book.borrow()
        return True


    def return_book(self, category_name : str, title : str):
        """Rends un livre selon sa categorie, son titre et sa disponibilité"""
        category = self.find_category(category_name)

        if category:
            book_cible = category.find_book(title)

            if book_cible:
                book_cible.return_book()

            else:
                raise LookupError("[ERREUR]: Livre introuvable")

        else:
            raise LookupError("[ERREUR]: Categorie introuvable")


    def total_available(self) -> int:
        """Somme des livres disponnibles"""
        return sum(category.total_available() for category in self.__categories)


    def list_all_books(self) -> list[Book]:
        """Récupère tous les livres"""
        all_books = []

        for category in self.__categories:
            for book in category.get_books():
                all_books.append(book)

        return all_books
