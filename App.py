import streamlit as st
import requests

# Konfigurasi API
API_KEY = "YOUR_GOOGLE_API_KEY"
CSE_ID = "YOUR_CUSTOM_SEARCH_ENGINE_ID"

def search_images(query, num_results=5):
    """Fungsi untuk mencari gambar di Google Image menggunakan API."""
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={CSE_ID}&searchType=image&num={num_results}&key={API_KEY}"
    
    response = requests.get(url)
    results = response.json()
    
    images = []
    if "items" in results:
        for item in results["items"]:
            images.append(item["link"])
    return images

# Streamlit UI
st.title("Mesin Pencari Gambar dengan Google Image")

query = st.text_input("Masukkan kata kunci pencarian:")
num_results = st.slider("Jumlah gambar yang diinginkan:", 1, 10, 5)

if st.button("Cari"):
    if query:
        images = search_images(query, num_results)
        if images:
            for img in images:
                st.image(img, use_column_width=True)
        else:
            st.error("Tidak ditemukan gambar untuk kata kunci ini.")
    else:
        st.warning("Silakan masukkan kata kunci.")

