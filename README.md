 Flora Market - Collecte & Analyse Descriptive
//Projet de TP INF232 EC2 - Analyse de données//


ce projet consiste à développer une application interactive de collecte de données en ligne. 
L'objectif est de permettre la saisie d'articles de marché et de générer instantanément une analyse 
statistique descriptive (prix moyen, min, max) pour transformer des données brutes en informations utiles.

   Fonctionnalités de l'Application
  
   -Saisie Dynamique :Formulaire complet pour enregistrer le nom de l'article, sa note de qualité (0 à 5) et son prix.
   -Statistiques en Temps Réel : Calcul automatique des indicateurs clés (Prix Minimum, Maximum, Moyen et Total des articles).
   -Visualisation Graphique : Génération d'histogrammes pour analyser la distribution des prix de manière visuelle.

   Architecture et Frameworks
Pour assurer la robustesse du projet, nous avons utilisé :
-Streamlit : Pour l'interface web interactive et la mise à jour dynamique des données.
-Pandas : Pour la structuration des données en *DataFrames* et les calculs statistiques (moyenne, agrégations).
- Plotly : Pour la création des graphiques d'analyse.
- GitHub & Streamlit Cloud : Pour le versionnage et l'hébergement de l'application exécutable.

  Lien de l'application en ligne
     L'application est déployée sur un serveur et accessible ici :
     [Accéder à Flora Market](https://nacpieup599-nacpieup-towe-ange-24g2259-collect-wlxhay.streamlit.app/)

   Installation locale
1. `git clone https://github.com/Nacpieup599/NACPIEUP-TOWE-ANGE-24G2259.git`
2. `pip install -r requirements.txt`
3. `streamlit run collect.py`
   conclusion   
Ce projet de collecte de données a permis de mettre en pratique les concepts fondamentaux de l'Analyse de données (EC2). 

À travers le développement de cette application, j'ai pu :
- Maîtriser le cycle complet de la donnée : de la saisie utilisateur au traitement statistique.
- Comprendre l'importance de la visualisation pour l'interprétation des prix du marché.
- Apprendre à déployer une solution logicielle sur un serveur cloud, rendant l'analyse accessible partout et en temps réel.

Ce TP constitue une base solide pour l'étude ultérieure des régressions et des modèles de classification supervisée.
 Informations sur l'auteur
- Nom : NACPIEUP TOWE ANGE
- Matricule : 24G2259
- niveau 2 Informatique
- Système : Ubuntu
