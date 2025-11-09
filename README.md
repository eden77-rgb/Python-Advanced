# Python-Advanced

## 📚 Module métier — Gestion de fonds pour médiathèque
Logique métier de la gestion des fonds de livres d'une médiathèque. L'objectif n'est pas de créer une interface, mais un module métier propre, structuré et réutilisable.

---

## 🎯 Fonctionnalités principales
- Chargement des données via un fichier ```.csv```
- Nettoyage des lignes
- Emprunt d'un livre

---

## 🎬 Scénario
- Afficher le nombre total de livres disponibles
- Emprunter un livre
- Tenter d'emprunter un livre déjà emprunté (gérer l'erreur via try/except)
- Rendre un livre
- Réafficher le nombre total disponible

---

## 🗂 Format du fichier de données (exemple)

Le module attend un fichier texte simple (par défaut UTF-8)
```text
Catégorie ; Titre ; Auteur ; Année ; Disponible
Roman;Le Rouge et le Noir;Stendhal;1830;yes
```

---

## 🧪 Installation et utilisation

1. Cloner le dépôt :
  ```bash
  git clone https://github.com/eden77-rgb/Python-Advanced.git
  cd Python-Advanced/librairie
  ```

2. Lancement :
  ```bash
  python .\main.py
  ```

---

## Licence

Ce projet est sous licence MIT. Consultez le fichier `LICENSE` pour plus d'informations.

---

## Crédits

- **Développeur** : [eden77-rgb](https://github.com/eden77-rgb)
