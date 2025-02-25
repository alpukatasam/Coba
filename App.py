import streamlit as st
import os
import requests

# Ambil Client ID dari Streamlit Secrets
IMGUR_CLIENT_ID = st.secrets["IMGUR_CLIENT_ID"]

# Fungsi untuk upload gambar ke Imgur
def upload_to_imgur(image_path):
    headers = {"Authorization": f"Client-ID {IMGUR_CLIENT_ID}"}
    with open(image_path, "rb") as f:
        response = requests.post("https://api.imgur.com/3/upload", headers=headers, files={"image": f})
    if response.status_code == 200:
        return response.json()["data"]["link"]
    else:
        return None

# Fungsi untuk menyimpan gambar sementara
def save_uploaded_file(uploaded_file):
    file_path = os.path.join("temp_image.jpg")
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

# Judul Aplikasi
st.title("Pencarian Gambar di Google & Yandex")

# Upload Gambar
uploaded_file = st.file_uploader("Upload gambar untuk mencari di Google/Yandex", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Simpan gambar sementara
    file_path = save_uploaded_file(uploaded_file)
    
    # Upload ke Imgur
    imgur_url = upload_to_imgur(file_path)
    
    if imgur_url:
        st.image(imgur_url, caption="Gambar yang diunggah", use_column_width=True)
        
        # URL untuk pencarian gambar langsung
        google_lens_url = "https://lens.google.com/upload"
        google_image_url = f"https://www.google.com/searchbyimage?image_url={imgur_url}"
        yandex_url = f"https://yandex.com/images/search?rpt=imageview&url={imgur_url}"
        
        st.write("### Pilih mesin pencari:")
        st.markdown(f"[🔍 Cari dengan Google Lens]({google_lens_url})", unsafe_allow_html=True)
        st.markdown(f"[🔍 Cari dengan Google Images]({google_image_url})", unsafe_allow_html=True)
        st.markdown(f"[🔍 Cari dengan Yandex]({yandex_url})", unsafe_allow_html=True)
    else:
        st.error("Gagal mengupload gambar ke Imgur. Coba lagi.")
