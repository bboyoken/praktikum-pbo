# praktikum-pbo

# Sistem Informasi Gizi

**Nama:** [Muhammad Zaki Fahriansyah]  
**NIM:** [2509106020]  
**Kelas:** [A1'25]

Post-test Praktikum Pemrograman Berorientasi Objek — mengimplementasikan konsep
**Class & Object**, **Atribut & Method** (instance, class, static), serta
**Encapsulation & Property** pada studi kasus sebuah klinik gizi.

## Deskripsi Program

Program ini mengelola data pasien, ahli gizi, menu diet, dan catatan kesehatan
pada sebuah klinik gizi. Setiap class berdiri sendiri (tidak menggunakan
inheritance) dan saling berinteraksi melalui objek — misalnya `AhliGizi`
menerima objek `Pasien` dan `MenuDiet` untuk membuat rekomendasi, sedangkan
`CatatanKesehatan` menyimpan objek `Pasien` sebagai salah satu atributnya.

## Struktur Class

### 1. `Pasien`
Menyimpan data pasien klinik gizi.

- **Atribut kelas**: `nama_klinik`, `total_pasien`, `kategori_valid`
- **Atribut public**: `id_pasien`, `nama`, `kategori`
- **Atribut private**: `__password`, `__berat_badan`, `__tinggi_badan`, `__riwayat_penyakit`
- **Property (getter/setter)**: `berat_badan`, `tinggi_badan`, `riwayat_penyakit`
  - Validasi: berat/tinggi badan harus > 0, riwayat penyakit tidak boleh kosong
- **Instance method**: `hitung_kebutuhan_kalori()`, `tampilkan_profil()`, `verifikasi_password()`
- **Class method**: `dari_dict()` (factory method), `ganti_nama_klinik()`
- **Static method**: `validasi_kategori()`

### 2. `AhliGizi`
Menyimpan data ahli gizi yang bertugas di klinik.

- **Atribut kelas**: `total_ahli_gizi`, `spesialisasi_valid`
- **Atribut public**: `id_ahli`, `nama`, `spesialisasi`
- **Atribut private**: `__password`, `__nomor_str`
- **Property (getter/setter)**: `nomor_str`
  - Validasi: minimal 6 karakter dan tidak boleh kosong
- **Instance method**: `buat_rekomendasi()` (menerima objek `Pasien` dan `MenuDiet`), `verifikasi_password()`
- **Class method**: `dari_dict()` (factory method)
- **Static method**: `validasi_spesialisasi()`

### 3. `MenuDiet`
Menyimpan data menu diet yang disusun oleh ahli gizi.

- **Atribut kelas**: `total_menu`, `kategori_menu_valid`
- **Atribut public**: `nama_menu`, `daftar_bahan`, `kategori_menu`
- **Atribut private**: `__kalori`
- **Property (getter/setter)**: `kalori`
  - Validasi: harus berupa angka dan lebih dari 0
- **Instance method**: `tampilkan_menu()`
- **Class method**: `dari_dict()` (factory method)
- **Static method**: `validasi_kalori()`

### 4. `CatatanKesehatan`
Mencatat riwayat pemeriksaan kesehatan seorang pasien pada kunjungan tertentu.

- **Atribut kelas**: `total_catatan`, `format_tanggal`
- **Atribut public**: `pasien` (objek `Pasien`), `tanggal`, `catatan_tambahan`
- **Atribut private**: `__berat_badan_tercatat`
- **Property (getter/setter)**: `berat_badan_tercatat`
  - Validasi: harus > 0
- **Instance method**: `tampilkan_catatan()`
- **Class method**: `rekap_total()`
- **Static method**: `validasi_format_tanggal()`

## Penerapan Encapsulation

Semua data fisik/medis dan data sensitif (berat badan, tinggi badan, riwayat
penyakit, password, nomor STR, kalori menu) disimpan sebagai atribut **private**
(`__nama_atribut`) dan hanya dapat diakses/diubah melalui **getter** (`@property`)
dan **setter** (`@nama_properti.setter`) yang sudah dilengkapi validasi. Jika
data yang dimasukkan tidak valid (misalnya angka negatif atau string kosong),
setter akan menolak perubahan dan mencetak pesan peringatan, sehingga nilai
lama tetap dipertahankan.

Password tidak diberi getter sama sekali — hanya bisa diperiksa lewat method
`verifikasi_password()` yang mengembalikan `True`/`False`, tanpa pernah
mengekspos nilai aslinya ke luar class.

## Cara Menjalankan Program

```bash
python 2509106020-MuhammadZakiFahriansyah-PT-1.py
# atau (untuk pengguna Linux/macOS):
python3 2509106020-MuhammadZakiFahriansyah-PT-1.py
```

Seluruh proses pembuatan objek, pemanggilan method, dan pengujian setter sudah
didemonstrasikan otomatis di bagian `if __name__ == "__main__":` pada akhir
file — tidak perlu input manual dari pengguna.

## Panduan Pengujian (Main Code)

Saat dijalankan, program akan mencetak output berurutan sesuai tahapan berikut:

1. **Pembuatan objek** — minimal 2 objek untuk tiap class (`Pasien`, `AhliGizi`,
   `MenuDiet`, `CatatanKesehatan`), sebagian dibuat lewat constructor biasa dan
   sebagian lewat class method `dari_dict()`.
2. **Instance method** — `hitung_kebutuhan_kalori()` dipanggil untuk pasien
   kategori reguler, kondisi medis, dan atlet untuk menunjukkan hasil yang
   berbeda-beda; `buat_rekomendasi()` dipanggil oleh objek `AhliGizi` dengan
   memakai objek `Pasien` dan `MenuDiet`.
3. **Class method** — `ganti_nama_klinik()` mengubah atribut kelas `nama_klinik`
   yang berlaku untuk semua objek `Pasien`; masing-masing class juga
   menampilkan atribut kelas totalnya (`total_pasien`, `total_ahli_gizi`, dst).
4. **Static method** — dipanggil langsung lewat nama class untuk memvalidasi
   kategori, spesialisasi, nilai kalori, dan format tanggal.
5. **Uji setter** — setiap property diuji dua kali: sekali dengan nilai valid
   (berhasil tersimpan) dan sekali dengan nilai tidak valid seperti angka
   negatif atau string terlalu pendek (ditolak, nilai lama tetap dipakai).
6. **Verifikasi password** — membuktikan bahwa data private (`__password`)
   tidak pernah bisa diakses langsung, hanya bisa diverifikasi lewat method.

## Struktur Repositori

```
.
praktikum-pbo/
├── kelas/
└── post-test/
    └── post-test-1/
        ├── 2509106020-MuhammadZakiFahriansyah-PT-1.py   # Program utama
        └── README.md                                    # Dokumentasi post-test 1
```