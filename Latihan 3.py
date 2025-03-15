class Barang:
    def __init__(self, merek,harga_satuan):
        self.merek = merek
        self.harga_satuan = harga_satuan #dalam rib

    def __mul__(self, kuantitas):
        print('Banyaknya penjualan :', kuantitas.qty_jual, 'buah')
        return self.harga_satuan * kuantitas.qty_jual

class Penjualan:
    def __init__(self, merek, qty_jual):
        self.merek = merek
        self.qty_jual = qty_jual
    

redmi10 = Barang('Redmi 10', 2140)
qty_maret = Penjualan('Redmi 10', 20)
print(f"Total penjualan {redmi10.merek}: {redmi10 * qty_maret} ribu")