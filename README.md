# 📊 Analyse de la Performance des Finances Publiques (Mali 2019-2021)

## 📝 Présentation du Projet
Ce projet consiste en la mise en place d'un pipeline de données complet (ETL et BI) pour analyser les budgets nationaux du Mali sur trois années consécutives. L'objectif est de transformer des fichiers budgétaires bruts en un tableau de bord stratégique permettant de piloter l'exécution financière et d'auditer les dépenses sensibles.

**Compétences démontrées :**
* **Python :** Automatisation du nettoyage (ETL) et gestion de la qualité des données.
* **SQL (MySQL) :** Modélisation de données et unification de tables volumineuses.
* **Power BI & DAX :** Création d'indicateurs de performance (KPI) et visualisation.

---

## 🛠️ Architecture du Projet

Le projet est structuré de manière modulaire pour garantir la robustesse du traitement :

1.  **Dossier `scripts/` :** Contient le script Python de nettoyage.
    * Gestion automatique des caractères non-numériques (ex: les tirets `-`) via `pd.to_numeric` et `fillna(0)`.
    * Automatisation du traitement des fichiers 2019, 2020 et 2021 via une boucle `for` et la bibliothèque `os`.
    * Injection directe dans MySQL via `SQLAlchemy`.

2.  **Dossier `sql/` :** Contient les requêtes de structuration.
    * Unification des données annuelles dans une table unique `budget_global` via une opération `UNION ALL`.
    * Optimisation des types de données pour faciliter les jointures.

3.  **Dossier `power_bi/` :** Contient la logique d'analyse.
    * Développement de mesures DAX complexes (Taux d'exécution, % de répartition via `ALL`, calcul d'écarts).
    * Focus spécifique sur l'audit des **Frais de Mission** pour analyser leur poids relatif dans les dépenses réelles.

---

## 📈 Indicateurs Clés (KPI)
Le tableau de bord final permet de répondre aux questions suivantes :
* **Taux d'exécution :** Quel est le ratio entre le budget initial et les liquidations réelles ?
* **Répartition :** Quelle est la part du budget consommée par les Institutions, les Ministères et les Charges Communes ?
* **Contrôle budgétaire :** Quel pourcentage du budget de fonctionnement est alloué aux déplacements et missions ?

---

## 🔐 Sécurité & Bonnes Pratiques
* Les identifiants de connexion aux bases de données sont gérés via des variables d'environnement (non incluses dans ce dépôt pour des raisons de sécurité).
* Utilisation du principe **DRY (Don't Repeat Yourself)** grâce à la création de fonctions réutilisables en Python.

## 📊 Aperçu du Tableau de Bord & Analyses

### 💻 Page 1 : Analyse de la consommation budgétaire
Cette vue offre un contrôle macro de l'exécution budgétaire (Prévu vs Réalisé) sur trois années et isole instantanément les écarts globaux.

<img width="1203" height="673" alt="GIT1" src="https://github.com/user-attachments/assets/af4f60d2-9e91-4061-85ac-78f2f67a5480" />

### 📈 Page 2 : Synthèse pluriannuelle des performances
Une perspective temporelle dynamique permettant de suivre la vélocité, l'évolution et la capacité d'absorption des fonds d'une année à l'autre (2019-2021).

<img width="1205" height="671" alt="GIT2" src="https://github.com/user-attachments/assets/e27b4268-d7bb-494e-b7a1-952e5f2ba5c2" />

### 🏛️ Page 3 : Audit de la distribution budgétaire par type de charge
Ce rapport met en lumière la répartition institutionnelle fine. Il permet de surveiller l'intensité budgétaire et d'identifier le poids des structures clés.

<img width="1226" height="680" alt="GIT3" src="https://github.com/user-attachments/assets/9363c128-0836-4c4b-8ddc-3870df3a61b4" />

---

---

## 👩‍💻 À propos de moi
Je suis **Safiatou Sidibé**, Data Analyst passionnée par l'utilisation de la donnée pour améliorer la transparence et la prise de décision, notamment dans le secteur des finances publiques et de l'éducation à Bamako.




