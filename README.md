# Simple Cashier

Aplikasi kasir sederhana berbasis Python, dikembangkan bertahap pada mata kuliah **Pemrograman Komputer 2 (BD322)**, Program Studi Bisnis Digital, Universitas Panca Bhakti Pontianak.

## Tujuan

Membangun aplikasi kasir yang menampilkan daftar produk dan menghitung subtotal belanja.

- **Minggu 01:** menyiapkan repository dan program pertama. Data produk disimpan sebagai dictionary di dalam list, lalu dicatat tiga keterbatasannya.
- **Minggu 02:** mengganti dictionary dengan object dari class `Product`, dan memindahkan perhitungan subtotal menjadi method `subtotal(quantity)`.
- **Minggu 03:** menerapkan encapsulation pada class `Product` dengan property `price` dan `stock`, serta method `change_price(new_price)` dan `reduce_stock(quantity)` untuk menjaga aturan perubahan harga dan stok.

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

Jalankan dari akar repository (folder yang memuat `main.py` dan `models/`), supaya `from models.product import Product` dapat ditemukan.

Pada Linux dan WSL, gunakan `python3`, bukan `python`.

## Struktur Proyek

```text
cashier-app/
├── .gitignore
├── README.md
├── main.py
└── models/
    └── product.py
```

## Ringkasan Per Minggu

### Minggu 01 — Foundation

- Satu produk = satu dictionary (`code`, `name`, `price`, `stock`).
- Banyak produk = list berisi dictionary.
- Subtotal dihitung langsung di `main.py` (`price * quantity`).
- Keterbatasan dictionary yang dicatat: harga negatif diterima, salah ketik key baru ketahuan saat error (`KeyError`), dan rumus subtotal terpisah dari datanya.

### Minggu 02 — Class, Object, Attribute, Method

- Class `Product` di `models/product.py` dengan empat attribute dan method `subtotal(quantity)`.
- `product["name"]` menjadi `product.name`; rumus subtotal ditulis satu kali di dalam class.
- Salah ketik attribute menghasilkan `AttributeError` yang menyebut nama attribute-nya.
- Masih terbuka: harga dan stok negatif masih diterima lewat assignment langsung.

### Minggu 03 — Encapsulation & Modularization

- Atribut internal `_price` dan `_stock` digunakan untuk menyimpan harga dan stok produk.
- Property `price` dan `stock` memungkinkan data dibaca dari luar tanpa penulisan langsung melalui kedua property tersebut.
- Method `change_price(new_price)` menolak harga negatif dengan `ValueError`.
- Method `reduce_stock(quantity)` menolak quantity nol, negatif, atau melebihi stok yang tersedia.
- Pengujian menggunakan `try-except` memastikan percobaan yang tidak valid ditolak tanpa menghentikan program.
- Setelah pengujian, harga Indomie menjadi `3500` dan stok menjadi `15`.
- Import `Product` tetap menggunakan `from models.product import Product`.

## Weekly Progress

| Minggu | Topik | Status |
|--------|-------|--------|
| 01 | Foundation: repository, program pertama, data produk sebagai dictionary | Selesai |
| 02 | Class, Object, Attribute, Method: class `Product` dan method `subtotal(quantity)` | Selesai |
| 03 | Encapsulation & Modularization: property `price` dan `stock`, method `change_price()` dan `reduce_stock()` | Selesai |