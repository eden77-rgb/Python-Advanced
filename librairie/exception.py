"""
Module de gestion des exceptions

Ce module permet de :
- générer un Exception personnalisé
"""

class BookAvailableError(Exception):
    """
    Représente une exception levé si un livre est deja emprunté ou deja disponible

    Attribut : 
        book_title (str) : représente le titre du livre déja emprunté ou déja disponible
    """

    def __init__(self, book_title : str):
        super().__init__(f"\n[ERREUR]: Disponibilité du livre : {book_title}\n")
