# MILESTONE — Simple Cashier

## Minggu 02 — Class, Object, Attribute, Method

### Prasyarat

- [ ] Minggu 01 sudah ter-merge ke `main`
- [ ] `git switch main`, `git pull`, `git tag -l week-01` menampilkan `week-01`
- [ ] `python3 main.py` (versi Minggu 01) masih berjalan

### Todo

- [ ] `git status --short` kosong
- [ ] `git switch -c feature/product-model` (dari `main`, bukan dari cabang minggu lalu)
- [ ] Buat folder `models/`
- [ ] `models/product.py`: class `Product` dengan `__init__(code, name, price, stock)`
- [ ] `models/product.py`: method `subtotal(quantity)` yang mengembalikan `self.price * quantity`
- [ ] `main.py`: `from models.product import Product`, satu object `Product`
- [ ] `main.py`: list berisi tiga object `Product`, cetak daftar dengan `item.code`, `item.name`, dst.
- [ ] `main.py`: bagian pembanding dictionary versus object
- [ ] `main.py`: catatan bahwa harga dan stok negatif masih diterima
- [ ] Commit: `feat: add product model`
- [ ] Perbarui Weekly Progress di `README.md` (satu baris untuk Minggu 02)
- [ ] Commit: `docs: mark week 02 complete in milestone tracker`
- [ ] `git push -u origin feature/product-model`
- [ ] Buka Pull Request **Week 02 — Add Product Model** memakai template di bawah
- [ ] Setelah merge: `git switch main`, `git pull`, `git tag week-02`, `git push origin week-02`

### Verifikasi

- [ ] `python3 main.py` berjalan tanpa traceback dan keluarannya sesuai modul
- [ ] `python3 -c "from models.product import Product; print(Product('P001','Indomie',3000,20).subtotal(2))"` mencetak `6000`
- [ ] `main.py` tidak memuat `price * quantity` untuk data produk, kecuali baris pembanding dictionary
- [ ] `models/` hanya berisi `product.py`
- [ ] `models/product.py` belum memuat `@property` atau `_price` (materi Minggu 03)

### Checkpoint

Class, object, attribute, method, branch, dan commit bekerja.

### Pertanyaan Lisan

1. Apa beda attribute dan method?
2. Apa yang dikerjakan `__init__`?
3. Mengapa `subtotal()` diletakkan di dalam class alih-alih di `main.py`?

### Template Deskripsi Pull Request

```
## What

## Why

## How

## Testing

## Screenshot / Evidence

## Learning Point
```
