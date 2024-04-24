# Projet de Session en Développement de Logiciels et Sécurité des Applications – Système de Réservation de Billets

Ce projet a pour but de faire étalage des concepts acquis en développement de logiciels et d’applications.

## Table des Matières

- [Installation](#installation)
- [Utilisation](#utilisation)
- [Fonctionnalités](#fonctionnalités)
- [Technologies Utilisées](#technologies-utilisées)
- [Sécurité](#sécurité)
- [Contributeurs](#contributeurs)

## Installation

Instructions étape par étape pour installer et configurer votre projet localement.

```bash
git clone https://github.com/votreusername/votrerepo.git
cd votrerepo
pip install -r requirements.txt
```
## Utilisation

Afin de tester les fonctionalitées admin, veuillez vous connecter en tant que  admin/password.

## Fonctionnalités
 Gestion des Événements

 Gestion des Utilisateurs
 

Authentification : Système d'authentification pour les utilisateurs.
Profil : Création et gestion de profils utilisateurs avec nom complet, username, password et status.

## Gestion des Événements

Administration des Événements : Ajout, modification et suppression d'événements.
Catégorisation : Attribution de catégories ou de tags à chaque événement.
Visualisation : Affichage d'une liste d'événements avec nom, date, emplacement et prix.

## Gestion des Utilisateurs

Administration des Utilisateurs : Gestion des comptes utilisateurs, attribution des rôles "Admin" ou "Client". 
Catégorisation : Attribution des privilèges et permissions correspondants à chaque rôle. 
Visualisation : Affichage d'une liste des utilisateurs avec leur rôle attribué.

## Système de Réservation

Réservations : Système de réservation de billets, avec gestion des statuts (confirmé, en attente, annulé).

## Interface Utilisateur

Navigation : Interface intuitive avec des pages pour l'accueil, les événements, et le login.

## Technologies Utilisées

Python3
Flask
SQL
Jinja2
MySQL Workbench

## Sécurité

Validation des formulaires : Assurer que les données entrées par les utilisateurs sont valides.
Encryption avec Bcrypt : Utilisation de Bcrypt pour l'encryption des mots de passe.

## Contributeurs

Maxime St-Pierre
Michael Brunet
Stéphane Labrie
