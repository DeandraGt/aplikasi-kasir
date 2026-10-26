# Simple Cashier

Program Simple Cashier merupakan proyek praktikum Pemrograman Komputer 2 (BD322) yang dikembangkan menggunakan Python. Proyek ini dibuat secara bertahap untuk mempelajari dasar pemrograman berorientasi objek (*Object-Oriented Programming* atau OOP), pengelolaan data produk, encapsulation, inheritance, polymorphism, serta struktur data list, dictionary, stack, dan queue.

## Deskripsi Proyek

Simple Cashier merupakan program kasir sederhana yang berfokus pada pengelolaan data produk, harga, stok, perhitungan subtotal, katalog produk, antrean order, dan riwayat tindakan. Pengembangan dilakukan secara bertahap sesuai materi praktikum setiap minggu.

## Teknologi yang Digunakan

- **Bahasa pemrograman:** Python
- **Version control:** Git
- **Repository hosting:** GitHub
- **Konsep pemrograman:** Object-Oriented Programming (OOP), List, Dictionary, Stack, dan Queue

## Struktur Proyek

```text
aplikasi-kasir/
├── main.py
├── models/
│   ├── product.py
│   ├── food_product.py
│   ├── digital_product.py
│   └── product_catalog.py
├── services/
│   ├── order_queue.py
│   └── action_history.py
└── README.md
```

Keterangan:

- `main.py`: Menjalankan program dan menguji fitur yang dikembangkan.
- `models/product.py`: Berisi class utama `Product`, termasuk data dan perilaku dasar produk.
- `models/food_product.py`: Berisi class `FoodProduct` untuk produk makanan yang memiliki tanggal kedaluwarsa.
- `models/digital_product.py`: Berisi class `DigitalProduct` untuk produk digital.
- `models/product_catalog.py`: Berisi class `ProductCatalog` untuk menyimpan, mengambil, menghapus, menampilkan, dan mencari produk.
- `services/order_queue.py`: Berisi class `OrderQueue` untuk mengelola antrean order menggunakan `deque`.
- `services/action_history.py`: Berisi class `ActionHistory` untuk mengelola riwayat tindakan menggunakan list.
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
| 05 | List & Dictionary: `ProductCatalog`, penyimpanan produk berdasarkan kode, pengambilan produk, penghapusan produk, dan pencarian berdasarkan nama | Selesai |
| 06 | Stack & Queue: `ActionHistory`, `OrderQueue`, LIFO, FIFO, `push()`, `pop()`, `enqueue()`, dan `dequeue()` | Selesai |

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

### Minggu 05 — List & Dictionary

Mengembangkan class `ProductCatalog` untuk mengelola kumpulan produk menggunakan dictionary dan list.

- Dictionary digunakan untuk menyimpan produk dengan `code` sebagai key dan objek produk sebagai value.
- Method `add(product)` menambahkan produk ke katalog berdasarkan kode produk.
- Method `get(code)` mengambil produk berdasarkan kode dan mengembalikan `None` jika kode tidak ditemukan.
- Method `remove(code)` menghapus produk berdasarkan kode tanpa menimbulkan error jika kode tidak tersedia.
- Method `all()` mengembalikan seluruh produk dalam bentuk list.
- Method `search(keyword)` mencari produk berdasarkan potongan nama tanpa membedakan huruf besar dan kecil.
- List digunakan untuk menampilkan kumpulan produk dan menampung hasil pencarian.
- Katalog mendukung berbagai jenis objek produk, termasuk `Product`, `FoodProduct`, dan `DigitalProduct`.

### Minggu 06 — Stack & Queue

Mengembangkan dua struktur data untuk mengelola urutan pekerjaan dan riwayat tindakan dalam konteks aplikasi kasir.

**1. Queue — `OrderQueue`**

Queue digunakan untuk mengelola antrean order di dapur dengan prinsip FIFO (*First In, First Out*), yaitu order yang masuk lebih dahulu akan dilayani lebih dahulu.

- Menggunakan `deque` dari modul `collections`.
- Method `enqueue(order)` menambahkan order ke belakang antrean.
- Method `dequeue()` mengambil order dari depan antrean.
- Method `is_empty()` memeriksa apakah antrean kosong.
- Jika antrean kosong, `dequeue()` mengembalikan `None` tanpa menghentikan program.
- `deque` dipilih karena penambahan di belakang dan pengambilan dari depan dapat dilakukan secara efisien.

**2. Stack — `ActionHistory`**

Stack digunakan untuk menyimpan riwayat tindakan kasir yang dapat dibatalkan dengan prinsip LIFO (*Last In, First Out*), yaitu tindakan yang terakhir dilakukan akan dibatalkan terlebih dahulu.

- Menggunakan list Python.
- Method `push(action)` menambahkan tindakan baru ke tumpukan.
- Method `pop()` mengambil tindakan paling terakhir dari tumpukan.
- Method `is_empty()` memeriksa apakah riwayat tindakan kosong.
- Jika riwayat kosong, `pop()` mengembalikan `None` tanpa menghentikan program.
- List dipilih karena penambahan dan pengambilan tindakan sama-sama dilakukan pada ujung list.

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

## Hasil Pengujian Minggu 05

Program diuji menggunakan perintah `python main.py` atau `python3 main.py`.

Hasil yang diharapkan:

- Katalog dapat menyimpan produk biasa, produk makanan, dan produk digital.
- Produk dapat ditampilkan melalui method `all()`.
- Produk dapat diambil berdasarkan kode menggunakan `get()`.
- Kode yang tidak tersedia menghasilkan `None`.
- Pencarian nama tidak membedakan huruf besar dan kecil, misalnya `teh` dan `TEH`.
- Pencarian dapat menghasilkan beberapa produk, satu produk, atau tidak menemukan produk.
- Produk dapat dihapus menggunakan `remove()`.
- Penghapusan kode yang tidak tersedia tidak menghentikan program.

## Hasil Pengujian Minggu 06

Program diuji menggunakan perintah `python main.py` atau `python3 main.py`.

Hasil yang diharapkan:

- Antrean menerima tiga order melalui `enqueue()`.
- Pemanggilan `dequeue()` menghasilkan order sesuai urutan masuknya, yaitu `ORD-001`, `ORD-002`, lalu `ORD-003`.
- Pemanggilan `dequeue()` ketika antrean kosong menghasilkan `None`.
- Riwayat menerima tiga tindakan melalui `push()`.
- Pemanggilan `pop()` menghasilkan tindakan dalam urutan terbalik dari urutan masuknya.
- Tindakan terakhir yang dilakukan menjadi tindakan pertama yang dibatalkan.
- Pemanggilan `pop()` ketika riwayat kosong menghasilkan `None`.
- Katalog, antrean, dan riwayat dapat digunakan secara terpisah tanpa saling mengimpor.

## Tujuan Pembelajaran

Melalui proyek Simple Cashier, mahasiswa diharapkan memahami dasar pemrograman Python, pemodelan produk menggunakan class, encapsulation untuk menjaga validitas data, inheritance untuk menggunakan kembali perilaku class induk, polymorphism untuk menjalankan perilaku berbeda melalui method yang sama, penggunaan list dan dictionary untuk mengelola kumpulan data, serta penerapan stack dan queue untuk mengatur urutan tindakan.

## Version Control

Pengembangan proyek dilakukan secara bertahap menggunakan Git dan GitHub. Setiap minggu dikerjakan melalui branch tersendiri, kemudian diajukan melalui Pull Request untuk ditinjau dan digabungkan ke branch utama sesuai alur praktikum.

Checkpoint setiap minggu menggunakan tag Git, seperti `week-02`, `week-03`, `week-04`, `week-05`, dan `week-06`, sesuai tahapan yang telah diselesaikan.

## Status Proyek

**Minggu 01–06: Selesai.**

Proyek telah mencakup model produk dasar, encapsulation, inheritance, polymorphism, pengelolaan katalog produk menggunakan list dan dictionary, serta pengelolaan antrean order dan riwayat tindakan menggunakan queue dan stack. Pengembangan selanjutnya mengikuti materi dan kebutuhan pada minggu praktikum berikutnya.