import unittest

def satuan(jumlah_barang):
    satuan_lusin = jumlah_barang / 12
    return satuan_lusin

class SimpleTest(unittest.TestCase):
    def testLusin(self):
        jumlah_barang = int(input("Masukkan jumlah barang: "))
        perkiraan_jumlah_barang = int(input("Masukkan perkiraan lusin: "))
        self.assertEquals(satuan(jumlah_barang), perkiraan_jumlah_barang)

if __name__ == '__main__':
    unittest.main()


