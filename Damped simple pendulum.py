import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle

# Parameters for the damped pendulum
g = 9.81  # gravity (m/s^2)
L = 1.0   # length of the pendulum (m)
mu = 1.0  # damping coefficient (kg/s)
m = 1.0   # mass of the bob (kg)

# Initial conditions
theta0 = np.pi / 2  # initial angle (rad)
omega0 = 0          # initial angular velocity (rad/s)

# Time settings
t_max = 10          # total simulation time (s)
fps = 30            # frames per second
num_frames = t_max * fps
t = np.linspace(0, t_max, num_frames)

def damped_pendulum(y, t, g, L, mu, m):
    theta, omega = y
    dydt = [omega, -(g / L) * np.sin(theta) - (mu / m) * omega]
    return dydt

from scipy.integrate import odeint

# Solve the differential equation
y0 = [theta0, omega0]
solution = odeint(damped_pendulum, y0, t, args=(g, L, mu, m))
theta = solution[:, 0]

# Convert to Cartesian coordinates
x = L * np.sin(theta)
y = -L * np.cos(theta)

# Trail settings
trail_secs = 0.8
trail_length = int(trail_secs * fps)

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.2 * L, 1.2 * L)
ax.set_ylim(-1.2 * L, 1.2 * L)
ax.set_aspect('equal', adjustable='box')
ax.grid(True)

line, = ax.plot([], [], 'o-', lw=2, color='blue')
trail, = ax.plot([], [], '-', lw=1, color='green', alpha=0.7)
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
ani.save('damped_pendulum_simulation.gif', writer='pillow')
plt.show()
