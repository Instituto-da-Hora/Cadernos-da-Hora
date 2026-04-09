"""
Cadernos da Hora — Trilha 1, Volume 2, Capítulo 2
Gráficos Matplotlib para impressão e tela.

Uso:
    python graficos_matplotlib.py

Saída em ../assets/:
    funcoes_ativacao.png / .pdf
    superficie_erro_3d.png / .pdf
    overfitting_vs_aprendizado.png / .pdf
    heatmap_atencao.png / .pdf
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
import os

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# ─── Estilo global ───────────────────────────────────────────────────────────
CORAL = "#E8634A"
CORAL_CLARO = "#F4A393"
TEAL = "#2AABB3"
TEAL_CLARO = "#7CC8CE"
ROXO = "#8B5CF6"
CINZA = "#6B7280"
FUNDO = "#1A1A2E"
BRANCO = "#E8E8E8"

rcParams.update({
    "figure.facecolor": FUNDO,
    "axes.facecolor": FUNDO,
    "axes.edgecolor": CINZA,
    "axes.labelcolor": BRANCO,
    "text.color": BRANCO,
    "xtick.color": CINZA,
    "ytick.color": CINZA,
    "font.family": "sans-serif",
    "font.size": 11,
    "savefig.dpi": 200,
    "savefig.bbox": "tight",
    "savefig.facecolor": FUNDO,
})


def save(fig, name):
    for ext in ["png", "pdf"]:
        path = os.path.join(ASSETS_DIR, f"{name}.{ext}")
        fig.savefig(path)
    plt.close(fig)
    print(f"  ✓ {name}.png / .pdf")


# ═════════════════════════════════════════════════════════════════════════════
# 1. Funções de Ativação (Seção 2.2.5)
# ═════════════════════════════════════════════════════════════════════════════

def funcoes_ativacao():
    x = np.linspace(-6, 6, 300)

    fig, axes = plt.subplots(1, 3, figsize=(14, 4))

    # Sigmoid
    ax = axes[0]
    sigmoid = 1 / (1 + np.exp(-x))
    ax.plot(x, sigmoid, color=CORAL, linewidth=2.5)
    ax.axhline(0.5, color=CINZA, linewidth=0.5, linestyle="--")
    ax.set_title("Sigmoid", color=CORAL, fontsize=14, fontweight="bold")
    ax.set_xlabel("entrada")
    ax.set_ylabel("saída")
    ax.set_ylim(-0.1, 1.1)
    ax.text(3, 0.15, "Espreme tudo\nentre 0 e 1", fontsize=9, color=CORAL_CLARO)

    # ReLU
    ax = axes[1]
    relu = np.maximum(0, x)
    ax.plot(x, relu, color=TEAL, linewidth=2.5)
    ax.axhline(0, color=CINZA, linewidth=0.5, linestyle="--")
    ax.set_title("ReLU", color=TEAL, fontsize=14, fontweight="bold")
    ax.set_xlabel("entrada")
    ax.set_ylim(-1, 6.5)
    ax.text(-5.5, 4, "Positivo: mantém\nNegativo: zera", fontsize=9, color=TEAL_CLARO)

    # Softmax (barras)
    ax = axes[2]
    categorias = ["Gato", "Cão", "Outro"]
    probs = [0.70, 0.20, 0.10]
    cores = [ROXO, CORAL_CLARO, CINZA]
    bars = ax.bar(categorias, probs, color=cores, width=0.5, edgecolor="none")
    for bar, p in zip(bars, probs):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02,
                f"{int(p*100)}%", ha="center", fontsize=11, color=BRANCO)
    ax.set_title("Softmax", color=ROXO, fontsize=14, fontweight="bold")
    ax.set_ylim(0, 0.95)
    ax.set_ylabel("probabilidade")

    fig.suptitle("Funções de Ativação", fontsize=16, fontweight="bold", color=CORAL, y=1.02)
    fig.tight_layout()
    save(fig, "funcoes_ativacao")


# ═════════════════════════════════════════════════════════════════════════════
# 2. Superfície de Erro 3D (Seção 2.4.2)
# ═════════════════════════════════════════════════════════════════════════════

def superficie_erro_3d():
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection="3d")
    ax.set_facecolor(FUNDO)

    x = np.linspace(-3, 3, 100)
    y = np.linspace(-3, 3, 100)
    X, Y = np.meshgrid(x, y)
    Z = 0.5 * X**2 + 0.5 * Y**2 + 0.3 * np.sin(3 * X) * np.cos(3 * Y)

    ax.plot_surface(X, Y, Z, cmap="magma", alpha=0.7, edgecolor="none")

    # Caminho do gradient descent
    path_x = [2.5, 1.8, 1.0, 0.4, 0.1, 0.0]
    path_y = [2.0, 1.4, 0.8, 0.3, 0.05, 0.0]
    path_z = [0.5 * px**2 + 0.5 * py**2 + 0.3 * np.sin(3*px)*np.cos(3*py) + 0.1
              for px, py in zip(path_x, path_y)]
    ax.plot(path_x, path_y, path_z, "o-", color="#FFDD44", markersize=5, linewidth=2, zorder=10)
    ax.scatter([path_x[0]], [path_y[0]], [path_z[0]], color="#FFDD44", s=80, zorder=11)
    ax.scatter([path_x[-1]], [path_y[-1]], [path_z[-1]], color=TEAL, s=80, zorder=11, marker="*")

    ax.set_xlabel("Peso 1", labelpad=8)
    ax.set_ylabel("Peso 2", labelpad=8)
    ax.set_zlabel("Erro", labelpad=8)
    ax.set_title("Superfície de Erro — Gradient Descent", color=CORAL, fontsize=14, pad=15)

    ax.view_init(elev=35, azim=-50)
    ax.tick_params(colors=CINZA)
    save(fig, "superficie_erro_3d")


# ═════════════════════════════════════════════════════════════════════════════
# 3. Overfitting vs. Aprendizado (Seção 2.4.3)
# ═════════════════════════════════════════════════════════════════════════════

def overfitting_vs_aprendizado():
    np.random.seed(42)
    xs = np.linspace(-2, 2, 15)
    ys_true = 0.5 * xs + 0.3
    ys = ys_true + np.random.normal(0, 0.35, len(xs))

    x_smooth = np.linspace(-2.2, 2.2, 200)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Overfitting
    coeffs = np.polyfit(xs, ys, 12)
    ax1.scatter(xs, ys, color=TEAL, s=40, zorder=5)
    ax1.plot(x_smooth, np.polyval(coeffs, x_smooth), color="#E85454", linewidth=2)
    ax1.set_title("Overfitting (Decoreba)", color="#E85454", fontsize=14, fontweight="bold")
    ax1.set_ylim(-2, 3)
    ax1.text(-2, 2.5, "Acerta 99% no treino\nAcerta 60% em dados novos",
             fontsize=10, color=CORAL_CLARO)

    # Bom aprendizado
    coeffs_good = np.polyfit(xs, ys, 1)
    ax2.scatter(xs, ys, color=TEAL, s=40, zorder=5)
    ax2.plot(x_smooth, np.polyval(coeffs_good, x_smooth), color=TEAL, linewidth=2.5)
    ax2.set_title("Aprendizado Adequado", color=TEAL, fontsize=14, fontweight="bold")
    ax2.set_ylim(-2, 3)
    ax2.text(-2, 2.5, "Acerta 85% no treino\nAcerta 83% em dados novos",
             fontsize=10, color=TEAL_CLARO)

    fig.suptitle("Decoreba vs. Aprendizado", fontsize=16, fontweight="bold", color=CORAL, y=1.02)
    fig.tight_layout()
    save(fig, "overfitting_vs_aprendizado")


# ═════════════════════════════════════════════════════════════════════════════
# 4. Heatmap de Atenção (Seção 2.5.5)
# ═════════════════════════════════════════════════════════════════════════════

def heatmap_atencao():
    palavras = ["fui", "ao", "banco", "sacar", "dinheiro"]
    atencao = np.array([
        [0.50, 0.10, 0.20, 0.10, 0.10],
        [0.10, 0.30, 0.30, 0.10, 0.20],
        [0.05, 0.05, 0.15, 0.40, 0.35],
        [0.10, 0.05, 0.25, 0.30, 0.30],
        [0.05, 0.10, 0.30, 0.25, 0.30],
    ])

    fig, ax = plt.subplots(figsize=(7, 6))
    im = ax.imshow(atencao, cmap="YlOrRd", aspect="auto", vmin=0, vmax=0.5)

    ax.set_xticks(range(len(palavras)))
    ax.set_yticks(range(len(palavras)))
    ax.set_xticklabels(palavras, fontsize=13, color=TEAL)
    ax.set_yticklabels(palavras, fontsize=13, color=CORAL_CLARO)
    ax.xaxis.tick_top()

    # Valores nas células
    for i in range(len(palavras)):
        for j in range(len(palavras)):
            cor_txt = "white" if atencao[i, j] > 0.25 else BRANCO
            ax.text(j, i, f"{atencao[i,j]:.2f}", ha="center", va="center",
                    fontsize=11, color=cor_txt)

    # Destaque na linha "banco"
    rect = plt.Rectangle((-0.5, 1.5), 5, 1, linewidth=2, edgecolor="#FFDD44", facecolor="none")
    ax.add_patch(rect)
    ax.annotate('"banco" presta mais atenção\nem "sacar" e "dinheiro"',
                xy=(4.5, 2), fontsize=10, color="#FFDD44",
                xytext=(5.5, 3.5), arrowprops=dict(arrowstyle="->", color="#FFDD44"))

    ax.set_title("Mecanismo de Atenção — Transformer", color=CORAL, fontsize=14, pad=20)
    plt.colorbar(im, ax=ax, label="Peso de atenção", shrink=0.8)
    fig.tight_layout()
    save(fig, "heatmap_atencao")


# ─── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Gerando gráficos Matplotlib...")
    funcoes_ativacao()
    superficie_erro_3d()
    overfitting_vs_aprendizado()
    heatmap_atencao()
    print("Pronto!")
