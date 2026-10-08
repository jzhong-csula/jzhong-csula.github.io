# 2026-10-08 — Ch3 §3.6: timelines for the outstanding loan balance OLB_k
# 风格沿用 img/math4050/Timeline.png：黑线 + 右箭头、刻度在下、现金流用向下箭头。
# 新增 jzhong 要的部分：把钱搬到估值日 k 的那根箭头（往前滚 / 往回折现）。
# 布局：现金流在轴上方；"搬运"箭头在轴下方，一行一根，标签就在各自箭头正上方，互不交叠。
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm", "font.size": 15})
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "img", "math4050")
BLUE, RED, INK, GREY = "#1f4e9c", "#c0392b", "black", "0.45"

def axis(ax, labels, xmax):
    ax.annotate("", xy=(xmax + .55, 0), xytext=(-.55, 0),
                arrowprops=dict(arrowstyle="-|>", lw=2.0, color=INK, mutation_scale=22))
    for x, lab, bold in labels:
        ax.plot([x, x], [-.09, .09], lw=2.6 if bold else 2.0, color=INK)
        ax.text(x, -.34, lab, ha="center", va="top", fontsize=15,
                weight="bold" if bold else "normal")

def payment(ax, x, lab, color):
    ax.annotate("", xy=(x, .07), xytext=(x, .92),
                arrowprops=dict(arrowstyle="-|>", lw=1.7, color=color, mutation_scale=16))
    ax.text(x, 1.00, lab, ha="center", va="bottom", color=color, fontsize=15)

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
    ax.text(xlab if xlab is not None else (x0 + x1) / 2, y + .16, lab, ha="center", va="bottom", color=color, fontsize=14.5)

def finish(ax, path, eq, title, xmax, ylo):
    ax.text(-.55, 2.55, title, ha="left", va="center", fontsize=17, weight="bold")
    ax.text((xmax + 1.1 - 1.1) / 2, ylo + .18, eq, ha="center", va="bottom", fontsize=18)
    ax.set_xlim(-1.1, xmax + 1.1); ax.set_ylim(ylo, 2.9); ax.axis("off")
    ax.figure.savefig(path, bbox_inches="tight", facecolor="white")

n, k = 10, 6

# ---------- 1. Retrospective ----------
fig, ax = plt.subplots(figsize=(11.2, 5.4), dpi=150)
axis(ax, [(0, "$0$", False), (1, "$1$", False), (2, "$2$", False),
          (k, "$k$", True), (n, "$n$", False)], n)
for x in (3.9, 8.0): ax.text(x, -.34, r"$\cdots$", ha="center", va="top", fontsize=15)
payment(ax, 0, "$L$", BLUE)
for x in (1, 2, k): payment(ax, x, "$Q$", RED)
ax.text(3.9, 1.08, r"$\cdots$", ha="center", va="center", color=RED, fontsize=15)
valuation(ax, k)
move(ax, 0, k, r"the loan, rolled forward:  $L\,(1+i)^{k}$", BLUE, 0)
move(ax, 1, k, r"what has been repaid, rolled forward:  $Q\,s_{\overline{k}|i}$", RED, 1)
finish(ax, os.path.join(OUT, "olb-retrospective.png"),
       r"$OLB_{k}\;=\;L\,(1+i)^{k}\;-\;Q\,s_{\overline{k}|i}$",
       "Retrospective - look back", n, -3.95)

# ---------- 2. Prospective ----------
fig, ax = plt.subplots(figsize=(11.2, 4.7), dpi=150)
axis(ax, [(0, "$0$", False), (k, "$k$", True), (k + 1, "$k+1$", False),
          (k + 2, "$k+2$", False), (n, "$n$", False)], n)
ax.text(3.0, -.34, r"$\cdots$", ha="center", va="top", fontsize=15)
for x in (k + 1, k + 2, n): payment(ax, x, "$Q$", RED)
ax.text(9.0, 1.08, r"$\cdots$", ha="center", va="center", color=RED, fontsize=15)
valuation(ax, k, ylo=0.12)
move(ax, n, k, r"discount every remaining payment back to $k$",
     RED, 0, rad=-0.12, xlab=(k + n) / 2)
finish(ax, os.path.join(OUT, "olb-prospective.png"),
       r"$OLB_{k}\;=\;Q\,a_{\overline{n-k}|i}$",
       "Prospective - look ahead", n, -2.85)
print("ok")
