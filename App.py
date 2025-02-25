import streamlit as st
import os

# Fungsi untuk menyimpan gambar sementara
def save_uploaded_file(uploaded_file):
    file_path = os.path.join("temp_image.jpg")  # Simpan sebagai temp file
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
    
    # Tampilkan gambar yang diunggah
    st.image(file_path, caption="Gambar yang diunggah", use_column_width=True)
    
    # URL untuk pencarian gambar (harus di-upload ke online hosting jika ingin otomatis)
    st.write("### Pilih mesin pencari:")
    
    google_lens_url = "https://lens.google.com/upload"
    st.markdown(f"[🔍 Cari dengan Google Lens]({google_lens_url})", unsafe_allow_html=True)
    
    google_image_url = "https://www.google.com/searchbyimage?image_url=YOUR_IMAGE_URL"
    st.markdown(f"[🔍 Cari dengan Google Images]({google_image_url})", unsafe_allow_html=True)
    
    yandex_url = "https://yandex.com/images/search?rpt=imageview&url=YOUR_IMAGE_URL"
    st.markdown(f"[🔍 Cari dengan Yandex]({yandex_url})", unsafe_allow_html=True)
    
    st.warning("Saat ini, Google Image & Yandex memerlukan URL gambar yang bisa diakses online. Untuk otomatisasi, perlu hosting gambar.")
