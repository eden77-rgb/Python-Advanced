"""
Module de gestion d'une categorie.

Ce module permet de :
- récupérer les informations d'une categori : nom, livres assignés
- trouver un livre
- ajouter un livre
- supprimer un livre
- récupérer les livres disponibles
- récupérer le nombre de livres disponibles
"""

from book import Book

class Category:
    """
    Représente une Categorie

    Attributs :
        name (str) : représente le nom de la categorie
        books (list[Book]) : représente les livres assigné a la categorie
    """

    def __init__(self, name : str, books : list[Book]):
        self.__name = name
        self.__books = books


    def get_name(self) -> str:
        """Récupère le nom de la catégorie"""
        return self.__name


    def get_books(self) -> list[Book]:
        """Récupère les livres de la catégorie"""
        return self.__books


    def find_book(self, title : str) -> Book | None:
        """Récupère un livre selon son titre"""
        for book in self.__books:
            if book.get_title() == title:
                return book

        return None


    def add_book(self, book : Book):
        """Ajoute un livre a la categorie"""
        if isinstance(book, Book):
            self.__books.append(book)

        else:
            raise TypeError("[ERREUR]: L'objet doit être un Book")


    def remove_book(self, title : str):
        """Supprime un livre de la categorie"""
        book = self.find_book(title)

        if book:
            self.__books.remove(book)

        else:
            raise LookupError("[ERREUR]: Livre introuvable")


    def available_books(self) -> list[Book]:
        """Renvoie la liste de tout les livres disponnible"""
        return [book for book in self.__books if book.is_available()]


    def total_available(self) -> int:
        """Renvoie le nombre de livre disponnible"""
        return len(self.available_books())
