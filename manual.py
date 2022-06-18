class Kalkulator:
    def __init__(self, bilangan1, bilangan2):
        self.bilangan1 = float(bilangan1)
        self.bilangan2 = float(bilangan2)

    def Pertambahan(self):
        hasil = self.bilangan1 + self.bilangan2
        return hasil

    def Pengurangan(self):
        hasil = self.bilangan1 - self.bilangan2
        return hasil

    def Perkalian(self):
        hasil = self.bilangan1 * self.bilangan2
        return hasil

    def Pembagian(self):
        hasil = self.bilangan1 // self.bilangan2
        return hasil

    def Akar(self):
        hasil = self.bilangan1 ** 0.5
        return hasil

    def AngkaKuadrat(self):
        hasil = self.bilangan1 ** self.bilangan2
        return hasil


def menu():
    print("======Daftar menu Kalkulator======")
    print("[1] Pertambahan")
    print("[2] Pengurangan")
    print("[3] Perkalian")
    print("[4] Pembagian")
    print("[5] Akar")
    print("[6] Angka Kuadrat")
    print("[7] Exit")

    pilihan = input("Pilih program yang ingin anda jalankan: ")
    if pilihan.lower() == "1":
        Pertambahan1()
    elif pilihan.lower() == "2":
        Pengurangan1()
    elif pilihan.lower() == "3":
        Perkalian1()
    elif pilihan.lower() == "4":
        Pembagian1()
    elif pilihan.lower() == "5":
        Akar1()
    elif pilihan.lower() == "6":
        AngkaKuadrat1()
    elif pilihan.lower() == "7":
        exit()
    else:
        print("Program tidak ada di menu")


def BackToMenu():
    menu()


def Pertambahan1():
    input_bilangan1 = float(input("Masukan bilngan 1: "))
    input_bilangan2 = float(input("Masukan bilangan 2: "))
    nilai = Kalkulator(input_bilangan1, input_bilangan2)
    print("Hasil Pertambahan: ", nilai.Pertambahan())
    print("\n")
    BackToMenu()
    

def Pengurangan1():
    input_bilangan1 = float(input("Masukan bilngan 1: "))
    input_bilangan2 = float(input("Masukan bilangan 2: "))
    nilai = Kalkulator(input_bilangan1, input_bilangan2)
    print("Hasil Pengurangan: ", nilai.Pengurangan())
    print("\n")
    BackToMenu()


def Perkalian1():
    input_bilangan1 = float(input("Masukan bilngan 1: "))
    input_bilangan2 = float(input("Masukan bilangan 2: "))
    nilai = Kalkulator(input_bilangan1, input_bilangan2)
    print("Hasil Perkalian: ", nilai.Perkalian())
    print("\n")
    BackToMenu()


def Pembagian1():
    input_bilangan1 = float(input("Masukan bilngan 1: "))
    input_bilangan2 = float(input("Masukan bilangan 2: "))
    nilai = Kalkulator(input_bilangan1, input_bilangan2)
    print("Hasil Pembagian: ", nilai.Pembagian())
    print("\n")
    BackToMenu()


def Akar1():
    input_bilangan1 = float(input("Masukan bilngan 1: "))
    input_bilangan2 = float(input("Masukan bilangan 2: "))
    nilai = Kalkulator(input_bilangan1, input_bilangan2)
    print("Hasil Akar: ", nilai.Akar())
    print("\n")
    BackToMenu()


def AngkaKuadrat1():
    input_bilangan1 = float(input("Masukan bilngan 1: "))
    input_bilangan2 = float(input("Masukan bilangan 2: "))
    nilai = Kalkulator(input_bilangan1, input_bilangan2)
    print("Hasil Akar kudarat: ", nilai.AngkaKuadrat())
    print("\n")
    BackToMenu()


def exit():
    exit


if __name__ == "__main__":
    menu()
