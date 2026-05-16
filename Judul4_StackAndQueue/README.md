# ANTRIAN TIKET WAHANA PERMAINAN

## DESKRIPSI SINGKAT PROGRAM
Program ini merupakan implementasi struktur data queue menggunakan bahasa Python untuk mengatur sistem antrian pembelian tiket wahana permainan. Program menggunakan metode Queue Linked List dengan prinsip FIFO (First In First Out), yaitu data yang masuk terlebih dahulu akan diproses lebih dahulu. Setiap data antrian disimpan dalam node yang saling terhubung menggunakan pointer.

Pada prosesnya, program menyediakan fitur untuk menambahkan antrian pembelian tiket, memproses pengambilan tiket, melihat daftar antrian yang sedang berlangsung, serta mengecek antrian terdepan. Program akan memproses data secara berurutan sesuai urutan kedatangan pengguna. Jika antrian kosong, program akan menampilkan pesan bahwa tidak terdapat antrian yang tersedia.

## SOURCE CODE
<img width="439" height="115" alt="image" src="https://github.com/user-attachments/assets/6d6879ee-17c4-4133-9f5d-f2784a63e2d5" />

baris 1 merupakan inisialisasi  dari class Node
baris 2 merupakan fungsi dari node dengan parameter self dan data 
baris 3 berfungsi  untuk menyimpan isi data 
baris 4 berufungsi untuk menjadi penghubung ke node berikutnya, inisialisasi  di awal adalah None

<img width="381" height="115" alt="image" src="https://github.com/user-attachments/assets/a98669c3-3ef4-49fa-8aaf-55d9fa46dace" />

baris 6  merupakan class QueueLinkedlist
baris 7 merupakan contructor  
baris 8 merupakan inisialisasi pointer depan, dimana kondisi awal masi None
baris 9 merupakan inisialisasi pointer dari  belakang, dimana kondisi awal masi None

<img width="452" height="70" alt="image" src="https://github.com/user-attachments/assets/50c95460-895d-4404-ba9f-385c501c0a99" />
baris 11  merupakan fungsi untuk mengecek antrian kosong atau tidak

baris 12 untuk mengembalikan  nilai  mengecek apakah queue masih kosong dengan melihat pointer depannya.


