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

 <img width="735" height="194" alt="image" src="https://github.com/user-attachments/assets/6ca33e64-dc19-45ed-9295-54828c8f7b03" />

 baris 47 - 48 berfungsi untuk menambahkan data dengan key (ID) dan nama 

 baris 50 befungsi untuk mencari nilai minimal dari node

 baris 51 berfungsi untuk menelusuri tree mulai dari root

 baris 52-54 berfungsi untuk mengecek apakah current ini terisi dan currrent sebelah kiri juga terisi, jika ya maka akan dilakukan pencarian di sebelah kiri dan akan mengembalikan nilai current

 <img width="771" height="435" alt="image" src="https://github.com/user-attachments/assets/7fd8545a-2c55-4a26-9e91-f39c8880ccfe" /> 

 baris 56 berfungsi untuk menghapus node dengan key tertentu dari tree

 baris 57-58 berfungsi untuk mengecek apakah root kosong, jika kosong maka akan mereturn None

 baris 59 - 60 befungsi untuk mengecek apakah key lebih kecil dari root tertentu, jika iya maka akan menghapus dibagian kiri

baris 61-62 kondisi untuk mengecek aoakah key lebih besar dari root tertentu, jika ya maka akan dilakukan penghapusan disebelah kanan

baris 63-65 merupakan kondisi dimana jika root kiri dan kanan kosong maka akan mereturn None

baris 66 - 67 berfungsi untuk mengecek apakah root kiri kosong, jika root kiri kosong maka akan menghapus anak kanannya

baris 68-69 befungsi untuk mengcek apakah root kanan kosong, jika kosong maka akan menghapus anak kirinya

baris 70-71 merupakan kondisi terakhir dan menggunakan successor untuk mencari node pengganti ketika node yang akan dihapus memiliki 2 anak, mencari nilai terkecil dari root sebelah kanan

baris 72 berfungsi untuk menggantikan key dengan successor

baris 73- 74 berfungsi untuk menghapus successor setelah menggantikan node yang akan dihapus dan mengenmbalikan nilai root

<img width="606" height="398" alt="image" src="https://github.com/user-attachments/assets/5ad2994c-c6fb-41f8-9a7b-376bf5fdc5a4" />

baris 76 merupakan fungsi untuk menghapus dengan key tertentu 

baris 77 berfungsi untuk menghapus key dalam root 

baris 79 merupakan fungsi untuk menampilkan root

baris 80-82 berfungsi untuk mengecek apakah root kosong, jiika kosong maka akan menampilkan pesan kosong dan return 

baris 83 berfungsin untuk menyimpan nilai dari queue

baris 84 berfungsi untuk menambahkan root kedalam queue

baris 85 - 87 berfungsi sebagai perulangan while jika panjang queue lebih dari 0, maka akan menghapus elemen pertama dan menyimpannya dalam variabel current dan menampilkan nilai dari current tsb

baris 88 - 89 berfungsi untuk mengecek bagian kiri, jika tidak kosong maka akan menambahkan anak kiri ke dalam antrian

baris 90-91 berfungsi untuk mengecek bagian kanan, jika tidak kosong maka akan menambahkan anak ke dallam antrian

baris 92 berfungsi untuk membuat baris baru ketika sudah mencetak semua 

<img width="651" height="416" alt="image" src="https://github.com/user-attachments/assets/11cb7845-781a-43af-bdcf-c405f1ce0672" />

baris 94, merupakan fungsi untuk mencari successor dengan parameter key dan root 

baris 95 berfungsi untuk menyimpan root dalam variabe current

baris 96 menginisialisasikan sucessor itu none

baris 97 - 100 berfungsi untuk mengecek current jika tidak kosong maka akan memeriksa apakah key lebih kecil daripada key yg dituju, maika successor akan digantikan dengan nilai dari  current, dan pada baris 100 current sebelah kiri akan masuk dan disimpan dalam variabel current

baris 101 - 102 berfungsi untuk memeriksa key apakah lebih besar dari current key, jika lebih besar maka akan menggantikan nilai current sebelah kanan

baris 103-104 kondisi terakhir dan akan menghentikan looping 

baris 105 - 106 untuk kondisi current ini None maka akan mereturn False

107 - 108 untuk kondisi anak kanan tidak kosong, maka successor akan mencari node pengganti ketikda node yang akan dihapus memiliki 2 anak, dan mencari node terkecil di subtree kanan

baris 109 - 110 merupakan kondisi dimana sucessor itu kosong , maka akan mereturn None

baris 111 berfungsi untuk mengembalikan node sucessor dan status True

<img width="766" height="491" alt="image" src="https://github.com/user-attachments/assets/d6dadc90-748f-484c-838d-94d8f2e0e6ae" />

baris 113 merupakan fungsi untuk mencari predecessor dengan root dan key

baris 114 berfungsi untuk menelusuri pohon mulai dari rootnya

baris 115 berfungsi untuk inisialisasi predecessor kosong 

baris 116 - 117 berfungsi untuk kondisi current tidak kosong, lalu mengecek apakah key lebih kecil daro current key ini

baris 118 currrent akan mengarahkan ke sebelah kiri

baris 119 











