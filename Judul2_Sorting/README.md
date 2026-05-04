
# SISTEM PENGURUTAN KEUNTUNGAN SAHAM 

## DESKRIPSI PROGRAM

Program ini merupakan implementasi algoritma sorting menggunakan yaitu insertion sort dengan bahasa pemrograman Python. Program ini digunakan untuk mengurutkan data keuntungan saham yang disimpan dalam struktur data array. Setiap elemen data direpresentasikan dalam bentuk pasangan (tuple) yang terdiri dari nama saham dan nilai keuntungan. Algoritma Insertion Sort bekerja dengan cara mengambil satu elemen sebagai key, kemudian membandingkannya dengan elemen-elemen sebelumnya. Jika ditemukan elemen yang lebih besar, maka elemen tersebut akan digeser ke kanan untuk memberikan ruang. Proses ini dilakukan berulang hingga posisi yang tepat untuk key ditemukan, kemudian nilai tersebut disisipkan pada posisi tersebut.

Program ini dibuat untuk dapat menerima input data dari pengguna, kemudian menampilkan data sebelum dilakukan proses pengurutan. Setelah itu, program akan mengurutkan data berdasarkan nilai keuntungan menggunakan algoritma Insertion Sort, dan menampilkan hasil akhir berupa data yang telah tersusun dari nilai terkecil hingga terbesar.

## SOURCE CODE

<img width="741" height="100" alt="image" src="https://github.com/user-attachments/assets/29f4a6cb-4407-47bf-9e62-7c889da6f6ee" />

baris 1 merupakan fungsi main dimana kita akan membuat program didalam fungsi tersebut

baris 2 - 4 befungsi untuk menampilkan tulisan awal program yaitu "SELAMAT DATANG DI SISTEM PENGURUTAN KEUNTUNGAN SAHAM" 

<img width="453" height="258" alt="image" src="https://github.com/user-attachments/assets/ee633881-2926-41be-874d-c649d93d394f" />

baris 6 meupakan fungsi dari insertion sort, dimana kita akan menjalankan logika dari insert sort di dalam fungsi tersebut

baris 7 merupakan kondisi  perulangan dimana program akan memulai atau mengambil data dari indeks ke 1 sampai panjang (data), kenapa tidak dari indeks ke 0? karena dalam insertion sort indeks ke 0 dikatakan sudah terurut.

baris 8 terdapat variabel key, variabel ini berguna untuk menyimpan data sementara dari data[i] sebelum dibandingkan 

baris 9 yaitu j = i -1, j disini sebagai pembanding, lalu indeks ke i (mewakili elemen baru) dikurangi dengan 1 karena kita  akan menggeser elemen dari ujung kanan ke kiri. Nilai  -1 memastikan jika j dimulai dari indeks sebelum i 

baris 11 merupakan perulangan while True. j >= 0 and data[j][1] > key[1]:  disini jika nilai j itu lebih besar dari 0 maka akan dibandingkan lagi apakah j indeks pertama lebih besar dari key indeks pertama. [1] ini maksudnya adalah program akan mengambil nilai dari indeks pertama yaitu nilai dari harga, kita akan mengurutkan dari harga bukan dari nama sahamnya

baris 12 berfungsi untuk menggeser data j ke sebelah kanan dan menggantikan dengan nilai dari j tersebut

baris 13 berfungsi untuk mengurangi j dengan 1 sehingga elemen akan bergeser ke kiri agar dapat membandingkan elemen sebelumnya, akan terus bergeser hingga stop

baris 15 berfungsi  untuk memggeser data j ke kanan dan menggantikannya dnegan nilai dari variabel key 

<img width="594" height="61" alt="image" src="https://github.com/user-attachments/assets/7a8eb603-1b72-4bf5-bfe1-00ace308ce3d" />

baris 17 berfungsi untuk meminta input dari pengguna untuk memasukkan jumlah saham yang diinginkan dan akan disimpan dalam variabel x

baris 18 merupakan array yang menyimpan data saham nya 

<img width="435" height="125" alt="image" src="https://github.com/user-attachments/assets/f564804b-1121-43fb-a130-d7c74b873cdf" />

baris ke 20 merupakan perulangan for yg akan mengulang perintah selanjutnnya sebanyak data x

baris 21 dan 22 berfungsi untuk meminta input nama dan harga dari pengguna 

baris 23 berfungsi untuk menambahkan data dari nama dan harga ke dalam array data_saham dengan operasi append

<img width="390" height="85" alt="image" src="https://github.com/user-attachments/assets/f2c0d007-554e-491b-9d51-00dd550c4638" />

baris 25 berfungsi untuk menampilkan "data sebelum terurut"

baris 26 merupakanb perulangan for dimana akan menampilkan nama dan harga sesuai dengan jumlah di array data_saham

baris 27 berfungsi untuk menampilkan nama dan harga

<img width="301" height="37" alt="image" src="https://github.com/user-attachments/assets/cc9295a0-042a-49dd-a5ee-5baca243cb61" />

baris 29 berfungsi untuk memanggil fungsi insert sort untuk mengurutkan data dari data_saham secara ascending 

<img width="612" height="74" alt="image" src="https://github.com/user-attachments/assets/648d061b-fda7-4a54-b6d4-60f2a23bbced" />

baris 31 befungsi untuk menampilkan saham dari yang terkecil hingga terbesar

baris 32 merupakan perulangan for dimana akan menampilikan data yang sudah terurut dari data_saham

baris 33 akan menampilkan data berupa nama dan nilai keuntungan saham yang  sudah terurut

<img width="289" height="72" alt="image" src="https://github.com/user-attachments/assets/a025c1db-55c6-4f74-afcd-b7a8f1d0ec6b" />

baris 35 dan 36 ini berfungsi untuk menampilkan dan memanggil fungsi main yang digunakan oleh program

# OUTPUT

<img width="580" height="84" alt="image" src="https://github.com/user-attachments/assets/89331235-4723-45dc-a28c-7e93911d7872" />
ini merupakan tampilan awal ketika code di running dan user memasukkan jumlah saham yang inign diurutkan 

<img width="421" height="204" alt="image" src="https://github.com/user-attachments/assets/47bfbf53-e50c-4310-861d-441f47b29703" />
ini merupakan output dari nilai yang user inputkan kedalam sistem 

<img width="282" height="104" alt="image" src="https://github.com/user-attachments/assets/80e2d9c6-7bda-4843-b07d-b0993b760a38" />
ini output dari data yang belum terurutkan 

<img width="520" height="114" alt="image" src="https://github.com/user-attachments/assets/eb553a37-7c77-49e1-994a-24d2f7f606b0" />
ini merupakan output dari saham yang sudah diurutkan berdasaerkan nilai keuntungannya 






