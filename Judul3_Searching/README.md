# SISTEM PENCARIAN DATA MAHASISWA 

## DESKRIPSI PROGRAM

Program ini merupakan implementasi algoritma searching menggunakan bahasa Python untuk melakukan pencarian data mahasiswa. Data mahasiswa disimpan dalam struktur tuple yang berisi nama, IPK, dan program studi. Program ini menyediakan fitur pencarian berdasarkan nama mahasiswa maupun program studi menggunakan metode Sequential Search. Metode sequential search ini adalah metode yang melakukan pencarian data dengan memeriksa data satu persatu hingga target ditemukan

Pada proses pencarian, program akan memeriksa data secara berurutan dari awal hingga akhir hingga data yang dicari ditemukan. Jika data ditemukan, program akan menampilkan informasi mahasiswa beserta jumlah data yang sesuai. Jika data tidak ditemukan, program akan menampilkan pesan bahwa data tidak tersedia. 

## SOURCE CODE

<img width="591" height="35" alt="image" src="https://github.com/user-attachments/assets/d81f9082-49a3-46d5-9c84-89ffb2c000d1" />

Baris pertama menunjukkan program akan dimulai dan menampilkan kalimat "Selamat datang....."

<img width="376" height="74" alt="image" src="https://github.com/user-attachments/assets/35cafa4c-8830-45b0-bf01-a3867265b214" />

baris 3 merupakan fungsi untuk mencari data berdasakan prodi 

baris 4 adalah array rsult yang akan menyimpan hasilnya

baris 5 adalah variabel counter yanhg berfungsi untuk menyimpan seberapa banyak data yang ditemukan  

<img width="541" height="104" alt="image" src="https://github.com/user-attachments/assets/e8e1827d-c203-4b67-ac33-5584914b4faa" />

baris 7 merupakan kondisi perulangan jika item terdapat  di variabel data, dan mengambil data satu persatu

baris 8 befungsi jika item indeks ke 2 yaitu program studi sama dengan program studi yang dicari 

baris 9 berfungsi untuk menambahkan item ke dalam array result

baris 10 merupakan counter dimana jika data ditemukan maka counter akan bertambah 1 

<img width="791" height="205" alt="image" src="https://github.com/user-attachments/assets/9086c17a-da67-4ea0-9df9-85545fde1710" />

baris 12 -13 yaitu pengkondisian dinnana jika counter lebih besar dari 0 maka program akan menampilkan data dan ditemukan sebanyak berapa kali (counter)

baris 14 - 15 maksudnya adalah untuk setiap item dalam array result maka program akan menampilkan nama, ipk dan program studi

baris 16-17 berfungsi jika kesemua data tidak ada, maka program akan menampikkan data tidak ditemukan

baris 19 berfungsi untuk mengembalikan nilai dari result

<img width="559" height="191" alt="image" src="https://github.com/user-attachments/assets/a1e3e8ac-8acc-4270-acd1-bbd9cc8a4d1d" />

baris 21 merupakan fungsi untuk mencari data berdasarkan nama dengan parameter data dan target nama

baris 22 merupakan tempat menyimpan data dalam array result

baris 23 merupakan counter yang digunakan untuk mengetahui seberapa banyak data ditemukan

baris 25 merupakan kondisi perulangan jika item terdapat  di variabel data, dan mengambil data satu persatu

baeis 26 berfungsi untuk membandingkan apakah item indeks ke 0 yaitu nama sama dengan nama yang ingin dicari 

baeis 27 berfungsi untuk menambahkan item ke dalam data result

baris 28 counter sama seperti baris 10 dia befungsi untuk mengetahui data yg sama muncul berapa kali

<img width="702" height="189" alt="image" src="https://github.com/user-attachments/assets/6b3af1be-eefc-4c39-9b4e-429db6a7887f" />

baris 30-31 merupakan pengondisian apakah counter lebih besar  dari 0 maka program akan menampilkan data berupa nama dan ditemukan sebanyajk berapa kali 

baris 32-33 befungsi untuk menampilkan hasil jika data sudah ditemukan, program akan menampilkan nama, ipk dan prodi

baris 34-35 merupakan kondisi  terakhr dimana jika data tidak ditemukan maka sistem akan menampilkan data tidak ditemukan 
  
baris  37 befungsi untuk menghembalikan nilai result

<img width="560" height="375" alt="image" src="https://github.com/user-attachments/assets/b15d0fe2-ff04-4b8f-8bfb-3ba4a4f9b7f4" />

baris 39 merupakan fungsi main yg dimana didalamnya terdapat alur sistemnya

baris  40-54 merupakakan array berisi data

<img width="667" height="216" alt="image" src="https://github.com/user-attachments/assets/167efa1c-7b27-4619-89bf-179281305e34" />

baris 56 merupakan  perulangan while : true, jika keadaan benar maka fungsi akan berjalan

baris 57-62 berfungsi menampilkan menu dari sistem 

baris 64 berfungsi untuk meminta input dari user  terkait menu  yg akan dipilih dan disimpan dalam variabel pilihan

<img width="674" height="256" alt="image" src="https://github.com/user-attachments/assets/443cdcb9-5b07-43eb-ab60-341d6263118a" />

baris 66 - 67 merupakan pengkondisian jika memilih menu 1 maka sistem akan meminta input berupa program studi tujuan dan disimpan dalam variabel target_prodi

baris 68 berfunngsi untuk memanggil fungsi dari cari_prodi

baris 69 - 70 adalah pengkondisian jika user memilih 2, maka sistem akan meminta inputan data berdasarkan nama dan disimpan dalam variabel target_nama

baris 71 berfungsi untuk memanggil fungsi cari_nama

baris 72 - 73 merupakan pengkondisian jika user memilih menu ke 3, maka sistem akan menampilkan output "Terimakasih"

baris 74 yaitu break, berfungsi untuk menghentikan looping

baris 75 - 76 merupakan penngkondisian terakhir jika input yang dimasukkan oleh user  tidak sesuai dengan menu, maka akan tampil "Pilihan tidak valid"

<img width="603" height="35" alt="image" src="https://github.com/user-attachments/assets/80033b7e-2e67-4e45-8667-7b250e1200a8" />

baris 78 berfungsi untuk meminta user menekan enter guna melanjutkan program dan kembali menampilkan menu

<img width="322" height="92" alt="image" src="https://github.com/user-attachments/assets/082950ca-cab3-4454-8fad-402aa0e71b69" />

baris 80 - 81 berfungsi untuk memanggil fungsi main agar program dapat berjalan

## OUTPUT

<img width="511" height="140" alt="image" src="https://github.com/user-attachments/assets/6d15991c-f448-4dc3-817f-da41660eb57b" />

Ini merupakan output tampilan awal ketika code di run

<img width="394" height="188" alt="image" src="https://github.com/user-attachments/assets/bb8aa35b-2728-4bc5-9f72-659ad0270ac3" />

ini  merupakan output ketika user memilih menu 1 dan akan menampilkan data teknik elektro

<img width="471" height="99" alt="image" src="https://github.com/user-attachments/assets/18da38e0-d53f-45ef-ace8-d835e6d59376" />

ini merupakan output ketika kita menekan enter untuk melanjutkan program

<img width="521" height="166" alt="image" src="https://github.com/user-attachments/assets/7c5393d9-5c7a-454d-a897-5856ce59cd05" />

ini merupakan output ketika user memilih menu ke 2 dan mencari berdasarkan nama

<img width="391" height="48" alt="image" src="https://github.com/user-attachments/assets/90f5d90a-aa0e-4b54-b234-df8de0e027dc" />

ini merupakan kondisi output ketika memilih menu 1 berdasarkan prodi, maka akan menampilkan keseluruhan data yang terkait dengan prodi tujuan 

<img width="422" height="170" alt="image" src="https://github.com/user-attachments/assets/7966ff4f-2798-47cd-9f0b-6418e4b4e4be" />

ini merupakan output ketika user memilih 3, maka program akan berhenti 

# LINK  VIDEO YOUTUBE 
https://youtu.be/c0XQ9Hcs2-M













