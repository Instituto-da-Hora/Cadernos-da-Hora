Cadernos da Hora — Visualizações
Repositório de código aberto com as visualizações, diagramas e animações produzidas para os Cadernos da Hora, material educacional do Instituto da Hora sobre tecnologia, algoritmos e inteligência artificial.

Todas as imagens e animações deste repositório são geradas programaticamente — sem IA generativa de imagens. Usamos Python, Manim, Matplotlib e SVG para garantir reprodutibilidade, transparência e coerência com os valores do projeto.


Estrutura do Repositório
cadernos-da-hora/
├── caderno-trilha1-vol2/          # Trilha 1, Volume 2 — IA: Definições e Horizontes
│   ├── capitulo2/                 # Redes Neurais em Profundidade
│   │   ├── cenas_manim.py         # Animações Manim (vídeo/PNG)
│   │   ├── diagramas_svg.py       # Diagramas vetoriais (SVG)
│   │   ├── graficos_matplotlib.py # Gráficos estáticos (PNG/PDF)
│   │   └── README.md              # Índice das visualizações do capítulo
│   ├── capitulo1/                 # Conceituando a IA
│   │   └── ...
│   └── assets/                    # Imagens renderizadas prontas
├── docs/                          # Guias de contribuição e estilo
│   └── STYLE_GUIDE.md
├── requirements.txt
├── LICENSE
└── README.md                      # ← Você está aqui
Cada caderno futuro ganha sua própria pasta (caderno-trilha1-vol3/, caderno-trilha2-vol1/, etc.).

Início Rápido
Pré-requisitos
macOS:
bashbrew install py3cairo ffmpeg pango
Ubuntu/Debian:
bashsudo apt install build-essential python3-dev libcairo2-dev libpango1.0-dev ffmpeg
Windows:
bashchoco install manimce
Instalação
bashgit clone https://github.com/institutodahora/cadernos-da-hora.git
cd cadernos-da-hora
pip install -r requirements.txt
Renderizar uma animação
bash# Vídeo MP4 (qualidade média — rápido para testar)
manim -qm caderno-trilha1-vol2/capitulo2/cenas_manim.py ValeNaNeblina

# Vídeo em alta qualidade
manim -qh caderno-trilha1-vol2/capitulo2/cenas_manim.py ValeNaNeblina

# Exportar frame estático como PNG
manim -qh --format png -s caderno-trilha1-vol2/capitulo2/cenas_manim.py ValeNaNeblina

# Todas as cenas de um arquivo
manim -qm caderno-trilha1-vol2/capitulo2/cenas_manim.py
Gerar diagramas SVG
bashpython caderno-trilha1-vol2/capitulo2/diagramas_svg.py
# → Arquivos .svg gerados em caderno-trilha1-vol2/assets/
Gerar gráficos Matplotlib
bashpython caderno-trilha1-vol2/capitulo2/graficos_matplotlib.py
# → Arquivos .png e .pdf gerados em caderno-trilha1-vol2/assets/

Por que código em vez de IA generativa?
Os Cadernos da Hora tratam de transparência algorítmica. Seria contraditório ilustrá-los com imagens geradas por sistemas opacos. Ao gerar visualizações com código:

Reprodutibilidade — qualquer pessoa pode rodar o mesmo código e obter a mesma imagem
Transparência — o processo de criação é auditável, linha por linha
Acessibilidade — os SVGs são escaláveis e compatíveis com leitores de tela
Coerência pedagógica — o código em si é material educativo


Ferramentas Utilizadas
FerramentaPara quêSaídaManimAnimações explicativasMP4, GIF, PNGMatplotlibGráficos e plotsPNG, PDF, SVGSVG puro (Python)Diagramas vetoriaisSVGCairoBackend de renderização—

Cadernos Disponíveis
CadernoStatusVisualizaçõesTrilha 1, Vol. 2 — IA: Definições e Horizontes🟢 Em andamentoCapítulo 2

Contribuindo
Contribuições são bem-vindas! Veja o guia de estilo para manter a consistência visual. Abra uma issue para discutir novas visualizações antes de enviar um PR.

Licença
O código deste repositório é distribuído sob a licença MIT.
O conteúdo dos Cadernos da Hora é distribuído sob CC BY-NC-ND — Atribuição-NãoComercial-SemDerivações.

Instituto da Hora · institutodahora.org.br
