"""Model Product — Minggu 04.

Class induk untuk semua jenis produk Simple Cashier.
Mencakup attribute, method, encapsulation, dan deskripsi dasar.
"""


class Product:
    def __init__(self, code, name, price, stock):
        self.code = code
        self.name = name
        self._price = price
        self._stock = stock

    @property
    def price(self):
        # Harga boleh dibaca, tetapi tidak boleh diubah langsung.
        return self._price

    @property
    def stock(self):
        # Stock boleh dibaca, tetapi tidak boleh diubah langsung.
        return self._stock

    def subtotal(self, quantity):
        return self._price * quantity

    def change_price(self, new_price):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self._price = new_price

    def reduce_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if quantity > self._stock:
            raise ValueError("Insufficient stock")
        self._stock -= quantity

    def get_description(self):
        # Deskripsi dasar yang dapat di-override oleh subclass.
        return self.name
