# Simple Cashier

Program Simple Cashier merupakan proyek praktikum Pemrograman Komputer 2 (BD322) yang dikembangkan menggunakan Python. Proyek ini dibuat secara bertahap untuk mempelajari dasar pemrograman berorientasi objek (*Object-Oriented Programming* atau OOP), pengelolaan data produk, encapsulation, inheritance, polymorphism, struktur data list, dictionary, stack, queue, serta penyimpanan data menggunakan CSV dan JSON.

## Deskripsi Proyek

Simple Cashier merupakan program kasir sederhana yang berfokus pada pengelolaan data produk, harga, stok, perhitungan subtotal, katalog produk, antrean order, riwayat tindakan, dan persistensi data. Pengembangan dilakukan secara bertahap sesuai materi praktikum setiap minggu.

## Teknologi yang Digunakan

- **Bahasa pemrograman:** Python
- **Version control:** Git
- **Repository hosting:** GitHub
- **Format penyimpanan:** CSV dan JSON
- **Konsep pemrograman:** Object-Oriented Programming (OOP), Encapsulation, Inheritance, Polymorphism, List, Dictionary, Stack, Queue, File Handling, dan Persistence

## Struktur Proyek

```text
aplikasi-kasir/
├── main.py
├── data/
│   ├── products.csv
│   └── orders.json
├── models/
│   ├── product.py
│   ├── food_product.py
│   ├── digital_product.py
│   └── product_catalog.py
├── services/
│   ├── order_queue.py
│   └── action_history.py
├── repositories/
│   ├── product_repository.py
│   └── order_repository.py
└── README.md
```

### Keterangan

- `main.py`: Menjalankan program dan menguji fitur yang dikembangkan.
- `data/products.csv`: Menyimpan data produk dalam format CSV.
- `data/orders.json`: Menyimpan daftar order dalam format JSON.
- `models/product.py`: Berisi class utama `Product`, termasuk data dan perilaku dasar produk.
- `models/food_product.py`: Berisi class `FoodProduct` untuk produk makanan yang memiliki tanggal kedaluwarsa.
- `models/digital_product.py`: Berisi class `DigitalProduct` untuk produk digital.
- `models/product_catalog.py`: Berisi class `ProductCatalog` untuk menyimpan, mengambil, menghapus, menampilkan, dan mencari produk.
- `services/order_queue.py`: Berisi class `OrderQueue` untuk mengelola antrean order menggunakan `deque`.
- `services/action_history.py`: Berisi class `ActionHistory` untuk mengelola riwayat tindakan menggunakan list.
- `repositories/product_repository.py`: Membaca dan menyimpan data produk menggunakan CSV.
- `repositories/order_repository.py`: Membaca dan menyimpan data order menggunakan JSON.
- `README.md`: Dokumentasi proyek dan perkembangan praktikum.

## Cara Menjalankan Program

Pastikan Python sudah terpasang di komputer.

1. Buka terminal pada folder utama proyek.
2. Jalankan perintah berikut:

```bash
python main.py
```

Jika lingkungan menggunakan perintah `python3`, jalankan:

```bash
python3 main.py
```

3. Periksa keluaran terminal untuk memastikan program berjalan sesuai hasil yang diharapkan.
4. Periksa `data/products.csv` dan `data/orders.json` untuk memastikan perubahan data tersimpan.

## Minggu 03 — Encapsulation & Modularization

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
| 07 | File Handling & Persistence: CSV, JSON, `ProductRepository`, `OrderRepository`, `load()`, `save()`, dan persistensi data | Selesai |

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

Stack digunakan untuk menyimpan riwayat tindakan kasir dengan prinsip LIFO (*Last In, First Out*), yaitu tindakan yang terakhir dilakukan akan diambil terlebih dahulu.

- Menggunakan list Python.
- Method `push(action)` menambahkan tindakan baru ke tumpukan.
- Method `pop()` mengambil tindakan paling terakhir dari tumpukan.
- Method `is_empty()` memeriksa apakah riwayat tindakan kosong.
- Jika riwayat kosong, `pop()` mengembalikan `None` tanpa menghentikan program.
- List dipilih karena penambahan dan pengambilan tindakan sama-sama dilakukan pada ujung list.

### Minggu 07 — File Handling & Persistence

Mengembangkan mekanisme penyimpanan data ke berkas agar data produk dan order tetap tersedia meskipun program dihentikan dan dijalankan kembali.

**1. Penyimpanan Produk — CSV**

Produk disimpan dalam `data/products.csv` dengan empat kolom, yaitu `code`, `name`, `price`, dan `stock`.

- `csv.DictReader` digunakan untuk membaca baris CSV sebagai dictionary berdasarkan nama kolom.
- `csv.DictWriter` digunakan untuk menulis data produk kembali ke CSV.
- `FIELDNAMES` menentukan nama dan urutan kolom CSV.
- Nilai `price` dan `stock` dikonversi menggunakan `int()` ketika data dimuat.
- Method `load()` membaca data dan membuat objek `Product`.
- Method `save(products)` menyimpan seluruh produk ke berkas CSV.
- Parameter `newline=""` digunakan saat membuka berkas CSV untuk menghindari baris kosong tambahan.
- Jika berkas belum ditemukan, `load()` menangani `FileNotFoundError` dan mengembalikan list kosong.

**2. Penyimpanan Order — JSON**

Order disimpan dalam `data/orders.json` menggunakan format JSON.

- Modul `json` digunakan untuk membaca dan menulis data order.
- Method `load()` membaca order menggunakan `json.load()`.
- Method `save(orders)` menyimpan order menggunakan `json.dump()` dengan `indent=4`.
- JSON digunakan karena data order dapat berbentuk struktur bersarang.
- Jika berkas belum ditemukan, `load()` mengembalikan list kosong.

**3. Repository sebagai Lapisan Penyimpanan**

Dua repository dibuat untuk memisahkan pengelolaan berkas dari bagian program lainnya.

- `ProductRepository` menangani pembacaan dan penulisan data produk dalam CSV.
- `OrderRepository` menangani pembacaan dan penulisan data order dalam JSON.
- `main.py` menggunakan repository untuk memuat dan menyimpan data.
- `ProductCatalog`, `OrderQueue`, dan `ActionHistory` tetap dipertahankan tanpa perubahan dari Minggu 06.
- Akses berkas dibatasi pada lapisan `repositories/` agar penyimpanan dapat dikembangkan atau diganti pada minggu berikutnya tanpa mengubah lapisan lain.

**4. Persistensi Data**

Program memuat produk dari CSV ketika dijalankan, memproses penjualan selama stok mencukupi, lalu menyimpan perubahan ke berkas.

- Stok Indomie pada data awal adalah `20`.
- Program memproses penjualan sebanyak `3` unit sehingga stok menjadi `17`.
- Perubahan stok disimpan ke `data/products.csv`.
- Order penjualan disimpan ke `data/orders.json`.
- Program membaca ulang data melalui repository baru untuk memeriksa bahwa perubahan benar-benar tersimpan.
- Ketika program dijalankan kembali, stok dimuat dari nilai terakhir yang tersimpan, bukan kembali ke nilai awal.

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
- Tindakan terakhir yang dilakukan menjadi tindakan pertama yang diambil dari riwayat.
- Pemanggilan `pop()` ketika riwayat kosong menghasilkan `None`.
- Katalog, antrean, dan riwayat dapat digunakan secara terpisah tanpa saling mengimpor.

## Hasil Pengujian Minggu 07

Program diuji menggunakan perintah `python main.py` atau `python3 main.py`.

Hasil yang diharapkan:

- Produk berhasil dimuat dari `data/products.csv`.
- Data produk menampilkan kode, nama, harga, dan stok yang sesuai.
- Berkas produk yang tidak ditemukan ditangani tanpa menghentikan program.
- Nilai harga dan stok dibaca sebagai integer.
- Penjualan Indomie sebanyak 3 unit mengurangi stok dari `20` menjadi `17` pada pengujian pertama dengan data awal.
- Perubahan stok disimpan ke `data/products.csv`.
- Order penjualan disimpan ke `data/orders.json`.
- Pembacaan ulang melalui repository baru menghasilkan stok yang sama dengan nilai setelah penjualan.
- Ketika program dijalankan kembali, stok melanjutkan nilai terakhir yang tersimpan.
- Berkas CSV memiliki header kolom dan tidak berisi baris kosong tambahan.
- Data order tersimpan dalam JSON dengan indentasi empat spasi.
- Akses berkas hanya dilakukan melalui lapisan `repositories/`; folder `models/` dan `services/` tidak mengakses CSV atau JSON secara langsung.

### Perintah Verifikasi Minggu 07

```bash
python main.py
```

Memeriksa isi data produk:

```bash
cat data/products.csv
```

Memeriksa isi data order:

```bash
cat data/orders.json
```

Memastikan kode di `models/` dan `services/` tidak mengakses berkas secara langsung:

```bash
grep -rn "open(\|csv\|json" models/ services/
```

Perintah terakhir diharapkan tidak menghasilkan keluaran.

## Tujuan Pembelajaran

Melalui proyek Simple Cashier, mahasiswa diharapkan memahami dasar pemrograman Python, pemodelan produk menggunakan class, encapsulation untuk menjaga validitas data, inheritance untuk menggunakan kembali perilaku class induk, polymorphism untuk menjalankan perilaku berbeda melalui method yang sama, penggunaan list dan dictionary untuk mengelola kumpulan data, penerapan stack dan queue untuk mengatur urutan tindakan, serta file handling dan persistence untuk menyimpan data secara permanen melalui CSV dan JSON.

## Version Control

Pengembangan proyek dilakukan secara bertahap menggunakan Git dan GitHub. Setiap minggu dikerjakan melalui branch tersendiri, kemudian diajukan melalui Pull Request untuk ditinjau dan digabungkan ke branch utama sesuai alur praktikum.

Checkpoint setiap minggu menggunakan tag Git, seperti `week-02`, `week-03`, `week-04`, `week-05`, `week-06`, dan `week-07`, sesuai tahapan yang telah diselesaikan.

Untuk Minggu 07, branch yang digunakan adalah `feature/persistence`, dengan Pull Request berjudul **Week 07 — Add CSV and JSON Persistence**.

## Status Proyek

**Minggu 01–07: Selesai.**

Proyek telah mencakup model produk dasar, encapsulation, inheritance, polymorphism, pengelolaan katalog menggunakan list dan dictionary, pengelolaan antrean order dan riwayat tindakan menggunakan queue dan stack, serta penyimpanan data produk dan order menggunakan CSV dan JSON.

Pengembangan selanjutnya mengikuti materi dan kebutuhan pada minggu praktikum berikutnya.