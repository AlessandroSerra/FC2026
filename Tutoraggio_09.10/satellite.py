import numpy as np


def altezza_satellite(T, unita):
    if unita == "m":
        T *= min2sec  # T = T * min2sec
    elif unita == "h":
        T *= ore2sec
    elif unita == "s":
        T = T
    else:
        raise ValueError("Unita non riconosciuta, usa s, m, h")

    if T <= 0:
        raise ValueError("Il periodo non puo' essere zero o negativo")

    h = (G * M * (T / (2 * np.pi)) ** 2) ** (1 / 3) - R
    return max(0, h)


G = 6.67430e-11  # costante di gravitazione universale in m^3 kg^-1 s^-2
M = 5.972e24  # massa della Terra in kg
R = 6_371_000  # raggio della Terra in metri
min2sec = 60
ore2sec = 3600

T = float(input("Inserisci il periodo del satellite: "))
unita = input("Inserisci le unita del tempo (s, m, h)")

altezza = altezza_satellite(T, unita)

print(f"L'altezza relativa al periodo {T} vale {altezza:.2e}")

