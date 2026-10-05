class Pengguna:
    """Superclass untuk semua pengguna sistem."""
    def __init__(self, id_pengguna, nama, password):
        # Protected attribute (bisa diakses subclass)
        self._id_pengguna = id_pengguna
        self.nama = nama
        # Private attribute (hanya untuk superclass)
        self.__password = password

    def verifikasi_password(self, password_input):
        return password_input == self.__password

    def tampilkan_profil(self):
        """Method ini wajib di-override oleh subclass"""
        pass


class Pasien(Pengguna):
    # Atribut Kelas
    nama_klinik = "Klinik Gizi Sehat Samarinda"
    total_pasien = 0
    kategori_valid = ["reguler", "atlet", "kondisi_medis"]

    def __init__(self, id_pengguna, nama, password, berat_badan, tinggi_badan,
                 riwayat_penyakit="Tidak ada", kategori="reguler"):
        # 1. Menggunakan super() memanggil konstruktor parent
        super().__init__(id_pengguna, nama, password)
        
        # 2. Atribut unik subclass & Protected/Private
        self.kategori = kategori if kategori in Pasien.kategori_valid else "reguler"
        self._riwayat_penyakit = riwayat_penyakit # Protected
        self.__berat_badan = berat_badan          # Private
        self.__tinggi_badan = tinggi_badan        # Private

        # 3. Wadah untuk Agregasi & Komposisi
        self.menu_diet_harian = []    # Untuk menampung objek MenuDiet (Agregasi)
        self.riwayat_catatan = []     # Untuk menampung objek CatatanKesehatan (Komposisi)

        Pasien.total_pasien += 1

    # Getter & Setter
    @property
    def berat_badan(self):
        return self.__berat_badan

    @berat_badan.setter
    def berat_badan(self, nilai_baru):
        if nilai_baru <= 0:
            print(f"[Gagal] Berat badan {self.nama} tidak valid: harus lebih dari 0.")
        else:
            self.__berat_badan = nilai_baru

    @property
    def tinggi_badan(self):
        return self.__tinggi_badan

    @tinggi_badan.setter
    def tinggi_badan(self, nilai_baru):
        if nilai_baru <= 0:
            print(f"[Gagal] Tinggi badan {self.nama} tidak valid: harus lebih dari 0.")
        else:
            self.__tinggi_badan = nilai_baru

    @property
    def riwayat_penyakit(self):
        return self._riwayat_penyakit

    @riwayat_penyakit.setter
    def riwayat_penyakit(self, nilai_baru):
        if not nilai_baru or nilai_baru.strip() == "":
            print(f"[Gagal] Riwayat penyakit {self.nama} tidak boleh kosong.")
        else:
            self._riwayat_penyakit = nilai_baru

    # Instance Method
    def hitung_kebutuhan_kalori(self):
        kalori_dasar = 24 * self.__berat_badan

        if self.kategori == "atlet":
            faktor = 1.7
        elif self.kategori == "kondisi_medis":
            faktor = 1.2
        else:
            faktor = 1.375

        kebutuhan_kalori = kalori_dasar * faktor
        print(f"Kebutuhan kalori {self.nama} ({self.kategori}): "
              f"{kebutuhan_kalori:.0f} kkal/hari")
        return kebutuhan_kalori

    # Relasi Agregasi (Objek dibuat di luar, dimasukkan ke sini)
    def tambah_menu_harian(self, menu):
        self.menu_diet_harian.append(menu)
        print(f"Menu {menu.nama_menu} ditambahkan ke daftar {self.nama}.")

    # Relasi Komposisi (Objek dideklarasikan eksklusif di dalam kelas ini)
    def catat_kesehatan(self, tanggal, catatan_tambahan="-"):
        catatan = CatatanKesehatan(self, tanggal, self.__berat_badan, catatan_tambahan)
        self.riwayat_catatan.append(catatan)
        print(f"Catatan kesehatan {self.nama} pada {tanggal} berhasil dibuat.")

    # 4. Method Overriding
    def tampilkan_profil(self):
        print(f"--- Profil Pasien: {self.nama} ({self._id_pengguna}) ---")
        print(f"Kategori     : {self.kategori}")
        print(f"Berat Badan  : {self.__berat_badan} kg")
        print(f"Tinggi Badan : {self.__tinggi_badan} cm")
        print(f"Riwayat      : {self._riwayat_penyakit}")
        print(f"Klinik       : {Pasien.nama_klinik}")

    # Class Method
    @classmethod
    def dari_dict(cls, data):
        return cls(
            data["id_pasien"], data["nama"], data["password"],
            data["berat_badan"], data["tinggi_badan"],
            data.get("riwayat_penyakit", "Tidak ada"),
            data.get("kategori", "reguler"),
        )

    @classmethod
    def ganti_nama_klinik(cls, nama_baru):
        cls.nama_klinik = nama_baru

    # Static Method
    @staticmethod
    def validasi_kategori(kategori):
        return kategori in Pasien.kategori_valid


class AhliGizi(Pengguna):
    # Atribut Kelas
    total_ahli_gizi = 0
    spesialisasi_valid = ["gizi_klinik", "gizi_olahraga", "gizi_anak"]

    def __init__(self, id_pengguna, nama, password, spesialisasi, nomor_str):
        # 1. Menggunakan super() memanggil konstruktor parent
        super().__init__(id_pengguna, nama, password)
        
        # 2. Atribut unik & Protected
        self.spesialisasi = (spesialisasi if spesialisasi in AhliGizi.spesialisasi_valid
                              else "gizi_klinik")
        self._nomor_str = nomor_str

        AhliGizi.total_ahli_gizi += 1

    # Getter & Setter
    @property
    def nomor_str(self):
        return self._nomor_str

    @nomor_str.setter
    def nomor_str(self, nilai_baru):
        if not nilai_baru or len(nilai_baru.strip()) < 6:
            print(f"[Gagal] Nomor STR {self.nama} tidak valid: minimal 6 karakter.")
        else:
            self._nomor_str = nilai_baru

    # 4. Method Overriding
    def tampilkan_profil(self):
        print(f"--- Profil Ahli Gizi: {self.nama} ({self._id_pengguna}) ---")
        print(f"Spesialisasi : {self.spesialisasi}")
        print(f"Nomor STR    : {self._nomor_str}")

    # Instance Method (Relasi Asosiasi: Memakai objek Pasien & MenuDiet sementara)
    def buat_rekomendasi(self, pasien, menu):
        kebutuhan = pasien.hitung_kebutuhan_kalori()
        print(f"--- Rekomendasi dari {self.nama} ({self.spesialisasi}) ---")
        if menu.kalori <= kebutuhan:
            print(f"Menu '{menu.nama_menu}' ({menu.kalori} kkal) SESUAI "
                  f"untuk {pasien.nama}.")
        else:
            print(f"Menu '{menu.nama_menu}' ({menu.kalori} kkal) MELEBIHI "
                  f"kebutuhan kalori {pasien.nama}.")

    # Class Method
    @classmethod
    def dari_dict(cls, data):
        return cls(
            data["id_ahli"], data["nama"], data["password"],
            data["spesialisasi"], data["nomor_str"],
        )

    # Static Method
    @staticmethod
    def validasi_spesialisasi(spesialisasi):
        return spesialisasi in AhliGizi.spesialisasi_valid


class MenuDiet:
    # Atribut Kelas
    total_menu = 0
    kategori_menu_valid = ["sarapan", "makan_siang", "makan_malam", "camilan"]

    def __init__(self, nama_menu, daftar_bahan, kalori, kategori_menu="makan_siang"):
        self.nama_menu = nama_menu
        self.daftar_bahan = daftar_bahan
        self.kategori_menu = (kategori_menu if kategori_menu in
                               MenuDiet.kategori_menu_valid else "makan_siang")
        self.__kalori = kalori

        MenuDiet.total_menu += 1

    # Getter & Setter
    @property
    def kalori(self):
        return self.__kalori

    @kalori.setter
    def kalori(self, nilai_baru):
        if not isinstance(nilai_baru, (int, float)) or nilai_baru <= 0:
            print(f"[Gagal] Kalori menu '{self.nama_menu}' tidak valid: harus angka > 0.")
        else:
            self.__kalori = nilai_baru

    # Instance Method
    def tampilkan_menu(self):
        print(f"--- Menu: {self.nama_menu} ({self.kategori_menu}) ---")
        print(f"Bahan  : {', '.join(self.daftar_bahan)}")
        print(f"Kalori : {self.__kalori} kkal")

    # Class Method
    @classmethod
    def dari_dict(cls, data):
        return cls(
            data["nama_menu"], data["daftar_bahan"],
            data["kalori"], data.get("kategori_menu", "makan_siang"),
        )

    # Static Method
    @staticmethod
    def validasi_kalori(nilai):
        return isinstance(nilai, (int, float)) and nilai > 0


class CatatanKesehatan:
    # Atribut Kelas
    total_catatan = 0
    format_tanggal = "DD-MM-YYYY"

    def __init__(self, pasien, tanggal, berat_badan_tercatat, catatan_tambahan="-"):
        self.pasien = pasien
        self.tanggal = tanggal
        self.catatan_tambahan = catatan_tambahan
        self.__berat_badan_tercatat = berat_badan_tercatat

        CatatanKesehatan.total_catatan += 1

    # Getter & Setter
    @property
    def berat_badan_tercatat(self):
        return self.__berat_badan_tercatat

    @berat_badan_tercatat.setter
    def berat_badan_tercatat(self, nilai_baru):
        if nilai_baru <= 0:
            print("[Gagal] Berat badan tercatat tidak valid: harus lebih dari 0.")
        else:
            self.__berat_badan_tercatat = nilai_baru

    # Instance Method
    def tampilkan_catatan(self):
        print(f"--- Catatan Kesehatan: {self.pasien.nama} ({self.tanggal}) ---")
        print(f"Berat Badan Tercatat : {self.__berat_badan_tercatat} kg")
        print(f"Catatan Tambahan     : {self.catatan_tambahan}")

    # Class Method
    @classmethod
    def rekap_total(cls):
        print(f"Total catatan kesehatan tercatat: {cls.total_catatan}")
        return cls.total_catatan

    # Static Method
    @staticmethod
    def validasi_format_tanggal(tanggal_str):
        bagian = tanggal_str.split("-")
        return len(bagian) == 3 and all(b.isdigit() for b in bagian)


if __name__ == "__main__":
    print("=" * 60)
    print("SISTEM INFORMASI GIZI - DEMONSTRASI PROGRAM")
    print("=" * 60)
    
    print("\n[1] Membuat objek Pasien & Uji Overriding")
    pasien1 = Pasien("P001", "Dimas", "pass123", 70, 170, "Tidak ada", "reguler")
    data_pasien2 = {
        "id_pasien": "P002", "nama": "Rina", "password": "rina456",
        "berat_badan": 55, "tinggi_badan": 160,
        "riwayat_penyakit": "Diabetes", "kategori": "kondisi_medis",
    }
    pasien2 = Pasien.dari_dict(data_pasien2)
    pasien1.tampilkan_profil() # Ter-override
    pasien2.tampilkan_profil()

    print("\n[2] Membuat objek AhliGizi")
    ahli1 = AhliGizi("A001", "dr. Sari", "sari789", "gizi_klinik", "STR12345")
    ahli1.tampilkan_profil() # Ter-override

    print("\n[3] Membuat objek MenuDiet")
    menu1 = MenuDiet("Nasi Merah + Ayam Panggang",
                      ["nasi merah", "ayam", "brokoli"], 550, "makan_siang")
    menu2 = MenuDiet("Oatmeal Buah", ["oatmeal", "pisang", "madu"], 300, "sarapan")

    print("\n[4] Uji Relasi Asosiasi (buat_rekomendasi)")
    pasien1.hitung_kebutuhan_kalori()
    ahli1.buat_rekomendasi(pasien1, menu1)

    print("\n[5] Uji Relasi Agregasi (Pasien & MenuDiet)")
    pasien1.tambah_menu_harian(menu1)
    pasien1.tambah_menu_harian(menu2)
    
    print("\n[6] Uji Relasi Komposisi (Pasien & CatatanKesehatan)")
    pasien1.catat_kesehatan("01-09-2026", "Kondisi stabil")
    pasien1.riwayat_catatan[0].tampilkan_catatan()

    print("\n[7] Uji Class & Static Method")
    Pasien.ganti_nama_klinik("Klinik Gizi Sehat Cabang Samarinda")
    print(f"Total pasien terdaftar    : {Pasien.total_pasien}")
    print(f"Validasi kategori 'atlet' : {Pasien.validasi_kategori('atlet')}")

    print("\n[8] Uji Setter (Encapsulation)")
    pasien1.berat_badan = 72
    print(f"Berat badan {pasien1.nama} setelah diubah: {pasien1.berat_badan} kg")
    pasien1.berat_badan = -5

    print("\n[9] Uji Inheritance (Akses Method Superclass - Private Data)")
    print(f"Password 'pass123' untuk {pasien1.nama} benar? "
          f"{pasien1.verifikasi_password('pass123')}")

    print("\n" + "=" * 60)
    print("DEMONSTRASI SELESAI")
    print("=" * 60)