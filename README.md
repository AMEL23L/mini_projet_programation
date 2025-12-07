# Mini projet – Suivi et Analyse de la Consommation Énergétique

## Objectif du projet
Ce projet simule plusieurs capteurs énergétiques et environnementaux.
Il permet :
- de générer des mesures simulées
- de stocker ces mesures dans MongoDB
- d’analyser les données (moyennes)
- de détecter des anomalies
- de valider le code avec Pytest et Flake8

Aucune interface graphique ni communication IoT réelle.



## Technologies utilisées
- Python 3
- MongoDB
- Pytest
- Flake8



## Structure du projet
- capteurs/ : capteurs simulés
- stockage/ : gestion MongoDB
- analyse/ : analyse des données
- tests/ : tests unitaires
- main.py : script principal



## Exécution du projet
### Installer les dépendances :

```bash
pip install -r requirements.txt
```
### Lancer le programme :

```bash
python main.py
```
### Lancer les tests :

```bash
pytest
```
###  Vérifier le code :

```bash
flake8 .
```

## Auteur
Nom : milou
Filiere : Electronique
Date : 7/12/2025



