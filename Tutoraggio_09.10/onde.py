import numpy as np
import matplotlib.pyplot as plt

def onda(x, y, x0, y0, A, lambda_):
    r = distanza(x, y, x0, y0)
    return A * np.sin(2 * np.pi / lambda_ * r)

def distanza(x, y, x0, y0):
    return np.sqrt((x-x0)**2 + (y-y0)**2)


d = 0.2     # metri
A = 1
lambda_ = 0.05   # metri
x1_0, y1_0 = -d/2, 0.0
x2_0, y2_0 = d/2, 0.0

l = 1   # metri
x = np.linspace(-l/2, l/2, 500)
y = np.linspace(-l/2, l/2, 500)
X, Y = np.meshgrid(x, y)

Z1 = onda(X, Y, x1_0, y1_0, A, lambda_)
Z2 = onda(X, Y, x2_0, y2_0, A, lambda_)
Z_totale = Z1 + Z2

fig, ax = plt.subplots()
ax.imshow(Z_totale, extent=(-0.5, 0.5, -0.5, 0.5))
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_title('Interferenza tra onde sferiche')

fig.tight_layout()
plt.show()