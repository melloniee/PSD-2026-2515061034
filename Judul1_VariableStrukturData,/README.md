 # Manajemen Data Nilai Mahasiswa

## DESKRIPSI PROGRAM
Program ini adalah implementasi dari struktur data array 1 dimensi menggunakan bahasa python. Program ini digunakan untuk menyimpan dan mengelola sekumpulan data nilai siswa dalam satu variabel. Dalam pprogram ini, setiap nilai disimoan dalam sebuah array yang memiliki index tertentu, sehingga memudahkan proses pengolahan data secara terstruktur. 

Program ini dibuat untuk melakukan operasi dasar pada array, seperti menambahkan data nilai mahasiswa ke dalam list, menghapus nilai berdasarkan index, mencari nilai tertentu dan menampilkan seluruh data nilai yang tersimpan. Selain itu program ini juga dapat menampilkan addres atau  alamat memori dari tiap elemen sehingga pengguna dapat memahami bagaimana data disimpan dalam memori komputer. 

## Source Code
<img width="597" height="187" alt="image" src="https://github.com/user-attachments/assets/2a3c867b-31a6-468e-98ad-2b1b385a30b9" />

Baris pertama berfungsi untuk menampilkan output "Manajemen Data Nilai Mahasiswa"

baris 3 berfungsi untuk membuat fungsi yang bernama menu

baris 4 hingga 8 untuk menampilkan isi dari funsi menu pada baris 3


<img width="406" height="136" alt="image" src="https://github.com/user-attachments/assets/177b3d4b-8378-4ccb-9e10-5a6dcac441bf" />

baris 10 berfungsi untuk membuat function (fungsi) main untuk menjalankan program 

baris 11 a = [0] * 6 adalah variabel untuk menyimpan data pada list yang berisi 0 dalam array berjumlah 6

baris 12 berfungsi untuk mengontrol loop pada program. Selama program bernilai True maka loop akan terus berjalan

baris 13 berfungsi untuk menjalankan program utama 

baris 14 menunjukkan jika kondisi true maka akan memanggil fungsi menu

<img width="700" height="122" alt="image" src="https://github.com/user-attachments/assets/df0edb0d-f84b-4c0a-8588-a6cc6a3c5b20" />

baris 15 sampai 19 digunakan untuk menangani kesalahan input dari pengguna. Jika pengguna memasukkan sesuatu selain angka, maka program akan menampilkan pesan error dan meminta input kembali. lalu melanjutkan ke iterasi berikutnya 


<img width="691" height="210" alt="image" src="https://github.com/user-attachments/assets/2c641a58-c40e-42d2-9c2b-59f745f86e87" />


baris 21 dan 22 menunjukkan kondisi (if  -  elif - else) if pilihan == 1: berarti jika pengguna memilih angka 1 maka akan tampil "masukkan 6 nilai mahasiswa"

baris 23 berfungsi untuk melakukan perulangan sebanyak 6 kali 

baris 24 sampai 27 digunakan untuk menangani kesalahan input, jika user memasukkkan nilai selain angka maka akan tampil input tidak valid (27), tetapi jika user memasukkan sebuah angka maka akan muncul tampilan untuk memasukkan nilai mahasiswa (25) dan nilai akan tersimpan dalam variabel a

baris 28 berfungsi untuk menampilkan keseluruhan data yang tersimpan 

<img width="886" height="271" alt="image" src="https://github.com/user-attachments/assets/33ff5539-5938-473b-9acd-f56ae5556a7b" /> 

baris 30 menunjukkan pengkondisian jika memilih menu ke 2

baris 31 digunakan untuk menangani kesalahan input 

baris 32 berfungsi untuk meminta pengguna memasukkan nilai yang ingin dihapus, lalu nilai nanti akan disimpan dalam variabel index

baris 33 befungsi untuk memastikan bahwa index yang dimasukkan berada dalam rentang yang valid yaitu dari  0 sampai panjang list a 

baris 34 berfungsi untuk menggantikan index yang dihapus dengan 0

baris 35 berfungsi untuk menampilkan hasil dari nilai yang dihapus dari data

baris 36 merupakan operasi hapus dalam list 

baris 37 dan 38 digunakan jika user memasukkan index yang tidak valid 

baris 39 sampai 40 befungsi untuk menampilkan pesan error jika user memasukkan data tidak berupa angka 

<img width="980" height="239" alt="image" src="https://github.com/user-attachments/assets/bc0ab165-91f3-45e2-ab7d-eaade3f88a5e" />

baris 42 menunjukkan pengkondisian jika memilih menu ke 3

baris 43 berfungsi untuk menangani kesalahan input oleh user

baris 44 berfungsi untuk menampilkan input untuk memasukkan nilai yang ingin dicari, dan disimpan dalam variabel grade 

baris 45 befungsi untuk memastikan bahwa nilai yang dimasukkan oleh user ada dalam list a

baris 46 digunakan untuk mencari indeks pertama dari nilai yang ingin dicari dalam list a. jika ditemukan maka index akan mengembalikan nilai tersebut 

baris 47 berfungsi untuk menampilkan nilai yang dicari terdapat pada index berapa dan menunjukkan alamat data itu disimpan (menggunakan 'id' untuk mencari address)

baris 48 dan 49 menunjukkan jika nilai yang diinputkan oleh user tidak tedapat  dalam list a 

baris 50 dan 51 berfungsi untuk menampilkan kesalahan input jika user memasukkan nilai tidak berupa angka, maka sistem akan menampiljan pesan "input tidak valid"


<img width="816" height="101" alt="image" src="https://github.com/user-attachments/assets/976cdca9-39d7-45dc-8ce8-9e887b5fba9b" />

baris 53 merupakan pengkondisian jika user memilih menu ke 4 yaitu menampilkan semua nilai dengan addressnya 

baris 54 merupakan perulangan untuk menampilkan nilai mahasiswa sejumlah panjang dari list a

baris 55 berfungsi untuk menampilkan keseluruhan nilai dari  list a dengan addressnya ('id') 

<img width="504" height="155" alt="image" src="https://github.com/user-attachments/assets/7fa05077-cd57-4937-9c02-186e8dd42028" />

baris 57 merupakan pengkondisian jika user memilih menu ke 5  yaitu "keluar"

baris 58 'program = False' berfungsi untuk menghentikan loop  while karena kondisi sudah false

baris 59 berfungsi untuk menampilkan pesan 'program selesai'

baris 60 'break' digunakan untuk keluar dari loop while 

baris 61 dan 62 berfungsi sebagai pengkondisian terakhir (else) jika user tidak menginputkan angka pada menu yang tertera maka sistem akan menampilkan 'pilihan tidak valid'

<img width="313" height="88" alt="image" src="https://github.com/user-attachments/assets/41e0c3c1-448e-4f39-8010-b72bc575fd55" />

baris 64 dan 65 menunjukkan kapan sebuah fungsi dijalankan 'main'







