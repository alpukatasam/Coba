import requests
import streamlit as st

# API Key & CX
API_KEY = "AIzaSyCAYdkTkdm-v2uNdUT-jEjqcsYKL7hjxek"
CX = "61d16d0978b5a455e"

# Judul Aplikasi
st.title("Pencarian Gambar dengan Google Images")

# Input Kata Kunci dari User
query = st.text_input("Masukkan kata kunci pencarian:", "")

if st.button("Cari Gambar") and query:
