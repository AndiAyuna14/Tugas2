Link aplikasi : https://katalog-ayuna.herokuapp.com/todolist/login/?next=/todolist/

**Apa kegunaan {% csrf_token %} pada elemen form? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen form?**
Kegunaan {% csrf_token %} pada elemen form adalah untuk menangani ancaman dalam bentuk CSRF. CSRF itu sendiri merupakan serangan yang membuat user tanpa sadar mengirimkan request ke suatu form
yang sebenarnya bukan form yang dia kehendeki, bisa jadi form ini dikirim oleh hacker melalui injeksi code. Dengan adanya csrf_token ini, form kita akan dilindungi dari ancaman CSRF tersebut karena
csrf_token akan mengecek token terlebih dahulu sebelum dikirim ke server, jika valid akan diproses, dan jika tidak valid tentu tidak akan diproses. Ketika potongan kode csrf_token ini tidak ada, yang paling rugi
tentunya adalah si user karena request yang dikirimkan tidak sesuai dengan apa yang dia kehendaki dan data yang ada di server bisa terancam.

**Apakah kita dapat membuat elemen form secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat form secara manual.**
Ya, kita dapat membuat elemen form secara menual tanpa menggunakan generator seperti {{ form.as_table }}.Untuk membuat elemen form secara manual ini dapat menggunakan CSS di mana kita
akan mengakses tiap section satu-satu pada atribut-atribut models

**Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.**
User akan menulis alamat dari web yang kemudian HTTP request akan digenerate di browser lalu dikirimkan ke server. Server akan menerima request tadi dan akan mencari fungsi views.py mana yang akan menghandle path. Setelah itu halaman form akan
dikembalikan ke user dan ditampilkan lewat browser. User akan mengisi form kemudian browser akan generate HTTP request, method, dan arguments ke URL destination dan mengirimkannya ke server. Server menerima request berupa form yang sudah diisi kemudian
server akan mengecek dan mencari views.py mana yang akan menghandle atau memprosesnya. Setelah itu, akan digenerate halama HTML yang kemudian akan di display ke user.

**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.**
Dengan menggunakan perintah python manage.py startapp todolist, saya membentuk suatu aplikasi baru. Setelah perintah tersebut dijalankan, Django akan memberikan beberapa file yang dibutuhkan seperi models.py views.py, dll. Setelah itu,
aplikasi ini didaftarkan di settings.py pada project_django. Selanjutnya adalah menambahkan path di urls.py. Setelah itu, saya membuat model Task beserta atribut-atributnya (user, date, title, description) pada models.py
Untuk atribut user sendiri, menggunakan Foreign Key. Lalu saya membuat beberapa fungsi di views.py untuk mengimplementasikan form, regist, login, dan logout. Setelahnya, saya buat juga beberapa
file HTML yang nanti akan ditampilkan lewat browser. Lalu untuk form nya, saya buat di form.py alias pada file baru. Kemudian untuk button 'Tambah Task Baru', saya menambahkan button di dalam url agar setelah di klik, button tersebut akan mengarahkan user ke halaman untuk proses penambahan task. 
Setelah itu, melakukan routing dengan menambahkan path di urls.py pada todolost. Lalu di deploy ke heroku dengan add commit push. Lalu dengan link heroku, saya buat akun pengguna dengan dummy datanya. 



