# 2026-10-27 — Ch6 §6.2: a bond's cash flow, and why PMT and FV are both nonzero.
# jzhong 2026-10-27：「第六章现在还没有一片 timeline 图」。
# 要点不是「画条线」，是把 basic price formula 的两项各自对应到图上哪一段，
# 并且点明 **最后一期有两笔钱**（末期 coupon 和 redemption 同一天到），
# 这正是 TVM 里 PMT 和 FV 共用同一个 N 的原因。
import os
import matplotlib.pyplot as plt
from math4050_timeline import OUT, RED, GREEN, axis, payment, move, finish

N = 6   # x=6 代表第 n 期
fig, ax = plt.subplots(figsize=(11.6, 6.4), dpi=150)
axis(ax, [(0, "$0$", True), (1, "$1$", False), (2, "$2$", False),
          (5, "$n-1$", False), (N, "$n$", False)], N)
ax.text(3.5, -.34, r"$\cdots$", ha="center", va="top", fontsize=15)

# coupons：每期一笔 Fr，末期那笔往左挪一点，给 C 让位
for x in (1, 2, 5, N - .16):
    payment(ax, x, "$Fr$", RED)
ax.text(3.5, 1.00, r"$\cdots$", ha="center", va="center", color=RED, fontsize=16)

# redemption：跟末期 coupon 同一天，画高一点、往右挪一点
payment(ax, N + .16, "$C$", GREEN, top=1.66, lw=2.2)

ax.annotate("the last coupon and the redemption\nland on the same date",
            xy=(N - .05, 1.34), xytext=(3.45, 1.72), ha="center", va="center",
            fontsize=13.5, color="0.25",
            arrowprops=dict(arrowstyle="-", lw=1.1, color="0.55",
                            connectionstyle="arc3,rad=-0.18"))

move(ax, 1, 0, r"all $n$ coupons, discounted:   $Fr\,a_{\overline{n}|j}$",
     RED, 0, rad=-0.10, xlab=2.6)
move(ax, N, 0, r"the redemption, discounted:   $K = C\,v_j^{\,n}$",
     GREEN, 1, rad=-0.08, xlab=3.4)

# 两根箭头都落在 time 0：那笔钱就是买价 P
ax.text(-.72, -1.84, "$P$", ha="center", va="center", fontsize=19, weight="bold")

ax.text(2.55, -4.05, "on the TVM worksheet:        PMT $= Fr$        FV $= C$        N $= n$",
        ha="center", va="center", fontsize=15, color="0.15",
        bbox=dict(boxstyle="round,pad=0.45", fc="#f3f3f3", ec="0.72", lw=1.0))

finish(ax, os.path.join(OUT, "bond-cash-flow.png"),
       r"$P\;=\;Fr\,a_{\overline{n}|j}\;+\;C\,v_j^{\,n}$",
       "A bond is one cash flow stream, priced at time 0", N, -5.35)
print("ok: bond-cash-flow.png")
