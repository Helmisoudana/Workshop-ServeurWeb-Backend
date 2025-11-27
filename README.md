🧠 Workshop : Gestion des Sessions, Absences et Rattrapages avec FastAPI, SQLModel & Firebase

Ce workshop a pour objectif d’apprendre à créer une application complète backend permettant de gérer :

👩‍🏫 Les enseignants

🎓 Les étudiants

📅 Les sessions d’enseignement

❌ Les absences

🔁 Les sessions de rattrapage

Le tout en utilisant des outils modernes, simples et professionnels.

🚀 Technologies utilisées
Technologie	Rôle
FastAPI	Framework backend ultra rapide pour construire des API
SQLModel	ORM moderne pour gérer les bases SQL
MySQL	Base de données relationnelle
Firebase Realtime Database	Stockage en temps réel des rattrapages
Python	Langage principal du projet
🎯 Objectifs du workshop

✔ Comprendre comment construire une API REST
✔ Manipuler MySQL avec SQLModel
✔ Gérer les relations : enseignant → session → absence → rattrapage
✔ Envoyer des données vers Firebase en temps réel
✔ Créer un code propre, structuré et scalable

🏗 Architecture du projet
project/
│── models/
│     ├── student.py
│     ├── teacher.py
│     ├── session.py
│     └── makeup.py
│
│── routes/
│     ├── student_routes.py
│     ├── teacher_routes.py
│     ├── session_routes.py
│     └── makeup_routes.py
│
│── firebase_config.py
│── database.py
│── main.py

🔥 Fonctionnalités principales
👨‍🏫 Gestion des enseignants

Ajouter, lister, modifier, supprimer des enseignants.

🎓 Gestion des étudiants

Créer un étudiant, afficher ses infos, voir ses sessions.

🗓 Gestion des sessions

Créer une session pour un enseignant.
Lister les sessions d’un étudiant.

❌ Gestion des absences

Enregistrer une absence pour un étudiant.

🔁 Gestion des rattrapages

Créer une session de rattrapage et :

la sauvegarder dans MySQL

l’envoyer automatiquement dans Firebase Realtime Database en temps réel

🔥 Exemple : Enregistrement d’un rattrapage

Quand on crée un rattrapage :

{
  "student_id": 1,
  "session_id": 3,
  "new_date": "2025-03-10 10:00",
  "reason": "Absent pour maladie"
}


Il est automatiquement ajouté :

dans la table makeupsession (MySQL)

dans Firebase :

makeup/
   5/
      student_id: 1
      session_id: 3
      new_date: "2025-03-10 10:00"
      reason: "Absent pour maladie"

🎓 Public cible

Étudiants

Débutants en FastAPI

Développeurs voulant apprendre SQLModel

Toute personne souhaitant créer un backend professionnel

🤝 Contributeurs

Helmi Soudana
