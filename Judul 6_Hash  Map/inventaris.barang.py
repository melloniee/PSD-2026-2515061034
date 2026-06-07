class Node:
    def __init__(self, key, value): 
        self.key = key 
        self.value = value 
        self.next = None 


class HashMapSeparateChaining: 
    def __init__(self, size=10): #size bisa di kustom
        self.SIZE = size 
        self.table = [None] * self.SIZE #kosongkan semua slot dengan None

    def hash_function(self, key):
        total = 0
        for char in str(key):
            total += ord(char)
        return total % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key) #masukin hash functinnnya
        current = self.table[index] #menentukan nilai awalnya 
        while current is not None: 
            if current.key == key: #kalo sama di update value nya
                current.value = value 
                return
            current = current.next #current = saat ini, current.next = yang berikutnya
        new_node = Node(key, value) 
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key): 
        index = self.hash_function(key)
        current = self.table[index]
        while current is not None:
            if current.key == key: 
                return current
            current = current.next
        return None #kalo ga ketemu, return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None #nilai sebelumnya 
        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next #nilai prev sekarang ke current 
                return True
            prev = current
            current = current.next
        return False

    def display(self):
        print("\n==Stok Barang di Gudang==")
        for i in range(self.SIZE): #looping sebanyak SIZE untuk menampilkan semua slot
            print(f"{i}: ", end="")

            current = self.table[i] #print indeks ke 1 dulu dst

            while current is not None: #jika indeks 0 tidak kosong 
                print(f"({current.key},{current.value}) -> ", end="") 
                current = current.next #mengalamai inkremen 
            print("Tidak ada barang")


def main():
    gudang = HashMapSeparateChaining()
    gudang.insert("Pena", 12)
    gudang.insert("Buku", 50)
    gudang.insert("Penghapus", 13)
    gudang.insert("Pensil", 40)
    gudang.insert("Penggaris", 10)
    gudang.insert("Spidol", 15)
    gudang.insert("Kertas", 100)
    gudang.insert("Gunting", 22)
    gudang.insert("Stapler", 5)
    gudang.insert("Klip", 100)
    gudang.insert("Kalkulator", 7)
    gudang.display()

    while True:
        print("\nMenu:")
        print("1. Cari Stok Barang")
        print("2. Hapus Barang")
        print("3. Tampilkan Stok Barang")
        print("4. Keluar")

        pilih = input("Pilih menu (1-4): ")
        if pilih =='1':
            nama_barang = input("Masukkan nama barang yang ingin dicari: ")
            hasil = gudang.search(nama_barang)
            if hasil is not None:
                print(f"Stok {nama_barang} tersedia sebanyak {hasil.value} unit.")
            else:
                print(f"{nama_barang} tidak ditemukan di gudang.")

        elif pilih == '2':
            nama_barang = input("Masukkan nama barang yang ingin dihapus: ")
            if gudang.remove_key(nama_barang):
                print(f"{nama_barang} berhasil dihapus dari gudang.")
            else:
                print(f"{nama_barang} tidak ditemukan di gudang.")
        elif pilih == '3':
            gudang.display()
        elif pilih == '4':
            print("Terima kasih telah menggunakan sistem inventaris.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
if __name__ == "__main__":
    main()