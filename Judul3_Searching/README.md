# SISTEM PENCARIAN DATA MAHASISWA 

## DESKRIPSI PROGRAM

Program ini merupakan implementasi algoritma searching menggunakan bahasa Python untuk melakukan pencarian data mahasiswa. Data mahasiswa disimpan dalam struktur tuple yang berisi nama, IPK, dan program studi. Program ini menyediakan fitur pencarian berdasarkan nama mahasiswa maupun program studi menggunakan metode Sequential Search. Metode sequential search ini adalah metode yang melakukan pencarian data dengan memeriksa data satu persatu hingga target ditemukan

Pada proses pencarian, program akan memeriksa data secara berurutan dari awal hingga akhir hingga data yang dicari ditemukan. Jika data ditemukan, program akan menampilkan informasi mahasiswa beserta jumlah data yang sesuai. Jika data tidak ditemukan, program akan menampilkan pesan bahwa data tidak tersedia. 

## SOURCE CODE

<img width="366" height="68" alt="image" src="https://github.com/user-attachments/assets/8269bc79-1910-47de-bd93-16499000765c" />
Baris pertama menunjukkan program akan dimulai dan menampilkan kalimat "Selamat datang....."

<img width="539" height="109" alt="image" src="https://github.com/user-attachments/assets/b63539dc-6718-4d4a-a0a9-ae62afe26e5b"
baris 3 merupakan fungsi untuk mencari data berdasakan prodi 

baris 4 adalah array rsult yang akan menyimpan hasilnya

baris 5 adalah variabel counter yanhg berfungsi untuk menyimpan seberapa banyak data yang ditemukan  

<img width="753" height="160" alt="image" src="https://github.com/user-attachments/assets/b64c4ad4-dd69-4463-baa6-f7a407fe14e4" />

baris 7 merupakan kondisi perulangan jika item terdapat  di variabel data, dan mengambil data satu persatu

baris 8 befungsi jika item indeks ke 2 yaitu program studi sama dengan program studi yang dicari 

baris 9 berfungsi untuk menambahkan item ke dalam array result

baris 10 merupakan counter dimana jika data ditemukan maka counter akan bertambah 1 

![Uploading image.png…]()

baris 12 -13 yaitu pengkondisian dinnana jika counter lebih besar dari 0 maka program akan menampilkan data dan ditemukan sebanyak berapa kali (counter)

baris 14 - 15 maksudnya adalah untuk setiap item dalam array result maka program akan menampilkan nama, ipk dan program studi

baris 16-17 berfungsi jika kesemua data tidak ada, maka program akan menampikkan data tidak ditemukan

baris 19 berfungsi untuk mengembalikan nilai dari result







