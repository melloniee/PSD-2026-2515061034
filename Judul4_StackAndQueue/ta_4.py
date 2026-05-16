class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front_pointer = None
        self.rear_pointer = None

    def is_empty(self):
        return self.front_pointer is None
    
    def enqueue(self, x):
        new_node = Node(x)
        if self.is_empty():
            self.front_pointer = new_node
            self.rear_pointer = new_node

        else:
            self.rear_pointer.next = new_node 
            self.rear_pointer = new_node
        print(f"Data {x} berhasil ditambahkan ke antrian!")

    def dequeue(self):
        if self.is_empty():
            print("Antrian kosong saat ini")
            return
        temp = self.front_pointer
        self.front_pointer = self.front_pointer.next

        if self.front_pointer is None:
            self.rear_pointer = None

        return temp.data 
    
    def peek(self):
        if self.is_empty():
            return None
        return self.front_pointer.data

    def display(self):
        if self.is_empty():
            print("Antrian kosong")
            return
        print("Antrian saat ini: ", end="")
        current = self.front_pointer
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

def main():
    queue = QueueLinkedList()
    menu = 0

    while menu != 5:
        print("\n PEMBELIAN TIKET WAHANA PERMAINAN")
        print("1. Pesan Tiket")
        print("2. Ambil Tiket")
        print("3. Lihat Antrian Wahana")
        print("4. Cek Ketersediaan Tiket")
        print("5. Keluar")
        try:
            menu = int(input("Masukkan Pilihan Anda: "))
        except ValueError:
            print("Tidak Valid!")
            continue

        if menu == 1:
                pesan = int(input("Masukkan jumlah tiket yang ingin dibeli: "))
                nama = input("Masukkan nama pemesan: ")
                queue.enqueue(f"{nama} dengan {pesan} ticket")
                print(f"Tiket berjumlah {pesan} atas nama {nama} berhasil dibeli")

        elif menu == 2:
            proses = queue.dequeue()

            if proses is not None:
                print(f"Tiket atas nama {proses} berhasil diproses")

        elif menu == 3:
            queue.display()

        elif menu == 4:
            front_value = queue.peek()
            if front_value is None:
                print("Antrian kosong")
            else:
                print(f"Antrian tiket terdepan: {front_value}")

        elif menu == 5:
            while not queue.is_empty:
                queue.dequeue
            print("Program selesai. Terimakasih!")
        else:
            print("Tidak valid")

if __name__ == "__main__":
    main()  



