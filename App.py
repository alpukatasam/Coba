import requests
import streamlit as st

API_KEY = "AIzaSyCAYdkTkdm-v2uNdUT-jEjqcsYKL7hjxek"
CX = "61d16d0978b5a455e"
QUERY = "spices"

url = f"https://www.googleapis.com/customsearch/v1?q={QUERY}&cx={CX}&key={API_KEY}&searchType=image"

try:
    response = requests.get(url)
    data = response.json()

    if "items" in data:
        image_url = data["items"][0]["link"]
        st.image(image_url, caption="Hasil pertama dari Google Images")
        st.write(f"[Lihat Gambar]({image_url})")
    else:
        st.warning("Tidak ditemukan hasil.")

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
    st.write("Respon API:", data)  # Menampilkan respon API
