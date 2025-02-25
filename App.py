import streamlit as st
from duckduckgo_search import DDGS

def search_duckduckgo_images(query, num_results=5):
    """Mencari gambar menggunakan DuckDuckGo tanpa API key."""
    with DDGS() as ddgs:
        return [r["image"] for r in ddgs.images(query, max_results=num_results)]

# UI Streamlit
st.title("🔍 Mesin Pencari Gambar Tanpa Login!")
st.markdown("Cari gambar langsung tanpa perlu akun atau API key. Powered by DuckDuckGo.")

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

