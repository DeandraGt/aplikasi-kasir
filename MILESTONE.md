## Milestone Minggu 03 — Encapsulation & Modularization

### Tujuan
Menerapkan encapsulation pada class `Product` agar perubahan harga dan stok mengikuti aturan validasi.

### Implementasi
- Mengubah `price` dan `stock` menjadi property yang hanya dapat dibaca dari luar.
- Menyimpan nilai internal pada `_price` dan `_stock`.
- Menambahkan method `change_price(new_price)` untuk menolak harga negatif.
- Menambahkan method `reduce_stock(quantity)` untuk menolak jumlah nol, negatif, dan melebihi stok.
- Memperbarui `main.py` untuk menguji perubahan yang valid dan empat percobaan yang harus gagal.

### Kriteria keberhasilan
- Penulisan langsung ke `product.price` menghasilkan `AttributeError`.
- Harga negatif menghasilkan `ValueError`.
- Quantity nol dan negatif menghasilkan `ValueError`.
- Pengurangan stok melebihi persediaan menghasilkan `ValueError`.
- Harga akhir Indomie adalah 3500 dan stok akhir 15.
- Import `Product` melalui `from models.product import Product` tetap berfungsi.

### Dokumentasi dan kolaborasi
- Memperbarui bagian Weekly Progress di README.md.
- Mengerjakan perubahan pada branch `feature/product-encapsulation`.
- Membuka Pull Request berjudul `Week 03 — Encapsulate Product State`.