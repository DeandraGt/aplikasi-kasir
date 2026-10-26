# PRD — Simple Cashier (Minggu 01)

> Product Requirements Document untuk Minggu 01 — Foundation,
> Pemrograman Komputer 2 (BD322), Universitas Panca Bhakti Pontianak.
> Penomoran bagian mengikuti rujukan modul: §7 (WEEK 01), §11 (data model),
> §16 (rubrik), §17 (baseline README).

## 1. Ringkasan

Simple Cashier adalah aplikasi kasir sederhana berbasis Python. Minggu 01 menyiapkan
fondasinya: repository Git, program pertama yang berjalan, dan data produk
yang dimodelkan sebagai dictionary.

## 2. Tujuan Minggu 01

- Repository tersedia, dapat dijalankan dengan satu perintah, dan memiliki riwayat commit.
- Program mencetak daftar produk dan satu perhitungan subtotal.
- Mahasiswa memahami mengapa dictionary dipakai lebih dulu dan apa keterbatasannya.

## 3. Pengguna

Kasir toko kecil yang mencatat penjualan produk.

## 4. Ruang Lingkup Minggu 01

**Termasuk:** dictionary, list, perulangan `for`, perhitungan subtotal, Git dasar
(init, commit, branch, push, PR, tag).

**Tidak termasuk:** `class`, folder `models/`, module terpisah, fungsi untuk subtotal.
Dictionary dipakai dengan sengaja agar keterbatasannya terasa.

## 5. Kebutuhan Fungsional

1. Program menampilkan satu produk pertama (nama).
2. Program menampilkan daftar produk: kode, nama, harga, stok.
3. Program menghitung subtotal = harga × quantity.
4. Program mencatat tiga keterbatasan dictionary di bagian akhir keluaran.

## 6. Kebutuhan Non-Fungsional

- Dijalankan dengan `python3 main.py` tanpa traceback.
- Berkas hasil dan berkas rahasia tidak ikut ter-commit (`.gitignore`).
- Riwayat commit bermakna.

## 7. Rencana Mingguan

### WEEK 01 — Foundation

**Spesifikasi.**
- Satu produk = satu dictionary dengan key `code`, `name`, `price`, `stock`.
- Banyak produk = list berisi dictionary.
- Subtotal dihitung langsung di `main.py` (`price * quantity`) dan diulang bila dibutuhkan.
- Bagian akhir program mencatat tiga keterbatasan dictionary:
  1. Harga dan stok negatif diterima tanpa perlawanan.
  2. Salah ketik nama key baru ketahuan saat program error (`KeyError`).
  3. Rumus subtotal terpisah dari datanya dan harus ditulis ulang.

**Berkas.**

| Berkas | Keterangan |
|--------|------------|
| `main.py` | Program utama |
| `.gitignore` | `__pycache__/`, `*.pyc`, `.venv/`, `.env` |
| `README.md` | Nama proyek, tujuan, kebutuhan, cara menjalankan, Weekly Progress |

**Keluaran yang diharapkan.**

```
Produk pertama: Indomie

=========================
      SIMPLE CASHIER
=========================

P001 Indomie 3000 20
P002 Teh Botol 4000 15
P003 Roti 7000 8

Subtotal 2 Indomie = 6000

--- Catatan untuk Minggu 02 ---
Harga sekarang: -5000 (negatif, tetap diterima)
Stock sekarang: -100 (negatif, tetap diterima)
```

## 10. Alur Git

- Cabang utama `main`, remote `origin`.
- Cabang kerja: `feature/foundation`.
- Commit: `Initial commit`, `docs: add PRD, milestone breakdown, and project guidance`,
  `feat: add week 01 foundation`, `docs: mark week 01 complete in milestone tracker`.
- Akhir minggu: Pull Request **Week 01 — Initialize Cashier App**, review, merge,
  lalu tag `week-01`.

## 11. Data Model

Produk (dictionary):

| Key | Tipe | Contoh |
|-----|------|--------|
| `code` | string | `"P001"` |
| `name` | string | `"Indomie"` |
| `price` | integer | `3000` |
| `stock` | integer | `20` |

Nama key ditulis dalam bahasa Inggris dan dipertahankan di minggu-minggu berikutnya.

## 16. Penilaian

Kolaborasi Git bernilai **15%** pada rubrik. Deskripsi Pull Request
(What, Why, How, Testing, Screenshot / Evidence, Learning Point) adalah bukti yang dinilai.

## 17. Baseline README

Nama proyek, tujuan, kebutuhan, cara menjalankan, dan bagian **Weekly Progress**.s