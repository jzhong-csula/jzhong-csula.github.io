# 共享的 timeline 画图 helper —— MATH 4050 各章的 timeline 图都从这里取。
# 风格沿用 img/math4050/Timeline.png：黑线 + 右箭头、刻度在下、现金流用向下箭头。
# 2026-10-27 从 math4050-olb-timelines.py 抽出来，这样 Ch6 的 bond timeline
# 可以直接 import，不用复制粘贴一份 axis/payment/finish（AGENTS.md §3）。
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm", "font.size": 15})
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "img", "math4050")
BLUE, RED, INK, GREY, GREEN = "#1f4e9c", "#c0392b", "black", "0.45", "#1e7a4f"


def axis(ax, labels, xmax):
    ax.annotate("", xy=(xmax + .55, 0), xytext=(-.55, 0),
                arrowprops=dict(arrowstyle="-|>", lw=2.0, color=INK, mutation_scale=22))
    for x, lab, bold in labels:
        ax.plot([x, x], [-.09, .09], lw=2.6 if bold else 2.0, color=INK)
        ax.text(x, -.34, lab, ha="center", va="top", fontsize=15,
                weight="bold" if bold else "normal")


def payment(ax, x, lab, color, top=.92, lw=1.7):
    ax.annotate("", xy=(x, .07), xytext=(x, top),
                arrowprops=dict(arrowstyle="-|>", lw=lw, color=color, mutation_scale=16))
    ax.text(x, top + .08, lab, ha="center", va="bottom", color=color, fontsize=15)


def valuation(ax, k, ylo=1.34):
    # 虚线只画在现金流标签上方，免得压住 k 处那根付款箭头
    ax.plot([k, k], [ylo, 1.68], ls=(0, (4, 3)), lw=1.3, color=GREY, zorder=0)
    ax.text(k, 1.74, "valuation date $k$", ha="center", va="bottom", fontsize=13, color="0.3")


def move(ax, x0, x1, lab, color, row, rad=0.12, xlab=None):
    """轴下方第 row 行：一根略弓的箭头，标签在箭头正上方。"""
    y = -1.30 - 1.05 * row   # 第 0 行要让开轴下方的刻度标签
    ax.add_patch(FancyArrowPatch((x0, y), (x1, y), connectionstyle=f"arc3,rad={rad}",
                                 arrowstyle="-|>", mutation_scale=20, lw=2.0, color=color))
    ax.plot([x0, x0], [-.12, y], lw=1.0, ls=":", color=color, alpha=.55)
    ax.text(xlab if xlab is not None else (x0 + x1) / 2, y + .16, lab,
            ha="center", va="bottom", color=color, fontsize=14.5)


def finish(ax, path, eq, title, xmax, ylo):
    ax.text(-.55, 2.55, title, ha="left", va="center", fontsize=17, weight="bold")
    ax.text((xmax + 1.1 - 1.1) / 2, ylo + .18, eq, ha="center", va="bottom", fontsize=18)
    ax.set_xlim(-1.1, xmax + 1.1); ax.set_ylim(ylo, 2.9); ax.axis("off")
    ax.figure.savefig(path, bbox_inches="tight", facecolor="white")
