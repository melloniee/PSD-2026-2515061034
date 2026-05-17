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

baris 32 berfungsi untuk  mengecek apakah setelah dilakukan operasi dequeue antrian akan kosong 

baris 33 berfungsi jika node sebelumnya sudah tidak ada antrian, maka dari itu rear juga harus None, karena antrian sudah kosong

baris 35 berfungsi untuk mengembalikan data node yang sudah terhapus dari queue

<img width="496" height="120" alt="image" src="https://github.com/user-attachments/assets/fc01bc21-ffa3-4932-acd3-8179d9036579" />

baris 37 meruapakan fungsi operasi peek, yaitu melihat elemen teratas tanpa menghapus elemennya 

baris 38 dan 39 berfungsi untuk mengecek apakah antrian kosong dan akan mengembalikan nilai None

baris 40 merupakan fungsi untuk mengembalikan nilai pada front pointer teratas berdasarkan elemen di data 

<img width="494" height="242" alt="image" src="https://github.com/user-attachments/assets/0b10b148-6855-4922-91a7-94065a4d4510" />

baris 42 merupakan fungsi display atau menampilkan semua  data 

baris 43 dan 44 berfungsi untuk memeriksa apakah antrian kosong, jika kosong maka program akan menampilkan output "Antrian Kosong"

baris 45 berfungsi untuk menghentikan function 

baris 46 berfungsi untuk menampilkan antrian saat ini 

baris 47 berfungsi sebagai pointer semenetara untuk transerval yg akan ditelusuri , current = self.front_pointer maksudnya adalah current dimulai dari node paling depan 

baris 48 merupakan perulangan while jika current tidak kosong 

baris 49 berfungsi untuk menampilkan isi node yang sedang ditunjuk current

baris 50 berfungsi untuk menunjuk ke node berikutnya 

baris 51 berfungsi untuk pindah ke baris baru setelah semua data selesai ditampilkan.

<img width="531" height="290" alt="image" src="https://github.com/user-attachments/assets/e16b85d5-4c1a-4107-b905-a4c6dd0ef872" />

baris 53 berfungsi untuk membuat fungsi searching 

baris 54 - 56 berfungsi untuk memeriksa apakah antrian kosong, jika kosong maka program akan menampilkan "Antrian kosong" dan mengembalikan nilai false agar loop berhenti

baris 57 berfungsi untuk menyimpan pointer front sementara 

baris 58 berfungsi sebagai perulangan while jika kondisi terpenuhi atau antrian ada

baris 59 berfungsi untuk memeriksa apakah data yang dicari ada 

baris 60 berfungsi jika data yang dicari ditemukan lalu akan memngembalikan nilai true 

baris 61 berfungsi untuk menunjukkan atau memindahkan pointer current ke node berikutnya

baris 62 - 63 berfungsi jika data yang  dicari tidak ada,  maka program akan mengeluarkan output antrian tidak  ditemukan

baris 64 akan mengembalikan nilai false sehingga loop berhenti

<img width="328" height="104" alt="image" src="https://github.com/user-attachments/assets/fed89cb1-75ef-41e1-9343-da157d5c73b6" />

baris 66 merupakan fungsi utama yaitu fungsi main

baris 67 berfungsi untuk menyimpan queueLinkedlist yang akan disimpan pada variabel queue

baris 68 yaitu menu yang berfungsi menyimpan pilihan user 

<img width="513" height="191" alt="image" src="https://github.com/user-attachments/assets/7ecfa5c3-1e56-44cf-a09a-0e61bc3b441d" />

baris 70 merupakan perulangan while, jika kondisi benar

baris 71 - 77 merupakan menu yang ada pada program

<img width="585" height="133" alt="image" src="https://github.com/user-attachments/assets/874a46a5-ef19-47a1-8f2d-12a6b3853033" />

baris 79 merupakan fungsi try untuk menangani error

baris 80 merupakan fungsi untuk meminta input menu dari user dan akan disimpan pada variabel menu

baris 81 merupakan bagian dari fungsi try yaitu untuk menangani error jika user menginputkan data selain angka

baris 82 ketika error maka akan menampilkan pesan "Tidak valid"

baris 83 merupakan fungsi untuk melanjutkan ke pilihan selanjutnya 

<img width="754" height="262" alt="image" src="https://github.com/user-attachments/assets/d0c1c1e9-462c-407c-96d7-5b0f9335e155" />

baris 85 merupakan kondisi ketika user memilih menu pertama

baris 86 merupakan fungsi try unutk menangani error

baris 87 berfungsi untuk meminta user memasukkan jumlah tiket yang ingin dibeli

baris 88 - 89 merupakan bagian dari fungsi try, dimana ketika user menginputkan data selain angka maka program akan menampilkan pesan tidak valid 

baris 90 berfungsi untuk melanjutkan ke pilihan selanjutnya 

baris 92 berfungsi untuk meminta user menginputkan nama pemesan dan akan disimpan dalam variabel nama 

baris 93 merupakan fungsi queueue, jadi data terbaru akan ditambahkan ke antrian 

baris 94 berfungsi untuk menampilkan jumlah tiket dan nama pemesan 

<img width="636" height="168" alt="image" src="https://github.com/user-attachments/assets/7674eb9b-598b-4ee9-8812-c839d72414f6" />

baris 96 merupakan kondisi jika user memilih menu ke 2

baris 97 merupakan proses dequeue atau menghapus data dari antrian, lalu disimpan dalam variabel proses

baris 99 - 100 berfungsi jika data di variabel proses tidak kosong dan akan menampilkan proses berhasil 

baris 101 berfungsi untuk menampilkan pesan 

<img width="368" height="72" alt="image" src="https://github.com/user-attachments/assets/7a838a38-7c91-4542-bac2-6bb4bc8e0140" />

baris 103 merupakan kondisi ketika user memilih menu ke 3

baris 104 berfungsi untuk memanggil fungsi display, fungsi ini akan menampilkan data yang tersimpan 

<img width="674" height="164" alt="image" src="https://github.com/user-attachments/assets/d4fe90ea-2a34-4c14-9b88-593ed243c4e4" />

baris 106 merupakan kondisi jika user memilih menu ke 4

baris 107 berfungsi mengambil data paling depan dari queue menggunakan method peek() lalu menyimpannya ke variabel front_value

baris 108 - 109 berfungsi untuk mengecek apakah antrian kosong dan jika kosong program akan menampilkan pesan antrian kosong

baris 110 - 111 berfungsi jika terdapat data pada antrian, lalu program akan menampilkan tiker terdepan dengan mengambil data dari front_value

<img width="662" height="215" alt="image" src="https://github.com/user-attachments/assets/45c360d2-eb5d-43d7-8ed6-4b15c3625311" />

baris 113 merupakan kondisi jika user memilih menu ke 5

baris 114 berfungsi untuk meminta user memasukkan nama yang akan dicari dan disimpan dalam variabel cari

baris 116 merupakan proses pencarian dengan memanggil fungsi search dan mengambil data dari variabel cari dan queueu

baris 117 - 118 merupakan kondisi jika hasil ditemukan maka program akan menampilkan data nama yang dicari

baris 119 - 120 merupakan kondisi jika hasil tidak ada, maka program akan menampilkan data tidak ditemukan

<img width="640" height="136" alt="image" src="https://github.com/user-attachments/assets/57c45667-ba9c-4ed4-9c0f-f03da5a36e57" />

baris 122 merupakan kondisi jika user memilih menu ke 6

baris 123 - 124 berfungsi untuk menampilkan pesan terimakasihb dan program akan berhenti karena fungsi break 

baris 125 - 126 berfungsi jika user menginputkan data tidak sesuai dengan ketentuan menu 

<img width="299" height="72" alt="image" src="https://github.com/user-attachments/assets/17fda68c-67b6-478e-a67b-bfb89a28dd5a" />

baris 128 -129 berfungsi untuk memanggil fungsi main agar program dapat berjalan

# OUTPUT

<img width="345" height="187" alt="image" src="https://github.com/user-attachments/assets/3cf75559-9c7b-48b7-9410-11c307fcf753" />
ini merupakan output saat program pertama kali di run

<img width="570" height="115" alt="image" src="https://github.com/user-attachments/assets/02e48243-62a7-446f-a69b-74456886ba98" />
ini merupakan output saat user memilih menu 1 dan memasukkan data yang diminta

<img width="548" height="77" alt="image" src="https://github.com/user-attachments/assets/4a97090a-f0f6-46d8-92ad-bc4165af11f8" />
ini merupakan output saat user memilih menu ke 2 dan prosess tiket dimulai

<img width="769" height="60" alt="image" src="https://github.com/user-attachments/assets/51060be3-6e74-402b-92a0-246ce2a40967" />
ini merupakan output saat user memilih menu ke 3 maka akan tampil urutan antrian tiket

<img width="433" height="48" alt="image" src="https://github.com/user-attachments/assets/f78510c1-7c97-49da-8c66-05df5feffad1" />
ini merupakan output saat user memilih menu ke 4 dan akan tampil urutan terdepan pada antrian

<img width="454" height="73" alt="image" src="https://github.com/user-attachments/assets/5cd5b70a-8e8b-474c-a56c-8d675ffe03b2" />
ini merupakan output saat user memilih menu ke 5 akan tampil data nama pemesan yang dicari

<img width="294" height="45" alt="image" src="https://github.com/user-attachments/assets/f161a9b6-97f7-448f-a191-574e4b79bddb" />
ini merupakan output ketika user memilih menu 6 program akan berhenti 

<img width="459" height="56" alt="image" src="https://github.com/user-attachments/assets/ad9d68b6-4980-40f9-b007-a4ec6bc8b980" />
ini merupakan output jika input user tidak sesuai dengan yang program minta, maka code try - except akan bekerja 

<img width="394" height="49" alt="image" src="https://github.com/user-attachments/assets/236a2b65-0e09-49cb-a265-5bcd4cbcb242" />
ini kondisi jika user salah menginputkan angka untuk menu 








