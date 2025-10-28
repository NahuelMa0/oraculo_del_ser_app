import streamlit as st
import random

# --- CONFIGURACIÓN ---
st.set_page_config(
    page_title="El Oráculo del Ser — 100 Cartas Cuánticas",
    page_icon="🔮",
    layout="centered"
)

# --- DATOS DE LAS CARTAS ---
juegos = {
    1: "🌅 El Testigo Silente — Observa sin reaccionar durante 5 minutos.",
    2: "🍃 Respiración del Alma — Siente cómo el universo te inhala y exhala.",
    3: "🔥 Llama Interior — Cierra los ojos y siente el fuego de tu presencia.",
    4: "🌊 Danza del Agua — Mueve tu cuerpo como una ola hasta disolver el pensamiento.",
    5: "💨 El Suspiro de Dios — Exhala todo lo que no eres.",
    6: "🐚 Escucha Profunda — Escucha el sonido detrás de los sonidos.",
    7: "🌈 Luz en las Células — Imagina que cada célula brilla con consciencia.",
    8: "🌻 Gratitud Radical — Agradece incluso lo que te incomoda.",
    9: "🐦 Vuelo Interior — Imagina que tu atención es un pájaro libre.",
    10: "🪶 Ligereza — Cada pensamiento que sueltas te hace más liviano.",
    11: "🪞 El Espejo Sagrado — Mira tus ojos y di: 'Yo Soy el que observa'.",
    12: "🧘‍♀️ Sintonía Cuántica — Permite que la mente se sincronice con el corazón.",
    13: "🌌 Silencio Vibrante — Escucha la música del vacío.",
    14: "⚡ Campo Unificado — Siente cómo eres la red donde todo sucede.",
    15: "🔥 Renacimiento — Imagina que mueres y renaces en cada respiración.",
    16: "💎 Observador Transparente — Deja que la experiencia sea lo que es.",
    17: "🌾 Cosecha Interna — Recuerda las bendiciones de tu camino.",
    18: "🌕 Presencia Lunar — Observa sin intervenir durante la luna llena.",
    19: "🌞 Sol Interno — Visualiza tu pecho irradiando consciencia.",
    20: "🌍 Unidad — Percibe que todos los seres respiran contigo."
}

# Extiende automáticamente a 100 cartas con frases genéricas
for i in range(21, 101):
    juegos[i] = f"✨ Carta {i}: Contempla el instante presente sin juicio ni expectativa."

# --- IMÁGENES NATURALES (optimizadas) ---
imagenes_naturaleza = [
    "https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=400&h=800&fit=crop",
    "https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=400&h=800&fit=crop",
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=400&h=800&fit=crop",
    "https://images.unsplash.com/photo-1493246507139-91e8fad9978e?w=400&h=800&fit=crop",
    "https://images.unsplash.com/photo-1505483531331-fc3cf89c727c?w=400&h=800&fit=crop",
    "https://images.unsplash.com/photo-1519681393784-d120267933ba?w=400&h=800&fit=crop",
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=400&h=800&fit=crop",
    "https://images.unsplash.com/photo-1523413651479-597eb2da0ad6?w=400&h=800&fit=crop",
    "https://images.unsplash.com/photo-1499084732479-de2c02d45fc4?w=400&h=800&fit=crop",
    "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?w=400&h=800&fit=crop"
]

# --- ESTADO DE SESIÓN ---
if "baraja" not in st.session_state:
    st.session_state.baraja = list(range(1, 101))
    random.shuffle(st.session_state.baraja)

if "carta_elegida" not in st.session_state:
    st.session_state.carta_elegida = None

# --- CABECERA ---
st.title("🔮 EL ORÁCULO DEL SER 🔮")
st.markdown("### 100 Cartas para Despertar la Consciencia")
st.markdown("Haz clic en una carta del abanico para revelar su mensaje 🌟")

# --- BOTÓN DE BARAJAR ---
if st.button("🔁 Barajar y reiniciar"):
    random.shuffle(st.session_state.baraja)
    st.session_state.carta_elegida = None

# --- CSS DE DISEÑO ---
st.markdown("""
<style>
.container {
  position: relative;
  height: 300px;
  margin-top: 50px;
  display: flex;
  justify-content: center;
  align-items: flex-end;
}
.card {
  width: 80px;
  height: 160px;
  background: linear-gradient(135deg, #4a148c, #7b1fa2);
  border-radius: 8px;
  box-shadow: 1px 2px 4px rgba(0,0,0,0.3);
  cursor: pointer;
  position: absolute;
  transform-origin: bottom center;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  overflow: hidden;
  border: 1px solid rgba(255,255,255,0.2);
}
.card img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  opacity: 0.85;
}
.card:hover {
  transform: scale(1.05);
  box-shadow: 3px 4px 8px rgba(0,0,0,0.5);
}
.carta-activa {
  width: 300px;
  height: 500px;
  margin: 40px auto;
  border-radius: 16px;
  box-shadow: 2px 4px 12px rgba(0,0,0,0.4);
  background-size: cover;
  background-position: center;
  padding: 20px;
  text-align: center;
  color: white;
  font-size: 18px;
  text-shadow: 1px 1px 3px black;
}
</style>
""", unsafe_allow_html=True)

# --- MOSTRAR CARTAS EN ABANICO ---
n_cartas = 12
offset = 10
baraja = st.session_state.baraja

html = "<div class='container'>"
for i, num in enumerate(baraja[:n_cartas]):
    angle = -30 + i * (60 / n_cartas)
    img = random.choice(imagenes_naturaleza)
    html += f"""
    <div class='card' onclick="window.location.href='?carta={num}'" 
         style="transform: rotate({angle}deg) translateY(-5px); left:{i*offset}px;">
        <img src='{img}'/>
    </div>
    """
html += "</div>"
st.markdown(html, unsafe_allow_html=True)

# --- SELECCIÓN DE CARTA ---
params = st.query_params
if "carta" in params:
    num = int(params["carta"][0])
    st.session_state.carta_elegida = num

if st.session_state.carta_elegida:
    num = st.session_state.carta_elegida
    img = random.choice(imagenes_naturaleza)
    st.markdown(f"<div class='carta-activa' style=\"background-image: url('{img}')\">"
                f"<p>{juegos[num]}</p></div>", unsafe_allow_html=True)
