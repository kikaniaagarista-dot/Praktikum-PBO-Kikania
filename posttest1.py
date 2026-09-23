
# TEMA: GLAMORA - Sistem Manajemen Pemesanan Jasa Make Up

# PELANGGAN 
class Pelanggan:

    nama_salon = "GLAMORA Beauty Studio"
    total_pelanggan = 0

    def __init__(self, nama, email, nomor_telepon):

        self.nama = nama
        self.email = email

        self.__nomor_telepon = nomor_telepon
        
        Pelanggan.total_pelanggan += 1

    @property
    def nomor_telepon(self):
        """Getter - dipanggil seperti atribut biasa"""
        return self.__nomor_telepon

    @nomor_telepon.setter
    def nomor_telepon(self, nomor_baru):
        """Setter - dijalankan otomatis saat ada assignment, dilengkapi validasi"""
        if not str(nomor_baru).isdigit() or len(str(nomor_baru)) < 10:
            raise ValueError("Error: Nomor telepon harus berupa angka dan minimal 10 digit!")
        self.__nomor_telepon = nomor_baru

    def tampilkan_info(self):
        print(f"Nama: {self.nama} | Email: {self.email} | Telp: {self.__nomor_telepon}")

    @classmethod
    def ubah_nama_salon(cls, nama_baru):
        cls.nama_salon = nama_baru
        print(f"[Class Method] Nama salon berhasil diubah menjadi: {cls.nama_salon}")

    @staticmethod
    def validasi_format_email(email):
        return "@" in email and "." in email


#PAKET MAKE UP 
class PaketMakeUp:

    mata_uang = "IDR"
    total_paket = 0

    def __init__(self, kode_paket, nama_paket, harga):

        self.kode_paket = kode_paket
        self.nama_paket = nama_paket
        
        self.__harga = harga
        
        PaketMakeUp.total_paket += 1

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, harga_baru):
        if harga_baru <= 0:
            raise ValueError("Error: Harga paket tidak boleh nol atau negatif!")
        self.__harga = harga_baru

    def detail_paket(self):
        print(f"Kode: {self.kode_paket} | Paket: {self.nama_paket} | Harga: {PaketMakeUp.mata_uang} {self.__harga:,}")

    @classmethod
    def buat_dari_dict(cls, data):
        return cls(data["kode"], data["nama"], data["harga"])

    @staticmethod
    def cek_apakah_diskon_valid(persentase):
        return 0 <= persentase <= 100



#PEMESANAN 

class Pemesanan:
    # Atribut Kelas
    total_pemesanan = 0
    daftar_status_valid = ["Belum Lunas", "Lunas", "Dibatalkan"]

    def __init__(self, pelanggan, paket, tanggal_acara):
        # Atribut Instance Public (Berinteraksi dengan objek class lain)
        self.pelanggan = pelanggan
        self.paket = paket
        self.tanggal_acara = tanggal_acara

        self.__status = "Belum Lunas"
        
        Pemesanan.total_pemesanan += 1

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status_baru):
        if status_baru not in Pemesanan.daftar_status_valid:
            raise ValueError(f"Error: Status harus salah satu dari {Pemesanan.daftar_status_valid}!")
        self.__status = status_baru


    def cetak_struk(self):
        print(f"\n--- STRUK PEMESANAN #{Pemesanan.total_pemesanan} ---")
        print(f"Salon: {Pelanggan.nama_salon}")
        self.pelanggan.tampilkan_info()
        self.paket.detail_paket()
        print(f"Tanggal Acara: {self.tanggal_acara}")
        print(f"Status Pembayaran: {self.__status}")
        print("-" * 40)

    # Class Method
    @classmethod
    def reset_total_pemesanan(cls):
        cls.total_pemesanan = 0
        print("[Class Method] Total pemesanan telah direset menjadi 0.")

    # Static Method
    @staticmethod
    def hitung_estimasi_biaya_transport(jarak_km):
        return jarak_km * 5000

# ==============================================================================
if __name__ == "__main__":
    print("=" * 50)
    print("PENGUJIAN PROGRAM GLAMORA (OOP)")
    print("=" * 50)

    # 1. MEMBUAT OBJEK (Minimal 2 objek per class)
    print("\n[1] MEMBUAT OBJEK...")
    pelanggan1 = Pelanggan("Kikania Agarista", "kikania@email.com", "081234567890")
    pelanggan2 = Pelanggan("Dewi Sartika", "dewi@email.com", "089876543210")

    paket1 = PaketMakeUp("PK01", "Makeup Wisuda", 500000)
    # Membuat objek menggunakan Class Method (Factory dari dictionary)
    data_paket2 = {"kode": "PK02", "nama": "Makeup Pesta", "harga": 750000}
    paket2 = PaketMakeUp.buat_dari_dict(data_paket2)

    pesanan1 = Pemesanan(pelanggan1, paket1, "20 Desember 2024")
    pesanan2 = Pemesanan(pelanggan2, paket2, "25 Desember 2024")
    print("✓ Berhasil membuat 2 objek untuk tiap class.")

    # 2. MEMANGGIL INSTANCE METHOD
    print("\n[2] MEMANGGIL INSTANCE METHOD...")
    pesanan1.cetak_struk()

    # 3. MEMANGGIL CLASS METHOD
    print("\n[3] MEMANGGIL CLASS METHOD...")
    Pelanggan.ubah_nama_salon("GLAMORA Premium Studio")
    Pemesanan.reset_total_pemesanan() 

    # 4. MEMANGGIL STATIC METHOD
    print("\n[4] MEMANGGIL STATIC METHOD...")
    print(f"Email 'kikania@email.com' valid? {Pelanggan.validasi_format_email('kikania@email.com')}")
    print(f"Diskon 15% valid? {PaketMakeUp.cek_apakah_diskon_valid(15)}")
    print(f"Biaya transport 10km: IDR {Pemesanan.hitung_estimasi_biaya_transport(10):,}")

    # 5. UJI SETTER DATA VALID
    print("\n[5] UJI SETTER DENGAN DATA VALID...")
    try:
        pelanggan1.nomor_telepon = "081112223334"
        print(f"✓ Update telepon pelanggan1 berhasil: {pelanggan1.nomor_telepon}")
        
        paket1.harga = 600000
        print(f"✓ Update harga paket1 berhasil: IDR {paket1.harga:,}")
        
        pesanan1.status = "Lunas"
        print(f"✓ Update status pesanan1 berhasil: {pesanan1.status}")
    except ValueError as e:
        print(e)

    # 6. UJI SETTER DATA INVALID (VALIDASI BERJALAN)
    print("\n[6] UJI SETTER DENGAN DATA INVALID (HARUS DITOLAK)...")
    
    try:
        pelanggan2.nomor_telepon = "12345" 
    except ValueError as e:
        print(f"✗ Ditolak (Telepon): {e}")

    try:
        paket2.harga = -100000 
    except ValueError as e:
        print(f"✗ Ditolak (Harga): {e}")

    try:
        pesanan2.status = "Menunggu Konfirmasi" 
    except ValueError as e:
        print(f"✗ Ditolak (Status): {e}")

    print("\n" + "=" * 50)
    print("PENGUJIAN SELESAI!")
    print("=" * 50)