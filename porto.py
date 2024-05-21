import streamlit as st

# Judul aplikasi
st.title("Portofolio Saya")

# Sidebar
st.sidebar.title("Pilih Halaman")
pilihan = st.sidebar.selectbox("Navigasi", ["Tentangku", "Prestasi", "Pengalaman", "Pendidikan"])

# Konten halaman berdasarkan pilihan di sidebar
if pilihan == "Tentangku":
    st.header("Tentangku")
    st.write("""
    Halo! Saya [Nama Anda], seorang [profesi/pekerjaan] yang berdedikasi dengan pengalaman dalam [bidang/industri].
    Saya memiliki minat yang besar dalam [minat/hobi], dan saya selalu berusaha untuk meningkatkan keterampilan saya dalam [keahlian/keterampilan utama].
    """)

elif pilihan == "Prestasi":
    st.header("Prestasi")
    st.write("""
    - Prestasi 1: Deskripsi prestasi 1
    - Prestasi 2: Deskripsi prestasi 2
    - Prestasi 3: Deskripsi prestasi 3
    """)

elif pilihan == "Pengalaman":
    st.header("Pengalaman")
    st.write("""
    - Perusahaan A (Tahun): Posisi
      - Deskripsi tugas dan tanggung jawab
    - Perusahaan B (Tahun): Posisi
      - Deskripsi tugas dan tanggung jawab
    - Perusahaan C (Tahun): Posisi
      - Deskripsi tugas dan tanggung jawab
    """)

elif pilihan == "Pendidikan":
    st.header("Pendidikan")
    st.write("""
    - Universitas X (Tahun): Gelar
      - Deskripsi program studi
    - Universitas Y (Tahun): Gelar
      - Deskripsi program studi
    - SMA Z (Tahun): Jurusan
      - Deskripsi jurusan
    """)

# Footer
st.sidebar.markdown("© 2024 [Nama Anda]")
