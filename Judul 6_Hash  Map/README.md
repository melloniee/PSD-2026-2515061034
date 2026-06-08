# SISTEM INVERNTARIS BARANG

## DESKRIPSI UMUM 
Program ini merupakan implementasi struktur data Hash Map menggunakan metode Separate Chaining dengan bahasa Python. Program digunakan untuk menyimpan dan mengelola data stok barang dalam gudang secara efisien. Setiap data barang terdiri dari nama barang sebagai key dan jumlah stok sebagai value yang disimpan ke dalam hash table berdasarkan hasil fungsi hash.
Program ini dibuat untuk melakukan operasi dasar pada Hash Map, seperti menambahkan data barang, mencari stok barang berdasarkan nama, menghapus data barang, dan menampilkan seluruh data yang tersimpan dalam hash table. Untuk menangani collision yang terjadi ketika beberapa nama barang memiliki indeks hash yang sama, program menggunakan metode Separate Chaining dengan linked list. Selain itu, program juga dapat menampilkan isi hash table beserta distribusi data pada setiap indeks, sehingga pengguna dapat memahami cara kerja Hash Map, proses hashing, serta mekanisme penanganan collision menggunakan linked list.

## SOURCE CODE

<img width="423" height="117" alt="image" src="https://github.com/user-attachments/assets/6b3a28b3-4505-42e6-8dfc-505984a94d8b" />

baris 1 berfungsi untuk membuat Node yang akan digunakan pada linkedlist

baris 2 berfungsi untuk menyimpan key

baris 3 berfungsi untuk menyimpan value

baris 4 berfungsi untuk menginisialisasai data selanjutnya masih kosong 


<img width="488" height="104" alt="image" src="https://github.com/user-attachments/assets/82e96bb5-82e3-4dc8-9b94-acc7c4f3a493" />

baris 8 berfungsi untuk membuat class hashmap 

baris 9 ini buat ukuran hash map default = 10

baris 10 berfusngsi untuk menyimpan size dalam variabel 

baris 11 berfungsi untuk mengosongkan semua slot dengan None


<img width="484" height="122" alt="image" src="https://github.com/user-attachments/assets/f4c82cad-e806-4e15-b2f6-905b31a50247" />

baris 13 berfungsi untuk membuat fungsi hash nya dengan parameter key dan self

baris 14 berfungsi untuk menyimpan total nilai ASCII

baris 15 untuk mengubah key menjadi string dan melakukan looping di tiap hurufnya 

baris 16 untuk menjumlahkan nilai ASCII dari tiap karakter dalam key

baris 17 berfungsi untuk memastikan indeks tidak lebih  dari ukuran tabel




