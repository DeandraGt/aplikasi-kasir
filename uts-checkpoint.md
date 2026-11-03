# UTS Checkpoint — Simple Cashier (Minggu 01–07)

Pemrograman Komputer 2 (BD322), Program Studi Bisnis Digital, Universitas Panca Bhakti Pontianak.
Minggu 08 tidak menambah fitur. Dokumen ini mencatat hasil pemeriksaan ulang Minggu 01–07.

## 1. Cakupan requirement per minggu

| Minggu | Requirement | Bukti | Status |
|--------|-------------|-------|--------|
| 01 | Repository, program pertama, data produk sebagai dictionary | tag `week-01`; `main.py` Minggu 01 | Terpenuhi |
| 02 | Class `Product`, attribute, method `subtotal` | tag `week-02`; `models/product.py`; bagian W02-03 pada demo | Terpenuhi |
| 03 | Encapsulation: `_price`, `_stock`, property, `change_price`, `reduce_stock` | tag `week-03`; tiga penolakan pada bagian W02-03 | Terpenuhi |
| 04 | Inheritance dan polymorphism: `FoodProduct`, `DigitalProduct`, `get_description()` | tag `week-04`; bagian W04 (satu loop, tiga hasil) | Terpenuhi |
| 05 | `ProductCatalog`: dictionary untuk `get`, list untuk `all` dan `search` | tag `week-05`; bagian W05 | Terpenuhi |
| 06 | `OrderQueue` (FIFO) dan `ActionHistory` (LIFO) | tag `week-06`; bagian W06 | Terpenuhi |
| 07 | Persistence: `ProductRepository` (CSV), `OrderRepository` (JSON) | tag `week-07`; bagian W07 dan Alur penuh | Terpenuhi |

## 2. Temuan dan tindakan

| # | Temuan | Tindakan | Status |
|---|--------|----------|--------|
| 1 | Tag `week-02` sampai `week-07` menunjuk commit satu minggu lebih awal (misalnya `week-03` dan `week-04` sama-sama di `d49654c`). | Tag dipindahkan dengan `git tag -f` ke commit merge tiap minggu, lalu `git push -f origin <tag>`. | Diperbaiki |
| 2 | Berkas data yang ter-commit sudah berubah akibat program pernah dijalankan: stock Indomie 2 dan 6 order. Demo butuh data awal (stock 20, order kosong). | `data/products.csv` dan `data/orders.json` dikembalikan ke data awal dan di-commit sebelum program dijalankan. | Diperbaiki |
| 3 | `models/product.py` mendefinisikan property `stock` dua kali berurutan. Tidak berbahaya, tetapi duplikat. | Tidak diubah minggu ini karena `models/` tidak boleh berubah di Minggu 08. | Ditunda ke Minggu 09 |
| 4 | Cabang bawaan GitHub adalah `feature/foundation`, bukan `main`; PR Minggu 02–07 di-merge ke sana. | Tag dipasang pada commit merge di cabang itu. | Dicatat |

## 3. Hasil pemeriksaan batas lapisan

```
grep -rn "open(\|import csv\|import json" models services main.py
```

Keluarannya kosong. Akses berkas hanya ada di `repositories/product_repository.py` (`csv`) dan `repositories/order_repository.py` (`json`).

Struktur minimal ada: `main.py`, `data/`, `models/`, `repositories/`, `services/`, `README.md`, `.gitignore`.

## 4. Skenario demo sepuluh langkah

Jalankan `git checkout -- data/` lalu `python main.py`.

| # | Potongan keluaran | Yang dijelaskan |
|---|-------------------|-----------------|
| 1 | Judul `SIMPLE CASHIER — UTS Checkpoint W01-07` | Satu program memperagakan Minggu 02–07 berurutan |
| 2 | `subtotal(2) : 6000` | Method menempel pada datanya (Minggu 02) |
| 3 | `price = -5000 : ditolak` | Property tanpa setter (Minggu 03) |
| 4 | `change_price(...) : Price cannot be negative` | Aturan diperiksa sebelum nilai diubah, dengan `raise` |
| 5 | `reduce_stock(999): Insufficient stock` | Stock tidak boleh minus |
| 6 | Tiga produk, satu loop, tiga deskripsi | Polymorphism: `get_description()` (Minggu 04) |
| 7 | `Dimuat dari data/products.csv : 4 produk` dan `File tidak ada : []` | Repository membaca CSV dan menangani `FileNotFoundError` (Minggu 07) |
| 8 | `get('P001')`, `search('TEH')` | Dictionary untuk pencarian kode, list untuk hasil banyak (Minggu 05) |
| 9 | `Queue keluar: A B C`, `Stack keluar: C B A` | FIFO versus LIFO dari masukan yang sama (Minggu 06) |
| 10 | `Stock 20 -> 17 -> baca ulang 17`, `Order tersimpan : 1 order` | Aliran object sampai file |

## 5. Rantai yang harus dapat dijelaskan

`Class -> Object -> Data Structure -> Repository -> File`

- **Class:** `Product` dan turunannya mendefinisikan data dan aturannya (`models/product.py`).
- **Object:** `Product("P001", "Indomie", 3000, 20)` adalah satu produk nyata.
- **Data Structure:** `ProductCatalog` menyimpan object dalam dictionary (cari lewat kode) dan list (tampilan berurutan); `OrderQueue` dan `ActionHistory` menyimpan order dan tindakan.
- **Repository:** `ProductRepository` dan `OrderRepository` adalah satu-satunya bagian yang tahu bentuk file.
- **File:** `data/products.csv` (tabel datar) dan `data/orders.json` (daftar bersarang).

Alasan pilihan struktur data: dictionary agar pencarian per kode satu langkah; list agar urutan tampilan terjaga; queue karena pesanan diproses sesuai urutan masuk; stack karena tindakan terakhir yang dibatalkan lebih dulu.

## 6. Keadaan yang dibawa ke Minggu 09

- Ujung `File` pada rantai diganti `Database`; perubahan hanya di `repositories/`.
- `.gitignore` sudah memuat `*.db` dan `*.sqlite3`.
- Data awal: stock Indomie 20, `orders.json` kosong. Setiap menjalankan program mengubah data; pulihkan dengan `git checkout -- data/`.
- Temuan #3 (duplikat property `stock`) dibereskan saat `models/` boleh disentuh.
- Seluruh tag `week-01` sampai `week-07` dan `week-08-uts` dapat dibuka dan dijalankan.