import streamlit as st
from PIL import Image
import datetime

# Konfigurasi halaman
st.set_page_config(
    page_title="2 Tahun Bersama 💖",
    page_icon="💑",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Gaya CSS gemas
st.markdown("""
    <style>
    .big-title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: pink;
    }
    .subtitle {
        font-size: 30px;
        text-align: center;
        color: #ff66b2;
    }
    .heart {
        text-align: center;
        font-size: 80px;
        animation: pulse 1s infinite;
    }
    @keyframes pulse {
        0% {transform: scale(1);}
        50% {transform: scale(1.1);}
        100% {transform: scale(1);}
    }
    </style>
""", unsafe_allow_html=True)

# Tampilan judul dan emoji
st.markdown('<div class="big-title">Happy 2nd Anniversary! 🎉</div>', unsafe_allow_html=True)
st.markdown('<div class="heart">❤️</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">2 Tahun Bersama Kamu 💞</div>', unsafe_allow_html=True)

# Tambahkan foto berdua jika ada
uploaded_file = st.file_uploader("Upload foto kenangan kalian 📸", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Kenangan manis kita 💖", use_column_width=True)

# Pesan manis
st.markdown("## Surat Cinta Untukmu 💌")
message = """
Sayangku,

Hari ini tepat 2 tahun kita bersama. Setiap momen bersamamu begitu berarti dan penuh warna. 
Terima kasih sudah selalu ada, tertawa bersamaku, dan mencintaiku apa adanya.

Aku bersyukur banget bisa melewati semua ini dengan kamu 💕
Semoga kita bisa terus berjalan berdua, menua bersama 🥰

Love you always 💘
"""
st.write(message)

# Hitung waktu bersama
anniversary_date = datetime.date(2023, 5, 18)  # ganti sesuai tanggal jadian kalian
today = datetime.date.today()
days_together = (today - anniversary_date).days

st.markdown(f"### Kita sudah bersama selama **{days_together} hari** 🌈")

# Tombol kejutan
if st.button("Klik untuk peluk virtual 🤗"):
    st.balloons()
    st.success("Peluk dari jauh! 💞")

