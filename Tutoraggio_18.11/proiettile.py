import matplotlib.pyplot as plt
import numpy as np

from Vettori import Vec2D


# Equazioni del moto
def projectile(position, velocity, mass, drag, gravity):
    """
    Equations of motion: d(r, v)/dt = (v, a),
    with a = g - (b/m)v.
    """
    acceleration = gravity - (drag / mass) * velocity
    return velocity, acceleration


# Integratore RK4
def rk4(position, velocity, h, mass, drag, gravity):

    k1_r, k1_v = projectile(position, velocity, mass, drag, gravity)

    k2_r, k2_v = projectile(
        position + h / 2 * k1_r, velocity + h / 2 * k1_v, mass, drag, gravity
    )

    k3_r, k3_v = projectile(
        position + h / 2 * k2_r, velocity + h / 2 * k2_v, mass, drag, gravity
    )

    k4_r, k4_v = projectile(
        position + h * k3_r, velocity + h * k3_v, mass, drag, gravity
    )

    position_new = position + h / 6 * (k1_r + 2 * k2_r + 2 * k3_r + k4_r)

    velocity_new = velocity + h / 6 * (k1_v + 2 * k2_v + 2 * k3_v + k4_v)

    return position_new, velocity_new


# Energie
def kinetic_energy(velocity, mass):
    return 0.5 * mass * (velocity @ velocity)


def potential_energy(position, mass, gravity):
    return -mass * (gravity @ position)


# Parametri

mass = 1.0
gravity = Vec2D(0.0, -9.81)

v0 = 20.0
theta = np.pi / 4  # 45 gradi in radianti

initial_position = Vec2D(0.0, 0.0)
initial_velocity = Vec2D(
    v0 * np.cos(theta),
    v0 * np.sin(theta),
)

drag_values = [0.0, 0.2, 0.5]

t0 = 0.0
tf = 5.0
h = 0.01

n_steps = round((tf - t0) / h)
t = np.linspace(t0, tf, n_steps + 1)


# Risoluzione numerica

solutions = {}

for drag in drag_values:
    position = initial_position
    velocity = initial_velocity

    trajectory = [position]
    velocities = [velocity]

    for i in range(n_steps):
        dt = t[i + 1] - t[i]

        position, velocity = rk4(position, velocity, dt, mass, drag, gravity)

        if position.y < 0:
            break

        trajectory.append(position)
        velocities.append(velocity)

    solutions[drag] = (trajectory, velocities)


# Plotting

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

colors = ["tab:blue", "orange", "green"]

for i, drag in enumerate(drag_values):
    color = colors[i % len(colors)]

    trajectory, velocities = solutions[drag]
    times = t[: len(trajectory)]

    x = [r.x for r in trajectory]
    y = [r.y for r in trajectory]

    ek = np.array([kinetic_energy(v, mass) for v in velocities])

    ep = np.array([potential_energy(r, mass, gravity) for r in trajectory])

    etot = ek + ep

    # Traiettoria
    ax1.plot(x, y, color=color, label=rf"$b={drag}$")

    # Energie, plottiamo solo la prima legenda per non rendere la figura pesante
    ax2.plot(times, ek, color=color, ls="--", label="Cinetica" if i == 0 else None)

    ax2.plot(times, ep, color=color, ls=":", label="Potenziale" if i == 0 else None)

    ax2.plot(times, etot, color=color, ls="-", label="Totale" if i == 0 else None)


# Traiettoria

ax1.set_xlabel("Horizontal position (m)")
ax1.set_ylabel("Vertical position (m)")
ax1.set_title("Projectile trajectories")
ax1.axhline(0, color="black", ls="--", lw=1)
ax1.legend()
ax1.grid(alpha=0.3)


# Energie

ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Energy (J)")
ax2.set_title("Mechanical energy")
ax2.legend(loc="lower left")
ax2.grid(alpha=0.3)

fig.tight_layout()
plt.show()
