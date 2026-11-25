import numpy as np
import matplotlib.pyplot as plt

from Vettori import Vec2D as vec

from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle


def GetDistances(positions):
    """
    d_ij = p_i - p_j
    """
    N = len(positions)
    dist = np.full((N, N), fill_value=vec(0, 0))

    for i in range(N):
        for j in range(i+1, N):
            dist[i, j] = positions[i] - positions[j]
            dist[j, i] = - dist[i, j]

    return dist


def GetAcceleration(distances, G_value, masses, Conv):
    """
    F = -g Mm / d**2
    a = -G * m/d**2

          F_11 F_12 F_13 ....       
    F = (           )
          F_21 F_22
          F_31 F...

    """
    N = len(distances)
    forces = np.full((N, N), fill_value=vec(0, 0))

    for i in range(N):
        for j in range(i+1, N):
            dist = distances[i, j]

            forces[i, j] = -G_value * masses[i] * masses[j] / abs(dist)**2 * Conv * dist.unit()
            forces[j, i] = - forces[i, j]

    accelerations = np.sum(forces, axis=1) / masses
    return accelerations


def DoVerlet(old_positions, old_velocities, Tau, G_value, masses, Conv):
    """
    a dipende da p
    p_i+1 = p_i + v_i * dt + 1/2 a_i dt**2
    v_i+1 = v_i + 1/2(a_i + a_i+1)*dt
    """
    old_distances = GetDistances(old_positions)
    old_accelerations = GetAcceleration(old_distances, G_value, masses, Conv)

    new_positions = old_positions + old_velocities*Tau + 0.5 * old_accelerations * Tau**2

    new_distances = GetDistances(new_positions)
    new_accelerations = GetAcceleration(new_distances, G_value, masses, Conv)

    new_velocities = old_velocities + 0.5 * (old_accelerations + new_accelerations) * Tau

    return new_positions, new_velocities



def Simulate(params, constants):

    N_steps = params["N_steps"]
    Tau = params["Tau"]

    M_sun = constants["M_sun"]
    M_earth = constants["M_earth"]
    G_value = constants["G_value"]
    Conv = constants["Conv"]
    masses = np.array([M_sun, M_earth])

    positions = np.full((2, N_steps), fill_value=vec(0, 0))
    velocities = np.full((2, N_steps), fill_value=vec(0, 0))

    pos0_S = vec(0, 0)
    pos0_e = vec(1, 0)
    vel0_S = vec(0, 0)
    vel0_e = vec(0, 2*np.pi)

    positions[:, 0] = pos0_S, pos0_e
    velocities[:, 0] = vel0_S, vel0_e

    for i in range(N_steps - 1):
        old_positions = positions[:, i]
        old_velocities = velocities[:, i]

        new_positions, new_velocities = DoVerlet(old_positions, old_velocities, Tau, G_value, masses, Conv)
        
        positions[:, i+1] = new_positions
        velocities[:, i+1] = new_velocities

    return positions, velocities
    



# useremo AU per distanza e Years per tempi
constants = {
    "G_value": 6.6743e-11,  # m^3 kg^-1 s^-2
    "M_sun": 1.9884e30,     # kg
    "M_earth": 5.972e24,    # kg
    "AU_value": 1.49598e11,  # m
    "year2sec": np.pi * 1e7
}
constants["Conv"] = constants["AU_value"]**-3 * constants["year2sec"]**2

params = {
    "N_steps": 5000,
    "Period": 1,
    "N_cycles": 5
}
params["Tau"] = params["N_cycles"] * params["Period"] / params["N_steps"]


positions, velocities = Simulate(params, constants)


fig, ax = plt.subplots(figsize=(5, 5))

sun = ax.add_patch(
    Circle(
        (positions[0, 0].x, positions[0, 0].y),
        radius=0.04,
        fc="orange",
        label="Sole"
    )
)

earth = ax.add_patch(
    Circle(
        (positions[1, 0].x, positions[1, 0].y),
        radius=0.04,
        fc='blue',
        label="Terra"
    )
)

ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel("X [A.U.]")
ax.set_ylabel("Y [A.U.]")
ax.legend(loc="lower right")


def animate(i):
    sun.set_center((positions[0, i].x, positions[0, i].y))
    earth.set_center((positions[1, i].x, positions[1, i].y))

anim = FuncAnimation(fig, animate, frames=params["N_steps"], repeat=False, interval=10)

fig.tight_layout()
plt.show()