
import statistics

def analyser_ventes(transactions):
    # Nettoyage
    transactions_valides = []
    for montant in transactions:
        if montant > 0:
            transactions_valides.append(montant)

    # Nombre total de transactions valides
    nb_transactions = len(transactions_valides)

    # Somme totale des ventes
    somme_totale = sum(transactions_valides)

    # Moyenne
    moyenne = somme_totale / nb_transactions

    # Médiane
    mediane = statistics.median(transactions_valides)

    # Écart-type (dispersion autour de la moyenne)
    ecart_type = statistics.stdev(transactions_valides)

    # Valeurs extrêmes
    valeur_max = max(transactions_valides)
    valeur_min = min(transactions_valides)

    # Détection des anomalies : transactions > 2 fois la moyenne
    anomalies = [montant for montant in transactions_valides if montant > 2 * moyenne]

    resultats = {
        "nombre_transactions": nb_transactions,
        "somme_totale": somme_totale,
        "moyenne": moyenne,
        "mediane": mediane,
        "ecart_type": ecart_type,
        "valeur_max": valeur_max,
        "valeur_min": valeur_min,
        "anomalies": anomalies
    }

    return resultats


if __name__ == "__main__":
    # Jeu de données de test
    jeu_de_test = [150, 200, 89, -20, 0, 320, 1200, 175, 210]

    rapport = analyser_ventes(jeu_de_test)

    print("=== Rapport d'analyse des ventes ===")
    print(f"Nombre de transactions valides : {rapport['nombre_transactions']}")
    print(f"Somme totale : {rapport['somme_totale']} €")
    print(f"Moyenne : {rapport['moyenne']:.2f} €")
    print(f"Médiane : {rapport['mediane']} €")
    print(f"Écart-type : {rapport['ecart_type']:.2f}")
    print(f"Valeur max : {rapport['valeur_max']} €")
    print(f"Valeur min : {rapport['valeur_min']} €")
    print(f"Transactions anormalement élevées : {rapport['anomalies']}")