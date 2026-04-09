"""
Cadernos da Hora — Trilha 1, Volume 2, Capítulo 2
Animações Manim: Redes Neurais em Profundidade

Renderizar todas as cenas:
    manim -qh cenas_manim.py

Renderizar cena específica:
    manim -qh cenas_manim.py ValeNaNeblina

Exportar frame estático:
    manim -qh --format png -s cenas_manim.py NeuronioArtificial
"""

from manim import *
import numpy as np

# ─── Paleta de cores do projeto ──────────────────────────────────────────────
CORAL = "#E8634A"
CORAL_CLARO = "#F4A393"
TEAL = "#2AABB3"
TEAL_CLARO = "#7CC8CE"
ROXO = "#8B5CF6"
CINZA_ESCURO = "#2D2D2D"
CINZA_MEDIO = "#6B7280"
CREME = "#FFF8F0"


# ═════════════════════════════════════════════════════════════════════════════
# SEÇÃO 2.2 — O Neurônio Artificial
# ═════════════════════════════════════════════════════════════════════════════

class NeuronioArtificial(Scene):
    """Diagrama animado do neurônio artificial: entradas → pesos → soma → ativação → saída."""

    def construct(self):
        title = Text("O Neurônio Artificial", color=CORAL, font_size=36).to_edge(UP)
        subtitle = Text("Uma unidade de cálculo", color=CINZA_MEDIO, font_size=20)
        subtitle.next_to(title, DOWN, buff=0.2)

        # Nós de entrada
        entradas_labels = ["x₁", "x₂", "x₃"]
        entradas = VGroup()
        for i, label in enumerate(entradas_labels):
            circle = Circle(radius=0.35, color=TEAL, fill_opacity=0.15, stroke_width=2)
            circle.shift(LEFT * 4.5 + UP * (1 - i) * 1.4)
            txt = Text(label, font_size=22, color=TEAL).move_to(circle)
            entradas.add(VGroup(circle, txt))

        # Nó soma
        soma_circle = Circle(radius=0.5, color=CORAL, fill_opacity=0.15, stroke_width=2.5)
        soma_circle.move_to(LEFT * 1)
        soma_txt = MathTex(r"\Sigma", font_size=36, color=CORAL).move_to(soma_circle)
        soma = VGroup(soma_circle, soma_txt)

        # Nó ativação
        ativ_rect = RoundedRectangle(
            width=1.4, height=0.9, corner_radius=0.15,
            color=ROXO, fill_opacity=0.15, stroke_width=2.5
        ).move_to(RIGHT * 1.8)
        ativ_txt = MathTex(r"f(\cdot)", font_size=28, color=ROXO).move_to(ativ_rect)
        ativacao = VGroup(ativ_rect, ativ_txt)

        # Nó saída
        saida_circle = Circle(radius=0.35, color=CORAL, fill_opacity=0.3, stroke_width=2.5)
        saida_circle.move_to(RIGHT * 4.5)
        saida_txt = MathTex(r"\hat{y}", font_size=28, color=CORAL).move_to(saida_circle)
        saida = VGroup(saida_circle, saida_txt)

        # Pesos (labels nas setas)
        pesos_labels = ["w₁", "w₂", "w₃"]
        setas_entrada = VGroup()
        pesos_textos = VGroup()
        for i, (entrada, peso_label) in enumerate(zip(entradas, pesos_labels)):
            arrow = Arrow(
                entrada.get_right(), soma_circle.get_left(),
                buff=0.15, color=CINZA_MEDIO, stroke_width=2, max_tip_length_to_length_ratio=0.12
            )
            peso_txt = Text(peso_label, font_size=16, color=CORAL_CLARO)
            peso_txt.move_to(arrow.get_center() + UP * 0.25)
            setas_entrada.add(arrow)
            pesos_textos.add(peso_txt)

        seta_soma_ativ = Arrow(
            soma_circle.get_right(), ativ_rect.get_left(),
            buff=0.15, color=CINZA_MEDIO, stroke_width=2, max_tip_length_to_length_ratio=0.12
        )
        seta_ativ_saida = Arrow(
            ativ_rect.get_right(), saida_circle.get_left(),
            buff=0.15, color=CINZA_MEDIO, stroke_width=2, max_tip_length_to_length_ratio=0.12
        )

        # Labels embaixo
        label_entrada = Text("entradas", font_size=16, color=TEAL).next_to(entradas, DOWN, buff=0.4)
        label_pesos = Text("pesos", font_size=16, color=CORAL_CLARO).next_to(pesos_textos, DOWN, buff=0.6)
        label_soma = Text("soma\nponderada", font_size=14, color=CORAL).next_to(soma, DOWN, buff=0.3)
        label_ativ = Text("função de\nativação", font_size=14, color=ROXO).next_to(ativacao, DOWN, buff=0.3)
        label_saida = Text("saída", font_size=16, color=CORAL).next_to(saida, DOWN, buff=0.4)

        # Animar
        self.play(Write(title), FadeIn(subtitle))
        self.play(LaggedStart(*[FadeIn(e, shift=RIGHT * 0.3) for e in entradas], lag_ratio=0.2))
        self.play(FadeIn(label_entrada))
        self.play(
            LaggedStart(*[Create(a) for a in setas_entrada], lag_ratio=0.15),
            LaggedStart(*[FadeIn(p) for p in pesos_textos], lag_ratio=0.15),
        )
        self.play(FadeIn(soma, scale=0.8), FadeIn(label_soma))
        self.play(Create(seta_soma_ativ))
        self.play(FadeIn(ativacao, scale=0.8), FadeIn(label_ativ))
        self.play(Create(seta_ativ_saida))
        self.play(FadeIn(saida, scale=0.8), FadeIn(label_saida))
        self.wait(2)


class ExemploCredito(Scene):
    """Seção 2.2.2 — Exemplo concreto: decisão de crédito com valores numéricos."""

    def construct(self):
        title = Text("Decisão de Crédito", color=CORAL, font_size=32).to_edge(UP)

        # Dados de entrada
        dados = [
            ("Tempo de conta", "0.9", "0.4", TEAL),
            ("Renda", "0.7", "0.6", TEAL),
            ("Inadimplência", "0.8", "-0.9", "#E85454"),
        ]

        entradas_group = VGroup()
        for i, (nome, valor, peso, cor_peso) in enumerate(dados):
            y = 1.2 - i * 1.4

            # Box com nome
            box = RoundedRectangle(width=2.8, height=0.7, corner_radius=0.1)
            box.set_fill(TEAL, opacity=0.1).set_stroke(TEAL, width=1.5)
            box.move_to(LEFT * 4.2 + UP * y)
            nome_txt = Text(nome, font_size=14, color=WHITE).move_to(box)

            # Valor
            val_txt = Text(valor, font_size=20, color=TEAL_CLARO)
            val_txt.next_to(box, RIGHT, buff=0.3)

            # Peso
            peso_cor = cor_peso if float(peso) > 0 else "#E85454"
            peso_txt = Text(f"×{peso}", font_size=18, color=peso_cor)
            peso_txt.next_to(val_txt, RIGHT, buff=0.5)

            # Resultado parcial
            parcial = round(float(valor) * float(peso), 2)
            sinal = "+" if parcial >= 0 else ""
            parcial_txt = Text(f"= {sinal}{parcial}", font_size=18, color=CINZA_MEDIO)
            parcial_txt.next_to(peso_txt, RIGHT, buff=0.5)

            entradas_group.add(VGroup(box, nome_txt, val_txt, peso_txt, parcial_txt))

        # Resultado da soma
        soma_box = RoundedRectangle(width=2.2, height=0.8, corner_radius=0.15)
        soma_box.set_fill(CORAL, opacity=0.15).set_stroke(CORAL, width=2)
        soma_box.move_to(RIGHT * 3 + DOWN * 0.2)
        soma_txt = Text("Σ = 0.06", font_size=22, color=CORAL).move_to(soma_box)

        # Resultado final
        resultado = Text(
            '"Crédito provavelmente negado"',
            font_size=18, color=CORAL_CLARO
        ).next_to(soma_box, DOWN, buff=0.5)

        calculo = MathTex(
            r"(0.9 \times 0.4) + (0.7 \times 0.6) + (0.8 \times {-0.9})",
            font_size=22, color=CINZA_MEDIO
        ).next_to(soma_box, UP, buff=0.5)

        # Animar
        self.play(Write(title))
        for i, grupo in enumerate(entradas_group):
            self.play(FadeIn(grupo, shift=RIGHT * 0.3), run_time=0.6)

        self.play(Write(calculo))
        self.play(FadeIn(soma_box, scale=0.8), Write(soma_txt))
        self.play(FadeIn(resultado, shift=UP * 0.2))
        self.wait(2)


# ═════════════════════════════════════════════════════════════════════════════
# SEÇÃO 2.2.5 — Funções de Ativação
# ═════════════════════════════════════════════════════════════════════════════

class FuncoesAtivacao(Scene):
    """Sigmoid, ReLU e Softmax plotadas lado a lado."""

    def construct(self):
        title = Text("Funções de Ativação", color=CORAL, font_size=32).to_edge(UP)

        # ── Sigmoid ──
        ax1 = Axes(
            x_range=[-6, 6, 2], y_range=[-0.2, 1.2, 0.5],
            x_length=3.5, y_length=2.5,
            axis_config={"color": CINZA_MEDIO, "stroke_width": 1.5, "font_size": 16},
        ).shift(LEFT * 4 + DOWN * 0.5)
        sigmoid = ax1.plot(lambda x: 1 / (1 + np.exp(-x)), color=CORAL, stroke_width=3)
        label1 = Text("Sigmoid", font_size=18, color=CORAL).next_to(ax1, DOWN, buff=0.3)
        desc1 = Text("Saída entre 0 e 1", font_size=13, color=CINZA_MEDIO).next_to(label1, DOWN, buff=0.1)

        # ── ReLU ──
        ax2 = Axes(
            x_range=[-4, 4, 2], y_range=[-0.5, 4, 1],
            x_length=3.5, y_length=2.5,
            axis_config={"color": CINZA_MEDIO, "stroke_width": 1.5, "font_size": 16},
        ).shift(DOWN * 0.5)
        relu = ax2.plot(lambda x: max(0, x), color=TEAL, stroke_width=3)
        label2 = Text("ReLU", font_size=18, color=TEAL).next_to(ax2, DOWN, buff=0.3)
        desc2 = Text("Zero se negativo", font_size=13, color=CINZA_MEDIO).next_to(label2, DOWN, buff=0.1)

        # ── Softmax (barras de probabilidade) ──
        ax3_pos = RIGHT * 4 + DOWN * 0.5
        bars_data = [("Gato", 0.7, ROXO), ("Cão", 0.2, CORAL_CLARO), ("Outro", 0.1, CINZA_MEDIO)]
        bars = VGroup()
        for i, (nome, val, cor) in enumerate(bars_data):
            bar = Rectangle(width=0.6, height=val * 3, color=cor, fill_opacity=0.8, stroke_width=1)
            bar.move_to(ax3_pos + RIGHT * (i - 1) * 0.9 + UP * (val * 1.5 - 0.75))
            bar.align_to(ax3_pos + DOWN * 0.75, DOWN)
            pct = Text(f"{int(val*100)}%", font_size=14, color=cor).next_to(bar, UP, buff=0.1)
            lbl = Text(nome, font_size=13, color=WHITE).next_to(bar, DOWN, buff=0.15)
            bars.add(VGroup(bar, pct, lbl))
        label3 = Text("Softmax", font_size=18, color=ROXO).next_to(bars, DOWN, buff=0.3)
        desc3 = Text("Probabilidades somam 100%", font_size=13, color=CINZA_MEDIO).next_to(label3, DOWN, buff=0.1)

        # Animar
        self.play(Write(title))
        self.play(Create(ax1), Create(sigmoid), Write(label1), FadeIn(desc1), run_time=1.2)
        self.play(Create(ax2), Create(relu), Write(label2), FadeIn(desc2), run_time=1.2)
        self.play(
            LaggedStart(*[FadeIn(b, shift=UP * 0.3) for b in bars], lag_ratio=0.2),
            Write(label3), FadeIn(desc3), run_time=1.2
        )
        self.wait(2)


# ═════════════════════════════════════════════════════════════════════════════
# SEÇÃO 2.3 — Arquitetura da Rede Neural
# ═════════════════════════════════════════════════════════════════════════════

class ArquiteturaRede(Scene):
    """Rede neural com camadas de entrada, ocultas e saída."""

    def construct(self):
        title = Text("Arquitetura da Rede Neural", color=CORAL, font_size=32).to_edge(UP)

        camadas = [3, 5, 5, 2]  # entrada, oculta1, oculta2, saída
        cores = [TEAL, CORAL_CLARO, CORAL_CLARO, CORAL]
        nomes = ["Entrada", "Oculta 1", "Oculta 2", "Saída"]
        x_positions = [-4, -1.3, 1.3, 4]

        todos_nos = []
        labels = VGroup()

        for layer_idx, (n_neurons, cor, nome, x) in enumerate(zip(camadas, cores, nomes, x_positions)):
            layer_nodes = []
            total_height = (n_neurons - 1) * 0.9
            for i in range(n_neurons):
                y = total_height / 2 - i * 0.9
                circle = Circle(
                    radius=0.25, color=cor, fill_opacity=0.2, stroke_width=2
                ).move_to([x, y, 0])
                layer_nodes.append(circle)
            todos_nos.append(layer_nodes)

            label = Text(nome, font_size=14, color=cor)
            label.move_to([x, -total_height / 2 - 0.8, 0])
            labels.add(label)

        # Conexões entre camadas adjacentes
        conexoes = VGroup()
        for l in range(len(camadas) - 1):
            for node_a in todos_nos[l]:
                for node_b in todos_nos[l + 1]:
                    line = Line(
                        node_a.get_right(), node_b.get_left(),
                        color=CINZA_MEDIO, stroke_width=0.5, stroke_opacity=0.3
                    )
                    conexoes.add(line)

        # Animar
        self.play(Write(title))
        self.play(FadeIn(conexoes), run_time=0.8)
        for l, layer in enumerate(todos_nos):
            self.play(
                LaggedStart(*[FadeIn(n, scale=0.5) for n in layer], lag_ratio=0.08),
                run_time=0.6
            )
        self.play(FadeIn(labels))

        # Destaque: informação fluindo
        for l in range(len(camadas) - 1):
            flashes = VGroup()
            for node_a in todos_nos[l]:
                for node_b in todos_nos[l + 1]:
                    flash_line = Line(
                        node_a.get_right(), node_b.get_left(),
                        color=CORAL, stroke_width=1.5, stroke_opacity=0.6
                    )
                    flashes.add(flash_line)
            self.play(Create(flashes), run_time=0.4)
            self.play(FadeOut(flashes), run_time=0.3)

        self.wait(2)


# ═════════════════════════════════════════════════════════════════════════════
# SEÇÃO 2.4.1 — Ciclo de Treinamento
# ═════════════════════════════════════════════════════════════════════════════

class CicloTreinamento(Scene):
    """Diagrama circular: dados → cálculo → erro → ajuste → repete."""

    def construct(self):
        title = Text("O Ciclo de Treinamento", color=CORAL, font_size=32).to_edge(UP)

        etapas = [
            ("1  Dados\nentram", TEAL),
            ("2  Rede calcula\nsaída", CORAL_CLARO),
            ("3  Erro é\ncalculado", CORAL),
            ("4  Pesos\najustados", ROXO),
        ]

        n = len(etapas)
        radius = 2.2
        boxes = []
        arrows = []

        for i, (texto, cor) in enumerate(etapas):
            angle = np.pi / 2 - i * 2 * np.pi / n
            x, y = radius * np.cos(angle), radius * np.sin(angle)

            box = RoundedRectangle(width=2.4, height=1.0, corner_radius=0.15)
            box.set_fill(cor, opacity=0.15).set_stroke(cor, width=2)
            box.move_to([x, y - 0.3, 0])

            txt = Text(texto, font_size=15, color=WHITE).move_to(box)
            boxes.append(VGroup(box, txt))

        for i in range(n):
            start = boxes[i].get_center()
            end = boxes[(i + 1) % n].get_center()
            arrow = Arrow(start, end, buff=0.75, color=CINZA_MEDIO, stroke_width=2)
            arrows.append(arrow)

        repete = Text("(repete milhões de vezes)", font_size=16, color=CINZA_MEDIO)
        repete.move_to([0, -0.3, 0])

        # Animar
        self.play(Write(title))
        for i in range(n):
            self.play(FadeIn(boxes[i], scale=0.8), run_time=0.5)
            self.play(Create(arrows[i]), run_time=0.3)
        self.play(FadeIn(repete))
        self.wait(2)


# ═════════════════════════════════════════════════════════════════════════════
# SEÇÃO 2.4.2 — O Vale na Neblina (Gradient Descent)
# ═════════════════════════════════════════════════════════════════════════════

class ValeNaNeblina(Scene):
    """Animação do gradient descent como descida em paisagem montanhosa."""

    def construct(self):
        title = Text("O Vale na Neblina", color=CORAL, font_size=32).to_edge(UP)
        subtitle = Text("Gradient Descent", color=CINZA_MEDIO, font_size=18)
        subtitle.next_to(title, DOWN, buff=0.15)

        axes = Axes(
            x_range=[-4, 4, 1], y_range=[0, 7, 1],
            x_length=10, y_length=5,
            axis_config={"color": CINZA_MEDIO, "stroke_width": 1},
        ).shift(DOWN * 0.5)

        def erro_func(x):
            return 0.04 * x**4 - 0.35 * x**2 + 0.08 * x + 3.5

        curve = axes.plot(erro_func, color=CORAL, stroke_width=3)

        # Neblina (retângulo translúcido no topo)
        fog = Rectangle(
            width=12, height=2, fill_color=WHITE, fill_opacity=0.08, stroke_width=0
        ).move_to(UP * 2.5)

        # Labels dos eixos
        xlabel = Text("Configuração dos pesos", font_size=14, color=CINZA_MEDIO)
        xlabel.next_to(axes, DOWN, buff=0.3)
        ylabel = Text("Erro", font_size=14, color=CINZA_MEDIO)
        ylabel.next_to(axes, LEFT, buff=0.3).rotate(PI / 2)

        # Ponto inicial
        start_x = -3.0
        dot = Dot(color=YELLOW, radius=0.1).move_to(axes.c2p(start_x, erro_func(start_x)))
        dot_label = Text("Início\n(pesos aleatórios)", font_size=13, color=YELLOW)
        dot_label.next_to(dot, UP, buff=0.2)

        # Mínimo global marker
        min_x = 2.05  # aprox mínimo
        min_marker = DashedLine(
            axes.c2p(min_x, 0), axes.c2p(min_x, erro_func(min_x)),
            color=TEAL, stroke_width=1, dash_length=0.1
        )
        min_label = Text("Mínimo\n(menor erro)", font_size=13, color=TEAL)
        min_label.next_to(axes.c2p(min_x, erro_func(min_x)), DOWN + RIGHT, buff=0.2)

        self.play(Write(title), FadeIn(subtitle))
        self.play(Create(axes), FadeIn(xlabel), FadeIn(ylabel))
        self.play(Create(curve), FadeIn(fog))
        self.play(FadeIn(dot, scale=0.5), FadeIn(dot_label))
        self.wait(0.5)

        # Passos de descida
        passos = [-2.0, -1.0, 0.0, 0.8, 1.5, 2.0]
        step_labels = VGroup()

        self.play(FadeOut(dot_label))
        for i, px in enumerate(passos):
            py = erro_func(px)
            step_txt = Text(f"passo {i+1}", font_size=11, color=YELLOW)
            step_txt.next_to(axes.c2p(px, py), UP, buff=0.15)
            step_labels.add(step_txt)
            self.play(
                dot.animate.move_to(axes.c2p(px, py)),
                FadeIn(step_txt, run_time=0.3),
                run_time=0.6,
            )

        self.play(Create(min_marker), FadeIn(min_label))
        self.play(FadeOut(step_labels))
        self.wait(2)


# ═════════════════════════════════════════════════════════════════════════════
# SEÇÃO 2.4.3 — Overfitting vs. Aprendizado
# ═════════════════════════════════════════════════════════════════════════════

class OverfittingVsAprendizado(Scene):
    """Comparação visual: modelo que decora vs. modelo que generaliza."""

    def construct(self):
        title = Text("Decoreba vs. Aprendizado", color=CORAL, font_size=32).to_edge(UP)

        np.random.seed(42)
        xs = np.linspace(-2, 2, 12)
        ys_true = 0.5 * xs + 0.3
        noise = np.random.normal(0, 0.3, len(xs))
        ys = ys_true + noise

        # ── Overfitting (esquerda) ──
        ax1 = Axes(
            x_range=[-3, 3, 1], y_range=[-2, 3, 1],
            x_length=4.5, y_length=3.5,
            axis_config={"color": CINZA_MEDIO, "stroke_width": 1, "font_size": 14},
        ).shift(LEFT * 3.2 + DOWN * 0.5)

        dots1 = VGroup(*[
            Dot(ax1.c2p(x, y), color=TEAL, radius=0.06) for x, y in zip(xs, ys)
        ])

        # Curva wiggly passando por todos os pontos
        coeffs_over = np.polyfit(xs, ys, 11)
        overfit_curve = ax1.plot(
            lambda x: np.polyval(coeffs_over, x),
            x_range=[-2, 2], color="#E85454", stroke_width=2.5
        )

        label_over = Text("Overfitting", font_size=20, color="#E85454")
        label_over.next_to(ax1, DOWN, buff=0.4)
        desc_over = Text("Acerta 99% no treino\nAcerta 60% em dados novos", font_size=12, color=CINZA_MEDIO)
        desc_over.next_to(label_over, DOWN, buff=0.15)

        # ── Aprendizado adequado (direita) ──
        ax2 = Axes(
            x_range=[-3, 3, 1], y_range=[-2, 3, 1],
            x_length=4.5, y_length=3.5,
            axis_config={"color": CINZA_MEDIO, "stroke_width": 1, "font_size": 14},
        ).shift(RIGHT * 3.2 + DOWN * 0.5)

        dots2 = VGroup(*[
            Dot(ax2.c2p(x, y), color=TEAL, radius=0.06) for x, y in zip(xs, ys)
        ])

        # Reta simples
        coeffs_good = np.polyfit(xs, ys, 1)
        good_curve = ax2.plot(
            lambda x: np.polyval(coeffs_good, x),
            x_range=[-2.5, 2.5], color=TEAL, stroke_width=2.5
        )

        label_good = Text("Aprendizado adequado", font_size=20, color=TEAL)
        label_good.next_to(ax2, DOWN, buff=0.4)
        desc_good = Text("Acerta 85% no treino\nAcerta 83% em dados novos", font_size=12, color=CINZA_MEDIO)
        desc_good.next_to(label_good, DOWN, buff=0.15)

        # Animar
        self.play(Write(title))
        self.play(Create(ax1), Create(ax2))
        self.play(FadeIn(dots1), FadeIn(dots2))
        self.play(Create(overfit_curve), Write(label_over), FadeIn(desc_over), run_time=1.5)
        self.play(Create(good_curve), Write(label_good), FadeIn(desc_good), run_time=1.5)
        self.wait(2)


# ═════════════════════════════════════════════════════════════════════════════
# SEÇÃO 2.5.2 — Filtro Convolucional (CNN)
# ═════════════════════════════════════════════════════════════════════════════

class FiltroConvolucional(Scene):
    """Filtro 3×3 deslizando sobre uma grade de pixels."""

    def construct(self):
        title = Text("Redes Convolucionais (CNN)", color=CORAL, font_size=32).to_edge(UP)
        subtitle = Text("O filtro desliza pela imagem procurando padrões", color=CINZA_MEDIO, font_size=16)
        subtitle.next_to(title, DOWN, buff=0.15)

        CELL = 0.55
        GRID_SIZE = 6
        offset = LEFT * 2 + DOWN * 0.3

        # Grade de pixels com valores aleatórios
        np.random.seed(7)
        grid_vals = np.random.randint(0, 255, (GRID_SIZE, GRID_SIZE))

        cells = VGroup()
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                val = grid_vals[r, c]
                gray = val / 255.0
                rect = Square(side_length=CELL, stroke_width=1, stroke_color=CINZA_MEDIO)
                rect.set_fill(interpolate_color(BLACK, WHITE, gray), opacity=0.9)
                rect.move_to(offset + RIGHT * c * CELL + DOWN * r * CELL)
                cells.add(rect)

        # Filtro (janela destacada)
        filter_rect = Square(side_length=CELL * 3, stroke_width=3, stroke_color=CORAL, fill_opacity=0)

        label_img = Text("Imagem (6×6 pixels)", font_size=14, color=CINZA_MEDIO)
        label_img.next_to(cells, DOWN, buff=0.3)

        label_filter = Text("Filtro 3×3", font_size=14, color=CORAL)

        self.play(Write(title), FadeIn(subtitle))
        self.play(FadeIn(cells), FadeIn(label_img))

        # Posição inicial do filtro
        start_pos = offset + RIGHT * 1 * CELL + DOWN * 1 * CELL
        filter_rect.move_to(start_pos)
        label_filter.next_to(filter_rect, RIGHT, buff=0.4)

        self.play(Create(filter_rect), FadeIn(label_filter))

        # Deslizar o filtro
        for r in range(GRID_SIZE - 2):
            for c in range(GRID_SIZE - 2):
                target = offset + RIGHT * (c + 1) * CELL + DOWN * (r + 1) * CELL
                self.play(
                    filter_rect.animate.move_to(target),
                    label_filter.animate.next_to(target + RIGHT * CELL * 1.5, RIGHT, buff=0.2),
                    run_time=0.25,
                )

        self.wait(1)


# ═════════════════════════════════════════════════════════════════════════════
# SEÇÃO 2.5.5 — Mecanismo de Atenção (Transformer)
# ═════════════════════════════════════════════════════════════════════════════

class AtencaoTransformer(Scene):
    """Heatmap de atenção entre palavras — 'fui ao banco sacar dinheiro'."""

    def construct(self):
        title = Text("Mecanismo de Atenção", color=CORAL, font_size=32).to_edge(UP)
        subtitle = Text("Transformer: cada palavra 'presta atenção' nas outras", color=CINZA_MEDIO, font_size=16)
        subtitle.next_to(title, DOWN, buff=0.15)

        palavras = ["fui", "ao", "banco", "sacar", "dinheiro"]
        n = len(palavras)
        CELL = 0.75

        # Matriz de atenção simulada (foco: "banco" presta atenção em "sacar" e "dinheiro")
        atencao = np.array([
            [0.5, 0.1, 0.2, 0.1, 0.1],
            [0.1, 0.3, 0.3, 0.1, 0.2],
            [0.05, 0.05, 0.15, 0.40, 0.35],  # "banco" → foco em "sacar" e "dinheiro"
            [0.1, 0.05, 0.25, 0.3, 0.3],
            [0.05, 0.1, 0.30, 0.25, 0.3],
        ])

        grid_center = DOWN * 0.5
        cells = VGroup()

        for r in range(n):
            for c in range(n):
                val = atencao[r, c]
                rect = Square(side_length=CELL, stroke_width=0.5, stroke_color=CINZA_MEDIO)
                cor = interpolate_color(BLACK, CORAL, val / 0.5)
                rect.set_fill(cor, opacity=0.85)
                pos = grid_center + RIGHT * (c - n / 2 + 0.5) * CELL + DOWN * (r - n / 2 + 0.5) * CELL
                rect.move_to(pos)

                val_txt = Text(f"{val:.2f}", font_size=10, color=WHITE).move_to(rect)
                cells.add(VGroup(rect, val_txt))

        # Labels nas colunas (topo) e linhas (esquerda)
        col_labels = VGroup()
        row_labels = VGroup()
        for i, p in enumerate(palavras):
            col = Text(p, font_size=14, color=TEAL)
            col.move_to(grid_center + RIGHT * (i - n / 2 + 0.5) * CELL + UP * (n / 2 + 0.3) * CELL)
            col_labels.add(col)

            row = Text(p, font_size=14, color=CORAL_CLARO)
            row.move_to(grid_center + LEFT * (n / 2 + 0.6) * CELL + DOWN * (i - n / 2 + 0.5) * CELL)
            row_labels.add(row)

        # Destaque na linha do "banco"
        highlight = SurroundingRectangle(
            VGroup(*[cells[2 * n + c] for c in range(n)]),
            color=YELLOW, stroke_width=2, buff=0.02
        )
        hl_label = Text(
            '"banco" presta mais atenção\nem "sacar" e "dinheiro"',
            font_size=13, color=YELLOW
        ).next_to(highlight, RIGHT, buff=0.5)

        self.play(Write(title), FadeIn(subtitle))
        self.play(
            LaggedStart(*[FadeIn(c, scale=0.7) for c in cells], lag_ratio=0.01),
            run_time=1.5
        )
        self.play(FadeIn(col_labels), FadeIn(row_labels))
        self.play(Create(highlight), FadeIn(hl_label))
        self.wait(2)
