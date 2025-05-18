import streamlit as st
from PIL import Image
import datetime

# Konfigurasi halaman
st.set_page_config(
    page_title="2 Tahun Cinta Kita 💕",
    page_icon="💞",
    layout="wide",
)

# CSS untuk nuansa pink dan efek lucu
st.markdown("""
    <style>
    body {
        background-color: #ffe6f0;
    }
    .title {
        font-size: 60px;
        font-weight: bold;
        color: #ff3399;
        text-align: center;
    }
    .subtitle {
        font-size: 30px;
        color: #ff66b2;
        text-align: center;
    }
    .heart {
        font-size: 80px;
        text-align: center;
        animation: pulse 1s infinite;
    }
    @keyframes pulse {
        0% {transform: scale(1);}
        50% {transform: scale(1.1);}
        100% {transform: scale(1);}
    }
    </style>
""", unsafe_allow_html=True)

# Judul besar dan animasi hati
st.markdown('<div class="title">Selamat 2 Tahun, Sayang! 💖</div>', unsafe_allow_html=True)
st.markdown('<div class="heart">💕</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Perjalanan cinta kita yang penuh warna 🌸</div>', unsafe_allow_html=True)

# Hitung hari jadian
anniversary_date = datetime.date(2023, 5, 18)
today = datetime.date.today()
days_together = (today - anniversary_date).days
st.markdown(f"### Kita sudah bersama selama **{days_together} hari** 🌟")

# Surat cinta
st.markdown("## 💌 Surat Untuk Kamu")
st.success("""
Sayangku,

Dua tahun yang penuh cinta, tawa, dan pelukan hangat. 
Setiap hari bersamamu seperti mimpi indah yang terus berulang.

Terima kasih sudah menjadi rumah dan pelangi di setiap hariku 🌈

Dengan cinta yang tak pernah pudar,
**Aku ❤️ Kamu!**
""")

# Galeri Foto
st.markdown("## 📸 Galeri Kenangan Kita")

cols = st.columns(3)
with cols[0]:
    f1 = st.file_uploader("Foto 1", type=["jpg", "png", "jpeg"], key="foto1")
    if f1: st.image(Image.open(f1), use_column_width=True)
with cols[1]:
    f2 = st.file_uploader("Foto 2", type=["jpg", "png", "jpeg"], key="foto2")
    if f2: st.image(Image.open(f2), use_column_width=True)
with cols[2]:
    f3 = st.file_uploader("Foto 3", type=["jpg", "png", "jpeg"], key="foto3")
    if f3: st.image(Image.open(f3), use_column_width=True)

cols2 = st.columns(3)
with cols2[0]:
    f4 = st.file_uploader("Foto 4", type=["jpg", "png", "jpeg"], key="foto4")
    if f4: st.image(Image.open(f4), use_column_width=True)
with cols2[1]:
    f5 = st.file_uploader("Foto 5", type=["jpg", "png", "jpeg"], key="foto5")
    if f5: st.image(Image.open(f5), use_column_width=True)
with cols2[2]:
    f6 = st.file_uploader("Foto 6", type=["jpg", "png", "jpeg"], key="foto6")
    if f6: st.image(Image.open(f6), use_column_width=True)

# Kejutan balon
if st.button("Klik untuk kejutan spesial 🎁"):
    st.balloons()
    st.snow()
    st.success("Surprise peluk cium dari jauh 💞")

# Penutup manis
st.markdown("### 🌷 Terima kasih sudah jadi bagian terindah dalam hidupku.")
st.markdown("##### — Dibuat dengan cinta 💘 pakai Python + Streamlit —")

