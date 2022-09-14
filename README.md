**Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;**
![MVT Django](https://user-images.githubusercontent.com/112320001/190059645-79fab374-17f1-4edc-8d85-d791635edcc6.png)
Clients akan mengirimkan permintaan yang di mana permintaan ini nanti akan masuk ke dalam server Django lalu diproses melalui urls. Setelah itu, request akan diteruskan ke views. Apabila terdapat proses yang memerlukan akses ke database, maka views akan memanggil query ke models. Selanjutnya database akan mengembalikan query tersebut ke views. Seteleh request selesai diproses, selanjutnya akan memetakan data tersebut ke dalam halaman HTML. Kemudian halaman HTML ini akan dikembalikan ke clients sebagai respons. 




**Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?** 

Virtual environment berguna untuk memisahkan pengaturan dan *package* yang diinstal pada setiap proyek agar terisolasi. Hal ini dilakukan supaya kita tetap dapat mengerjakan beberapa proyek dengan modul yang sama namun dengan versi berbeda. Sebagai contoh, misalnya kita membuat proyek Django dengan versi 1.1 dan proyek aplikasi kita dapat berjalan dengan baik pada modul versi 1.1 ini. Lalu, selang beberapa waktu kemudian, Django merilis versi baru yang dimana versi baru ini dibutuhkan untuk membuat proyek yang lain. Setelah upgrade ke versi yang baru, proyek kita sebelumnya yang menggunakan versi lama ternyata tidak dapat berjalan pada versi baru ini. Untuk itu, kita membutuhkan *virtual environment* agar setiap aplikasi mempunyai modulnya masing-masing.
Lalu, apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment? Jawabannya bisa, namun hal ini menyebabkan modul-modulnya dapat diakses dari luar sehingga semua aplikasi bisa mengakses dan menggunakannya.




**Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.**

Yang pertama saya lakukan adalah membuat fungsi **show_catalog** yang menerima parameter request dan mengembalikan render(request, “katalog.html”). Fungsi ini saya buat di dalam views.py dalam folder katalog. Kemudian, agar dapat mengakses database, saya harus mengimport models ke dalam views.py ini. Class yang ada pada models.py akan digunakan untuk melakukan pengambilan data dari database. Lalu, fungsi show_catalog tadi saya modifikasi lagi agar bisa memanggil fungsi query ke model database dan menyimpan hasil query tersebut ke dalam sebuah variabel. Variabel context berguna untuk menyimpan data yang ingin dimunculkan pada halaman HTML nanti. Agar variabel context ini bisa ikut di-render oleh Django, kita perlu menambahkan context sebagai parameter ketiga pada pengembalian fungsi render di fungsi show_catalog tadi.

Lalu yang kedua, saya ingin membuat routing untuk memetakan fungsi yang ada pada views.py tadi sehingga nantinya halaman HTML dapat ditampilkan lewat browser. Caranya adalah dengan mengimport fungsi show_catalog lalu membuat variabel app_name yang berisi string katalog. Lalu, membuat variabel yang berisikan list berupa path. Lalu kemudian daftarkan aplikasi katalog ke dalam urls.py yang ada pada folder project_django dengan cara menambahkan path(’katalog/’, include(’katalog.urls’)) pada variabel urlpatterns.

Lalu yang ketiga, untuk melakukan mapping dari data yang telah ikut di-render untuk dimunculkan di halamatn HTML. Di dalam file katalog.html, saya menambahkan kode {{nama}} dan {{npm}} untuk memunculkan nama dan npm di HTML nanti. Lalu, agar daftar item dalam tabel, dibutuhkan iterasi terdahadap variabel list_katalog.

Kemudian, untuk melakukan deployment ke Heroku, langkah pertama adalah create new app.  Lalu membuat nama app-nya. Kemudia saya menyalin API key. Lalu di bagian secrets GitHub Actions ditambahkan variabel repository secret dan juga ditambahkan HEROKu_APP_NAME dan juga API key yang sudah disalin tadi. Lalu menjalankan kembali workflow, kemudian deploy.
