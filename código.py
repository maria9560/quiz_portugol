# quiz_portugol
import streamlit as st

st.set_page_config(page_title="Quiz Portugol", page_icon="💻", layout="centered")

# ─── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;600&family=Syne:wght@400;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
}

.stApp {
    background: #0d1117;
    color: #e6edf3;
}

h1, h2, h3 {
    font-family: 'Syne', sans-serif !important;
    font-weight: 800 !important;
}

.quiz-title {
    font-family: 'Syne', sans-serif;
    font-size: 2.2rem;
    font-weight: 800;
    background: linear-gradient(135deg, #58a6ff, #3fb950);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.2rem;
}

.quiz-subtitle {
    color: #8b949e;
    font-size: 0.95rem;
    margin-bottom: 1.5rem;
}

.code-block {
    background: #161b22;
    border: 1px solid #30363d;
    border-radius: 12px;
    padding: 1.4rem 1.6rem;
    font-family: 'Fira Code', monospace;
    font-size: 0.92rem;
    line-height: 2rem;
    color: #c9d1d9;
    white-space: pre;
    overflow-x: auto;
    margin-bottom: 1.2rem;
    position: relative;
}

.code-block .kw { color: #ff7b72; font-weight: 600; }
.code-block .str { color: #a5d6ff; }
.code-block .var { color: #79c0ff; }
.code-block .gap {
    background: #21262d;
    border: 2px dashed #58a6ff;
    border-radius: 6px;
    padding: 1px 10px;
    color: #58a6ff;
    font-weight: 600;
    cursor: pointer;
}

.banco-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.8rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    color: #8b949e;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
}

.correct-badge {
    background: #1a3a1e;
    border: 1px solid #3fb950;
    color: #3fb950;
    border-radius: 6px;
    padding: 2px 10px;
    font-size: 0.78rem;
    font-weight: 700;
}

.wrong-badge {
    background: #3a1a1a;
    border: 1px solid #f85149;
    color: #f85149;
    border-radius: 6px;
    padding: 2px 10px;
    font-size: 0.78rem;
    font-weight: 700;
}

.score-box {
    background: linear-gradient(135deg, #161b22, #1c2128);
    border: 1px solid #30363d;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    margin-top: 1rem;
}

.score-number {
    font-size: 4rem;
    font-weight: 800;
    background: linear-gradient(135deg, #58a6ff, #3fb950);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

div[data-testid="stSelectbox"] label {
    color: #8b949e !important;
    font-size: 0.8rem !important;
}

div[data-testid="stSelectbox"] > div > div {
    background: #161b22 !important;
    border: 1px solid #30363d !important;
    color: #e6edf3 !important;
    font-family: 'Fira Code', monospace !important;
    border-radius: 8px !important;
}

.stButton > button {
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    border-radius: 8px !important;
    border: none !important;
    transition: all 0.2s !important;
}

.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 4px 15px rgba(88,166,255,0.25) !important;
}

.step-indicator {
    display: flex;
    gap: 8px;
    margin-bottom: 1.2rem;
}

.step-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #30363d;
}

.step-dot.active { background: #58a6ff; }
.step-dot.done { background: #3fb950; }

hr { border-color: #21262d !important; }
</style>
""", unsafe_allow_html=True)

# ─── EXERCÍCIOS ────────────────────────────────────────────────────────────────

EXERCISES = [
    {
        "titulo": "Estrutura de Repetição — enquanto",
        "descricao": "Preencha as lacunas com os termos corretos do Portugol.",
        "codigo_display": """algoritmo "Repeticao"
var
   tem_combustivel : [1]
inicio
   tem_combustivel <- [2]
   [3] tem_combustivel faca
      escreval("Carro andando...")
      tem_combustivel <- [4]
   [5]
[6]""",
        "gabarito": {
            1: "logico",
            2: "verdadeiro",
            3: "enquanto",
            4: "falso",
            5: "fimenquanto",
            6: "fimalgoritmo",
        },
        "opcoes": ["logico", "verdadeiro", "enquanto", "falso", "fimenquanto", "fimalgoritmo", "inteiro", "real", "fimse"],
        "num_lacunas": 6,
    },
    {
        "titulo": "Estrutura Condicional — se...entao...senao",
        "descricao": "Preencha as lacunas com os termos corretos do Portugol.",
        "codigo_display": """algoritmo "Condicional"
var
   nota : [1]
inicio
   [2](nota)
   [3] nota >= 7 entao
      escreval("Aprovado!")
   [4]
      [5]("Reprovado!")
   [6]
fimalgoritmo""",
        "gabarito": {
            1: "inteiro",
            2: "leia",
            3: "se",
            4: "senao",
            5: "escreval",
            6: "fimse",
        },
        "opcoes": ["inteiro", "leia", "se", "senao", "escreval", "fimse", "logico", "enquanto", "fimalgoritmo"],
        "num_lacunas": 6,
    },
    {
        "titulo": "Estrutura de Escolha — caso...seja",
        "descricao": "Preencha as lacunas com os termos corretos do Portugol.",
        "codigo_display": """algoritmo "EscolhaDia"
var
   dia : [1]
inicio
   [2](dia)
   [3] dia [4]
      1: escreval("Segunda-feira")
      2: escreval("Terca-feira")
      3: escreval("Quarta-feira")
      outrocaso: [5]("Dia invalido")
   [6]
fimalgoritmo""",
        "gabarito": {
            1: "inteiro",
            2: "leia",
            3: "escolha",
            4: "seja",
            5: "escreval",
            6: "fimescolha",
        },
        "opcoes": ["inteiro", "leia", "escolha", "seja", "escreval", "fimescolha", "logico", "se", "fimse"],
        "num_lacunas": 6,
    },
]

# ─── SESSION STATE ─────────────────────────────────────────────────────────────

def init_state():
    if "ex_idx" not in st.session_state:
        st.session_state.ex_idx = 0
    if "respostas" not in st.session_state:
        st.session_state.respostas = [{} for _ in EXERCISES]
    if "verificado" not in st.session_state:
        st.session_state.verificado = [False] * len(EXERCISES)
    if "acertos_total" not in st.session_state:
        st.session_state.acertos_total = [None] * len(EXERCISES)
    if "finalizado" not in st.session_state:
        st.session_state.finalizado = False

init_state()

# ─── HEADER ────────────────────────────────────────────────────────────────────

st.markdown('<div class="quiz-title">💻 Quiz Portugol</div>', unsafe_allow_html=True)
st.markdown('<div class="quiz-subtitle">Complete os algoritmos preenchendo as lacunas corretamente.</div>', unsafe_allow_html=True)

# Step indicator
dots_html = '<div class="step-indicator">'
for i in range(len(EXERCISES)):
    if i < st.session_state.ex_idx:
        dots_html += '<div class="step-dot done"></div>'
    elif i == st.session_state.ex_idx:
        dots_html += '<div class="step-dot active"></div>'
    else:
        dots_html += '<div class="step-dot"></div>'
dots_html += '</div>'
st.markdown(dots_html, unsafe_allow_html=True)

# ─── TELA FINAL ────────────────────────────────────────────────────────────────

if st.session_state.finalizado:
    total_lacunas = sum(ex["num_lacunas"] for ex in EXERCISES)
    total_acertos = sum(a for a in st.session_state.acertos_total if a is not None)

    emoji = "🏆" if total_acertos == total_lacunas else ("👍" if total_acertos >= total_lacunas // 2 else "📚")
    msg = "Perfeito! Você domina Portugol!" if total_acertos == total_lacunas else (
        "Muito bem! Continue praticando!" if total_acertos >= total_lacunas // 2 else
        "Continue estudando, você vai melhorar!"
    )

    st.markdown(f"""
    <div class="score-box">
        <div style="font-size:3rem">{emoji}</div>
        <div class="score-number">{total_acertos}/{total_lacunas}</div>
        <div style="color:#8b949e; margin-top:0.5rem; font-size:1rem">{msg}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("**Resumo por exercício:**")
    for i, ex in enumerate(EXERCISES):
        ac = st.session_state.acertos_total[i] or 0
        total = ex["num_lacunas"]
        cor = "#3fb950" if ac == total else ("#f0883e" if ac >= total // 2 else "#f85149")
        st.markdown(f"- **Exercício {i+1}** — {ex['titulo']}: <span style='color:{cor}'>{ac}/{total} acertos</span>", unsafe_allow_html=True)

    if st.button("🔄 Recomeçar Quiz", use_container_width=True):
        for key in ["ex_idx", "respostas", "verificado", "acertos_total", "finalizado"]:
            del st.session_state[key]
        st.rerun()
    st.stop()

# ─── EXERCÍCIO ATUAL ───────────────────────────────────────────────────────────

idx = st.session_state.ex_idx
ex = EXERCISES[idx]

st.markdown(f"### Exercício {idx+1} de {len(EXERCISES)}: {ex['titulo']}")
st.markdown(f"<span style='color:#8b949e'>{ex['descricao']}</span>", unsafe_allow_html=True)

# Código com lacunas substituídas por [N]
codigo = ex["codigo_display"]
st.markdown('<div class="code-block">' + codigo.replace("<", "&lt;").replace(">", "&gt;") + '</div>', unsafe_allow_html=True)

st.markdown('<div class="banco-label">🗂 Banco de Termos</div>', unsafe_allow_html=True)
st.markdown(f"<span style='color:#58a6ff; font-family:Fira Code; font-size:0.85rem'>{'  •  '.join(ex['opcoes'])}</span>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("**Preencha cada lacuna:**")

# Selectboxes para cada lacuna
opcoes_com_vazio = ["— selecione —"] + ex["opcoes"]
cols_per_row = 3
lacunas = list(range(1, ex["num_lacunas"] + 1))

verificado = st.session_state.verificado[idx]
gabarito = ex["gabarito"]
respostas = st.session_state.respostas[idx]

for i in range(0, len(lacunas), cols_per_row):
    chunk = lacunas[i:i+cols_per_row]
    cols = st.columns(len(chunk))
    for j, num in enumerate(chunk):
        with cols[j]:
            label = f"Lacuna [{num}]"
            current = respostas.get(num, "— selecione —")
            if current not in opcoes_com_vazio:
                current = "— selecione —"
            selected = st.selectbox(
                label,
                opcoes_com_vazio,
                index=opcoes_com_vazio.index(current),
                key=f"ex{idx}_lac{num}",
                disabled=verificado,
            )
            st.session_state.respostas[idx][num] = selected

            if verificado:
                correto = gabarito[num]
                resp = st.session_state.respostas[idx].get(num, "")
                if resp == correto:
                    st.markdown('<span class="correct-badge">✓ Correto</span>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<span class="wrong-badge">✗ Era: {correto}</span>', unsafe_allow_html=True)

st.markdown("---")

# Botões
col1, col2 = st.columns(2)

with col1:
    if not verificado:
        if st.button("✅ Verificar", use_container_width=True, type="primary"):
            todas_preenchidas = all(
                st.session_state.respostas[idx].get(n, "— selecione —") != "— selecione —"
                for n in lacunas
            )
            if not todas_preenchidas:
                st.warning("⚠️ Preencha todas as lacunas antes de verificar!")
            else:
                st.session_state.verificado[idx] = True
                acertos = sum(
                    1 for n in lacunas
                    if st.session_state.respostas[idx].get(n) == gabarito[n]
                )
                st.session_state.acertos_total[idx] = acertos
                st.rerun()

with col2:
    if verificado:
        acertos = st.session_state.acertos_total[idx]
        total = ex["num_lacunas"]
        cor = "#3fb950" if acertos == total else ("#f0883e" if acertos >= total // 2 else "#f85149")
        st.markdown(f"<div style='text-align:center; padding:0.5rem; color:{cor}; font-weight:700; font-size:1.1rem'>🎯 {acertos}/{total} acertos</div>", unsafe_allow_html=True)

        proximo_label = "Próximo Exercício →" if idx < len(EXERCISES) - 1 else "Ver Resultado 🏁"
        if st.button(proximo_label, use_container_width=True, type="primary"):
            if idx < len(EXERCISES) - 1:
                st.session_state.ex_idx += 1
                st.rerun()
            else:
                st.session_state.finalizado = True
                st.rerun()
