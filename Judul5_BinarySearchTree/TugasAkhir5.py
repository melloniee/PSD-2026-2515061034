class Node:
    def __init__(self, key, nama):
        self.key = key
        self.left = None
        self.right = None 
        self.nama = nama 
        self.riwayat = StackArray() 

class StackArray:
    def __init__ (self):
        self.stack = []
        return 
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        
    def display(self):
        for item in reversed(self.stack):
            print(item)

class BSTLanjut:
    def __init__(self):
        self.root = None

    def insert_node(self, root, key, nama):
        if root is None:
            return Node(key, nama)
        if key < root.key:
            root.left = self.insert_node(root.left, key, nama)
        elif key > root.key:
            root.right = self.insert_node(root.right, key,nama)
        return root
    
    def insert(self, key, nama):
        self.root = self.insert_node(self.root, key, nama)

    def find_min_node(self, root):
        current = root
        while current is not None and current.left is not None:
            current = current.left
        return current 
    
    def delete_node(self, root, key):
        if root is None:
            return None
        if key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self.find_min_node(root.right)
                root.key = successor.key
                root.right = self.delete_node(root.right, successor.key)
        return root
    
    def delete(self, key):
        self.root = self.delete_node(self.root, key) 

    def level_order(self, root):
        if root is None:
            print("Kosong")
            return
        queue  = []
        queue.append(root)
        while len(queue) > 0:
            current = queue.pop(0)
            print(current.key, end=" ")
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        print()

    def find_successor(self, root, key):
        current = root
        successor = None
        while current is not None:
            if key < current.key:
                successor = current
                current = current.left
            elif key >  current.key:
                current = current.right
            else:
                break
        if current is None:
            return None, False
        if current.right is not None:
            successor = self.find_min_node(current.right)
        if successor is None:
            return None, False
        return successor, True
            
    def find_predecessor(self, root, key):
        current = root
        predecessor = None
        while current is not None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                predecessor = current  # Simpan sebagai kandidat predecessor
                current = current.right
            else:
                break
        if current is None:
            return None, False 
        if current.left is not None:
            temp = current.left
            while temp.right is not None:
                temp = temp.right
            predecessor = temp  # Di luar while, ambil node paling kanan yang mentok
        if predecessor is None:
            return None, False
        return predecessor, True
        
    def search(self, root, key):
        current = root  
        while current is not None:
            if key == current.key:
                return current, True
            elif key < current.key:
                current = current.left
            else:
                current = current.right
        return None, False
    
def main():
    bst = BSTLanjut()
    pilih = 0
    while True:
        print("\n===MENU PENCARIAN ORANG HILANG===")
        print("1. Tambah Data Orang Hilang")
        print("2. Proses Data Orang Hilang")
        print("3. Cari Data Orang Hilang")
        print("4. Tampilkan Semua Data Orang Hilang Dan Riwayat Pencarian Investigasi")
        print("5. Tambah Riwayat Investigasi")  
        print("6. Keluar")

        try:
            pilih = int(input("Masukkan Pilihan Anda:"))  
        except ValueError:
            print("Input tidak valid! Silakan masukkan angka antara 1-7.")
            continue

        if pilih == 1:
            try:
                key = int(input("Masukkan ID Orang Hilang: "))
                nama = str(input("Masukkan Nama Orang Hilang:"))  

                bst.insert(key, nama)
                print(f"Data orang hilang dengan ID {key} atas nama {nama} berhasil ditambahkan.")
            except ValueError:
                print("Input tidak valid! ID harus berupa angka.")

        elif pilih == 2:
            try:
                done = (str(input("Masukkan nama orang hilang yang sudah ditemukuan: "))) 
                print(f"Data orang hilang dengan nama {done} sudah diproses")
                bst.delete(key)
            except ValueError:
                print("Input tidak valid! Nama harus berupa teks.")

        elif pilih == 3:
            try:
                key = int(input("Masukkan ID orang hilang yang ingin dicari: "))
                ans, found = bst.search(bst.root, key)

                if found:
                    print(f"Data orang hilang dengan id -{key} ditemukan dengan  nama {ans.nama}")
                    print("Riwayat Investigasi: ")
                    ans.riwayat.display() #menampilkan riwayat investigasi setelah ditemukan data dengan id yang dicari

                else:
                    print(f"Data orang hilang dengan id {key} tidak ditemukan.")
            except ValueError:
                print("Input tidak valid! ID harus berupa angka.")

        elif pilih == 4:
            print("Data orang hilang: ", end="")
            bst.level_order(bst.root)

            x = int(input("Masukkan ID untuk melihat riwayat investigasi: "))

            pred_successor, found_successor = bst.find_successor(bst.root, x)
            if found_successor:
                print(f"===Riwayat Investigasi setelah ditemukan data dengan ID {pred_successor.key} atas nama {pred_successor.nama}===")
            else:
                print(f"Data orang hilang dengan ID {x} tidak ditemukan atau tidak memiliki successor.")

            pred_predecessor, found_predecessor = bst.find_predecessor(bst.root, x)
            if found_predecessor:
                print(f"===Riwayat Investigasi sebelum ditemukan data dengan ID {pred_predecessor.key} atas nama {pred_predecessor.nama}===")
            else:
                print(f"Data orang hilang dengan ID {x} tidak ditemukan atau tidak memiliki predecessor.")

        elif pilih == 5:
            try:
                key = int(input("Masukkan ID orang hilang untuk menambahkan riwayat investigasi: "))
                riwayat = str(input("masukkan riwayat investigasi: "))

                current = bst.root #current digunakan untuk menelusuri pohon mulai dari root
                while current is not None:
                    if key < current.key:
                        current = current.left
                    elif key > current.key:
                        current = current.right
                    else:
                        current.riwayat.push(riwayat)
                        print(f"Riwayat ditambahkan!")
                        break

                if current is None:
                    print(f"Data orang hilang dengan ID {key} tidak ditemukan.")
            except ValueError:
                print("Input tidak valid! ID harus berupa angka.")

        elif pilih == 6:
            print("Terima kasih telah menggunakan sistem pencarian data orang hilang di Polres DurainRuntuh. Sampai jumpa!")
            break
        else:   
            print("Pilihan tidak valid! Silakan masukkan angka antara 1-6.")

if __name__ == "__main__":
    main()