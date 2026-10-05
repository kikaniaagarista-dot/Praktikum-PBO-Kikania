# =======================================================
# TEMA: GLAMORA - Sistem Manajemen Pemesanan Jasa Make Up 
# =======================================================

class MUA:
    """Class MUA (Make Up Artist) yang akan di-agregasi oleh Salon."""
    def __init__(self, nama, spesialisasi):
        self.nama = nama
        self.spesialisasi = spesialisasi

    def info(self):
        return f"{self.nama} ({self.spesialisasi})"

class Salon:
    """Class Salon yang memiliki daftar MUA (Agregasi)."""
    def __init__(self, nama_salon):
        self.nama_salon = nama_salon
        self._daftar_mua = []  

    def rekrut_mua(self, mua):
        """MUA dibuat di luar, lalu didaftarkan ke Salon."""
        if isinstance(mua, MUA):
            self._daftar_mua.append(mua)
            print(f"[+] {mua.nama} bergabung dengan {self.nama_salon}")

    def tampilkan_tim(self):
        print(f"\nTim MUA {self.nama_salon}:")
        for mua in self._daftar_mua:
            print(f" - {mua.info()}")


class PaketMakeUp:
    """[SYARAT] Superclass (Parent Class)."""
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self._harga = harga          
        self.__kode_internal = "INT-SECRET" 

    def hitung_total(self):
        """Method yang akan di-override oleh subclass."""
        return self._harga

    def info_rahasia(self):
        """Hanya bisa mengakses atribut private di dalam superclass."""
        return f"Kode Internal: {self.__kode_internal}"


class PaketWisuda(PaketMakeUp):
    """[SYARAT] Subclass 1 (Child Class)."""
    def __init__(self, kode, nama, harga, include_foto):
        super().__init__(kode, nama, harga)
        self.include_foto = include_foto  

    def hitung_total(self):
        total_dasar = super().hitung_total()  
        if self.include_foto:
            total_dasar += 150000  
        return total_dasar


class PaketPengantin(PaketMakeUp):
    """[SYARAT] Subclass 2 (Child Class)."""
    def __init__(self, kode, nama, harga, jumlah_trial):
        super().__init__(kode, nama, harga)
        self.jumlah_trial = jumlah_trial  

    def hitung_total(self):
        total_dasar = super().hitung_total()
        return total_dasar + (self.jumlah_trial * 200000)


class CatatanTransaksi:
    """Objek bagian untuk Komposisi."""
    def __init__(self, deskripsi, nominal):
        self.deskripsi = deskripsi
        self.nominal = nominal

    def __str__(self):
        return f"{self.deskripsi}: Rp {self.nominal:,}"


class Pemesanan:
    """
    [SYARAT] Asosiasi: Menggunakan objek Pelanggan dan MUA (diterima via parameter).
    [SYARAT] Komposisi: Terdiri dari objek CatatanTransaksi (dibuat di dalam).
    """
    def __init__(self, id_pesanan, pelanggan, mua, paket):
        self.id_pesanan = id_pesanan
        self.pelanggan = pelanggan  
        self.mua = mua             
        self.paket = paket
        self._riwayat = []          
        
        self._tambah_catatan("Pemesanan Dibuat", paket.hitung_total())

    def _tambah_catatan(self, deskripsi, nominal):
        """[SYARAT] Komposisi: Objek bagian dibuat DI DALAM objek induk."""
        catatan = CatatanTransaksi(deskripsi, nominal)
        self._riwayat.append(catatan)

    def cetak_struk(self):
        print(f"\n--- STRUK #{self.id_pesanan} ---")
        print(f"Pelanggan: {self.pelanggan}")
        print(f"MUA Penanggung Jawab: {self.mua.nama}")
        print(f"Paket: {self.paket.nama}")
        print(f"Total Harga: Rp {self.paket.hitung_total():,}")
        print("Riwayat Transaksi:")
        for item in self._riwayat:
            print(f" - {item}")
        print("-" * 30)


# PENGUJIAN PROGRAM (MAIN CODE)
if __name__ == "__main__":
    print("=" * 50)
    print("PENGUJIAN POSTTEST LANJUTAN: GLAMORA")
    print("=" * 50)

    # 1. UJI AGREGASI (Salon & MUA)
    print("\n[1] UJI AGREGASI...")
    salon = Salon("GLAMORA Beauty Studio")
    mua1 = MUA("Kak Rina", "Wedding Specialist")
    mua2 = MUA("Kak Dinda", "Party & Wisuda")
    
    salon.rekrut_mua(mua1)
    salon.rekrut_mua(mua2)
    salon.tampilkan_tim()

    # 2. UJI INHERITANCE & OVERRIDING
    print("\n[2] UJI INHERITANCE & OVERRIDING...")
    # Superclass
    paket_biasa = PaketMakeUp("PK00", "Makeup Simple", 300000)
    # Subclass 1
    paket_wisuda = PaketWisuda("PK01", "Wisuda Ceria", 500000, include_foto=True)
    # Subclass 2
    paket_nikah = PaketPengantin("PK02", "Royal Wedding", 2000000, jumlah_trial=2)

    print(f"Total Paket Biasa: Rp {paket_biasa.hitung_total():,}")
    print(f"Total Paket Wisuda (inc. Foto): Rp {paket_wisuda.hitung_total():,}")
    print(f"Total Paket Nikah (inc. 2 Trial): Rp {paket_nikah.hitung_total():,}")

    # Uji Protected vs Private
    print(f"\nAkses Protected (_harga) di Wisuda: Rp {paket_wisuda._harga:,}")
    print(f"Akses Private di Superclass: {paket_biasa.info_rahasia()}")

    # 3. UJI ASOSIASI & KOMPOSISI
    print("\n[3] UJI ASOSIASI & KOMPOSISI...")
    pelanggan = "Kikania Agarista"
    
    pesanan1 = Pemesanan("ORD-001", pelanggan, mua1, paket_nikah)
    pesanan1.cetak_struk()

    print("\n" + "=" * 50)
    print("PENGUJIAN SELESAI!")
    print("=" * 50)
