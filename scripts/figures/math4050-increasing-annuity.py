# 2026-10-20 — Ch3 §3.9: 让 (I_{P,Q}a) 可以现推，不用背
#
# 为什么要这三张图（jzhong 2026-10-15）：课本 p.158-160 的推导"有点多，没什么用,
# 他们也不会记得"，而幻灯片上该公式只给结论。要的是一个记法，让 Q/i 和 -n v^n
# 各自对上一个**动作**：买票 / 退票。
#
# 风格沿用 math4050-olb-timelines.py（黑轴 + 右箭头、刻度在下、现金流是轴上方的
# 向下箭头、蓝=出钱 红=进钱）。
#
# 产出 3 张：
#   ipqa-split.png            把要的现金流劈成 level + increment 两层
#   ipqa-tickets.png          increment 那层从哪来：每年买一张永续票，第 n 年全退掉
#   ex3918-decomposition.png  Example 3.9.18 的三段分解（同一张图三条带，好对比）
import os, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

plt.rcParams.update({"font.family": "serif", "mathtext.fontset": "cm", "font.size": 15})
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "img", "math4050")
BLUE, RED, INK, GREY = "#1f4e9c", "#c0392b", "black", "0.55"

# ---------------------------------------------------------------- 画带的零件
def axis(ax, ticks, xmax, dots=()):
    """ticks: [(x, label, bold)]；dots: 轴下方要画省略号的 x。"""
    ax.annotate("", xy=(xmax + .55, 0), xytext=(-.55, 0),
                arrowprops=dict(arrowstyle="-|>", lw=2.0, color=INK, mutation_scale=22))
    for x, lab, bold in ticks:
        ax.plot([x, x], [-.09, .09], lw=2.6 if bold else 2.0, color=INK)
        ax.text(x, -.36, lab, ha="center", va="top", fontsize=14,
                weight="bold" if bold else "normal")
    for x in dots:
        ax.text(x, -.36, r"$\cdots$", ha="center", va="top", fontsize=15)

def flow(ax, x, lab, color, up=False, ls="-", alpha=1.0, fs=14):
    """现金流：轴上方的向下箭头，标签在箭头上端。up=True 画成离开轴（出钱）。"""
    y0, y1 = (.07, .95) if not up else (.95, .07)
    ax.annotate("", xy=(x, y0), xytext=(x, y1),
                arrowprops=dict(arrowstyle="-|>", lw=1.7, color=color,
                                mutation_scale=16, linestyle=ls, alpha=alpha))
    if lab:
        ax.text(x, 1.04, lab, ha="center", va="bottom", color=color,
                fontsize=fs, alpha=alpha)

def dots_mid(ax, x, color=RED, y=.52):
    ax.text(x, y, r"$\cdots$", ha="center", va="center", color=color, fontsize=16)

def band(ax, title, pv=None, xmax=6, ylim=(-.95, 1.95)):
    ax.text(-.55, ylim[1] - .03, title, ha="left", va="top", fontsize=15.5, weight="bold")
    if pv:
        ax.text(xmax + .9, .55, pv, ha="left", va="center", fontsize=17)
    ax.set_xlim(-1.1, xmax + 4.4); ax.set_ylim(*ylim); ax.axis("off")

def brace(ax, x0, x1, y, lab, color=GREY):
    ax.add_patch(FancyArrowPatch((x0, y), (x1, y), arrowstyle="|-|,widthA=3,widthB=3",
                                 mutation_scale=1, lw=1.4, color=color))
    ax.text((x0 + x1) / 2, y - .14, lab, ha="center", va="top", fontsize=13, color="0.35")


# ================================================================ 图 1：劈两层
# 显示的时点：0,1,2,3,…,n-1,n  →  x = 0,1,2,3,(4=…),5,6
T = [(0, "$0$"), (1, "$1$"), (2, "$2$"), (3, "$3$"), (5, "$n\\!-\\!1$"), (6, "$n$")]
XM, DOT = 6, (4,)

fig, axs = plt.subplots(3, 1, figsize=(13.6, 7.2), dpi=150)

ax = axs[0]
axis(ax, [(x, l, False) for x, l in T], XM, DOT)
for x, lab in [(1, "$P$"), (2, "$P\\!+\\!Q$"), (3, "$P\\!+\\!2Q$"),
               (5, "$P\\!+\\!Q(n\\!-\\!2)$"), (6, "$P\\!+\\!Q(n\\!-\\!1)$")]:
    flow(ax, x, lab, RED)
dots_mid(ax, 4)
band(ax, "What you are paid", r"$(I_{P,Q}\,a)_{\overline{n}|i}$", XM)

ax = axs[1]
axis(ax, [(x, l, False) for x, l in T], XM, DOT)
for x in (1, 2, 3, 5, 6): flow(ax, x, "$P$", RED)
dots_mid(ax, 4)
band(ax, "Layer 1 - a level annuity-immediate of $P$", r"$P\,a_{\overline{n}|i}$", XM)

ax = axs[2]
axis(ax, [(x, l, False) for x, l in T], XM, DOT)
ax.text(1, .50, "$0$", ha="center", va="center", color="0.45", fontsize=14)
for x, lab in [(2, "$Q$"), (3, "$2Q$"), (5, "$(n\\!-\\!2)Q$"), (6, "$(n\\!-\\!1)Q$")]:
    flow(ax, x, lab, RED)
dots_mid(ax, 4)
band(ax, "Layer 2 - the increments", r"$\dfrac{Q}{i}\left(a_{\overline{n}|i}-n v^{n}\right)$"
                                      "\n" r"$\;$ (see next slide)", XM)

fig.text(0.035, 0.680, "$=$", fontsize=26, ha="center", va="center")
fig.text(0.035, 0.372, "$+$", fontsize=26, ha="center", va="center")
fig.subplots_adjust(left=.07, right=.99, top=.98, bottom=.02, hspace=.30)
fig.savefig(os.path.join(OUT, "ipqa-split.png"), bbox_inches="tight", facecolor="white")
plt.close(fig)


# ================================================================ 图 2：买票/退票
# 同样的时点，但右边多画 n+1, n+2 用来说明"为什么要退票"
T2 = T + [(7, "$n\\!+\\!1$"), (8, "$n\\!+\\!2$")]
XM2, DOT2 = 8, (4,)

fig, axs = plt.subplots(3, 1, figsize=(13.6, 7.6), dpi=150)

ax = axs[0]
axis(ax, [(x, l, x == 6) for x, l in T2], XM2, DOT2)
for x in (1, 2, 3, 5, 6): flow(ax, x, r"$Q/i$", BLUE, up=True)
dots_mid(ax, 4, BLUE)
band(ax, "Step 1  Pay $Q/i$ at the end of each year $1,\\dots,n$ -"
         " one perpetuity-ticket each time",
     r"money out:  $\dfrac{Q}{i}\,a_{\overline{n}|i}$", XM2)

ax = axs[1]
axis(ax, [(x, l, x == 6) for x, l in T2], XM2, DOT2)
ax.text(1, .50, "$0$", ha="center", va="center", color="0.45", fontsize=14)
for x, lab in [(2, "$Q$"), (3, "$2Q$"), (5, "$(n\\!-\\!2)Q$"), (6, "$(n\\!-\\!1)Q$")]:
    flow(ax, x, lab, RED)
dots_mid(ax, 4)
for x in (7, 8): flow(ax, x, "$nQ$", GREY, ls=(0, (3, 2)), alpha=.85, fs=13)
ax.text(8.9, 1.10, "would keep coming\nfor ever", ha="left", va="center",
        fontsize=12.5, color="0.35")
band(ax, "Step 2  A ticket bought at $k$ pays $Q$ at $k\\!+\\!1,k\\!+\\!2,\\dots$ -"
         " at time $j$ you hold $j\\!-\\!1$ tickets",
     "", XM2)

ax = axs[2]
axis(ax, [(x, l, x == 6) for x, l in T2], XM2, DOT2)
flow(ax, 6, r"$n\cdot Q/i$", RED)
band(ax, "Step 3  At time $n$ hand all $n$ tickets back",
     r"money in:  $\dfrac{Q}{i}\,n\,v^{n}$", XM2)

fig.text(0.50, 0.012,
         r"PV of the increments $\;=\;$ money out $-$ money in $\;=\;"
         r"\dfrac{Q}{i}\,a_{\overline{n}|i}-\dfrac{Q}{i}\,n v^{n}"
         r"\;=\;\dfrac{Q}{i}\left(a_{\overline{n}|i}-n v^{n}\right)$",
         ha="center", va="bottom", fontsize=18)
fig.subplots_adjust(left=.01, right=.99, top=.98, bottom=.115, hspace=.34)
fig.savefig(os.path.join(OUT, "ipqa-tickets.png"), bbox_inches="tight", facecolor="white")
plt.close(fig)


# ================================================================ 图 3：Ex 3.9.18
# 时点 0,1,2,…,10,11,12,13,14,… 压缩成 x = 0,1,2,(3=…),4,5,6,7,8,(9=…)
T3 = [(0, "$0$"), (1, "$1$"), (2, "$2$"), (4, "$10$"), (5, "$11$"),
      (6, "$12$"), (7, "$13$"), (8, "$14$")]
XM3, DOT3 = 9, (3,)

fig, axs = plt.subplots(3, 1, figsize=(13.6, 7.4), dpi=150)

ax = axs[0]
axis(ax, [(x, l, False) for x, l in T3], XM3, DOT3)
for x in (1, 2, 4, 5): flow(ax, x, "$1000$", RED, fs=13)
for x, lab in [(6, "$1180$"), (7, "$1360$"), (8, "$1540$")]: flow(ax, x, lab, RED, fs=13)
dots_mid(ax, 3)
flow(ax, 9, "", RED, ls=(0, (3, 2)), alpha=.75)
ax.text(9.3, -.40, "$+180$ each year,\nfor ever", ha="center", va="top",
        fontsize=12.5, color=RED)
band(ax, "What Rafael buys", r"$=\;64{,}201.75$", XM3)

ax = axs[1]
axis(ax, [(x, l, x == 4) for x, l in T3], XM3, DOT3)
for x in (1, 2, 4): flow(ax, x, "$1000$", RED, fs=13)
dots_mid(ax, 3)
band(ax, "(1) Level annuity-immediate, $1000$ for ten years",
     r"$1000\,a_{\overline{10}|0.05}$" "\n" r"$=\;7{,}721.73$", XM3)

ax = axs[2]
axis(ax, [(x, l, x == 4) for x, l in T3], XM3, DOT3)
for x, lab in [(5, "$1000$"), (6, "$1180$"), (7, "$1360$"), (8, "$1540$")]:
    flow(ax, x, lab, RED, fs=13)
flow(ax, 9, "", RED, ls=(0, (3, 2)), alpha=.75)
ax.text(9.3, -.40, "$+180$ each year,\nfor ever", ha="center", va="top",
        fontsize=12.5, color=RED)
brace(ax, 0, 4, -1.02, "deferred ten years")
band(ax, "(2) Arithmetically increasing perpetuity-immediate, deferred",
     r"$(1.05)^{-10}\!\left(\dfrac{1000}{0.05}+\dfrac{180}{0.05^{2}}\right)$"
     "\n" r"$=\;56{,}480.02$", XM3, ylim=(-1.70, 1.95))

fig.text(0.035, 0.690, "$=$", fontsize=26, ha="center", va="center")
fig.text(0.035, 0.385, "$+$", fontsize=26, ha="center", va="center")
fig.subplots_adjust(left=.07, right=.99, top=.98, bottom=.02, hspace=.34)
fig.savefig(os.path.join(OUT, "ex3918-decomposition.png"), bbox_inches="tight", facecolor="white")
plt.close(fig)

print("ok:", "ipqa-split.png", "ipqa-tickets.png", "ex3918-decomposition.png")
