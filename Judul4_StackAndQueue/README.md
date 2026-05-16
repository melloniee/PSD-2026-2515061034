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

<img width="754" height="247" alt="image" src="https://github.com/user-attachments/assets/9f6f3d90-6c2c-4189-b48c-43108b0b2cbe" />

baris 14 merupakan fungsin enqueue dengan parameter self dan x 

baris 15 berfungsi untuk menyimpan node baru yaitu x dalam variabel new_node

baris 16 berfungsi untuk mengecek apakah antrian kosong

baris 17 dan 18 berfungsi jika kondisi 16 terpenuhi, dimana jika antrian kosong maka pointer di depan (front) dan di  belakang (rear) akan menuju ke new node 

baris 20 berfungsi untuk kondisi ke 2

baris 21 berunngsi jika antrian tidak kosong, maka pointer belakang (rear) akan beralih ke node selanjutnya. karena itu buat .next, node baru akan ditambahkan di bagiann belakang antrian 

baris 22 berfungi untuk memindahka pointer rear ke node baru, karena node baru sudah menjadi elemen paling belakang  

baris 23 berfungsi untuk memberikan output dari operasi enqueue atau penambahan data 

<img width="541" height="274" alt="image" src="https://github.com/user-attachments/assets/9efa7c61-deac-44c2-9d01-b0e8ec94439b" />

baris 25 berfungsi melakukan operasi hapus yaitu  dequeue

baris 26 berfungsi untuk mengecek apakah antrian ini kosong 

baris 27 jika antrian kosong maka program akan menampilkan pesan "antrian saat ini kosong" 

Baris 28 berfungsi untuk menghentikan proses function apabila antrian kosong, sehingga proses dequeue tidak dapat dilanjutkan.

baris 29 berfungsi sebagai tempat penyimpanan sementara node yang akan di hapus (front) 

baris 30 berfungsi untuk memindahkan pointer front ke node berikutnya, sehingga node paling depan dianggap sudah terhapus 




