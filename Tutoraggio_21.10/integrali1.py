import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxw


def f(x):
    return np.sin(np.sqrt(50*x)) ** 2


def trapezi(x, y):
    h = x[1] - x[0]
    risultato = h/2 * (y[0] + y[-1]) + h * np.sum(y[1:-1])
    return risultato

def rettangoli(x, f):
    h = x[1] - x[0]
    x_medi = (x[:-1] + x[1:]) / 2
    risultato = h * np.sum(f(x_medi))
    return risultato

def simpson(x, y):
    h = x[1] - x[0]
    risultato = h/3 * (y[0] + y[-1] + 4*np.sum(y[1:-1:2]) + 2*np.sum(y[2:-1:2]))
    return risultato

def gauss(f, a, b, N):
    x, w = gaussxw(N, a, b)
    risultato = np.sum(w * f(x))
    return risultato

def calcola_errore(integrale, esatto):
    err_relativo = np.abs((integrale - esatto) / esatto)
    return err_relativo

A, B = 0, 1
N_points = np.arange(4, 31, 2)
esatto = 0.4343150380359837   # valore esatto dell'integrale

x_list = [np.linspace(A, B, N+1) for N in N_points]
y_list = [f(x) for x in x_list]

int_rett_list, err_rett_list = [], []
int_trap_list, err_trap_list = [], []
int_simps_list, err_simps_list = [], []
int_gauss_list, err_gauss_list = [], []

for i in range(len(x_list)):
    int_rett = rettangoli(x_list[i], f)
    err_rett = calcola_errore(int_rett, esatto)
    int_rett_list.append(int_rett)
    err_rett_list.append(err_rett)

    int_trap = trapezi(x_list[i], y_list[i])
    err_trap = calcola_errore(int_trap, esatto)
    int_trap_list.append(int_trap)
    err_trap_list.append(err_trap)

    int_simps = simpson(x_list[i], y_list[i])
    err_simps = calcola_errore(int_simps, esatto)
    int_simps_list.append(int_simps)
    err_simps_list.append(err_simps)

    int_gauss = gauss(f, A, B, N_points[i])
    err_gauss = calcola_errore(int_gauss, esatto)
    int_gauss_list.append(int_gauss)
    err_gauss_list.append(err_gauss)

fig, axs = plt.subplots(2, figsize=(8, 8), sharex=True)

ax = axs[0]
ax.plot(N_points, int_rett_list, marker='o', label='Rettangoli')
ax.plot(N_points, int_trap_list, marker='o', label='Trapezi')
ax.plot(N_points, int_simps_list, marker='o', label='Simpson')
ax.plot(N_points, int_gauss_list, marker='o', label='Gauss')
ax.axhline(y=esatto, ls='--', color='black', label='Esatto')
ax.set_ylabel('Valore Integrale')
ax.legend()

ax = axs[1]
ax.plot(N_points, err_rett_list, marker='o', label='Rettangoli')
ax.plot(N_points, err_trap_list, marker='o', label='Trapezi')
ax.plot(N_points, err_simps_list, marker='o', label='Simpson')
ax.plot(N_points, err_gauss_list, marker='o', label='Gauss')
ax.set_ylabel('Errore relativo')
ax.set_yscale('log')
ax.set_xlabel('# Punti')
ax.legend()

fig.tight_layout()
plt.show()