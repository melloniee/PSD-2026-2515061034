#Tugas Akhir List 1D

print("Tugas Akhir List 1D")
print("Manajemen Data Nilai Mahasiswa")

def menu():
    print("1. Masukkan nilai mahasiswa")
    print("2. Hapus nilai mahasiswa")
    print("3. Cari nilai mahasiswa")
    print("4. Tampilkan semua nilai mahasiswa addressnya")
    print("5. Keluar")

def main():
    a = [0] *  6
    program = True
    while program:
        menu()
        try:
            pilihan = int(input("Menu yang dipilih:"))
        except ValueError:
            print("Masukkan angka yang valid!")
            continue

        if pilihan == 1:
            print("Masukkan 6 nilai mahasiswa: ")
            for i in range(6):
                try:
                    a[i] = int(input(f"Nilai mahasiswa {i} = "))
                except ValueError:
                    print("input tidak valid, silahkan masukkkan angka!")
            print(f"Array sekarang {a}")

        elif pilihan ==2:
            try:
                index = int(input(f"Masukkan index nilai yang ingin di hapus dari data {a}: "))
                if 0 <= index < len(a):
                    a[index] = 0
                    print(f"Nilai pada index {index} telah dihapus. data sekarang: {a}")
                    a.pop(index)
                else:
                    print("Index tidak ada!")
            except ValueError:
                print("Input tidak valid, silahkan masukkan angka!")

        elif pilihan == 3:
            try:
                grade = int(input("Masukkan nilai yang ingin dicari: "))
                if grade in a:
                    index = a.index(grade) #ini buat ngasih tau index dari nilai yang dicari
                    print(f"Nilai {grade} ditemukan pada index {index} dengan address {id(a[index])}")
                else: 
                    print(f"nilai {grade} tidak ditemukan!")
            except ValueError:
                print("Input tidak valid, Silahkan masukkan angka!")

        elif pilihan == 4:
            for i in range(len(a)):
                print(f"nilai mahasiswa ke- a[{i}] = {a[i]} dengan address {id(a[i])}")
        elif pilihan == 5:
            program = False
            print("Program Selesai. Terimakasih:)")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__": #ini buat ngecek apakah file ini dijalankan langsung atau diimpor sebagai modul. Jika dijalankan langsung, maka kode di dalam blok ini akan dieksekusi. Jika diimpor sebagai modul, maka kode di dalam blok ini tidak akan dieksekusi.
    main()