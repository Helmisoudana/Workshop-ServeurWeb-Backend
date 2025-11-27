# 🧠 Workshop : Gestion des Sessions, Absences et Rattrapages avec FastAPI, SQLModel & Firebase

Ce workshop a pour objectif d'apprendre à construire une **API backend complète** permettant de gérer les enseignants, les étudiants, les sessions d’enseignement, les absences et les sessions de rattrapage.  
Le projet utilise une architecture professionnelle et des technologies modernes telles que **FastAPI**, **SQLModel**, **MySQL** et **Firebase Realtime Database**.

## 🚀 Technologies utilisées
- **FastAPI** – Framework rapide pour créer des API REST
- **SQLModel** – ORM moderne basé sur Pydantic + SQLAlchemy
- **MySQL** – Base de données relationnelle
- **Firebase Realtime Database** – Stockage en temps réel pour les rattrapages
- **Python 3.10+**

## 🎯 Objectifs du Workshop
- Comprendre le fonctionnement d’une API REST
- Manipuler MySQL à travers SQLModel
- Gérer les relations entre les différents modèles (Teacher, Student, Session, Absence, MakeUpSession)
- Enregistrer automatiquement les données des rattrapages dans Firebase
- Organiser un projet backend de manière propre et scalable

## 🏗 Architecture du Projet
```
project/
│── models/
│ ├── student.py
│ ├── teacher.py
│ ├── session.py
│ └── makeup.py
│
│── routes/
│ ├── student_routes.py
│ ├── teacher_routes.py
│ ├── session_routes.py
│ └── makeup_routes.py
│
│── firebase_config.py
│── database.py
│── main.py
```

## 🔁 Fonctionnalité principale : Rattrapage
Lorsqu'une session de rattrapage est créée, elle est :
- enregistrée dans **MySQL** via SQLModel
- envoyée automatiquement dans **Firebase Realtime Database**, en temps réel

Exemple d’objet envoyé :
```json
{
  "student_id": 1,
  "session_id": 3,
  "new_date": "2025-03-10 10:00",
  "reason": "Absent pour maladie"
}
```

Ce workshop est destiné aux étudiants, développeurs débutants en FastAPI, et toute personne souhaitant apprendre à construire un backend professionnel.

