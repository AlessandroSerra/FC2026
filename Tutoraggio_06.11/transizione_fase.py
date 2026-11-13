import numpy as np
import matplotlib.pyplot as plt
import scienceplots

plt.style.use(["science", "notebook", "no-latex"])


def relaxation(c, x0=1.0, tol=1e-8, max_iter=100000):

    x = x0

    for i in range(max_iter):
        x_new = 1 - np.exp(-c * x)

        if abs(x_new - x) < tol:
            return x_new, i + 1

        x = x_new

    raise RuntimeError(f"Mancata convergenza per c={c}")


# Punto a: soluzione per c = 2
x, iterations = relaxation(c=2)

print(f"Soluzione per c=2: {x:.10f}")
print(f"Iterazioni: {iterations}")


# Punto b: soluzioni per c tra 0 e 3
c_values = np.linspace(0, 3, 301)

x_values = []
n_iterations = []

for c in c_values:
    x, n = relaxation(c)

    x_values.append(x)
    n_iterations.append(n)

x_values = np.array(x_values)
n_iterations = np.array(n_iterations)


# Grafico della transizione
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(c_values, x_values, lw=2)

ax.axvline(1, color="red", ls="--", label="$c=1$")

ax.set_xlabel("$c$")
ax.set_ylabel("$x$")
ax.set_title("Transizione di fase")
ax.legend()
ax.grid(alpha=0.3)

plt.show()


# Soluzione numerica già calcolata nell'esercizio
# c_values, x_values

c_near = np.linspace(1, 1.3, 200)

# Approssimazione analitica vicino a c = 1
x_approx = 2 * (c_near - 1) / c_near**2

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(c_values, x_values, label="Soluzione numerica")
ax.plot(c_near, x_approx, "--", label="Sviluppo perturbativo")

ax.set_xlim(0.9, 1.3)
ax.set_ylim(-0.02, 0.45)

ax.set_xlabel("$c$")
ax.set_ylabel("$x$")
ax.legend()
ax.grid(alpha=0.3)

plt.show()
