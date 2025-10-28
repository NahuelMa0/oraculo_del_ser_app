import streamlit as st
import random
import datetime

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="El Oráculo del Ser — Juego de Naipes Cuánticos",
    page_icon="🔮",
    layout="centered"
)

# --- ESTILOS VISUALES (CSS) ---
st.markdown("""
<style>
body {
    background: radial-gradient(circle at center, #f4e1ff, #d4b5f9);
    color: #2e004f;
    font-family: 'Verdana', sans-serif;
}
h1, h2, h3 {
    text-align: center;
    color: #4a148c;
}
.card-container {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 20px;
}
.card {
    width: 110px;
    height: 160px;
    background: linear-gradient(135deg, #4a148c, #7b1fa2);
    border-radius: 12px;
    box-shadow: 3px 3px 6px rgba(0,0,0,0.3);
    cursor: pointer;
    transition: all 0.5s ease;
    transform-style: preserve-3d;
    position: relative;
}
.card:hover {
    transform: scale(1.05);
}
.card.flipped {
    transform: rotateY(180deg);
}
.card-front, .card-back {
    position: absolute;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    border-radius: 12px;
    text-align: center;
    padding-top: 60px;
    font-size: 16px;
    color: white;
}
.card-back {
    background: linear-gradient(145deg, #b39ddb, #7e57c2);
    transform: rotateY(180deg);
    color: #fff;
}
</style>
""", unsafe_allow_html=True)

# --- BASE DE DATOS DE JUEGOS (simplificada aquí) ---
juegos = {
    1: "🪞 El Espejo Silente — Mírate sin juicio por 5 minutos.",
    2: "🎭 Cambio de Nombre — Usa otro nombre un día.",
    3: "🌊 El Cuerpo Respira — Deja que el cuerpo respire sin controlarlo.",
    4: "💃 Danza Espontánea — Deja que el cuerpo se mueva solo.",
    5: "🧘‍♀️ Reprogramación Vibracional — Repite un pensamiento elevado 21 días.",
    6: "🌈 Visualización Fotónica — Llena tus células de luz coherente.",
    7: "💞 Reflejo Honesto — Agradece a quien te muestra tus sombras.",
    8: "😂 Risa Cuántica — Ríe sin motivo durante 3 minutos.",
    9: "🌅 Observador Activo — Visualiza tu mañana antes de dormir.",
    10: "🌍 Meditación de Unidad — Cada ser es una célula del mismo cuerpo."
}

# --- SESIÓN ---
if "mazo" not in st.session_state:
    st.session_state.mazo = list(juegos.keys())
    random.shuffle(st.session_state.mazo)
if "seleccionada" not in st.session_state:
    st.session_state.seleccionada = None
if "historial" not in st.session_state:
    st.session_state.historial = {}

# --- ENCABEZADO ---
st.title("🔮 EL ORÁCULO DEL SER 🔮")
st.subheader("100 Juegos para Despertar la Consciencia")

st.markdown("Selecciona una carta o deja que el oráculo te muestre tu mensaje del día.")

# --- CARTA DEL DÍA (automática) ---
today = datetime.date.today()
if today not in st.session_state.historial:
    carta_dia = random.choice(st.session_state.mazo)
    st.session_state.historial[today] = carta_dia
else:
    carta_dia = st.session_state.historial[today]

st.info(f"✨ Tu carta del día ({today.strftime('%d/%m/%Y')}): {juegos[carta_dia]}")

st.write("---")

# --- BOTONES DE CONTROL ---
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🎴 Barajar Mazo"):
        random.shuffle(st.session_state.mazo)
        st.session_state.seleccionada = None
        st.success("El mazo ha sido barajado 🌪️")
with col2:
    if st.button("🎲 Carta Aleatoria"):
        st.session_state.seleccionada = random.choice(st.session_state.mazo)
with col3:
    if st.button("📜 Ver Historial"):
        st.session_state.seleccionada = None
        st.write("#### 📅 Historial de Cartas del Día")
        for fecha, carta in st.session_state.historial.items():
            st.write(f"{fecha.strftime('%d/%m/%Y')} — {juegos[carta]}")

st.write("---")

# --- MOSTRAR CARTAS VISUALMENTE ---
st.markdown("### 🌟 Elige una carta:")

cols = st.columns(5)
for i, col in enumerate(cols):
    with col:
        carta_num = st.session_state.mazo[i]
        if st.button(f"🂠 Carta {carta_num}", key=f"carta_{i}"):
            st.session_state.seleccionada = carta_num

st.write("---")

# --- MOSTRAR RESULTADO ---
if st.session_state.seleccionada:
    num = st.session_state.seleccionada
    st.markdown(f"### 🃏 Carta Revelada — #{num}")
    st.success(juegos[num])
    st.markdown("🌸 *Contempla su mensaje y juega con él durante el día.*")
else:
    st.markdown("*Haz clic en una carta o usa los botones de arriba para comenzar.*")
