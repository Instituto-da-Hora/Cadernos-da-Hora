"""
Cadernos da Hora — Trilha 1, Volume 2, Capítulo 2
Diagramas vetoriais SVG gerados com Python puro.

Uso:
    python diagramas_svg.py

Saída:
    ../assets/neuronio_artificial.svg
    ../assets/camadas_rede.svg
    ../assets/ciclo_treinamento.svg
    ../assets/tabela_arquiteturas.svg
    ../assets/caixa_preta.svg
"""

import math
import os

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# ─── Paleta ──────────────────────────────────────────────────────────────────
CORAL = "#E8634A"
CORAL_CLARO = "#F4A393"
TEAL = "#2AABB3"
TEAL_CLARO = "#7CC8CE"
ROXO = "#8B5CF6"
CINZA = "#6B7280"
BRANCO = "#FFFFFF"
FUNDO = "#1A1A2E"


def save_svg(filename: str, content: str, width: int = 800, height: int = 500):
    """Salva SVG com cabeçalho padrão."""
    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}"
     width="{width}" height="{height}" style="background:{FUNDO}">
  <style>
    text {{ font-family: 'Inter', 'Segoe UI', system-ui, sans-serif; }}
  </style>
  {content}
</svg>"""
    path = os.path.join(ASSETS_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"  ✓ {path}")


# ═════════════════════════════════════════════════════════════════════════════
# 1. Neurônio Artificial (Seção 2.2)
# ═════════════════════════════════════════════════════════════════════════════

def neuronio_artificial():
    entradas = [("x₁", 120), ("x₂", 230), ("x₃", 340)]
    pesos = ["w₁", "w₂", "w₃"]
    soma_x, soma_y = 370, 230
    ativ_x, ativ_y = 530, 230
    saida_x, saida_y = 680, 230

    parts = []

    # Título
    parts.append(f'<text x="400" y="40" text-anchor="middle" fill="{CORAL}" font-size="22" font-weight="600">O Neurônio Artificial</text>')

    # Entradas
    for i, (label, y) in enumerate(entradas):
        parts.append(f'<circle cx="100" cy="{y}" r="30" fill="none" stroke="{TEAL}" stroke-width="2"/>')
        parts.append(f'<text x="100" y="{y+5}" text-anchor="middle" fill="{TEAL}" font-size="18">{label}</text>')
        # Seta para soma
        parts.append(f'<line x1="130" y1="{y}" x2="{soma_x-30}" y2="{soma_y}" stroke="{CINZA}" stroke-width="1.5" marker-end="url(#arrow)"/>')
        # Label do peso
        mx = (130 + soma_x - 30) / 2
        my = (y + soma_y) / 2 - 12
        parts.append(f'<text x="{mx}" y="{my}" text-anchor="middle" fill="{CORAL_CLARO}" font-size="13">{pesos[i]}</text>')

    # Soma
    parts.append(f'<circle cx="{soma_x}" cy="{soma_y}" r="35" fill="none" stroke="{CORAL}" stroke-width="2.5"/>')
    parts.append(f'<text x="{soma_x}" y="{soma_y+8}" text-anchor="middle" fill="{CORAL}" font-size="24">Σ</text>')

    # Seta soma → ativação
    parts.append(f'<line x1="{soma_x+35}" y1="{soma_y}" x2="{ativ_x-45}" y2="{ativ_y}" stroke="{CINZA}" stroke-width="1.5" marker-end="url(#arrow)"/>')

    # Ativação
    parts.append(f'<rect x="{ativ_x-40}" y="{ativ_y-25}" width="80" height="50" rx="8" fill="none" stroke="{ROXO}" stroke-width="2.5"/>')
    parts.append(f'<text x="{ativ_x}" y="{ativ_y+6}" text-anchor="middle" fill="{ROXO}" font-size="18">f(·)</text>')

    # Seta ativação → saída
    parts.append(f'<line x1="{ativ_x+40}" y1="{ativ_y}" x2="{saida_x-30}" y2="{saida_y}" stroke="{CINZA}" stroke-width="1.5" marker-end="url(#arrow)"/>')

    # Saída
    parts.append(f'<circle cx="{saida_x}" cy="{saida_y}" r="30" fill="{CORAL}" fill-opacity="0.2" stroke="{CORAL}" stroke-width="2.5"/>')
    parts.append(f'<text x="{saida_x}" y="{saida_y+6}" text-anchor="middle" fill="{CORAL}" font-size="18">ŷ</text>')

    # Labels inferiores
    labels = [
        (100, 400, "entradas", TEAL),
        (240, 400, "pesos", CORAL_CLARO),
        (soma_x, 400, "soma", CORAL),
        (ativ_x, 400, "ativação", ROXO),
        (saida_x, 400, "saída", CORAL),
    ]
    for x, y, txt, cor in labels:
        parts.append(f'<text x="{x}" y="{y}" text-anchor="middle" fill="{cor}" font-size="12">{txt}</text>')

    # Marker para setas
    arrow_def = f"""<defs>
    <marker id="arrow" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="{CINZA}"/>
    </marker>
  </defs>"""

    save_svg("neuronio_artificial.svg", arrow_def + "\n".join(parts), 800, 450)


# ═════════════════════════════════════════════════════════════════════════════
# 2. Camadas da Rede (Seção 2.3.1)
# ═════════════════════════════════════════════════════════════════════════════

def camadas_rede():
    camadas = [3, 5, 5, 2]
    cores = [TEAL, CORAL_CLARO, CORAL_CLARO, CORAL]
    nomes = ["Entrada", "Oculta 1", "Oculta 2", "Saída"]
    x_positions = [100, 280, 460, 640]
    r = 18
    spacing = 55

    parts = []
    parts.append(f'<text x="400" y="35" text-anchor="middle" fill="{CORAL}" font-size="20" font-weight="600">Arquitetura da Rede Neural</text>')

    # Desenhar conexões primeiro (ficam atrás)
    for l in range(len(camadas) - 1):
        for i in range(camadas[l]):
            y1 = 80 + (250 - camadas[l] * spacing / 2) / 2 + i * spacing
            for j in range(camadas[l + 1]):
                y2 = 80 + (250 - camadas[l + 1] * spacing / 2) / 2 + j * spacing
                parts.append(
                    f'<line x1="{x_positions[l]+r}" y1="{y1}" '
                    f'x2="{x_positions[l+1]-r}" y2="{y2}" '
                    f'stroke="{CINZA}" stroke-width="0.5" stroke-opacity="0.25"/>'
                )

    # Desenhar nós
    for l, (n, cor, nome, x) in enumerate(zip(camadas, cores, nomes, x_positions)):
        for i in range(n):
            y = 80 + (250 - n * spacing / 2) / 2 + i * spacing
            parts.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{cor}" fill-opacity="0.2" stroke="{cor}" stroke-width="2"/>')

        label_y = 80 + (250 - n * spacing / 2) / 2 + (n - 1) * spacing + 50
        parts.append(f'<text x="{x}" y="{max(label_y, 400)}" text-anchor="middle" fill="{cor}" font-size="13">{nome}</text>')

    save_svg("camadas_rede.svg", "\n".join(parts), 750, 440)


# ═════════════════════════════════════════════════════════════════════════════
# 3. Ciclo de Treinamento (Seção 2.4.1)
# ═════════════════════════════════════════════════════════════════════════════

def ciclo_treinamento():
    etapas = [
        ("① Dados entram", TEAL),
        ("② Rede calcula saída", CORAL_CLARO),
        ("③ Erro é calculado", CORAL),
        ("④ Pesos ajustados", ROXO),
    ]
    cx, cy = 300, 250
    radius = 140
    n = len(etapas)
    box_w, box_h = 160, 50

    parts = []
    parts.append(f'<text x="300" y="40" text-anchor="middle" fill="{CORAL}" font-size="20" font-weight="600">O Ciclo de Treinamento</text>')

    arrow_def = f"""<defs>
    <marker id="arrowC" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="{CINZA}"/>
    </marker>
  </defs>"""
    parts.append(arrow_def)

    positions = []
    for i, (texto, cor) in enumerate(etapas):
        angle = math.pi / 2 - i * 2 * math.pi / n
        x = cx + radius * math.cos(angle)
        y = cy - radius * math.sin(angle)
        positions.append((x, y))

        parts.append(
            f'<rect x="{x - box_w/2}" y="{y - box_h/2}" width="{box_w}" height="{box_h}" '
            f'rx="8" fill="{cor}" fill-opacity="0.15" stroke="{cor}" stroke-width="2"/>'
        )
        parts.append(
            f'<text x="{x}" y="{y + 5}" text-anchor="middle" fill="{BRANCO}" font-size="13">{texto}</text>'
        )

    # Setas entre etapas
    for i in range(n):
        x1, y1 = positions[i]
        x2, y2 = positions[(i + 1) % n]
        dx, dy = x2 - x1, y2 - y1
        dist = math.sqrt(dx**2 + dy**2)
        ux, uy = dx / dist, dy / dist
        sx = x1 + ux * (box_w / 2 + 10)
        sy = y1 + uy * (box_h / 2 + 10)
        ex = x2 - ux * (box_w / 2 + 10)
        ey = y2 - uy * (box_h / 2 + 10)
        parts.append(
            f'<line x1="{sx}" y1="{sy}" x2="{ex}" y2="{ey}" '
            f'stroke="{CINZA}" stroke-width="1.5" marker-end="url(#arrowC)"/>'
        )

    parts.append(f'<text x="300" y="{cy + 8}" text-anchor="middle" fill="{CINZA}" font-size="12">(repete milhões de vezes)</text>')

    save_svg("ciclo_treinamento.svg", "\n".join(parts), 600, 480)


# ═════════════════════════════════════════════════════════════════════════════
# 4. Tabela de Arquiteturas (Seção 2.5)
# ═════════════════════════════════════════════════════════════════════════════

def tabela_arquiteturas():
    headers = ["Arquitetura", "Melhor para", "Exemplo de uso"]
    rows = [
        ("Feedforward", "Dados tabulares simples", "Prever preço de imóvel"),
        ("CNN", "Imagens", "Reconhecimento facial"),
        ("RNN / LSTM", "Sequências curtas", "Análise de sentimento"),
        ("Transformer", "Texto longo, linguagem", "ChatGPT, tradutores"),
    ]

    col_widths = [160, 200, 200]
    row_h = 45
    x0, y0 = 60, 80
    total_w = sum(col_widths)

    parts = []
    parts.append(f'<text x="340" y="40" text-anchor="middle" fill="{CORAL}" font-size="20" font-weight="600">Arquiteturas em Resumo</text>')

    # Header
    cx = x0
    for i, (header, w) in enumerate(zip(headers, col_widths)):
        parts.append(f'<rect x="{cx}" y="{y0}" width="{w}" height="{row_h}" fill="{CORAL}" fill-opacity="0.2" stroke="{CORAL}" stroke-width="1"/>')
        parts.append(f'<text x="{cx + w/2}" y="{y0 + 28}" text-anchor="middle" fill="{CORAL}" font-size="13" font-weight="600">{header}</text>')
        cx += w

    # Rows
    for r, (c1, c2, c3) in enumerate(rows):
        y = y0 + row_h * (r + 1)
        cor_bg = TEAL if r % 2 == 0 else ROXO
        cx = x0
        for val, w in zip([c1, c2, c3], col_widths):
            parts.append(f'<rect x="{cx}" y="{y}" width="{w}" height="{row_h}" fill="{cor_bg}" fill-opacity="0.05" stroke="{CINZA}" stroke-width="0.5"/>')
            parts.append(f'<text x="{cx + w/2}" y="{y + 28}" text-anchor="middle" fill="{BRANCO}" font-size="12">{val}</text>')
            cx += w

    save_svg("tabela_arquiteturas.svg", "\n".join(parts), 680, 350)


# ═════════════════════════════════════════════════════════════════════════════
# 5. Caixa-Preta (Seção 2.6)
# ═════════════════════════════════════════════════════════════════════════════

def caixa_preta():
    parts = []
    parts.append(f'<text x="350" y="40" text-anchor="middle" fill="{CORAL}" font-size="20" font-weight="600">A Caixa-Preta</text>')

    arrow_def = f"""<defs>
    <marker id="arrowBP" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
      <polygon points="0 0, 8 3, 0 6" fill="{CINZA}"/>
    </marker>
  </defs>"""
    parts.append(arrow_def)

    # Entrada
    for i, label in enumerate(["Dados pessoais", "Renda", "Histórico"]):
        y = 120 + i * 50
        parts.append(f'<rect x="30" y="{y-18}" width="120" height="36" rx="6" fill="{TEAL}" fill-opacity="0.15" stroke="{TEAL}" stroke-width="1.5"/>')
        parts.append(f'<text x="90" y="{y+5}" text-anchor="middle" fill="{TEAL}" font-size="12">{label}</text>')
        parts.append(f'<line x1="150" y1="{y}" x2="230" y2="170" stroke="{CINZA}" stroke-width="1" marker-end="url(#arrowBP)"/>')

    # Caixa preta central
    parts.append(f'<rect x="230" y="100" width="220" height="140" rx="10" fill="#0D0D0D" stroke="{CINZA}" stroke-width="2"/>')
    parts.append(f'<text x="340" y="160" text-anchor="middle" fill="{CINZA}" font-size="16">???</text>')
    parts.append(f'<text x="340" y="185" text-anchor="middle" fill="{CINZA}" font-size="11">milhões de pesos</text>')
    parts.append(f'<text x="340" y="200" text-anchor="middle" fill="{CINZA}" font-size="11">opacos e inexplicáveis</text>')

    # Saída
    parts.append(f'<line x1="450" y1="170" x2="530" y2="170" stroke="{CINZA}" stroke-width="1.5" marker-end="url(#arrowBP)"/>')
    parts.append(f'<rect x="530" y="145" width="140" height="50" rx="8" fill="{CORAL}" fill-opacity="0.2" stroke="{CORAL}" stroke-width="2"/>')
    parts.append(f'<text x="600" y="168" text-anchor="middle" fill="{CORAL}" font-size="13" font-weight="600">Crédito negado</text>')
    parts.append(f'<text x="600" y="185" text-anchor="middle" fill="{CORAL_CLARO}" font-size="11">Sem explicação</text>')

    # Pergunta
    parts.append(f'<text x="350" y="290" text-anchor="middle" fill="{ROXO}" font-size="14" font-style="italic">"Por que fui negado?"</text>')
    parts.append(f'<text x="350" y="310" text-anchor="middle" fill="{CINZA}" font-size="12">O sistema não sabe responder.</text>')

    save_svg("caixa_preta.svg", "\n".join(parts), 700, 340)


# ─── Main ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Gerando diagramas SVG...")
    neuronio_artificial()
    camadas_rede()
    ciclo_treinamento()
    tabela_arquiteturas()
    caixa_preta()
    print("Pronto!")
