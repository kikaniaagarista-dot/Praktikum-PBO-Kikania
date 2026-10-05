# Laporan Posttest PBO Lanjutan: GLAMORA

**Nama**: Kikania Agarista  
**NIM**: 2509106086  
**Tema**: GLAMORA - Sistem Manajemen Pemesanan Jasa Make Up  

---

## 1. Implementasi Relasi UML
Program ini menerapkan tiga hubungan antar kelas :

### A. Agregasi (Aggregation) - "Memiliki"
*   **Kelas Terlibat**: `Salon` dan `MUA` (Make Up Artist).
*   **Penjelasan**: `Salon` memiliki daftar `MUA` yang disimpan dalam atribut `_daftar_mua`. Objek `MUA` dibuat di luar kelas `Salon` dan hanya direferensikan ke dalamnya. Jika objek `Salon` dihapus, objek `MUA` tetap ada (masih bisa bekerja di tempat lain).

### B. Asosiasi (Association) - "Menggunakan"
*   **Kelas Terlibat**: `Pemesanan`, `Pelanggan` (String/Objek), dan `MUA`.
*   **Penjelasan**: Kelas `Pemesanan` menggunakan objek `MUA` dan data `Pelanggan` yang diterima melalui parameter constructor (`__init__`). Tidak ada kepemilikan permanen; `MUA` hanya "dipinjam" untuk menangani satu pesanan.

### C. Komposisi (Composition) - "Terdiri Dari"
*   **Kelas Terlibat**: `Pemesanan` dan `CatatanTransaksi`.
*   **Penjelasan**: `Pemesanan` terdiri dari kumpulan `CatatanTransaksi`. Objek `CatatanTransaksi` dibuat secara eksklusif di dalam method `_tambah_catatan()` milik `Pemesanan`. Jika objek `Pemesanan` dihapus, riwayat `CatatanTransaksi` ikut musnah.

---

## 2. Implementasi Inheritance (Pewarisan)
Program ini menerapkan pewarisan sesuai materi:

### A. Struktur Superclass & Subclass
*   **Superclass**: `PaketMakeUp` (Berisi atribut dan method dasar semua paket).
*   **Subclass**: `PaketWisuda` dan `PaketPengantin` (Mewarisi `PaketMakeUp`).

### B. Penggunaan `super()`
Kedua subclass memanggil konstruktor induk menggunakan `super().__init__(kode, nama, harga)` untuk menginisialisasi atribut dasar, lalu menambahkan atribut spesifiknya sendiri.

### C. Atribut Tambahan (Spesifik)
*   `PaketWisuda` memiliki atribut unik: `include_foto` (Boolean).
*   `PaketPengantin` memiliki atribut unik: `jumlah_trial` (Integer).

### D. Method Overriding
Method `hitung_total()` dari superclass di-override pada kedua subclass:
*   Di `PaketWisuda`: Menambahkan biaya jika `include_foto` bernilai True.
*   Di `PaketPengantin`: Menambahkan biaya berdasarkan `jumlah_trial * 200000`.

### E. Tingkat Akses (Protected & Private)
*   **Protected (`_harga`)**: Digunakan di superclass `PaketMakeUp` agar bisa diakses dan dimanipulasi langsung oleh subclass saat melakukan overriding method `hitung_total()`.
*   **Private (`__kode_internal`)**: Digunakan di superclass untuk data rahasia. Subclass tidak bisa mengaksesnya secara langsung (terkena *name mangling*), membuktikan enkapsulasi yang ketat pada data eksklusif induk.

---

## 3. Cara Menjalankan Program
1. Pastikan Python 3.x sudah terinstal.
2. Jalankan file melalui terminal:
   ```bash
   python main.py
