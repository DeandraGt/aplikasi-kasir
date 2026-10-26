"""Simple Cashier — Minggu 03 (Encapsulation).

Data produk menggunakan object dari class Product.
Perubahan harga dan stok harus melalui method yang menjaga aturannya.
"""

from models.product import Product


# Banyak object, disimpan dalam list.
products = [
    Product("P001", "Indomie", 3000, 20),
    Product("P002", "Teh Botol", 4000, 15),
    Product("P003", "Roti", 7000, 8),
]

print("=========================")
print("     SIMPLE CASHIER")
print("=========================")
print()

for item in products:
    print(item.code, item.name, item.price, item.stock)

print()
print("--- Masalah Minggu 02 ---")

indomie = products[0]

# Harga tidak boleh diubah langsung karena property tidak memiliki setter.
try:
    indomie.price = -5000
except AttributeError:
    print("Menulis langsung ke price ditolak (property tanpa setter).")

print()
print("--- Perubahan lewat method ---")

# Perubahan harga dilakukan melalui method.
indomie.change_price(3500)
print("Harga baru:", indomie.price)

# Stok dikurangi melalui method.
indomie.reduce_stock(5)
print("Stock setelah terjual 5:", indomie.stock)

print()
print("--- Setiap aturan diuji ---")

# Percobaan 1: harga negatif harus ditolak.
try:
    indomie.change_price(-5000)
except ValueError as error:
    print("change_price(-5000) ->", error)

# Percobaan 2: jumlah nol harus ditolak.
try:
    indomie.reduce_stock(0)
except ValueError as error:
    print("reduce_stock(0)    ->", error)

# Percobaan 3: jumlah negatif harus ditolak.
try:
    indomie.reduce_stock(-3)
except ValueError as error:
    print("reduce_stock(-3)   ->", error)

# Percobaan 4: jumlah melebihi stok harus ditolak.
try:
    indomie.reduce_stock(999)
except ValueError as error:
    print("reduce_stock(999)  ->", error)

print()
print("Harga akhir:", indomie.price, "| Stock akhir:", indomie.stock)
print("Percobaan yang gagal tidak mengubah apa pun.")