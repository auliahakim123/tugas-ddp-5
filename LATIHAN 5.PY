my_list = ["1234","beat pop", "125", "2015"]
print(my_list)

my_list.append("15.000.000")
my_list.append("2")
my_list.insert(2,"honda")
my_list.insert(3,"motor")
print(my_list)

def hitung_luas(pilihan):
    # Match case untuk menghitung luas bangun datar
    match pilihan:
        case 1:
            sisi = float(input("Masukkan panjang sisi persegi: "))
            luas = sisi * sisi
            print("Luas persegi:", luas)
        case 2:
            jari_jari = float(input("Masukkan panjang jari-jari lingkaran: "))
            luas = 3.14 * jari_jari * jari_jari
            print("Luas lingkaran:", luas)
        case 3:
            alas = float(input("Masukkan panjang alas segitiga: "))
            tinggi = float(input("Masukkan tinggi segitiga: "))
            luas = 0.5 * alas * tinggi
            print("Luas segitiga:", luas)
        case _:
            print("Pilihan yang dimasukkan salah!")

# Meminta input pilihan dari pengguna
pilihan = int(input("Masukkan pilihan (1-3): "))

# Memanggil fungsi hitung_luas dengan pilihan yang dimasukkan
hitung_luas(pilihan)