# -----------------------------------------------
#               CONSEGNA
# -----------------------------------------------
"""
Una palla viene lasciata cadere dalla cima di una torre di altezza h
Trascuriamo l’attrito dell’aria.
Scrivere un programma che:
- chiede all’utente di fornire l’altezza della torre in metri
- chiede all’utente di fornire un intervallo di tempo t in secondi
- calcola a che altezza si trova la palla dopo t secondi e stampa il risultato
- calcola il tempo di volo della palla e stampa il risultato
"""


def prendi_input(cosa):
    while True:
        variabile = float(input(f"Inserisci {cosa}: "))

        if variabile < 0:
            print("La variabile non puo essere negativa")
        else:
            break

    return variabile


def legge_oraria(h0, t):
    g = 9.81
    h = h0 - (0.5 * g * t**2)
    return max(0, h)


def tempo_volo(h0):
    g = 9.81
    t = (2 * h0 / g) ** 0.5
    return t


h0 = prendi_input("altezza")
t = prendi_input("tempo")

altezza = legge_oraria(h0, t)
tempo_totale = tempo_volo(h0)

print(f"La palla si trova ad altezza {altezza:.2f} metri")
print(f"Il tempo totale di volo e' {tempo_totale:.2f} secondi")
