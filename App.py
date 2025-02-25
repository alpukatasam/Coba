import requests
import streamlit as st

# API Key & CX
API_KEY = "AIzaSyCAYdkTkdm-v2uNdUT-jEjqcsYKL7hjxek"
CX = "61d16d0978b5a455e"

# Judul Aplikasi
st.title("Pencarian Gambar dengan Google Images")

# Input Kata Kunci dari User
query = st.text_input("Masukkan kata kunci pencarian:", "")

# Pastikan input tidak kosong sebelum menjalankan pencarian
if st.button("Cari Gambar"):
    if query:  # Pastikan query tidak kosong
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={CX}&key={API_KEY}&searchType=image"

        try:
            response = requests.get(url)
            data = response.json()

            if "items" in data:
                for item in data["items"][:3]:  # Tampilkan 3 gambar pertama
                    st.image(item["link"], caption=item["title"], use_column_width=True)
                    st.write(f"[Lihat Gambar]({item['link']})")
            else:
                st.warning("Tidak ditemukan hasil.")

        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")
    else:
        st.warning("Masukkan kata kunci terlebih dahulu.")
