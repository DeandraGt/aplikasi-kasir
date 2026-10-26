# PRD — Simple Cashier (Minggu 02)

> Product Requirements Document untuk Minggu 02 — Class, Object, Attribute, Method,
> Pemrograman Komputer 2 (BD322), Universitas Panca Bhakti Pontianak.
> Penomoran bagian mengikuti rujukan modul: §7 (WEEK 02), §11 (data model),
> §16 (rubrik), §17 (baseline README).

## 1. Ringkasan

Simple Cashier adalah aplikasi kasir sederhana berbasis Python. Minggu 02 mengganti
dictionary produk dengan object dari class `Product`, sehingga data dan perilakunya
berada di satu tempat.

## 2. Tujuan Minggu 02

- Produk tidak lagi berupa dictionary, melainkan object dari class `Product`.
- Perhitungan subtotal berpindah dari `main.py` ke method `subtotal(quantity)`,
  sehingga rumusnya ditulis satu kali dan dipakai dari mana pun.
- Salah ketik nama attribute (`product.nama`) menghasilkan `AttributeError`
  yang menyebut nama attribute-nya, bukan `KeyError` pada kunci dictionary.
- Mahasiswa dapat menyandingkan versi dictionary (Minggu 01) dan versi object (Minggu 02).

## 3. Pengguna

Kasir toko kecil yang mencatat penjualan produk.

## 4. Ruang Lingkup Minggu 02

**Termasuk:** class, object, attribute, method, `__init__`, `self`, import dari folder `models/`.

**Tidak termasuk:** encapsulation, validasi, `@property`, subclass.
Assignment langsung seperti `products[0].price = -5000` masih diterima dan masih
menghasilkan harga negatif. Menutupnya adalah pekerjaan Minggu 03.

## 5. Kebutuhan Fungsional

1. Program membuat satu object `Product` dan menampilkan namanya.
2. Program menampilkan subtotal melalui `product.subtotal(2)`.
3. Program menyimpan banyak object `Product` dalam list dan mencetak daftarnya.
4. Program menyandingkan baris dictionary dan baris object, dengan hasil subtotal sama (6000).
5. Program menampilkan catatan bahwa harga dan stok negatif masih diterima.

## 6. Kebutuhan Non-Fungsional

- Dijalankan dengan `python3 main.py` dari akar repository, tanpa traceback.
- Folder `models/` hanya berisi `product.py`.
- `models/product.py` setara: satu class, empat attribute, satu method (18 baris).

## 7. Rencana Mingguan

### WEEK 02 — Class, Object, Attribute, Method

**Spesifikasi.**
- Class `Product` di `models/product.py`.
- `__init__(self, code, name, price, stock)` menyimpan empat attribute, dengan nama
  yang sama persis dengan key dictionary Minggu 01.
- Method `subtotal(self, quantity)` mengembalikan `self.price * quantity`.
- `main.py` mengimpor class dengan `from models.product import Product`.
- Bagian penutup `main.py` menyandingkan dictionary dan object, lalu mencatat
  masalah yang belum selesai.

**Berkas.**

| Berkas | Perubahan | Keterangan |
|--------|-----------|------------|
| `models/product.py` | TAMBAH | Class `Product`: empat attribute, satu method |
| `main.py` | UBAH | Dictionary diganti object; ditambah bagian pembanding |
| `README.md` | UBAH | Satu baris baru di Weekly Progress |

**Keluaran yang diharapkan.**

```
Produk pertama: Indomie
Subtotal 2 Indomie = 6000

=========================
     SIMPLE CASHIER
=========================

P001 Indomie 3000 20
P002 Teh Botol 4000 15
P003 Roti 7000 8

--- Minggu 01 vs Minggu 02 ---
dictionary : Indomie subtotal 6000
object     : Indomie subtotal 6000

--- Catatan untuk Minggu 03 ---
Harga sekarang: -5000 (negatif, masih diterima)
Stock sekarang: -100 (negatif, masih diterima)
Belum ada yang menjaga aturan ini -> encapsulation di Minggu 03.
```

## 10. Alur Git

- Cabang kerja: `feature/product-model`, dibuat dari `main` yang sudah memuat merge Minggu 01.
- Working tree harus bersih (`git status --short` kosong) sebelum mulai.
- Commit: `feat: add product model`, lalu `docs: mark week 02 complete in milestone tracker`.
- Akhir minggu: Pull Request **Week 02 — Add Product Model**, review, merge, lalu tag `week-02`.

## 11. Data Model

Produk (object dari class `Product`):

| Attribute | Tipe | Contoh |
|-----------|------|--------|
| `code` | string | `"P001"` |
| `name` | string | `"Indomie"` |
| `price` | integer | `3000` |
| `stock` | integer | `20` |

| Method | Keterangan |
|--------|------------|
| `subtotal(quantity)` | Mengembalikan `price * quantity` |

## 16. Penilaian

Kolaborasi Git bernilai **15%** pada rubrik. Deskripsi Pull Request
(What, Why, How, Testing, Screenshot / Evidence, Learning Point) adalah bukti yang dinilai.

## 17. Baseline README

Nama proyek, tujuan, kebutuhan, cara menjalankan, dan bagian **Weekly Progress**.