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

baris 119 berfungsi untuk membandingkan key dengan current key, jika lebiih besar 

baris 120 prodecessor akan menyimpan current 

baris 121 current diarahkan ke kanan

baris 122 - 123 berfungsi untuk menghentikan loop

baris 124 - 125 berfungsi dengan kondisi current kosong, maka akan mereturn None

baris 126 berfungsi untuk mencari node predecessor dri node kunci ke arah kiri

baris 127 telusuri sub tree kanan

baris 128 - 129 berfungsi untuk ketika temp.right tidak kosong, maka akan menulusuri dari kanan

baris 130 predecessor mengambil node paling kanan 

baris 131 - 132 berfungsi jika predecessor kosong, maka akan return false

barsi 133 mengembalkikan nilai predecessor

<img width="558" height="240" alt="image" src="https://github.com/user-attachments/assets/0e9e9c35-c5a3-41b6-a307-2252652c46d0" />

baris 135 merupakan fungsi search dengan root dan key (id)

baris 136 berfungsi untuk menelusuri tree dari root

baris 137 berfungsi jika current tidak kosong

baris 138 - 139 jika key sama dengan key yg dicari, maka akan menampilkan hasilnya dan mereturn TRUE

baris 140 kondisi jika key lebih kecil dari yg dicari

baris 141 current akan menelusuri ke bagian kiri 

baris 142 - 143 kondisi jika key lebih besar, maka akan menelusuri sebelah kanan

baris 144 berfungsi jika root kosong dan akan mereturn False 

<img width="763" height="329" alt="image" src="https://github.com/user-attachments/assets/d846c3c0-f503-40db-930b-3a0ec4483f18" />

baris 146 merupakan fungsi main

baris 147 berfungsi untuk membuat instance dri class BST

baris 148 berfungsi untuk menyimpan pilihan menu

baris 149 merupakan perulangan while 

baris 150 - 156 merupakan menu dari sistem dan akan dijalankan ketika input bernilai True

baris 158 merupakan fungsi try except

baris 159 berfungsi untuk meminta input dari user dan disimpan dalam variabel pilih

baris 160 - 161 berfungsi sebagai penanganan error jika input tidak sesuai

baris 162 berfungsi untuk melanjutkan ke prses selanjutnya

<img width="763" height="180" alt="image" src="https://github.com/user-attachments/assets/ff16603d-a70a-45ee-ae7f-8bfe32ab3203" />

baris 164 merupakan kondisi pilihan 1

baris 165 merupakan penanganan error 

baris 166 berfungsi untuk meminta id dri user dan disimpan dalam key

baris 167 berfungsi untuk meminta nama 

baris 169 berfungsi untuk menambahkan key dan nama ke dalam BST

baris 170 akan menampilkan output berhasil ditambahkan

baris 171 - 172 penanganan error jika input tidak sesuai 

<img width="734" height="144" alt="image" src="https://github.com/user-attachments/assets/a6a171f8-dc3d-44c9-ae6e-23db029c8806" />

baris 174 merupakan pilihan ke 2

baris 175 berfungsi sebagai penanganan error try

baris 176 befungsi untuk meminta input dri user untuk memasukkan nama dan disimpan dalam variabel done

baris 177 akan menampilkan output 

baris 178 berfungsi untuj menghapus key atau yg diminta  user

baris 179 - 180 berfungsi sebagai output jika error

<img width="769" height="257" alt="image" src="https://github.com/user-attachments/assets/5f04c438-1080-42eb-8b70-875fc23ebb66" />

baris 182 merupakan kondisi pilihan ke 3

baris 183 penanganan error

baris 184 berfunggsi untuk meminta user menginputkan id yg ingin dicari 

baris 185 berfungsi memanggil fungsi search untuk mencari data  di bst.root 

baris 187 kondisi jika data ditemukan

baris 188 - 190 berfungsi menampilkan data yang dicari

baris 191 - 192 kondisi jika data tidak ditemukan

baris 193 - 194 jika id tidak berupa angka

<img width="1442" height="400" alt="image" src="https://github.com/user-attachments/assets/e19d94bf-dad6-466e-a628-2953ae099cc6" />

baris 196 merupakan kondisi ke 4 

baris 197 - 198 berfungsi untuk menampilkan data orang hilang dengan memanggil fungsi level_order

baris 200 berfungsi untuk meminta user memasukkan id untuk melihat riwayat 

baris 202 berfungsi untuk mencari node sucessor dan disimpan dalam variabel pred_sucessor dan found sucessor untuk menyimpan node yg ditemukan

baris 203 - 204 berfungsi jika node ditemukan, amka akan menampilkan output

baris 205 - 206 jika node tidak ditemmukan

baris 208 berfungsi untuk mencari prdecessor dengan key tertentu dan menyimpannya dalam variabel pred predecessor dan fpound preedecessor 

baris 209 - 210 berfungsi jika predecessor ditemukan maka aakan menampilkan riwayat data sebelumnnya 

baris 211 - 212 jika data tidak ditemukan

<img width="1002" height="464" alt="image" src="https://github.com/user-attachments/assets/7339e038-31d7-44c2-9949-881b427f3d15" />

baris 214 merupakan kondisi ke 5 

baris 215 merupakan penanganan error

baris 216 & 217 berfungsi meminta input id dan data tambahan investigasi

baris 219 berfungsi untuk menelusuri node tree dri root

baris 220 merupakan perulangan while jika currrent terisi

baris 221 - 222 mengecek apakah key lebih kecil current key, jika lebih kecil maka akan menelusuri sebelah kiri

baris 223 - 224 memgecek apakah key lebih besar dari current key, jika besar maka akan menelusuri dari sebelah kanan

baris 225 - 227 berfungsi untuk menambahkan data riwayat ke dalam stack menggunakan push dan menampilkan output berhasil

baris 228 berfungsi untuk menghentikan loop

baris 230 berfungsi jika current kosong

baris 231 berfungsi untuk menampilkan id yg tiidak ditemukan

baris 232 - 233 merupakan penaganan error jika id diinputkan tidak berupa angka

<img width="1330" height="201" alt="image" src="https://github.com/user-attachments/assets/05ba1e5b-50f3-44d7-a1da-3a080a0473b4" />

baris 235 merupakan kondisi ke 6

baris 236 akan menampilkan output terimakasih

baris 237 menghentikan loop dan program

baris 238 - 239 diesekusi jika salah input menu

baris 241 - 242 berfungsi untuk memanggil fungsi main 

## OUTPUT

<img width="707" height="182" alt="image" src="https://github.com/user-attachments/assets/209f3e79-5946-4356-8f11-5beb002b7e4c" />

Output ketika run code nya

<img width="684" height="91" alt="image" src="https://github.com/user-attachments/assets/22c368d4-afa6-4da1-a320-bc1b2978d3b8" />

output ketika memilih menu 1 dan menginputkan  id serta nama 

<img width="521" height="79" alt="image" src="https://github.com/user-attachments/assets/9dc23cc2-883b-462f-a2e1-18e1d4f8e499" />

output ketika memilih menu 2, sistem akan memproses data dan menghapusnya dari root

<img width="574" height="92" alt="image" src="https://github.com/user-attachments/assets/0bafcb98-beb4-442c-b24b-2da523ed000a" />

merupakan output ketika memilih menu 3 dan menampilkan nama orang hilang 

<img width="737" height="127" alt="image" src="https://github.com/user-attachments/assets/15c4ef14-7e2e-489d-a30f-d245fbad2bf4" />

merupakan output ketika memilih menu 4 dan menampilkan riiwayat data investigasi

<img width="651" height="81" alt="image" src="https://github.com/user-attachments/assets/bd8a7ce1-1041-4a46-8eb1-317756591dda" />

merupakan output ketika memilih menu 5 dan riwayat investigasi ditambahkan

<img width="567" height="98" alt="image" src="https://github.com/user-attachments/assets/844e725e-d329-46dc-8179-73100b275baf" />

output ketika riwayat investigasi sudah ditambahkan

<img width="1068" height="44" alt="image" src="https://github.com/user-attachments/assets/506f522c-24c0-4c24-b6df-0907fa9dc307" />

output ketika memilih menu 6 dan program berhenti

<img width="536" height="52" alt="image" src="https://github.com/user-attachments/assets/86c6a530-9779-4f1e-8852-90b69cc10fc1" />

kondisi ketika user tidak menginputkan menu dengan benar

<img width="413" height="47" alt="image" src="https://github.com/user-attachments/assets/ccd18c1d-5de5-43b3-b212-86dc31da2231" />

kondisi ketika user memasukkan data tidak berupa angka 

## LINK YOUTUBE
https://youtu.be/NSL6-3mxG8M













