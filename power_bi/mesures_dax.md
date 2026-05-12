# 📊 Analyse Budgétaire : Mesures DAX & Indicateurs Clés

Ce document répertorie les mesures DAX créées pour analyser le budget national du Mali (2019-2021). Chaque mesure répond à une problématique métier précise d'audit et de performance.

## 1. Suivi des Enveloppes Budgétaires
Ces mesures permettent de comparer les intentions de l'État (Initial) par rapport à la réalité du terrain (Liquidation).

* **Budget Initial Global** : Calcule le montant total prévu dans le budget initial.
    ```dax
    Budget_Initial_global = CALCULATE(SUM(budget_global[MONTANT]), budget_global[BUDGET_TYPE] = "INITIALE")
    ```

* **Budget Liquidation Global** : Calcule le montant total des dépenses réellement réalisées (le budget "réalisé").
    ```dax
    Budget_liquidation_global = CALCULATE(SUM(budget_global[MONTANT]), budget_global[BUDGET_TYPE] = "LIQUIDATION")
    ```

* **Écart Budgétaire** : Différence absolue entre le budget prévu et le budget réalisé.
    ```dax
    Ecart = [Budget_Initial_global] - [Budget_liquidation_global]
    ```

## 2. Indicateurs de Performance
* **Taux d'Exécution Global** : C'est l'indicateur central. Il permet de mesurer le pourcentage d'utilisation des fonds par rapport aux prévisions.
    ```dax
    Taux_Exécution_global = DIVIDE([Budget_liquidation_global], [Budget_Initial_global], 0)
    ```

## 3. Analyse de la Structure & Répartition
* **% Répartition Budget Global** : Permet de voir la part de chaque catégorie (Institutions, Ministères, Charges communes) dans le budget total réalisé. L'utilisation de `ALL` permet de comparer chaque catégorie au total global.
    ```dax
    % Répartition_budget_global = 
    DIVIDE(
      [Budget_liquidation_global], 
      CALCULATE([Budget_liquidation_global], ALL(budget_global[CATEGORIE]))
    )
    ```

## 4. Focus sur les Frais de Fonctionnement (Audit)
Un volet important de l'analyse a consisté à isoler les dépenses sensibles pour en vérifier le poids.

* **Frais de Missions Global** : Isole spécifiquement les sommes dépensées pour les déplacements et missions dans le budget réalisé.
    ```dax
    Frais Missions_global = 
    CALCULATE(
        SUM(budget_global[MONTANT]), 
        budget_global[LIBELLE_CP] = "Déplacement & Mission",
        budget_global[Budget_type] = "LIQUIDATION"
    )
    ```

* **% Missions Global** : Mesure le poids relatif des frais de mission par rapport au budget total de la structure. C'est un indicateur clé pour l'optimisation des dépenses.
    ```dax
    %Missions_global = DIVIDE([Frais Missions_global], [Budget_liquidation_global], 0)
    ```
