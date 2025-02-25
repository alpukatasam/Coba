import streamlit as st

def search_unsplash(query, num_results=5):
    return [f"https://source.unsplash.com/featured/?{query}"] * num_results

st.title("🔍 Mesin Pencari Gambar Tanpa Login")
query = st.text_input("Masukkan kata kunci pencarian:")
num_results = st.slider("Jumlah gambar:", 1, 10, 5)

if st.button("Cari 🔎"):
    if query:
        images = search_unsplash(query, num_results)
        for img in images:
            st.image(img, use_column_width=True)
