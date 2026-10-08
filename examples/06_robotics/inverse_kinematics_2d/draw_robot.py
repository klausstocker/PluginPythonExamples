"""Zeichne Robotergeometrie und Gelenkwinkel und speichere ein PNG."""

import math
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc

from answer import ARM_1_MM, ARM_2_MM, inverse_kinematik


def zeichne_roboter(x: float, y: float) -> plt.Figure:
    """Zeichne die gewählte Gelenkkonfiguration für ein Ziel in Millimetern."""
    winkel = inverse_kinematik(x, y)
    if winkel is None:
        raise ValueError("Für einen unerreichbaren Zielpunkt gibt es keine Armstellung.")
    alpha, beta = winkel
    alpha_rad = math.radians(alpha)
    gelenk_x = ARM_1_MM * math.cos(alpha_rad)
    gelenk_y = ARM_1_MM * math.sin(alpha_rad)
    abstand = math.hypot(x, y)
    zielrichtung = math.degrees(math.atan2(y, x))
    dreieckswinkel = zielrichtung - alpha
    radius = min(ARM_1_MM, ARM_2_MM) * 0.25

    figur, (achse, formeln) = plt.subplots(
        1, 2, figsize=(13, 7), gridspec_kw={"width_ratios": [1.5, 1]},
        layout="constrained",
    )
    figur.suptitle("Inverse Kinematik – planarer Roboter mit zwei Drehgelenken", fontsize=16)
    achse.set_aspect("equal")
    achse.set_xlabel("x [mm]")
    achse.set_ylabel("y [mm]")
    achse.grid(alpha=0.2)
    achse.axhline(0, color="0.6", linewidth=1)
    achse.axvline(0, color="0.6", linewidth=1)

    # Das Armdreieck liefert die Seiten für den Kosinussatz.
    achse.fill([0, gelenk_x, x], [0, gelenk_y, y], color="lightblue", alpha=0.25)
    achse.plot([0, x], [0, y], "--", color="0.45", label="Abstand r zum Ziel")
    achse.plot([x, x, 0], [0, y, y], ":", color="0.65", label="Zielkoordinaten x, y")
    achse.plot([0, gelenk_x], [0, gelenk_y], color="tab:blue", linewidth=5, label="Arm 1")
    achse.plot([gelenk_x, x], [gelenk_y, y], color="tab:orange", linewidth=5, label="Arm 2")
    achse.plot([0, gelenk_x, x], [0, gelenk_y, y], "ko", markersize=7)
    achse.annotate("Basis O", (0, 0), xytext=(-12, -22), textcoords="offset points")
    achse.annotate("Gelenk G", (gelenk_x, gelenk_y), xytext=(10, -22), textcoords="offset points")
    achse.annotate(
        f"Ziel P ({x:g}, {y:g}) mm", (x, y), xytext=(10, 12), textcoords="offset points",
    )
    achse.annotate(
        f"l₁ = {ARM_1_MM:g} mm", (gelenk_x / 2, gelenk_y / 2),
        xytext=(0, -42), textcoords="offset points", ha="center", color="tab:blue",
    )
    achse.annotate(
        f"l₂ = {ARM_2_MM:g} mm", ((gelenk_x + x) / 2, (gelenk_y + y) / 2),
        xytext=(12, 0), textcoords="offset points", color="tab:orange",
    )
    achse.annotate(
        f"r = {abstand:.2f} mm", (x / 2, y / 2), xytext=(-12, 12),
        textcoords="offset points", ha="right", color="0.35",
    )

    # Beta wird von der Verlängerung des ersten Arms aus gemessen.
    achse.plot(
        [gelenk_x, gelenk_x + 2.5 * radius * math.cos(alpha_rad)],
        [gelenk_y, gelenk_y + 2.5 * radius * math.sin(alpha_rad)],
        "--", color="tab:blue", linewidth=1.5, label="Verlängerung von Arm 1",
    )
    for mittelpunkt, start, ende, beschriftung, farbe, bogenradius in [
        ((0, 0), min(0, alpha), max(0, alpha), f"α = {alpha:.1f}°", "tab:green", radius),
        ((gelenk_x, gelenk_y), alpha, alpha + beta, f"β = {beta:.1f}°", "tab:red", radius),
        ((gelenk_x, gelenk_y), alpha + beta, alpha + 180, "γ", "tab:purple", 0.7 * radius),
        ((0, 0), alpha, alpha + dreieckswinkel, "δ", "tab:purple", 2 * radius),
        ((0, 0), min(0, zielrichtung), max(0, zielrichtung), "θ", "0.35", 3 * radius),
    ]:
        achse.add_patch(Arc(
            mittelpunkt, 2 * bogenradius, 2 * bogenradius,
            theta1=start, theta2=ende, color=farbe, linewidth=2,
        ))
        mitte_rad = math.radians((start + ende) / 2)
        achse.text(
            mittelpunkt[0] + 1.4 * bogenradius * math.cos(mitte_rad),
            mittelpunkt[1] + 1.4 * bogenradius * math.sin(mitte_rad),
            beschriftung, color=farbe, ha="center", va="center",
            bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.8},
        )

    rand = 0.55 * (ARM_1_MM + ARM_2_MM)
    achse.set_xlim(min(0, gelenk_x, x) - rand, max(0, gelenk_x, x) + rand)
    achse.set_ylim(min(0, gelenk_y, y) - rand, max(0, gelenk_y, y) + rand)
    achse.legend(loc="upper left", fontsize=9)

    formeln.axis("off")
    formeln.text(0, 0.96, "Zusammenhänge im Dreieck", fontsize=13, weight="bold")
    formeln.text(0, 0.86, f"Eingabe: x = {x:g} mm, y = {y:g} mm\nAusgabe: α = {alpha:.2f}°, β = {beta:.2f}°")
    formeln.text(0, 0.73, "1. Arbeitsbereich prüfen", weight="bold")
    formeln.text(0, 0.66, r"$r = \sqrt{x^2+y^2},\quad |l_1-l_2| \leq r \leq l_1+l_2$")
    formeln.text(0, 0.55, "2. Kosinussatz im Armdreieck", weight="bold")
    formeln.text(0, 0.47, r"$r^2 = l_1^2 + l_2^2 - 2l_1l_2\cos\gamma$" "\n" r"$\gamma + \beta = 180^\circ$", fontsize=13)
    formeln.text(0, 0.35, "3. Winkel an der Basis und Zielrichtung", weight="bold")
    formeln.text(0, 0.25, r"$l_2^2 = l_1^2 + r^2 - 2l_1r\cos\delta$" "\n" r"$x = r\cos\theta,\quad y = r\sin\theta$" "\n" r"$\theta = \alpha + \delta\quad (\mathrm{mod}\ 360^\circ)$", fontsize=12)
    formeln.text(
        0, 0.04,
        "α: Winkel zur positiven x-Achse\n"
        "β: relativer Winkel zwischen den Armen\n"
        "γ, δ: Innenwinkel des Armdreiecks\n"
        "θ: Richtung von der Basis zum Ziel\n"
        "Formeln in Bogenmaß; Ausgabe in Grad.",
        fontsize=10,
    )
    return figur


if __name__ == "__main__":
    # Ein Ziel mit zwei deutlich sichtbaren Gelenkwinkeln.
    figur = zeichne_roboter(100.0, 120.0)
    bildpfad = Path(__file__).with_name("robot_kinematics.png")
    figur.savefig(bildpfad, dpi=180, bbox_inches="tight")
    print(f"Diagramm gespeichert: {bildpfad}")
    plt.show()
