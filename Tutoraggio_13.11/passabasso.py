import numpy as np
import matplotlib.pyplot as plt


def vin(t):
    """
    prende un valore di t, applica la funzione ceiling 1.2 -> 2
    se [2t] pari -> 1, se [2t] dispari -> -1
    """
    n = np.ceil(2 * t).astype(int)
    v = np.where(n % 2 == 0, 1.0, -1.0)
    return v


def f(vout, tau, vinput):
    """
    eq. differenziale circuito RC

    dVout/dt = (Vin - Vout) / tau
    """

    return (vinput - vout) / tau


def rk4(t, tau, V0=0.0):

    vout = np.zeros_like(t)
    vout[0] = V0

    for i in range(len(t) - 1):
        dt = t[i + 1] - t[i]
        yn = vout[i]

        in_volt = vin(t[i] + dt / 2)

        k1 = f(yn, tau, in_volt)
        k2 = f(yn + dt * k1 / 2, tau, in_volt)
        k3 = f(yn + dt * k2 / 2, tau, in_volt)
        k4 = f(yn + dt * k3, tau, in_volt)

        vout[i + 1] = yn + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

    return vout


# tau non e' altro che RC

t_start = 0.0  # s
t_end = 10.0  # s
h = 0.001

# tau = RC
tau_list = [0.01, 0.1, 1]  # s

# f = 1 / (2pi tau) -> 16Hz per tau = 0.01

# numero di passi = (t_f - t_i) / h

# {"chiave": valore}
soluzioni = {}

t = np.linspace(t_start, t_end, round((t_end - t_start) / h) + 1)

for tau in tau_list:
    soluzione = rk4(t, tau)
    soluzioni[tau] = soluzione


# Il limite di stabilità di RK4 è h/tau ~ 2.785, quindi per tau = 0.01
# diverge per h > ~ 0.0278.
tau_conv = 0.01
h_values = [0.01, 0.015, 0.02, 0.025, 0.03]
t_conv_end = 1.0  # s

soluzioni_conv = {}
t_conv = {}

for h in h_values:
    t_c = np.linspace(t_start, t_conv_end, round((t_conv_end - t_start) / h) + 1)
    t_conv[h] = t_c
    soluzioni_conv[h] = rk4(t_c, tau_conv)

fig, axs = plt.subplots(1, 2, figsize=(14, 5))

ax = axs[0]
ax.plot(t, vin(t), "--", color="black", alpha=0.5, label=r"$V_{in}$")

for tau in tau_list:
    f_cut = 1 / (2 * np.pi * tau)
    ax.plot(t, soluzioni[tau], label=rf"RC = {tau} s, fcut = {f_cut:.2f} Hz")

ax.set_xlabel("Tempo [s]")
ax.set_ylabel("Tensione [V]")
ax.set_title("Filtro passa basso RC con RK4")
ax.legend(frameon=True, framealpha=0.9, loc="upper left")

ax = axs[1]
for h in h_values:
    ax.plot(t_conv[h], soluzioni_conv[h], "o-", label=f"h = {h}")

ax.plot(t, vin(t), "--", color="black", alpha=0.8, label=r"$V_{in}$")
ax.set_xlabel("Tempo [s]")
ax.set_ylabel("Tensione [V]")
ax.set_title("Test convergenza passo integrazione")
ax.legend(frameon=True, framealpha=0.9, loc="upper left")
ax.set_xlim(0, t_conv_end)
ax.grid(alpha=0.6)

# NOTE: quando RK4 diventa instabile V -> infinito. Usiamo symlog
# perché la scala log non rappresenta valori <= 0 e V oscilla tra -1 e +1.
# symlog è lineare in [-linthresh, +linthresh] (qui le curve stabili restano
# leggibili) e logaritmica fuori (qui si vede la crescita della soluzione instabile).
ax.set_yscale("symlog", linthresh=1)

fig.tight_layout()
plt.show()

