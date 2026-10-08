"""Zeichne das Messdreieck und speichere es neben diesem Skript als PNG."""

import math
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import Arc

from answer import turmhoehe


def zeichne_dreieck(
    abstand_m: float, winkel_grad: float, messhoehe_m: float = 1.5
) -> plt.Figure:
    """Erstelle ein maßstäbliches Diagramm für einen positiven Höhenwinkel."""
    if not math.isfinite(abstand_m) or abstand_m <= 0:
        raise ValueError("Der Abstand muss positiv und endlich sein.")
    if not math.isfinite(winkel_grad) or not 0 < winkel_grad < 90:
        raise ValueError("Der Winkel muss zwischen 0 und 90 Grad liegen.")
    if not math.isfinite(messhoehe_m) or messhoehe_m < 0:
        raise ValueError("Die Messhöhe muss nichtnegativ und endlich sein.")

    hoehe_m = turmhoehe(abstand_m, winkel_grad, messhoehe_m)
    hoehenunterschied_m = hoehe_m - messhoehe_m
    sichtlinie_m = math.hypot(abstand_m, hoehenunterschied_m)
    groesse_m = max(abstand_m, hoehe_m)

    figur, achse = plt.subplots(figsize=(11, 7), layout="constrained")
    achse.set_aspect("equal")
    achse.set_title("Turmhöhe bestimmen – Tangens im rechtwinkligen Dreieck")
    achse.set_xlabel("Waagerechter Abstand [m]")
    achse.set_ylabel("Höhe über dem Boden [m]")
    achse.grid(alpha=0.2)

    # Die Dreiecksecken sind Messgerät, Punkt am Turm und Turmspitze.
    achse.fill(
        [0, abstand_m, abstand_m],
        [messhoehe_m, messhoehe_m, hoehe_m],
        color="lightblue", alpha=0.35,
    )
    achse.axhline(0, color="saddlebrown", linewidth=2)
    achse.plot([abstand_m, abstand_m], [0, hoehe_m], color="0.65", linewidth=7)
    achse.plot([0, abstand_m], [messhoehe_m, messhoehe_m], color="tab:blue", linewidth=2)
    achse.plot([abstand_m, abstand_m], [messhoehe_m, hoehe_m], color="tab:green", linewidth=3)
    achse.plot([0, abstand_m], [messhoehe_m, hoehe_m], color="tab:orange", linewidth=2)
    achse.plot([0, 0], [0, messhoehe_m], color="tab:purple", linewidth=2)
    achse.plot(0, messhoehe_m, "ko")

    achse.annotate(
        f"Ankathete: d = {abstand_m:.2f} m",
        (abstand_m / 2, messhoehe_m), xytext=(0, -20),
        textcoords="offset points", ha="center", color="tab:blue",
    )
    achse.annotate(
        f"Gegenkathete: Δh = {hoehenunterschied_m:.2f} m",
        (abstand_m, messhoehe_m + hoehenunterschied_m / 2),
        xytext=(-12, 0), textcoords="offset points", ha="right",
        rotation=90, va="center", color="tab:green",
    )
    achse.annotate(
        f"Sichtlinie (Hypotenuse): {sichtlinie_m:.2f} m",
        (abstand_m / 2, messhoehe_m + hoehenunterschied_m / 2),
        xytext=(0, 12), textcoords="offset points", ha="center",
        rotation=winkel_grad, rotation_mode="anchor", color="darkorange",
    )
    achse.annotate(
        f"Messhöhe: {messhoehe_m:.2f} m", (0, messhoehe_m / 2),
        xytext=(-12, 0), textcoords="offset points", ha="right",
        color="tab:purple",
    )
    achse.annotate(
        "Messgerät", (0, messhoehe_m), xytext=(-12, 12),
        textcoords="offset points", ha="right",
    )

    # Gleiche Achsenmaßstäbe sorgen dafür, dass der Winkel richtig erscheint.
    radius_m = min(abstand_m, hoehenunterschied_m) * 0.25
    achse.add_patch(Arc(
        (0, messhoehe_m), 2 * radius_m, 2 * radius_m,
        theta1=0, theta2=winkel_grad, color="darkorange", linewidth=2,
    ))
    halber_winkel_rad = math.radians(winkel_grad / 2)
    achse.text(
        1.3 * radius_m * math.cos(halber_winkel_rad),
        messhoehe_m + 1.3 * radius_m * math.sin(halber_winkel_rad),
        f"α = {winkel_grad:g}°", color="darkorange", va="center",
    )
    markierung_m = min(abstand_m, hoehenunterschied_m) * 0.06
    achse.plot(
        [abstand_m - markierung_m, abstand_m - markierung_m, abstand_m],
        [messhoehe_m, messhoehe_m + markierung_m, messhoehe_m + markierung_m],
        color="black",
    )

    pfeil_x = abstand_m + 0.12 * groesse_m
    achse.annotate(
        "", (pfeil_x, hoehe_m), xytext=(pfeil_x, 0),
        arrowprops={"arrowstyle": "<->", "color": "black"},
    )
    achse.text(
        pfeil_x + 0.03 * groesse_m, hoehe_m / 2,
        f"Turmhöhe\nh = {hoehe_m:.2f} m", va="center",
    )
    figur.text(
        0.5, 0.02,
        f"tan(α) = Δh / d     →     h = d · tan(α) + Messhöhe = {hoehe_m:.2f} m",
        ha="center", fontsize=12,
        bbox={"facecolor": "white", "edgecolor": "0.8", "pad": 8},
    )
    achse.set_xlim(-0.3 * groesse_m, abstand_m + 0.45 * groesse_m)
    achse.set_ylim(-0.22 * groesse_m, hoehe_m + 0.15 * groesse_m)
    return figur


if __name__ == "__main__":
    # Diese Messwerte können für andere Aufgaben angepasst werden.
    figur = zeichne_dreieck(20.0, 35.0, 1.5)
    bildpfad = Path(__file__).with_name("tower_triangle.png")
    figur.savefig(bildpfad, dpi=180, bbox_inches="tight")
    print(f"Diagramm gespeichert: {bildpfad}")
    plt.show()
