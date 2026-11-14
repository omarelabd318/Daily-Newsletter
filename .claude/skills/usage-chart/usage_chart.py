#!/usr/bin/env python3
"""Draw the daily-runs usage chart (Markets Desk vs Newsletter, list-price $ per run,
with the share of the weekly limit on the right axis and a 'Weekly limit' row under it).

usage: usage_chart.py START END OUT.png [--today YYYY-MM-DD] [--proj DATE=desk,lo,hi:news,lo,hi ...]
       [--proj-note TEXT] [--earlier DATE=desk,news]
Actual figures come from runs.json next to this script; projected days are passed with --proj.
"""
import argparse, datetime as dt, json, os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.lines import Line2D

HERE = os.path.dirname(os.path.abspath(__file__))
BLUE, RED, PINK, GOLD = "#2c6e99", "#c8553d", "#e3a594", "#7a5a00"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("start"); ap.add_argument("end"); ap.add_argument("out")
    ap.add_argument("--today")
    ap.add_argument("--proj", nargs="*", default=[])
    ap.add_argument("--proj-note", default="")
    ap.add_argument("--earlier", nargs="*", default=[])
    ap.add_argument("--title")
    a = ap.parse_args()
    data = json.load(open(os.path.join(HERE, "runs.json")))
    per = data["dollars_per_percent"]; days = data["days"]
    proj = {}
    for p in a.proj:
        d, rest = p.split("="); de, nw = rest.split(":")
        proj[d] = ([float(x) for x in de.split(",")], [float(x) for x in nw.split(",")])
    earlier = {p.split("=")[0]: [float(x) for x in p.split("=")[1].split(",")] for p in a.earlier}

    plt.rcParams["font.family"] = ["Inter", "DejaVu Sans"]
    plt.rcParams["text.parse_math"] = False
    d0 = dt.date.fromisoformat(a.start); d1 = dt.date.fromisoformat(a.end)
    dates = [d0 + dt.timedelta(i) for i in range((d1 - d0).days + 1)]
    fig, ax = plt.subplots(figsize=(20, 10), dpi=100)
    w = 0.38; ymax = 0; first_proj = None
    for i, d in enumerate(dates):
        k = d.isoformat()
        if k in days:
            r = days[k]
            ax.bar(i - w/2, r["desk"], w, color=BLUE)
            nb = r["newsletter"]
            hatch = "//" if r.get("hatch") else None
            ax.bar(i + w/2, nb, w, color=RED, hatch=hatch, edgecolor="white" if hatch else None, linewidth=0)
            if r.get("recap"):
                ax.bar(i + w/2, r["recap"], w, bottom=nb, color=PINK); nb += r["recap"]
            for x, v in ((i - w/2, r["desk"]), (i + w/2, nb)):
                ax.text(x, v + 0.25, f"${v:.2f}", ha="center", va="bottom", fontsize=13, color="#333")
            ymax = max(ymax, nb, r["desk"])
            if "newsletter_flag" in r:
                ax.annotate(r["newsletter_flag"], xy=(i + w/2, nb), xytext=(i + r.get("flag_at", [-2.4, nb + 2])[0], r.get("flag_at", [-2.4, nb + 2])[1]),
                            fontsize=13, color="#555", va="center", ha="left",
                            arrowprops=dict(arrowstyle="->", color="#888", lw=1.2))
            total = r["desk"] + nb
            lbl = f"{total/per:.1f}%"
        elif k in proj:
            first_proj = first_proj if first_proj is not None else i
            (dv, dlo, dhi), (nv, nlo, nhi) = proj[k]
            ax.bar(i - w/2, dv, w, color=BLUE, alpha=0.45, hatch="/", edgecolor="white", linewidth=0)
            ax.bar(i + w/2, nv, w, color=RED, alpha=0.45, hatch="/", edgecolor="white", linewidth=0)
            ev = earlier.get(k, [0, 0])
            for x, v, lo, hi, e in ((i - w/2, dv, dlo, dhi, ev[0]), (i + w/2, nv, nlo, nhi, ev[1])):
                ax.errorbar(x, v, yerr=[[v - lo], [hi - v]], color="#444", capsize=8, lw=1.6)
                ax.text(x, max(hi, e + 0.4) + 0.25, f"~${v:.2f}", ha="center", va="bottom", fontsize=13, color="#333")
            ymax = max(ymax, dhi, nhi)
            lbl = f"~{(dv + nv)/per:.1f}%"
        else:
            lbl = ""
        if k in earlier:
            ax.scatter([i - w/2, i + w/2], earlier[k], marker="D", s=110, color="#222", zorder=5)
        ax.text(i, -0.17, lbl, transform=ax.get_xaxis_transform(), ha="center", fontsize=14,
                fontweight="bold", color=GOLD)
    ax.text(-0.9, -0.17, "Weekly limit:", transform=ax.get_xaxis_transform(), ha="left", fontsize=14,
            fontweight="bold", color=GOLD)
    if first_proj is not None:
        ax.axvline(first_proj - 0.5, color="#bbb", ls="--", lw=1.5)
        if a.proj_note:
            ax.text(first_proj + (len(dates) - first_proj - 1) / 2, ymax + 4.2, a.proj_note,
                    ha="center", va="top", fontsize=12.5, color="#333")

    labels = []
    for d in dates:
        s = d.strftime("%a ") + str(d.day)
        if a.today and d.isoformat() == a.today: s += "\n(today)"
        elif d.isoformat() in proj: s += "\n(projected)"
        labels.append(s)
    ax.set_xticks(range(len(dates))); ax.set_xticklabels(labels, fontsize=15)
    ax.set_xlim(-1, len(dates) - 0.4)
    top = max(ymax + 4.5, 12); ax.set_ylim(0, top)
    ax.set_ylabel("Cost per run (list-price $)", fontsize=15)
    ax.tick_params(axis="y", labelsize=15)
    ax.grid(axis="y", color="#e6e6e6"); ax.set_axisbelow(True)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax2 = ax.twinx(); ax2.set_ylim(0, top / per)
    ax2.set_ylabel(f"Share of the weekly limit (%, 1% ≈ ${per:.2f})", fontsize=15)
    ax2.tick_params(axis="y", labelsize=15); ax2.spines["top"].set_visible(False)

    handles = [Patch(color=BLUE, label="Markets Desk"),
               Patch(color=RED, label="Newsletter (Saturdays: the Weekly Recap)")]
    if any(days.get(d.isoformat(), {}).get("recap") for d in dates):
        handles.append(Patch(color=PINK, label="Weekly Recap, a separate run then"))
    if earlier:
        handles.insert(0, Line2D([], [], marker="D", ls="", color="#222", markersize=10, label="What I projected earlier"))
    if proj:
        handles.append(Patch(facecolor="#bbb", hatch="/", edgecolor="white", label="Projected (bars: range)"))
    ax.legend(handles=handles, loc="upper left", frameon=False, fontsize=15)
    actual = sum(days[d.isoformat()]["desk"] + days[d.isoformat()]["newsletter"] + days[d.isoformat()].get("recap", 0)
                 for d in dates if d.isoformat() in days)
    projected = sum(proj[d.isoformat()][0][0] + proj[d.isoformat()][1][0] for d in dates if d.isoformat() in proj)
    title = a.title or (f"Daily runs, {dates[0]:%a %b} {dates[0].day} to {dates[-1]:%a %b} {dates[-1].day}: "
                        f"~${actual + projected:.0f}, ≈{(actual + projected)/per:.0f}% of the weekly limit")
    ax.set_title(title, fontsize=19, loc="left", pad=16)
    fig.subplots_adjust(bottom=0.2, left=0.06, right=0.94)
    fig.savefig(a.out, dpi=100)

if __name__ == "__main__":
    main()
