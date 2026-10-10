import matplotlib.pyplot as plt
import numpy as np


def trapezi(t, v):

    h = t[1] - t[0]
    risultato = h / 2 * (v[0] + v[-1]) + h * np.sum(v[1:-1])  # [a, b)
    return risultato


def trapezi_bis(t, v):
    spazio = []

    distanza_iniziale = 0
    for i in range(1, len(t)):
        h = t[i] - t[i - 1]
        distanza = distanza_iniziale + h / 2 * (v[i] + v[i - 1])
        distanza_iniziale = distanza
        spazio.append(distanza)

    return spazio


t, v_t = np.loadtxt("velocities.txt", unpack=True)

distanza = trapezi(t, v_t)
s_t = trapezi_bis(t, v_t)

print(f"La distanza percorsa vale {distanza:.2f} metri")

fig, ax = plt.subplots()

ax.plot(t, v_t, label="Velocita'", color="blue")
ax.set_xlabel("tempo [s]")
ax.set_ylabel("velocita [m/s]", color="blue")

ax2 = ax.twinx()
ax2.plot(t[1:], s_t, label="Posizione", color="red")
ax2.set_ylabel("posizione [m]", color="red")

fig.tight_layout()
plt.show()

