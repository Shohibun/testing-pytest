import pytest

def testPangkat():
    input_bilangan1 = 25
    input_bilangan2 = 2
    input_perkiraan = 62

    assert input_bilangan1 ** input_bilangan2 == input_perkiraan


#Failure adalah ketidakmampuan sistem atau komponen untuk melakukan fungsi yang diperlukan dalam persyaratan kinerja yang ditentukan  mengacu pada penyimpangan perilaku dari kebutuhan pengguna atau spesifikasi produk
#assert adalah fungsi dari library pytest yang berfungsi untuk memvalidasi suatu proses 
#Dalam pelaksanaan testing variabel tidak boleh bernilai kosong/input user/null karena testing bertujuan untuk menguji sebuah proses 
