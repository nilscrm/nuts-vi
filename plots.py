import matplotlib.pyplot as plt
import numpy as np

FIGSIZE = (10, 7)

plt.rcParams.update(
  {
    "axes.prop_cycle": plt.cycler(
      "color",
      [
        "#000000",
        "#1b6989",
        "#e69f00",
        "#009e73",
        "#f0e442",
        "#50b4e9",
        "#d55e00",
        "#cc79a7",
      ],
    ),
    "figure.figsize": [12.0, 5.0],
    "font.serif": [
      "Palatino",
      "Palatino Linotype",
      "Palatino LT STD",
      "Book Antiqua",
      "Georgia",
      "DejaVu Serif",
    ],
    "font.family": "serif",
    "figure.facecolor": "#fffff8",
    "axes.facecolor": "#fffff8",
    "figure.constrained_layout.use": True,
    "font.size": 14.0,
    "hist.bins": "auto",
    "lines.linewidth": 3.0,
    "lines.markeredgewidth": 2.0,
    "lines.markerfacecolor": "none",
    "lines.markersize": 8.0,
  }
)

with open("samples.txt", "r") as f:
  samples_chunks = f.read().split("\n\n")

### Plot 1 ###
samples = [float(x) for x in samples_chunks[0].split("\n")]

fig, ax = plt.subplots(figsize=FIGSIZE)
ax.hist(samples, bins="auto")
ax.axvline(0, color="C1", linestyle="--")
ax.set_title("1D Gaussians!")
plt.savefig("plots/plot1.png")

### Plot 2 ###
samples = [float(x) for x in samples_chunks[1].split("\n")]
positions = [[float(x) for x in l.split(",") if l.strip()] for l in samples_chunks[2].split("\n")]
momenta = [[float(x) for x in l.split(",") if l.strip()] for l in samples_chunks[3].split("\n")]

fig, ax = plt.subplots(figsize=FIGSIZE)
for q, p in zip(positions, momenta):
    ax.plot(q, p)

y_min, _ = ax.get_ylim()
ax.plot(samples, y_min + np.zeros_like(samples), "ko")
ax.set_xlabel("Position")
ax.set_ylabel("Momentum")

ax.set_title("1D Gaussian trajectories in phase space!")
plt.savefig("plots/plot2.png")

### Plot 7 ###
samples = np.array([[float(x) for x in l.split(" ")] for l in samples_chunks[4].split("\n") if l.strip()])

fig, ax = plt.subplots(figsize=FIGSIZE)

means = np.array([np.array([1.0, 2.0]), -np.ones(2), np.array([-1.0, 2.0])])
ax.plot(samples[:, 0], samples[:, 1], "o", alpha=0.5)
ax.plot(means[:, 0], means[:, 1], "o", color="w", ms=20, mfc="C1")
ax.set_title("Multivariate Mixtures!")
plt.savefig("plots/plot7.png")

### Plot 8 ###
samples = np.array([[float(x) for x in l.split(" ")] for l in samples_chunks[5].split("\n") if l.strip()])
positions = np.array([[[float(x) for x in t.split(" ")] for t in l.split(",")] for l in samples_chunks[6].split("\n") if l.strip()])
momenta = np.array([[[float(x) for x in t.split(" ")] for t in l.split(",")] for l in samples_chunks[7].split("\n") if l.strip()])

fig, ax = plt.subplots(figsize=FIGSIZE)

steps = slice(None, None, 20)

ax.plot(means[:, 0], means[:, 1], "o", color="w", ms=20, mfc="C1")
for q, p in zip(positions, momenta):
    ax.quiver(
        q[steps, 0],
        q[steps, 1],
        p[steps, 0],
        p[steps, 1],
        headwidth=6,
        scale=100,
        headlength=7,
        alpha=0.8,
    )
    ax.plot(q[:, 0], q[:, 1], "k-", lw=1)
    ax.plot(samples[:, 0], samples[:, 1], "o", color="w", mfc="C2")

ax.set_title("Multivariate mixture trajectories!\nArrows show momentum!")
plt.savefig("plots/plot8.png")
