def main():
    print("=======================================================")
    print("SELAMAT DATANG DI SISTEM PENGURUTAN KEUNTUNGAN SAHAM")
    print("=======================================================")

    def insertion_sort(data):
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1

            while j >= 0 and data[j][1] > key[1]:
                data[j + 1] = data[j]
                j -= 1

            data[j + 1] = key

    x = int(input("Masukkan jumlah saham yang diinginkan: "))
    data_saham = [] 

    for i in range(x):
        nama = input("Nama saham: ")
        harga = int(input("Keuntungan: "))
        data_saham.append((nama, harga))

    print("\nData sebelum sorting:")
    for nama, harga in data_saham:
        print(f"{nama} : {harga}")

    insertion_sort(data_saham)  

    print("\nSaham dengan Keuntungan terkecil hingga terbesar:")
    for nama, harga in data_saham:
        print(f"{nama} : {harga}")

if __name__ == "__main__":
    main()