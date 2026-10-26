## Kebutuhan Produk — Encapsulation pada Product

### Latar belakang
Pada Minggu 02, atribut harga dan stok masih dapat diubah langsung sehingga nilai yang tidak masuk akal dapat diterima.

### Kebutuhan fungsional
1. Sistem menyediakan informasi harga dan stok yang dapat dibaca melalui property.
2. Sistem menolak penulisan langsung ke property `price`.
3. Sistem menolak perubahan harga negatif melalui `change_price()`.
4. Sistem menolak pengurangan stok dengan quantity nol atau negatif.
5. Sistem menolak pengurangan stok yang melebihi persediaan.
6. Perubahan yang tidak valid tidak boleh mengubah nilai harga maupun stok.

### Kriteria penerimaan
- Harga negatif ditolak dengan `ValueError`.
- Quantity nol atau negatif ditolak dengan `ValueError`.
- Quantity melebihi stok ditolak dengan `ValueError`.
- Harga dan stok akhir hanya mencerminkan perubahan yang valid.

### Batasan
Implementasi menggunakan class `Product`, property, method, dan exception Python. Inheritance, subclass, dan catalog berada di luar cakupan Minggu 03.