import streamlit as st
import requests

ACCESS_KEY = "MASUKKAN_API_KEY_ANDA"  # Ganti dengan API Key dari Unsplash

def search_unsplash(query, num_results=5):
    url = f"https://api.unsplash.com/photos/random?query={query}&count={num_results}&client_id={ACCESS_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return [img["urls"]["regular"] for img in response.json()]
    return []

st.title("🔍 Mesin Pencari Gambar Tanpa Login")
query = st.text_input("Masukkan kata kunci pencarian:")
num_results = st.slider("Jumlah gambar:", 1, 10, 5)

if st.button("Cari 🔎"):
    if query:
        images = search_unsplash(query, num_results)
        if images:
            for img in images:
                st.image(img, use_container_width=True)
        else:
            st.error("❌ Tidak ditemukan gambar.")
