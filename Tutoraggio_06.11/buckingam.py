import matplotlib.pyplot as plt
import numpy as np
import scienceplots

plt.style.use(["science", "notebook", "no-latex"])


# Potenziale adimensionale V/V0
def V(x):
    return 1 / x**6 - np.exp(-x)


def golden_section(f, a, b, tol=1e-10, max_iter=1000):

    alpha = (np.sqrt(5) - 1) / 2

    x1 = b - alpha * (b - a)
    x2 = a + alpha * (b - a)

    f1 = f(x1)
    f2 = f(x2)

    for i in range(max_iter):
        if b - a < tol:
            break

        if f1 < f2:
            b = x2

            x2, f2 = x1, f1
            x1 = b - alpha * (b - a)
            f1 = f(x1)

        else:
            a = x1

            x1, f1 = x2, f2
            x2 = a + alpha * (b - a)
            f2 = f(x2)

    else:
        raise RuntimeError("Numero massimo di iterazioni raggiunto")

    return (a + b) / 2, i + 1


# Parametri
sigma = 1.0  # nm

x_min, n_iter = golden_section(V, 1.0, 4.0)

r_min = sigma * x_min

print(f"Minimo in x = {x_min:.12f}")
print(f"Distanza di equilibrio = {r_min:.12f} nm")
print(f"Potenziale minimo V/V0 = {V(x_min):.12f}")
print(f"Iterazioni = {n_iter}")


x = np.linspace(0.9, 8, 1000)

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(x, V(x), label="Potenziale di Buckingham")

ax.scatter(x_min, V(x_min), color="red", zorder=3, label=f"Minimo: {r_min:.4f} nm")

ax.axhline(0, color="black", ls="--", lw=1)

ax.set_xlabel(r"$r/\sigma$")
ax.set_ylabel(r"$V(r)/V_0$")
ax.set_ylim(-0.2, 0.25)

ax.legend()
ax.grid(alpha=0.3)

fig.tight_layout()
plt.show()
