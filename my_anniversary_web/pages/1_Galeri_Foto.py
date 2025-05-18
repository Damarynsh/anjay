import streamlit as st
from PIL import Image

st.set_page_config(page_title="Galeri Kenangan 💕", page_icon="📸", layout="wide")
st.title("📸 Galeri Kenangan Kita")

st.markdown("Unggah beberapa foto manis kita berdua yaa 😍")

cols = st.columns(3)
for i in range(6):
    with cols[i % 3]:
        foto = st.file_uploader(f"Foto {i+1}", type=["jpg", "png", "jpeg"], key=f"foto_{i}")
        if foto:
            img = Image.open(foto)
            st.image(img, use_column_width=True)
