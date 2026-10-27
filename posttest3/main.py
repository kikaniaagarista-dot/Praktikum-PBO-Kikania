# ==============================================================================
# TEMA: GLAMORA - Sistem Manajemen Pemesanan Jasa Make Up
# Memenuhi: UML, Abstraksi (ABC), Inheritance, Polimorfisme, & SOLID (DIP)
# ==============================================================================
from abc import ABC, abstractmethod


# 1. ABSTRAKSI & INHERITANCE 
class PaketMakeUp(ABC):
    """Superclass Abstract: Memiliki kontrak method yang wajib diimplementasikan."""
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self._harga = harga              # Protected: bisa diakses subclass
        self.__kode_internal = "INT-SECRET"  # Private: hanya untuk superclass

    @abstractmethod
    def hitung_total(self):
        """ Abstract method 1: Wajib diimplementasikan subclass."""
        pass

    @abstractmethod
    def deskripsi_paket(self):
        """ Abstract method 2: Wajib diimplementasikan subclass."""
        pass

    def info_rahasia(self):
        """ Concrete method: Dipakai bersama semua subclass."""
        return f"Kode Internal: {self.__kode_internal}"


class PaketWisuda(PaketMakeUp):
    """Subclass 1: Mengimplementasikan kontrak dari PaketMakeUp."""
    def __init__(self, kode, nama, harga, include_foto):
        super().__init__(kode, nama, harga)  # Memanggil konstruktor superclass
        self.include_foto = include_foto     # Atribut unik subclass

    def hitung_total(self):  
        # Akses langsung protected attribute _harga 
        return self._harga + 150000 if self.include_foto else self._harga

    def deskripsi_paket(self):
        return f"[Wisuda] {self.nama} - Include Foto: {'Ya' if self.include_foto else 'Tidak'}"


class PaketPengantin(PaketMakeUp):
    """Subclass 2: Mengimplementasikan kontrak dari PaketMakeUp."""
    def __init__(self, kode, nama, harga, jumlah_trial):
        super().__init__(kode, nama, harga)
        self.jumlah_trial = jumlah_trial

    def hitung_total(self):  # [Modul 6] Method Overriding
        return self._harga + (self.jumlah_trial * 200000)

    def deskripsi_paket(self):
        return f"[Pengantin] {self.nama} - Trial: {self.jumlah_trial}x"


# 2. UML: AGREGASI
class MUA:
    """Objek bagian yang bisa hidup mandiri (Agregasi)."""
    def __init__(self, nama, spesialisasi):
        self.nama = nama
        self.spesialisasi = spesialisasi

    def info(self):
        return f"{self.nama} ({self.spesialisasi})"


class Salon:
    """Memiliki daftar MUA. MUA dibuat di luar, lalu didaftarkan ke sini."""
    def __init__(self, nama_salon):
        self.nama_salon = nama_salon
        self._daftar_mua = []  # Agregasi

    def rekrut_mua(self, mua):
        if isinstance(mua, MUA):
            self._daftar_mua.append(mua)

    def tampilkan_tim(self):
        print(f"Tim MUA {self.nama_salon}:")
        for mua in self._daftar_mua:
            print(f" - {mua.info()}")



# 3. UML: KOMPOSISI, ASOSIASI & OPERATOR OVERLOADING 
class CatatanTransaksi:
    """Objek bagian yang TIDAK bisa hidup tanpa induknya (Komposisi)."""
    def __init__(self, deskripsi, nominal):
        self.deskripsi = deskripsi
        self.nominal = nominal

    def __str__(self):
        return f"{self.deskripsi}: Rp {self.nominal:,}"


class Pemesanan:
    """
    Asosiasi: Menerima MUA & Pelanggan via parameter.
    Komposisi: Membuat CatatanTransaksi di dalam.
    Operator Overloading: __str__ dan __lt__
    """
    def __init__(self, id_pesanan, pelanggan, mua, paket):
        self.id_pesanan = id_pesanan
        self.pelanggan = pelanggan  # Asosiasi
        self.mua = mua              # Asosiasi
        self.paket = paket
        self._riwayat = []          # Komposisi
        
        self._tambah_catatan("Pemesanan Dibuat", paket.hitung_total())

    def _tambah_catatan(self, deskripsi, nominal):
        catatan = CatatanTransaksi(deskripsi, nominal) 
        self._riwayat.append(catatan)

    def __str__(self):  
        return f"Pesanan #{self.id_pesanan} | {self.paket.nama} | Total: Rp {self.paket.hitung_total():,}"

    def __lt__(self, other):  
        return self.paket.hitung_total() < other.paket.hitung_total()

    def cetak_struk(self):
        print(f"\n--- STRUK #{self.id_pesanan} ---")
        print(f"Pelanggan: {self.pelanggan} | MUA: {self.mua.nama}")
        print(f"Paket: {self.paket.deskripsi_paket()}")
        print(f"Total Harga: Rp {self.paket.hitung_total():,}")
        print("Riwayat Transaksi:")
        for item in self._riwayat:
            print(f" - {item}")
        print("-" * 30)



# 4. DUCK TYPING & SOLID (DIP) 
class NotifikasiEmail:
    """Duck Typing: Tidak ada hubungan pewarisan, tapi punya method 'kirim'."""
    def kirim(self, pesan):
        print(f"  [EMAIL] Terkirim: {pesan}")

class NotifikasiWhatsApp:
    """Duck Typing: Tidak ada hubungan pewarisan, tapi punya method 'kirim'."""
    def kirim(self, pesan):
        print(f"  [WHATSAPP] Terkirim: {pesan}")

def proses_notifikasi(notifier, pesan):
    """
    [Modul 7] SOLID - Dependency Inversion Principle (DIP).
    Fungsi bergantung pada abstraksi (objek dengan method 'kirim'), 
    bukan pada kelas konkret.
    """
    notifier.kirim(pesan)



# PENGUJIAN PROGRAM (MAIN CODE)
if __name__ == "__main__":
    print("=" * 60)
    print("PENGUJIAN POSTTEST FINAL: GLAMORA")
    print("=" * 60)

    # 1. BUKTI ABSTRAKSI 
    print("\n[1] BUKTI ABSTRAKSI (Abstract Class)...")
    print("Mencoba instantiate PaketMakeUp (abstract class)...")
    try:
        paket_gagal = PaketMakeUp("XX", "Gagal", 0)
    except TypeError as e:
        print(f"✓ Berhasil diblokir: {e}")

    # 2. UJI AGREGASI 
    print("\n[2] UJI AGREGASI (Salon & MUA)...")
    salon = Salon("GLAMORA Beauty Studio")
    mua1 = MUA("Kak Rina", "Wedding Specialist")
    mua2 = MUA("Kak Dinda", "Party & Wisuda")
    salon.rekrut_mua(mua1)
    salon.rekrut_mua(mua2)
    salon.tampilkan_tim()

    # 3. UJI POLIMORFISME VIA PEWARISAN 
    print("\n[3] UJI POLIMORFISME VIA PEWARISAN (Loop)...")
    paket_wisuda = PaketWisuda("PK01", "Wisuda Ceria", 500000, include_foto=True)
    paket_nikah = PaketPengantin("PK02", "Royal Wedding", 2000000, jumlah_trial=2)
    paket_biasa = PaketWisuda("PK03", "Wisuda Simple", 300000, include_foto=False)
    
    daftar_paket = [paket_wisuda, paket_nikah, paket_biasa]
    for p in daftar_paket:
        print(f" -> {p.deskripsi_paket()} | Total: Rp {p.hitung_total():,}")

    # 4. UJI ASOSIASI, KOMPOSISI & OPERATOR OVERLOADING 
    print("\n[4] UJI ASOSIASI, KOMPOSISI & OPERATOR OVERLOADING...")
    pesanan1 = Pemesanan("ORD-001", "Kikania", mua1, paket_nikah)
    pesanan2 = Pemesanan("ORD-002", "Dewi", mua1, paket_wisuda)
    
    print("Cetak Objek (menggunakan __str__):")
    print(pesanan1)
    print(pesanan2)
    
    print(f"\nUji __lt__ (Pesanan 2 lebih murah dari Pesanan 1?): {pesanan2 < pesanan1}")
    pesanan1.cetak_struk()

    # 5. UJI DUCK TYPING & SOLID (DIP) 
    print("\n[5] UJI DUCK TYPING & SOLID (Dependency Inversion)...")
    notifier_email = NotifikasiEmail()
    notifier_wa = NotifikasiWhatsApp()
    
    daftar_notifier = [notifier_email, notifier_wa]
    for notifier in daftar_notifier:
        proses_notifikasi(notifier, "Pemesanan ORD-001 berhasil dibuat!")

    print("\n" + "=" * 60)
    print("PENGUJIAN SELESAI!")
    print("=" * 60)
