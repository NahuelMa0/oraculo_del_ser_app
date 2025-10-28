import streamlit as st
import random
import datetime
import base64

# --- CONFIGURACIÓN INICIAL ---
st.set_page_config(
    page_title="El Oráculo del Ser — Juego Cuántico",
    page_icon="🔮",
    layout="centered"
)

# --- SONIDOS (archivos base64 simulados para ejemplo) ---
# Puedes reemplazarlos por tus propios archivos MP3/WAV
sound_flip = "https://actions.google.com/sounds/v1/cartoon/wood_plank_flicks.ogg"
sound_shuffle = "https://actions.google.com/sounds/v1/cartoon/wood_plank_flicks.ogg"

# --- CSS Y JS PARA ANIMACIÓN DE VOLTEO ---
st.markdown("""
<style>
body {
    background: radial-gradient(circle at center, #f7e6ff, #e0b9ff);
    color: #2e004f;
    font-family: 'Verdana', sans-serif;
}
h1, h2, h3 {
    text-align: center;
    color: #4a148c;
}
.deck {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 16px;
    margin-top: 30px;
}
.scene {
  width: 130px;
  height: 180px;
  perspective: 600px;
}
.card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform 0.8s;
  cursor: pointer;
}
.card.is-flipped {
  transform: rotateY(180deg);
}
.card__face {
  position: absolute;
  width: 100%;
  height: 100%;
  backface-visibility: hidden;
  border-radius: 12px;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 15px;
  text-align: center;
  padding: 10px;
}
.card__face--front {
  background: linear-gradient(145deg, #4a148c, #7b1fa2);
  color: white;
}
.card__face--back {
  background: linear-gradient(145deg, #d1c4e9, #b39ddb);
  transform: rotateY(180deg);
  color: #4a148c;
}
button {
    border-radius: 10px;
    padding: 8px 16px;
    margin: 4px;
}
</style>

<script>
function playSound(url){
    var audio = new Audio(url);
    audio.play();
}
function flipCard(id, soundUrl){
    var card = document.getElementById(id);
    if(card.classList.contains('is-flipped')){
        card.classList.remove('is-flipped');
    } else {
        card.classList.add('is-flipped');
        playSound(soundUrl);
    }
}
</script>
""", unsafe_allow_html=True)

# --- BASE DE DATOS DE CARTAS ---
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
if "historial" not in st.session_state:
    st.session_state.historial = {}

# --- ENCABEZADO ---
st.title("🔮 EL ORÁCULO DEL SER 🔮")
st.markdown("#### 100 Juegos para Despertar la Consciencia")

st.markdown("Selecciona una carta o deja que el oráculo te muestre su mensaje cuántico...")

# --- CARTA DEL DÍA ---
today = datetime.date.today()
if today not in st.session_state.historial:
    carta_dia = random.choice(st.session_state.mazo)
    st.session_state.historial[today] = carta_dia
else:
    carta_dia = st.session_state.historial[today]
st.info(f"✨ Carta del día ({today.strftime('%d/%m/%Y')}): {juegos[carta_dia]}")

st.write("---")

# --- BOTONES DE CONTROL ---
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🔀 Barajar"):
        random.shuffle(st.session_state.mazo)
        st.markdown(f"<script>playSound('{sound_shuffle}');</script>", unsafe_allow_html=True)
        st.success("El mazo ha sido barajado 🌪️")
with col2:
    if st.button("🎲 Carta Aleatoria"):
        carta_random = random.choice(st.session_state.mazo)
        st.markdown(f"### 🃏 Carta Aleatoria: {juegos[carta_random]}")
        st.markdown(f"<script>playSound('{sound_flip}');</script>", unsafe_allow_html=True)
with col3:
    if st.button("📜 Ver Historial"):
        st.write("#### 📅 Historial de Cartas del Día")
        for fecha, carta in st.session_state.historial.items():
            st.write(f"{fecha.strftime('%d/%m/%Y')} — {juegos[carta]}")

st.write("---")

# --- BARAJA VISUAL ---
st.markdown("### 🌟 Elige una carta:")

st.markdown("<div class='deck'>", unsafe_allow_html=True)
for num in st.session_state.mazo[:10]:  # muestra solo 10 cartas visibles
    card_id = f"card_{num}"
    front = f"<div class='card__face card__face--front'>🂠</div>"
    back = f"<div class='card__face card__face--back'>{juegos[num]}</div>"
    st.markdown(
        f"<div class='scene'><div class='card' id='{card_id}' onclick=\"flipCard('{card_id}', '{sound_flip}')\">{front}{back}</div></div>",
        unsafe_allow_html=True
    )
st.markdown("</div>", unsafe_allow_html=True)
