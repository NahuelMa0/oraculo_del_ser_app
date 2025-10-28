import streamlit as st
import random

# --- CONFIGURACIÓN ---
st.set_page_config(
    page_title="El Oráculo del Ser — 100 Cartas",
    page_icon="🔮",
    layout="centered"
)

# --- CARTAS Y MENSAJES ---
juegos = {}
mensajes_iniciales = [
    "🌅 El Testigo Silente — Observa sin reaccionar durante 5 minutos.",
    "🍃 Respiración del Alma — Siente cómo el universo te inhala y exhala.",
    "🔥 Llama Interior — Cierra los ojos y siente el fuego de tu presencia.",
    "🌊 Danza del Agua — Mueve tu cuerpo como una ola hasta disolver el pensamiento.",
    "💨 El Suspiro de Dios — Exhala todo lo que no eres.",
    "🐚 Escucha Profunda — Escucha el sonido detrás de los sonidos.",
    "🌈 Luz en las Células — Imagina que cada célula brilla con consciencia.",
    "🌻 Gratitud Radical — Agradece incluso lo que te incomoda.",
    "🐦 Vuelo Interior — Imagina que tu atención es un pájaro libre.",
    "🪶 Ligereza — Cada pensamiento que sueltas te hace más liviano.",
    "🪞 El Espejo Sagrado — Mira tus ojos y di: 'Yo Soy el que observa'.",
    "🧘‍♀️ Sintonía Cuántica — Permite que la mente se sincronice con el corazón.",
    "🌌 Silencio Vibrante — Escucha la música del vacío.",
    "⚡ Campo Unificado — Siente cómo eres la red donde todo sucede.",
    "🔥 Renacimiento — Imagina que mueres y renaces en cada respiración.",
    "💎 Observador Transparente — Deja que la experiencia sea lo que es.",
    "🌾 Cosecha Interna — Recuerda las bendiciones de tu camino.",
    "🌕 Presencia Lunar — Observa sin intervenir durante la luna llena.",
    "🌞 Sol Interno — Visualiza tu pecho irradiando consciencia.",
    "🌍 Unidad — Percibe que todos los seres respiran contigo."
]

for i in range(1, 21):
    juegos[i] = mensajes_iniciales[i - 1]

for i in range(21, 101):
    juegos[i] = f"✨ Carta {i}: Contempla el instante presente sin juicio ni expectativa."

# --- IMÁGENES OPTIMIZADAS ---
imagenes = [
    "https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=200&h=400&fit=crop",
    "https://images.unsplash.com/photo-1469474968028-56623f02e42e?w=200&h=400&fit=crop",
    "https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?w=200&h=400&fit=crop",
    "https://images.unsplash.com/photo-1493246507139-91e8fad9978e?w=200&h=400&fit=crop",
    "https://images.unsplash.com/photo-1505483531331-fc3cf89c727c?w=200&h=400&fit=crop",
    "https://images.unsplash.com/photo-1519681393784-d120267933ba?w=200&h=400&fit=crop",
    "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=200&h=400&fit=crop",
    "https://images.unsplash.com/photo-1523413651479-597eb2da0ad6?w=200&h=400&fit=crop",
    "https://images.unsplash.com/photo-1499084732479-de2c02d45fc4?w=200&h=400&fit=crop",
    "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?w=200&h=400&fit=crop"
]

# --- SESIÓN ---
if "baraja" not in st.session_state:
    st.session_state.baraja = list(range(1, 101))
    random.shuffle(st.session_state.baraja)

if "carta_elegida" not in st.session_state:
    st.session_state.carta_elegida = None

# --- CABECERA ---
st.title("🔮 EL ORÁCULO DEL SER 🔮")
st.markdown("### 100 Cartas para Despertar la Consciencia")
st.markdown("Haz clic en una carta del abanico para revelar su mensaje 🌟")

# --- BOTÓN BARAJAR ---
if st.button("🔁 Barajar y reiniciar"):
    random.shuffle(st.session_state.baraja)
    st.session_state.carta_elegida = None

# --- MOSTRAR ABANICO ---
cols = st.columns(12)
for i, col in enumerate(cols):
    carta_num = st.session_state.baraja[i]
    if col.button("🂠", key=f"carta_{carta_num}"):
        st.session_state.carta_elegida = carta_num

# --- REVELAR CARTA ---
if st.session_state.carta_elegida:
    carta = st.session_state.carta_elegida
    img = random.choice(imagenes)
    st.image(img, width=200)
    st.markdown(f"### {juegos[carta]}")
