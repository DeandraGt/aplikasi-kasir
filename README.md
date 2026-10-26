# Simple Cashier

Aplikasi kasir sederhana berbasis Python, dikembangkan bertahap pada mata kuliah
**Pemrograman Komputer 2 (BD322)**, Program Studi Bisnis Digital,
Universitas Panca Bhakti Pontianak.

## Tujuan

Membangun aplikasi kasir yang menampilkan daftar produk dan menghitung subtotal belanja.
Pada Minggu 02, data produk berpindah dari dictionary ke object dari class `Product`,
dan perhitungan subtotal menjadi method milik class tersebut.

## Kebutuhan

- Python 3
- Git
- Akun GitHub (repository kelompok)

## Cara Menjalankan

```bash
git clone <URL repository kelompok>
cd cashier-app
python3 main.py
```

Jalankan dari akar repository (folder yang memuat `main.py` dan `models/`),
supaya `from models.product import Product` dapat ditemukan.
Pada Linux dan WSL, gunakan `python3`, bukan `python`.

## Struktur Proyek

```
cashier-app/
├── .gitignore
├── README.md
├── main.py
└── models/
    └── product.py
```

## Weekly Progress

| Minggu | Topik | Status |
|--------|-------|--------|
| 01 | Foundation: repository, program pertama, data produk sebagai dictionary | Selesai |
| 02 | Class, Object, Attribute, Method: class `Product` dan method `subtotal(quantity)` | Selesai |
