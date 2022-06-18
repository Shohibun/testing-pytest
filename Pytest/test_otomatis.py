import pytest

def testPangkat():
    input_bilangan1 = float(input("Masukkan bilangan yang akan dikuadratkan: "))
    input_bilangan2 = float(input("Masukkan pangkat bilangan: "))
    input_perkiraan = float(input("Masukkan hasil perkiraan dari hasil proses pangkat: "))

    assert input_bilangan1 ** input_bilangan2 == input_perkiraan

