import streamlit as st
import random
import datetime

st.set_page_config(
    page_title="El Oráculo del Ser — Edición Mística 3D",
    page_icon="🔮",
    layout="centered"
)

# --- DATOS DE CARTAS ---
juegos = {i: f"Carta #{i}: 🌿 Mensaje del Oráculo — Vive la consciencia del instante." for i in range(1, 101)}

# --- IMÁGENES NATURALES ---
imagenes_naturaleza = [
    "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
    "https://images.unsplash.com/photo-1469474968028-56623f02e42e",
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee",
    "https://images.unsplash.com/photo-1493246507139-91e8fad9978e",
    "https://images.unsplash.com/photo-1505483531331-fc3cf89c727c",
    "https://images.unsplash.com/photo-1519681393784-d120267933ba",
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
    "https://images.unsplash.com/photo-1523413651479-597eb2da0ad6",
    "https://images.unsplash.com/photo-1499084732479-de2c02d45fc4",
    "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429",
]

# --- CABECERA ---
st.title("🔮 EL ORÁCULO DEL SER 🔮")
st.markdown("### 100 Cartas para Despertar la Consciencia")

st.markdown("Haz clic en una carta para revelarla... 🌟")

# --- ESTILOS Y SCRIPT ---
st.markdown("""
<style>
.container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 12px;
  margin-top: 20px;
}
.scene {
  width: 160px;
  height: 220px;
  perspective: 800px;
}
.card {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform 1s;
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
  overflow: hidden;
  box-shadow: 2px 2px 8px rgba(0,0,0,0.3);
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  color: white;
  font-size: 16px;
  font-weight: bold;
}
.card__face--front {
  background: linear-gradient(135deg, #4a148c, #7b1fa2);
}
.card__face--back {
  background-size: cover;
  background-position: center;
  color: #fff;
  transform: rotateY(180deg);
  padding: 10px;
  text-shadow: 1px 1px 3px black;
}
</style>

<script>
function playFlipSound() {
  const audio = new Audio("https://actions.google.com/sounds/v1/cartoon/wood_plank_flicks.ogg");
  audio.play();
}
function flipCard(id) {
  var card = document.getElementById(id);
  card.classList.toggle('is-flipped');
  playFlipSound();
}
</script>
""", unsafe_allow_html=True)

# --- GENERACIÓN DE MAZO VISUAL ---
mazo = list(juegos.keys())
random.shuffle(mazo)
mazo = mazo[:9]  # muestra 9 cartas por pantalla

# --- CONSTRUCCIÓN HTML DE LAS CARTAS ---
html_cartas = "<div class='container'>"
for num in mazo:
    img_url = random.choice(imagenes_naturaleza)
    html_cartas += f"""
    <div class="scene">
      <div class="card" id="card_{num}" onclick="flipCard('card_{num}')">
        <div class="card__face card__face--front">🂠</div>
        <div class="card__face card__face--back" style="background-image: url('{img_url}');">
          <div>{juegos[num]}</div>
        </div>
      </div>
    </div>
    """
html_cartas += "</div>"

st.components.v1.html(html_cartas, height=900, scrolling=True)
