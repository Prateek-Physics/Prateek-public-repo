import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Parameters for the damped spring pendulum
g = 9.81  # gravity (m/s^2)
L0 = 3 # natural length of the spring (m)
k = 12.0  # spring constant (N/m)
mu = 1.0  # damping coefficient (kg/s)
m = 1   # mass of the bob (kg)

# Initial conditions
theta0 = np.pi / 3  # initial angle (rad)
omega0 = 0          # initial angular velocity (rad/s)
L_initial = L0 + 0.2  # initial spring length (m)
Ldot_initial = 0      # initial rate of change of spring length (m/s)

# Time settings
t_max = 15          # total simulation time (s)
fps = 30            # frames per second
num_frames = t_max * fps
t = np.linspace(0, t_max, num_frames)

def damped_spring_pendulum(y, t, g, L0, k, mu, m):
    theta, omega, L, Ldot = y
    dydt = [
        omega,
        -(g / L) * np.sin(theta) - 2 * Ldot * omega / L,
        Ldot,
        L * omega**2 - (k / m) * (L - L0) - (mu / m) * Ldot + g * np.cos(theta)
    ]
    return dydt

from scipy.integrate import odeint

# Solve the differential equation
y0 = [theta0, omega0, L_initial, Ldot_initial]
solution = odeint(damped_spring_pendulum, y0, t, args=(g, L0, k, mu, m))
theta = solution[:, 0]
L = solution[:, 2]

# Convert to Cartesian coordinates
x = L * np.sin(theta)/2
y = -L * np.cos(theta)/2

# Trail settings
trail_secs = 5
trail_length = int(trail_secs * fps)

# Determine maximum length for setting the frame limits
max_length = np.max(L_initial + 0.2)

fig, ax = plt.subplots(figsize=(12, 12))
ax.set_xlim(-2.2 * max_length, 2.2 * max_length)
ax.set_ylim(-2.2 * max_length, 2.2 * max_length)
ax.set_aspect('equal', adjustable='box')
ax.grid(True)

line, = ax.plot([], [], 'o-', lw=2, color='blue')
trail, = ax.plot([], [], '-', lw=1, color='red', alpha=0.7)
anchor = Circle((0, 0), 0.02, color='black')
ax.add_patch(anchor)

def init():
    line.set_data([], [])
    trail.set_data([], [])
    return line, trail, anchor

def update(frame):
    # Update pendulum
    line.set_data([0, x[frame]], [0, y[frame]])

    # Update trail
    start = max(0, frame - trail_length)
    trail.set_data(x[start:frame+1], y[start:frame+1])

    return line, trail, anchor

ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, interval=1000/fps)

# Save the animation
ani.save('damped_spring_pendulum_simulation.gif', writer='pillow')
plt.show()
