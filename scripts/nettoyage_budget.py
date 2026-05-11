import pandas as pd
from sqlalchemy import create_engine
import os

# --- CONFIGURATION ---
user = " "
password = " "
host = "localhost"
db_name = "finance_publique_mali"
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db_name}")

fichiers = {
    2019: r"C:\Users\TRAORE\Documents\Budget_2019.csv",
    2020: r"C:\Users\TRAORE\Documents\Budget_2020.csv",
    2021: r"C:\Users\TRAORE\Documents\Budget_2021.csv"
}


def traiter_budget(annee, chemin):
    print(f"\n--- ANALYSE DU BUDGET {annee} ---")

    df = pd.read_csv(chemin, sep=',', encoding='UTF8')

    # Nettoyage des colonnes
    df.columns = df.columns.str.strip().str.upper().str.replace(' ', '_')

    # --- PHASE DE DIAGNOSTIC ---
    # On crée une série de test pour identifier les caractères qui bloquent
    # (On nettoie juste les virgules pour le test)
    test_numerique = pd.to_numeric(df['MONTANT'].astype(
        str).str.replace(',', ''), errors='coerce')

    # On repère les lignes qui ne sont pas des nombres (ex: les tirets)
    anomalies = df[test_numerique.isna() & df['MONTANT'].notna()]

    if len(anomalies) > 0:
        print(
            f"⚠️ {len(anomalies)} lignes contiennent des caractères non-numériques.")
        print(
            f"Exemples de valeurs trouvées : {anomalies['MONTANT'].unique()}")

    # --- NETTOYAGE ET CONVERSION ---
    # 1. On enlève les virgules
    df['MONTANT'] = df['MONTANT'].astype(str).str.replace(',', '')
    # 2. On transforme en nombre (les erreurs deviennent NaN)
    df['MONTANT'] = pd.to_numeric(df['MONTANT'], errors='coerce')
    # 3. On remplace les NaN par 0 pour la compatibilité MySQL
    df['MONTANT'] = df['MONTANT'].fillna(0)

    # On s'assure que la colonne ANNEE est bien au format entier
    if 'ANNEE' in df.columns:
        df['ANNEE'] = df['ANNEE'].astype(int)

    # --- INJECTION ---
    try:
        df.to_sql(f'Budget_{annee}', con=engine,
                  if_exists='replace', index=False, chunksize=1000)
        print(f"✅ Table 'Budget_{annee}' mise à jour dans MySQL.")
    except Exception as e:
        print(f"❌ Erreur MySQL : {e}")


# Boucle d'exécution
for annee, chemin in fichiers.items():
    if os.path.exists(chemin):
        traiter_budget(annee, chemin)
