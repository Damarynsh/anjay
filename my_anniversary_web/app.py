import streamlit as st
import datetime

st.set_page_config(page_title="Anniversary Kita 💖", page_icon="💘", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #fff0f5;
    }
    .judul {
        font-size: 60px;
        color: #ff3399;
        text-align: center;
        font-weight: bold;
    }
    .heart {
        font-size: 80px;
        text-align: center;
        animation: pulse 1s infinite;
    }
    .surat {
        font-size: 18px;
        padding: 20px;
        background-color: #ffe6f0;
        border-radius: 10px;
        color: #99004d;
    }
    @keyframes pulse {
        0% {transform: scale(1);}
        50% {transform: scale(1.1);}
        100% {transform: scale(1);}
    }
    audio {
        display: block;
        margin: auto;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="judul">Selamat 2 Tahun Sayangku! 💖</div>', unsafe_allow_html=True)
st.markdown('<div class="heart">💕</div>', unsafe_allow_html=True)

tanggal_jadian = datetime.date(2023, 5, 18)
hari_ini = datetime.date.today()
jumlah_hari = (hari_ini - tanggal_jadian).days
st.markdown(f"<h4 style='text-align:center'>Kita sudah bersama selama <span style='color:#ff3399'>{jumlah_hari} hari</span> 🌸</h4>", unsafe_allow_html=True)

st.markdown("""
    <audio controls autoplay loop>
      <source src="https://github.com/username/repo-name/raw/main/assets/musik.mp3" type="audio/mp3">
      Your browser does not support the audio element.
    </audio>
""", unsafe_allow_html=True)

st.markdown("""
<div class="surat">
    Terima kasih sudah selalu ada untukku. Terima kasih untuk cinta, tawa, pelukan, dan semua kenangan indah.  
    Aku bahagia banget bisa jalan bareng kamu selama ini.  
    Aku cinta kamuuuuu! 💘
</div>
""", unsafe_allow_html=True)

st.balloons()
