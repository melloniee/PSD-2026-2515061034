print("SELAMAT DATANG DI SISTEM PENCARIAN DATA MAHASISWA")

def cari_prodi(data, target_prodi):
    result = []
    counter = 0
    
    for item in data:
        if item[2].lower() == target_prodi.lower():
            result.append(item)
            counter += 1
    
    if counter > 0:
        print(f"Data '{target_prodi}' ditemukan sebanyak {counter} kali")
        for item in result:
            print(f"Nama: {item[0]}, IPK: {item[1]}, Prodi: {item[2]}")
    else:
        print("Data tidak ditemukan!")
    
    return result

def cari_nama(data, target_nama):
    result = []
    counter = 0
    
    for item in data:
        if item[0].lower() == target_nama.lower():
            result.append(item)
            counter += 1
    
    if counter > 0:
        print(f"Data '{target_nama}' ditemukan sebanyak {counter}")
        for item in result:
            print(f"Nama: {item[0]}, IPK: {item[1]}, Prodi: {item[2]}")
    else:
        print("Data Tidak Ditemukan!")
    
    return result

def main():
    data = [
        ("Zahra", 3.7, "Teknik Informatika"),
        ("Fahra", 3.7, "Teknik Informatika"),
        ("Ardandy", 3.5, "Teknik Elektro"),
        ("Alfay", 3.6, "Teknik Elektro"),
        ("Adrian", 3.8, "Teknik Mesin"),
        ("Echa", 3.6, "Teknik Sipil"),
        ("Tara", 3.7, "Teknik Geofisika"),
        ("Cindy", 3.4, "Teknik Informatika"),
        ("Yoga", 3.5, "Teknik Mesin"),
        ("Vivi", 3.5, "Teknik Elektro"),
        ("Zura", 3.7, "Teknik Lingkungan"),
        ("Dzaki", 3.6, "Teknik Sipil"),
        ("Okta", 3.8, "Teknik Informatika")
    ]                                                    

    print(f"{data}")
    
    while True:
        print("======================================")
        print("MENU")
        print("1. Cari Berdasarkan Program Studi")
        print("2. Cari Berdasarkan Nama")
        print("3. Keluar")
        print("======================================")

        pilihan = input("Masukkan pilihan anda: ")
        
        if pilihan == "1":
            target_prodi = input("Masukkan Program Studi Tujuan: ")
            cari_prodi(data, target_prodi)
        elif pilihan == "2":
            target_nama = input("Silahkan Masukkan Nama: ")
            cari_nama(data, target_nama)
        elif pilihan == "3":
            print("Terimakasih")
            break
        else:
            print("Pilihan tidak valid!")
        
        input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()
