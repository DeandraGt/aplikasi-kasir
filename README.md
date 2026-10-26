# Simple Cashier

Program Simple Cashier merupakan proyek praktikum Pemrograman Komputer 2 (BD322) yang dikembangkan menggunakan Python. Proyek ini dibuat secara bertahap untuk mempelajari dasar pemrograman berorientasi objek (*Object-Oriented Programming* atau OOP), pengelolaan data produk, encapsulation, inheritance, dan polymorphism.

## Deskripsi Proyek

Simple Cashier merupakan program kasir sederhana yang berfokus pada pengelolaan data produk, harga, stok, dan perhitungan subtotal. Pengembangan dilakukan secara bertahap sesuai materi praktikum setiap minggu.

## Teknologi yang Digunakan

- **Bahasa pemrograman:** Python
- **Version control:** Git
- **Repository hosting:** GitHub
- **Konsep pemrograman:** Object-Oriented Programming (OOP)

## Struktur Proyek

```text
aplikasi-kasir/
├── main.py
├── models/
│   ├── product.py
│   ├── food_product.py
│   └── digital_product.py
└── README.md
```

Keterangan:

- `main.py`: Menjalankan program dan menguji fitur yang dikembangkan.
- `models/product.py`: Berisi class utama `Product`, termasuk data dan perilaku dasar produk.
- `models/food_product.py`: Berisi class `FoodProduct` untuk produk makanan yang memiliki tanggal kedaluwarsa.
- `models/digital_product.py`: Berisi class `DigitalProduct` untuk produk digital.
- `README.md`: Dokumentasi proyek dan perkembangan praktikum.

## Cara Menjalankan Program

Pastikan Python sudah terpasang di komputer.

1. Buka terminal pada folder proyek.
2. Jalankan perintah berikut:

   ```bash
   python main.py
   ```

   Jika menggunakan lingkungan yang menyediakan perintah `python3`, jalankan:

   ```bash
   python3 main.py
   ```

3. Periksa keluaran terminal untuk memastikan program berjalan sesuai hasil yang diharapkan.

### Minggu 03 — Encapsulation & Modularization

- Atribut internal `_price` dan `_stock` digunakan untuk menyimpan harga dan stok produk.
- Property `price` dan `stock` memungkinkan data dibaca dari luar tanpa penulisan langsung melalui kedua property tersebut.
- Method `change_price(new_price)` menolak harga negatif dengan `ValueError`.
- Method `reduce_stock(quantity)` menolak quantity nol, negatif, atau melebihi stok yang tersedia.
- Pengujian menggunakan `try-except` memastikan percobaan yang tidak valid ditolak tanpa menghentikan program.
- Setelah pengujian, harga Indomie menjadi `3500` dan stok menjadi `15`.
- Import `Product` tetap menggunakan `from models.product import Product`.

## Weekly Progress

| Minggu | Materi | Status |
|---|---|---|
| 01 | Dasar Python dan fondasi program Simple Cashier | Selesai |
| 02 | Object-Oriented Programming: class `Product`, atribut, method, dan perhitungan subtotal | Selesai |
| 03 | Encapsulation & Modularization: property, `_price`, `_stock`, `change_price()`, dan `reduce_stock()` | Selesai |
| 04 | Inheritance & Polymorphism: `FoodProduct`, `DigitalProduct`, `super()`, method overriding, dan `get_description()` | Selesai |

## Ringkasan Pengembangan

### Minggu 01 — Dasar Pemrograman

Mempelajari dasar pemrograman Python sebagai fondasi pengembangan program Simple Cashier.

### Minggu 02 — Product Model

Mengembangkan class `Product` untuk merepresentasikan produk dengan atribut seperti kode, nama, harga, dan stok. Class ini juga menyediakan method `subtotal(quantity)` untuk menghitung subtotal berdasarkan harga dan jumlah produk.

### Minggu 03 — Encapsulation & Modularization

Menerapkan encapsulation pada class `Product` dengan menyimpan harga dan stok dalam `_price` dan `_stock`.

Perubahan nilai dilakukan melalui method khusus:

- `price` dan `stock` dibaca menggunakan `@property`.
- `change_price(new_price)` menolak harga negatif.
- `reduce_stock(quantity)` menolak jumlah nol, negatif, atau melebihi stok yang tersedia.
- Percobaan perubahan yang tidak valid menghasilkan error tanpa mengubah nilai yang tersimpan.

### Minggu 04 — Inheritance & Polymorphism

Mengembangkan variasi produk melalui inheritance dan polymorphism.

- `FoodProduct` merupakan turunan `Product` dengan atribut tambahan `expiry_date`.
- `DigitalProduct` merupakan turunan `Product` untuk produk digital.
- `super().__init__()` digunakan untuk memanggil konstruktor class induk pada `FoodProduct`.
- `get_description()` digunakan untuk menunjukkan method overriding pada jenis produk yang berbeda.
- Satu list dan satu loop digunakan untuk menampilkan deskripsi berbagai jenis produk.
- Aturan encapsulation dari Minggu 03 tetap berlaku pada class turunan.

## Hasil Pengujian Minggu 04

Program diuji menggunakan perintah `python main.py` atau `python3 main.py`.

Hasil yang diharapkan:

- Produk biasa menampilkan nama produk.
- Produk makanan menampilkan nama dan tanggal kedaluwarsa.
- Produk digital menampilkan nama dan keterangan produk digital.
- Subtotal 3 Roti dengan harga Rp7.000 per unit menghasilkan `21000`.
- Harga produk tidak dapat diubah melalui assignment langsung ke `price`.
- Harga negatif ditolak.
- Pengurangan stok melebihi persediaan ditolak.
- Stok Roti berubah dari 8 menjadi 5 setelah dikurangi 3.

## Tujuan Pembelajaran

Melalui proyek Simple Cashier, mahasiswa diharapkan memahami dasar pemrograman Python, pemodelan produk menggunakan class, encapsulation untuk menjaga validitas data, inheritance untuk menggunakan kembali perilaku class induk, dan polymorphism untuk menjalankan perilaku berbeda melalui method yang sama.

## Version Control

Pengembangan proyek dilakukan secara bertahap menggunakan Git dan GitHub. Setiap minggu dikerjakan melalui branch tersendiri, kemudian diajukan melalui Pull Request untuk ditinjau dan digabungkan ke branch utama sesuai alur praktikum.

Checkpoint setiap minggu menggunakan tag Git, seperti `week-02`, `week-03`, dan `week-04`, sesuai tahapan yang telah diselesaikan.

## Status Proyek

**Minggu 01–04: Selesai.**

Proyek telah mencakup model produk dasar, encapsulation, inheritance, dan polymorphism. Pengembangan selanjutnya mengikuti materi dan kebutuhan pada minggu praktikum berikutnya.
