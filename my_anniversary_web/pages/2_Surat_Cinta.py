import streamlit as st

st.set_page_config(page_title="Surat Cinta 💌", page_icon="💌")
st.title("💌 Surat Cinta Untuk Kamu")

st.markdown("""
<div style='background-color: #ffe6f0; padding: 20px; border-radius: 10px; color: #99004d'>
    Sayangku,

    <br><br>
    Dua tahun yang luar biasa.  
    Terima kasih sudah hadir, mencintai, dan menerima aku.  
    Semoga setiap langkah ke depan bisa kita lalui bersama,  
    dengan cinta yang semakin besar setiap harinya 💖

    <br><br>
    Dengan penuh cinta,<br>
    Aku 🥰
</div>
""", unsafe_allow_html=True)

if st.button("Peluk dari jauh 🤗"):
    st.snow()
    st.success("Kamu dapat peluk hangat dariku 💘")
