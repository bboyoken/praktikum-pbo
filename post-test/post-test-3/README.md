# Sistem Informasi Gizi

**Nama:** Muhammad Zaki Fahriansyah  
**NIM:** 2509106020  
**Kelas:** A1'25  

Post-test 3 melanjutkan program Post-test 2 dengan mempertahankan konsep **Class & Object**, **Encapsulation & Property**, **Inheritance**, dan relasi UML. Materi baru yang ditambahkan adalah **Abstraksi**, **Polimorfisme**, dan prinsip **Open/Closed (OCP)**.

## Deskripsi Program

Program ini mengelola data pasien, ahli gizi, menu diet, dan catatan kesehatan
pada sebuah klinik gizi. `Pasien` dan `AhliGizi` mewarisi `User`. Program juga
menyediakan layanan rekomendasi dan pencatatan yang mengikuti kontrak abstrak
`LayananKlinik`, serta mengirim notifikasi melalui beberapa kanal.

---

## Struktur Class

### 1. `User`
Superclass untuk akun pasien dan ahli gizi.

- **Atribut public**: `nama`
- **Atribut protected**: `_status_aktif`
- **Atribut private**: `__password`
- **Instance method**: `verifikasi_password()`, `nonaktifkan_akun()`, `info_dasar()`

### 2. `Pasien(User)`
Menyimpan data pasien klinik gizi.

- **Atribut kelas**: `nama_klinik`, `total_pasien`, `kategori_valid`
- **Atribut public**: `id_pasien`, `nama`, `kategori`
- **Atribut private**: `__password`, `__berat_badan`, `__tinggi_badan`, `__riwayat_penyakit`
- **Property (getter/setter)**: `berat_badan`, `tinggi_badan`, `riwayat_penyakit`
  - Validasi: berat/tinggi badan harus > 0, riwayat penyakit tidak boleh kosong
- **Instance method**: `hitung_kebutuhan_kalori()`, `tampilkan_profil()`, `catat_riwayat_kesehatan()`, `info_dasar()` (override)
- **Class method**: `dari_dict()` (factory method), `ganti_nama_klinik()`
- **Static method**: `validasi_kategori()`

### 3. `AhliGizi(User)`
Menyimpan data ahli gizi yang bertugas di klinik.

- **Atribut kelas**: `total_ahli_gizi`, `spesialisasi_valid`
- **Atribut public**: `id_ahli`, `nama`, `spesialisasi`
- **Atribut private**: `__password`, `__nomor_str`
- **Property (getter/setter)**: `nomor_str`
  - Validasi: minimal 6 karakter dan tidak boleh kosong
- **Instance method**: `buat_rekomendasi()` (menerima objek `Pasien` dan `MenuDiet`), `tambah_pasien_binaan()`, `info_dasar()` (override), `nonaktifkan_akun()` (override)
- **Class method**: `dari_dict()` (factory method)
- **Static method**: `validasi_spesialisasi()`

### 4. `MenuDiet`
Menyimpan data menu diet yang disusun oleh ahli gizi.

- **Atribut kelas**: `total_menu`, `kategori_menu_valid`
- **Atribut public**: `nama_menu`, `daftar_bahan`, `kategori_menu`
- **Atribut private**: `__kalori`
- **Property (getter/setter)**: `kalori`
  - Validasi: harus berupa angka dan lebih dari 0
- **Instance method**: `tampilkan_menu()`
- **Class method**: `dari_dict()` (factory method)
- **Static method**: `validasi_kalori()`

### 5. `CatatanKesehatan`
Mencatat riwayat pemeriksaan kesehatan seorang pasien pada kunjungan tertentu.

- **Atribut kelas**: `total_catatan`, `format_tanggal`
- **Atribut public**: `pasien` (objek `Pasien`), `tanggal`, `catatan_tambahan`
- **Atribut private**: `__berat_badan_tercatat`
- **Property (getter/setter)**: `berat_badan_tercatat`
  - Validasi: harus > 0
- **Instance method**: `tampilkan_catatan()`, `__str__()` (operator overloading untuk representasi teks)
- **Class method**: `rekap_total()`
- **Static method**: `validasi_format_tanggal()`

### 6. `LayananKlinik(ABC)` dan layanan turunannya

`LayananKlinik` mendefinisikan kontrak abstrak untuk proses layanan klinik.
`LayananRekomendasi` memakai objek `AhliGizi`, `Pasien`, dan `MenuDiet`, sedangkan
`LayananCatatan` memakai objek `Pasien` untuk membuat catatan.

- **Abstract method**: `validasi()`, `proses()`
- **Method konkret bersama**: `jalankan()` memeriksa hasil validasi lalu memanggil proses.
- **Subclass**: `LayananRekomendasi` dan `LayananCatatan` mengimplementasikan kedua abstract method.

### 7. Kelas notifikasi

`EmailNotifikasi` dan `SMSNotifikasi` tidak memiliki hubungan inheritance, tetapi
keduanya memiliki method `kirim(pesan)` yang dipanggil melalui fungsi
`kirim_notifikasi()`.

## Penerapan Encapsulation

Semua data fisik/medis dan data sensitif (berat badan, tinggi badan, riwayat
penyakit, password, nomor STR, kalori menu) disimpan sebagai atribut **private**
(`__nama_atribut`) dan hanya dapat diakses/diubah melalui **getter** (`@property`)
dan **setter** (`@nama_properti.setter`) yang sudah dilengkapi validasi. Jika
data yang dimasukkan tidak valid (misalnya angka negatif atau string kosong),
setter akan menolak perubahan dan mencetak pesan peringatan, sehingga nilai
lama tetap dipertahankan.

Password tidak diberi getter sama sekali; hanya bisa diperiksa lewat method
`verifikasi_password()` yang mengembalikan `True`/`False`, tanpa pernah
mengekspos nilai aslinya ke luar class.

---

## Diagram Class UML

Diagram berikut menampilkan seluruh kelas dalam satu kanvas. Ada dua hierarki
pewarisan: `User` menjadi induk `Pasien` dan `AhliGizi`, sedangkan `LayananKlinik`
menjadi induk `LayananRekomendasi` dan `LayananCatatan`. Keduanya terhubung dalam
model melalui relasi layanan dengan kelas domain yang dipakai.

![Class Diagram Sistem Informasi Gizi](diagram-posttest-3-terpadu.svg)


---

### 1. Relasi UML

| Relasi | Kata Kunci | Lokasi di Program | Penjelasan |
|---|---|---|---|
| **Asosiasi** | "menggunakan" | `AhliGizi.buat_rekomendasi(pasien, menu)` dan kelas layanan | `AhliGizi.buat_rekomendasi()` memakai objek `Pasien` dan `MenuDiet` sebagai parameter. `LayananRekomendasi` menyimpan dependency `AhliGizi`, `Pasien`, dan `MenuDiet`, sedangkan `LayananCatatan` menyimpan objek `Pasien`. |
| **Agregasi** | "memiliki" | `AhliGizi._daftar_pasien_binaan` + `tambah_pasien_binaan()` / `tampilkan_pasien_binaan()` | Objek `Pasien` dibuat **di luar** `AhliGizi`, lalu didaftarkan ke dalam list `_daftar_pasien_binaan`. Jika objek `AhliGizi` dihapus, objek `Pasien` tetap ada secara independen (tidak ikut musnah). |
| **Komposisi** | "terdiri dari" | `Pasien._riwayat_kesehatan` + `catat_riwayat_kesehatan()` / `tampilkan_riwayat_kesehatan()` | Objek `CatatanKesehatan` dibuat oleh method milik `Pasien` dan disimpan dalam daftar riwayat pasien. Karena catatan dikelola sebagai bagian dari riwayat pasien, relasi ini dimodelkan sebagai komposisi. |

### 2. Inheritance

Ditambahkan superclass baru **`User`** yang menaungi dua subclass: **`Pasien`**
dan **`AhliGizi`**. Keduanya lolos uji *is-a* ("Pasien adalah User", "AhliGizi
adalah User"), sehingga inheritance memang relasi yang tepat digunakan di sini.

**Superclass `User`**
- Atribut public: `nama`
- Atribut protected: `_status_aktif`, dibaca subclass `Pasien` dan `AhliGizi`
  melalui method `info_dasar()`.
- Atribut private: `__password` - benar-benar rahasia/eksklusif milik `User`,
  hanya bisa diverifikasi lewat method `verifikasi_password()`, tidak bisa
  diakses langsung oleh subclass maupun dari luar class.
- Method: `verifikasi_password()`, `nonaktifkan_akun()`, `info_dasar()`

**Subclass `Pasien(User)`**
- Memanggil `super().__init__(nama, password)` di dalam `__init__`.
- Atribut spesifik/unik: `berat_badan`, `tinggi_badan`, `riwayat_penyakit`,
  `kategori`, serta `_riwayat_kesehatan` (komposisi).
- **Method overriding**: `info_dasar()` ditulis ulang untuk menampilkan
  kategori pasien sekaligus status akun, sambil mengakses atribut protected
  `_status_aktif` milik `User` secara langsung.

**Subclass `AhliGizi(User)`**
- Memanggil `super().__init__(nama, password)` di dalam `__init__`.
- Atribut spesifik/unik: `spesialisasi`, `nomor_str`, serta
  `_daftar_pasien_binaan` (agregasi).
- **Method overriding**: `info_dasar()` menampilkan spesialisasi ahli gizi;
  `nonaktifkan_akun()` juga ditulis ulang - selain
  menjalankan perilaku bawaan `User` lewat `super().nonaktifkan_akun()`,
  method ini juga melepas seluruh pasien binaan milik ahli gizi tersebut.

---

## Abstraksi (Abstract Base Class)

`LayananKlinik` mewarisi `ABC` dan menetapkan dua abstract method, yaitu
`validasi()` dan `proses()`. Method konkret `jalankan()` menjadi alur bersama:
memvalidasi layanan, lalu memanggil `proses()` jika valid.

`LayananRekomendasi` dan `LayananCatatan` adalah subclass yang mengimplementasikan
kedua abstract method. Keduanya memanggil `super().__init__(...)` dan memiliki
data layanan masing-masing. Program mencoba membuat objek `LayananKlinik` dalam
`try-except`; Python menolak instansiasi dengan `TypeError` karena abstract
method belum diimplementasikan.

## Polimorfisme

- **Via pewarisan:** `Pasien` dan `AhliGizi` meng-override `User.info_dasar()`
  dengan keluaran berbeda. Keduanya dipanggil melalui satu loop.
- **Duck typing:** `EmailNotifikasi` dan `SMSNotifikasi` tidak saling mewarisi,
  tetapi keduanya menyediakan `kirim(pesan)`. Fungsi `kirim_notifikasi()`
  memanggil method yang sama pada semua kanal.
- **Operator overloading:** `CatatanKesehatan.__str__()` mengatur representasi
  teks objek, sehingga catatan dapat langsung dicetak.

Perilaku tersebut dijalankan melalui method tiap objek, tanpa membedakan tipe
dengan `type()` atau rantai kondisi berdasarkan jenis objek.

## Prinsip SOLID — Nilai Plus

Prinsip **Open/Closed (OCP)** diterapkan pada `LayananKlinik`. Alur umum
`jalankan()` tidak perlu diubah ketika layanan baru ditambahkan; cukup buat
subclass yang mengimplementasikan `validasi()` dan `proses()`. Contohnya
`LayananRekomendasi` dan `LayananCatatan`.

## Bukti Output Post-test 3

Gambar berikut menampilkan cuplikan output program, termasuk bukti abstract
class tidak dapat diinstansiasi.

![Cuplikan output Post-test 3](output-posttest-3.svg)

```text
[13] Bukti Abstract Base Class
LayananKlinik tidak dapat dibuat: Can't instantiate abstract class LayananKlinik without an implementation for abstract methods 'proses', 'validasi'

[14] Polimorfisme via Pewarisan
Dimas | Kategori: reguler | Status: Aktif
dr. Sari | Spesialisasi: gizi_klinik | Status: Aktif

[15] Duck Typing Notifikasi
[EMAIL ke dimas@mail.com] Jadwal konsultasi gizi telah tersedia.
[SMS ke 081234567890] Jadwal konsultasi gizi telah tersedia.

[17] Operator Overloading (__str__) pada CatatanKesehatan
Catatan Dimas | 22-10-2026 | 72 kg
```

---

## Cara Menjalankan Program

```bash
python 2509106020-MuhammadZakiFahriansyah-PT-3.py
# atau (untuk pengguna Linux/macOS):
python3 2509106020-MuhammadZakiFahriansyah-PT-3.py
```
Program menjalankan demonstrasi objek, method, validasi setter, relasi, abstraksi,
dan polimorfisme secara otomatis di dalam blok `if __name__ == "__main__"`.

---

## Struktur Repositori

```
.
praktikum-pbo/
├── kelas/
└── post-test/
    └── post-test-1/
        ├── 2509106020-MuhammadZakiFahriansyah-PT-1.py   # Program utama
        └── README.md                                    # Dokumentasi post-test 1
    └── post-test-2/
        ├── 2509106020-MuhammadZakiFahriansyah-PT-2.py   # Program utama
        ├── README.md                                    # Dokumentasi post-test 2
    └── post-test-3/
        ├── 2509106020-MuhammadZakiFahriansyah-PT-3.py   # Program utama
        ├── diagram-posttest-3-terpadu.svg               # Class diagram
        ├── output-posttest-3.svg                        # Cuplikan output
        └── README.md                                    # Dokumentasi post-test 3
```
