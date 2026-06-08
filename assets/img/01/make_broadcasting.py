"""Generate broadcasting.png for the Day 3 tutorial.

Run with an ephemeral env (no project deps needed):

    uv run --with matplotlib --with numpy python assets/img/01/make_broadcasting.py
"""

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def grid(ax, x0, y0, data, color, title):
    rows, cols = len(data), len(data[0])
    for i in range(rows):
        for j in range(cols):
            ax.add_patch(
                Rectangle((x0 + j, y0 - i), 1, 1, facecolor=color, edgecolor="white", lw=2)
            )
            ax.text(
                x0 + j + 0.5, y0 - i + 0.5, str(data[i][j]),
                ha="center", va="center", fontsize=12, color="#1f2329",
            )
    ax.text(x0 + cols / 2, y0 + 1.25, title, ha="center", fontsize=11, weight="bold")


def main():
    fig, ax = plt.subplots(figsize=(8, 2.6))
    A = [[10], [20], [30]]          # (3, 1)
    b = [[1, 2, 3]]                 # (1, 3)
    R = [[a[0] + bb for bb in b[0]] for a in A]  # (3, 3)

    grid(ax, 0, 3, A, "#aed581", "A  (3, 1)")
    ax.text(2.0, 2.0, "+", ha="center", va="center", fontsize=22)
    grid(ax, 3, 3, b, "#4fc3f7", "b  (1, 3)")
    ax.text(6.7, 2.0, "=", ha="center", va="center", fontsize=22)
    grid(ax, 7.5, 3, R, "#ffb74d", "A + b  (3, 3)")

    ax.set_xlim(-0.5, 11.5)
    ax.set_ylim(-0.2, 4.8)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.suptitle(
        "Broadcasting: a (3,1) column and a (1,3) row stretch to a (3,3) result", fontsize=12
    )
    fig.tight_layout()
    fig.savefig("assets/img/01/broadcasting.png", dpi=130, bbox_inches="tight")
    print("wrote assets/img/01/broadcasting.png")


if __name__ == "__main__":
    main()
