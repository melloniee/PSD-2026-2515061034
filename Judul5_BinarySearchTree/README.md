# SISTEM PENCARIAN DATA ORANG HILANG DI POLRES DURIANRUNTUH

## DESKRIPSI SINGKAT PROGRAM
Program ini merupakan sistem pencarian data orang hilang menggunakan metode Binary Search Tree (BST) yang digunakan untuk mengelola data laporan secara terstruktur berdasarkan ID sebagai key. Setiap data disimpan dalam node yang berisi ID, nama orang hilang, serta riwayat investigasi yang dikelola menggunakan struktur Stack agar dapat merekam aktivitas secara berurutan (LIFO). Sistem ini mendukung operasi utama seperti penambahan data (insert), pencarian data (search), penghapusan data (delete), serta penelusuran seluruh data menggunakan traversal level-order. Selain itu, program juga menyediakan fitur untuk menambahkan riwayat investigasi pada setiap node serta mencari posisi predecessor dan successor untuk melihat urutan data sebelum dan sesudah node tertentu dalam BST. Dengan kombinasi BST, Stack, dan Queue, program ini mampu mengelola data secara efisien sekaligus merepresentasikan proses investigasi secara sistematis.

#SOURCE CODE

<img width="570" height="200" alt="image" src="https://github.com/user-attachments/assets/78d4cbb6-2171-4bd8-9bef-69767367c752" />

baris 1 merupakan fungsi dari class Node 

baris 2 berfungsi sebagai konstruktor saat node dibuat, menerima id dan nama 

baris 3 berfungsi untuk menyimpan key pada variabel self.key

baris 4 dan 5 befungsi untuk menginisialiasikan bahwa bagian kanan dan kiri kosong

baris 6 berfungsi untuk menyimpan nama dalam variabel self.nama

baris 7 berfungsi membuat stack untuk menyimpan riawayat investigasi per node

<img width="488" height="120" alt="image" src="https://github.com/user-attachments/assets/b3bf094e-03e4-4897-a817-2772ff54c66a" />

baris 9 merupakan class StackArray

baris 10 befungsi sebagai konstruktor 

baris 11 berfungsi untuk membuat penyimpnana stack kosong

baris 12 befungsi untuk mengembalikan nilai

<img width="504" height="438" alt="image" src="https://github.com/user-attachments/assets/0fcb0d96-e4f9-4079-ac81-c5a2d138c018" />

baris 14 merupakan fungsi untuk mengecek apakah array koosng 

baris 15 menamplkan elemen data 

baris 17 merupakan fungsi push pada array

baris 18 untuk menambahkan data item ke satck

baris 20 merupakan fungsi pop untuk menghapus

baris 21 mengecek stack kosong atau tidak

baris 22 mengembalikan nilai stack yg di hapus

baris 23-24 jika kosong maka mengembalikan None

baris 26 untuk melihat elemen teatas tanpa menghapus

baris 27-28 mengecek stack kosong apa ga, jika tidak kosong maka tampilkan nilai paling atas

baris 30 untuk menampilkan semua data 

baris 31-32 untuk menampilkan data tersimpan dalam reversed dan menampilkan data item tsb

<img width="699" height="270" alt="image" src="https://github.com/user-attachments/assets/e8bde816-c536-4f7f-816f-74571a9ba487" />

baris 34 merupakan class BinarySearchTree Lanjut

baris 35 merupakan konstarktor 

baris 36 merupakan inisialisasi dari root bahwa root kosong

baris 38 berfungsi untuk menambahkan node dengan parameter self, root, key dan nama

baris 39-40 befungsi untuk mengecek apakah root kosong, jika kosong maka akan mereturn node 

baris 41-42 berfungsi jika key lebih kecil dari root.key maka akan ditambahkan ke sebelah kiri tree 

baris 43-44 berfungsi jika key lebih besar dari root.key maka akan ditambahkan di tree sebelah kanan

baris 45 befungsi untuk mengembalikan nilai root

 aris



