import streamlit as st
import requests
from bs4 import BeautifulSoup

def search_duckduckgo_images(query, num_results=5):
    """Mencari gambar menggunakan scraping DuckDuckGo."""
    url = f"https://duckduckgo.com/?q={query}&iax=images&ia=images"
    headers = {"User-Agent": "Mozilla/5.0"}
    
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    images = []
    for img_tag in soup.find_all("img", limit=num_results):
        img_url = img_tag.get("src")
        if img_url and img_url.startswith("http"):
            images.append(img_url)
    
    return images

# UI Streamlit
st.title("🔍 Mesin Pencari Gambar Tanpa API!")
st.markdown("Cari gambar langsung tanpa perlu akun atau API key.")

query = st.text_input("Masukkan kata kunci pencarian:")
num_results = st.slider("Jumlah gambar yang diinginkan:", 1, 10, 5)

if st.button("Cari 🔎"):
    if query:
        images = search_duckduckgo_images(query, num_results)
        if images:
            for img in images:
                st.image(img, use_column_width=True)
        else:
            st.error("❌ Tidak ditemukan gambar untuk kata kunci ini.")
    else:
        st.warning("⚠️ Silakan masukkan kata kunci.")
