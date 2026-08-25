#!/usr/bin/env python3
"""MATH 4050 Ch.1 - the four A_K(t) examples, answering the four questions on
the "Examples" slide and setting up the taxonomy on the slide after it:
constant / continuous linear / continuous exponential / discrete.

Panels 1-3 share the axes of img/math4050/BlankAmount.png (t in [0,3],
A_K in [0,45]).  Panel 4 grows by only 1 per year, so it gets its own
vertical scale - otherwise the steps are invisible.  That is called out on
the panel itself.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

K, I = 20, 0.30      # principal; rate chosen large enough that the linear vs
                     # exponential contrast is visible over only three years
BLUE, GREY = "#1874CD", "#9a9a9a"

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Palatino", "Georgia", "DejaVu Serif"],
    "font.size": 13, "axes.titlesize": 15, "axes.labelsize": 13,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.linewidth": 1.1, "figure.facecolor": "white",
})

fig, axes = plt.subplots(2, 2, figsize=(12.6, 7.4), dpi=200)
t = np.linspace(0, 3, 400)

def frame(ax, title, kind, ylim=(0, 45), yticks=(0, 10, 20, 30, 40)):
    ax.set_title(title, pad=26)
    ax.set_xlim(-0.06, 3.2); ax.set_ylim(*ylim)
    ax.set_xticks([0, 1, 2, 3]); ax.set_yticks(list(yticks))
    ax.set_xlabel("$t$ (years)"); ax.set_ylabel("$A_K(t)$")
    # descriptor sits just under the title, outside the data area
    ax.text(0.5, 1.02, kind, transform=ax.transAxes, ha="center", va="bottom",
            fontsize=11.5, style="italic", color="#666")
    ax.axhline(K, color=GREY, lw=0.9, ls=(0, (4, 3)), zorder=1)
    # right end of the reference line: the only spot free in every panel
    ax.text(3.17, K, "$K=20$", ha="right", va="bottom", color=GREY, fontsize=10.5)
    ax.plot(0, K, "o", color=BLUE, ms=6.5, zorder=5)

# 1 - parents: no interest at all, A_K never grows
ax = axes[0, 0]
frame(ax, "Borrow 20 from your parents", "no interest  $\\Rightarrow$  constant")
ax.plot(t, np.full_like(t, K), color=BLUE, lw=2.8, zorder=4)

# 2 - friend: simple interest, A_K is linear
ax = axes[0, 1]
frame(ax, "Borrow 20 from your friend", "simple interest  $\\Rightarrow$  continuous, linear")
ax.plot(t, K * (1 + I * t), color=BLUE, lw=2.8, zorder=4)

# 3 - bank: compound interest, A_K is exponential
ax = axes[1, 0]
frame(ax, "Borrow 20 from a bank", "compound interest  $\\Rightarrow$  continuous, exponential")
ax.plot(t, K * (1 + I) ** t, color=BLUE, lw=2.8, zorder=4)

# 4 - deposit earning 1 at each year end: step function, own vertical scale
ax = axes[1, 1]
frame(ax, "Deposit 20, earns 1 at each year end", "discrete  $\\Rightarrow$  step function",
      ylim=(19.2, 23.8), yticks=(20, 21, 22, 23))
for n in range(3):
    ax.hlines(K + n, n, n + 1, color=BLUE, lw=2.8, zorder=4)
    ax.plot(n, K + n, "o", color=BLUE, ms=6.5, zorder=5)                        # value attained
    ax.plot(n + 1, K + n, "o", mfc="white", mec=BLUE, mew=1.9, ms=6.5, zorder=5)  # limit from left
ax.plot(3, K + 3, "o", color=BLUE, ms=6.5, zorder=5)
ax.text(0.97, 0.05, "vertical scale differs", transform=ax.transAxes,
        ha="right", va="bottom", fontsize=10, color="#999", style="italic")

fig.tight_layout(pad=1.4, h_pad=3.0, w_pad=2.8)
out = os.path.normpath(os.path.join(os.path.dirname(__file__),
                                    "../../img/math4050/AmountExamples.png"))
fig.savefig(out, bbox_inches="tight", facecolor="white")
print("wrote", out)
