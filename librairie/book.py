"""
Module de gestion d'un livre.

Ce module permet de :
- récupérer les informations d'un livre : titre, auteur, année, disponibilité
- emprunter un livre
- rendre un livre
"""

from exception import BookAvailableError

class Book:
    """
    Représente un Livre

    Attributs :
        title (str) : représente le titre du livre
        author (str) : représente l'auteur du livre
        year (int) : représente l'année du livre
        available (bool) : représente la disponibilité du livre
    """

    def __init__(self, title : str, author : str, year : int, available : bool):
        for attribut, type_attr in [(title, str), (author, str), (year, int), (available, bool)]:
            if not isinstance(attribut, type_attr):
                raise TypeError(f"[ERREUR]: Type incorrect pour: {attribut}, aulieu de {type_attr}")

        self.__title = title
        self.__author = author
        self.__year = year
        self.__available = available


    def get_title(self) -> str:
        """Récupère le titre du livre"""
        return self.__title


    def get_author(self) -> str:
        """Récupère l'auteur du livre"""
        return self.__author


    def get_year(self) -> int:
        """Récupère l'annee du livre"""
        return self.__year


    def is_available(self) -> bool:
        """Récupère la disponnibilité du livre"""
        return self.__available


    def borrow(self):
        """Modifie la disponibilité a faux"""
        if not self.__available:
            raise BookAvailableError(self.get_title())

        self.__available = False


    def return_book(self):
        """Modifie la disponibilité a vrai"""
        if self.__available:
            raise BookAvailableError(self.get_title())

        self.__available = True
