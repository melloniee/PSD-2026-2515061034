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

<img width="488" height="325" alt="image" src="https://github.com/user-attachments/assets/ad01bcac-4ae5-485e-9846-04ea101b6f05" />

baris 19 berfungsi untuk membuat fungsi insert untuk menambahkan data 

baris 20 berfungsi untuk mengubah key menjadi huruf kecil

baris 22 untuk memasukkan fungsi hash

baris 23 untuk menentukan nilai awal

baris 24 merupakan loop while, dan mengecek kondisi current tidak kosong

baris 25 jika current tidak kosong, maka update key nya

baris 26 sama dengan baris 25 update value nya

baris 27 berfungsi untuk keluar dri loop setelah update

baris 28 berfungsi untuk memindahkan current saat ini ke next

baris 29 membuat node baru dengan key dan value 

baris 30  berfungsi untuk menempatkan node baru ke depan tabel hash

baris 31 berfungsi untuk memasukkan data ke dalam tabel dengan indeks yg sesuai 

<img width="436" height="232" alt="image" src="https://github.com/user-attachments/assets/add2ef94-b1d5-4618-9b06-06fda16dadde" />

baris 33 membuat fungsi search

baris 34 berfungsi untuk mengubah key menjadi huruf kecil

baris 36 untuk memasukkan fungsi hash

baris 37 untuk menentukan nilai awal

baris 38 merupakan perulangan while dan mengecek kondisi current not none

baris 39 dan 40 jika key ditemukan pada curent saaat ini maka akan menampilkan nilai tsb

baris 41 berfungsi jika key yg dicari tidak ada di current saat ini maka pencarian dilanjutkan kan current selanjutya

baris 42 jika key tidak ada pada data

<img width="613" height="368" alt="image" src="https://github.com/user-attachments/assets/33248c6d-11c5-459e-b724-5e99591f309e" />

baris 44 merupakan fungsi remove

baris 45 untuk mengubah key menjadi huruf kecil

baris 47 untuk memasukkan fungsi hash

baris 48 untuk menentukan nilai awal

baris 49 berfungsi untuk menginisialisasi nilai sebelumnya

baris 50 merupakan loop while dan mengecek kondisi current tidak kosong

baris 51 jika current saat ini sama dengan key (*data yg dicari) maka key akan dihapus

baris 52  - 53 jika nilai sebelumnya kosong maka nilai pada tabel hash skrg akan berpindah ke current selannjutnya 

baris 54 merupakan kondisi else

baris 55 berfungsi untuk memetakan nilai prev sekarang ke current selanjutnya 

baris 56 berfungsi untuk menghapus

baris 57 nilaii prev sekarang adalah current saat ini

baris 58 current saat ini akan berpindah ke current selanjutya 

baris 59 jika data kosong maka akan return false, loop akan berhenti

<img width="769" height="301" alt="image" src="https://github.com/user-attachments/assets/beb29ad4-156b-4c31-b3b6-4e81223d95aa" />

baris 61 merupakan fungsi display

baris 62 untuk menunjukkan output stok barang 

baris 63 berfungsi untuk looping sebanya size

baris 64 menampilkan isi data 

baris 65 current saat ini akan menampilkan data dari indeks ke1 dulu 

baris 67 - 68 jika current saat ini kosong, maka akan mengeluarkan output "tidak ada barang"

baris 69 - 70 kondisi selanjutnya jika current tidak kosong 

baris 71 print key dan value nya

baris 72 current akan mengalami inkrement dan mengulangi alur yg sama 

baris 73 jika current kosong maka akan menampilkan "null"

<img width="433" height="399" alt="image" src="https://github.com/user-attachments/assets/7ffaa8ed-0daf-4c90-99e0-a49544d6cf1a" />

baris 76 meupakan fungsi main

baris 77 - 92 merupakan data yg disimpan 

<img width="567" height="149" alt="image" src="https://github.com/user-attachments/assets/e5fc32ff-510a-46eb-bf91-e4c2281837a4" />

baris 94 merupakan perulangan while jika kondisi true

baris 95 - 99 merupakan tampilan menu yg ada pada sistem 

<img width="902" height="197" alt="image" src="https://github.com/user-attachments/assets/fb27e9e4-93bc-44d9-b42e-a9da67e592b5" />

baris 101 berfungsi untuk menampilkan pilihan menu dan menyimpannya dalam variabel pilih

baris 102 jika user memilih menu 1

baris 103 user diminta untui memasukkan nama barang yang ingin dicari dan akan disimpan dalam variabel nama_barang

baris 104 untuk memanggil fungsi search dan disimpan dalam variabel hasil

baris 105 - 106 jika hasil tidak kosong, maka akan menampilkan stok 

baris 107 - 108 jika hasil kosong maka akan menampilkan data tidak ditemukan

<img width="861" height="146" alt="image" src="https://github.com/user-attachments/assets/bd1b4d10-dac0-4c5b-9b3b-edbaa487987d" />

baris 110 jika user memilih menu 2

baris 111 user diminta untuk memasukkan nama barang yang akan dihapus

baris 112 memanggil fungsi remove untuk menghapus data yg diminta

baris 113 menampilkan output data berhasil dihapus

baris 114 - 115 jika data tidak ditemukan

<img width="355" height="51" alt="image" src="https://github.com/user-attachments/assets/86f36015-b8f9-4fbc-86a0-2ae1084233b6" />

baris 116 jiika user memilih menu ke 3

baris 117 memanggil fungsi display

<img width="816" height="166" alt="image" src="https://github.com/user-attachments/assets/e5f213b8-3ec7-486d-8563-0fe13236f93b" />

baris 118 jika user memilih menu ke 4

baris 119 - 120 akan keluar program dan prpgram berhenti

baris 121 - 122 jika user menginputkan angka pada menu tidak sesuai

baris 123- 124 berfungsi untuk memanggil fungsi main dan memastikan fungsi berjalan kektika file di eksekusi

## OUTPUT

<img width="595" height="855" alt="image" src="https://github.com/user-attachments/assets/36564432-e10c-4abc-bc6a-32e630e23c3d" />

ini merupakan output ketika sistem berjalan normal

<img width="388" height="126" alt="image" src="https://github.com/user-attachments/assets/0eef5ac3-9731-4090-8800-e7fd7a7e117f" />

output ketika tidak memilih menu yg benar

<img width="355" height="139" alt="image" src="https://github.com/user-attachments/assets/b8958e2a-6287-4dab-8fd2-65e99c3b74b4" />

output ketika barang tidak ditemukan 

## YOUTUBE 












