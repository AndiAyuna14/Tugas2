Link aplikasi : https://katalog-ayuna.herokuapp.com/mywatchlist/


Jelaskan perbedaan antara JSON, XML, dan HTML!

JSON dan XML merupakan dua format data yang digunakan untuk menyimpan, membaca, dan
menukar data dari webserver sehingga dapat dibaca oleh user.
Meskipun memiliki kegunaan yang serupa dengan XML, namun JSON memiliki perbedaan di 
beberap sektor. Contohnya pada cara penyimpanan elemennya, keefisienan, dan strukturnya.
JSON dapat menyimpan data dalam bentuk array sehingga transfer data akan lebih efisien.
Format JSON berbentuk text, sehingga kode mudah untuk dibaca dan membuat JSON banyak
terdapat dibanyak bahasa pemrograman. Sedangkan, XML sangat membantuk dalam konfigurasi
dinamis karena dapat membuat pertukaran data yang lebih mudah. Namun, XML membutuhkan sintaks
yang berlebihan sehingga kurang efisien dalam pengimplementasiannya. Sementara untuk HTML
sendiri berfokus pada penyajian data, yang berbeda dengan JSON dan XML yang fokus pada
pertukaran data.



Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Data delivery dibutuhkan dalam pengimplementasian sebuah platform karena ada masa 
ketika sedang mengembangkan suatu platform, kita membutuhkan untuk mengirimkan data dari satu
stack ke stack yang lainnya. Bentuk data yang dikirimkan ada banyak bentuknya, bida dalam
format HTML, XML, dan JSON. 



Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.


Pertama, saya membuat aplikasi baru yang bernama mywatchlist. Caranya dengan 
memberikan perintah manage.py startapp mywatchlist. Setelah ini dijalankan,
Django akan memunculkan folder mywatchlist yang berisi file-file yang nantinya
akan digunakan seperti models.py, views.py, admin.py, dan apps.py. Setelah membuat
aplikasi, saya mendaftarkan aplikasi tersebut di folder project_django, yaitu 
dengan cara menambahkan 'mywatchlist' pada settings.py dan juga menambahkan path-nya
di urls.py. Selanjutnya adalah membuat 5 atribut data di models.py. Selanjutnya,
membuat data di initial_mywatchlist_data.json yang berisi 10 data lengkap dengan
masing-masing atributnya. Setelah itu saya melakukan migrasi dan loaddata. Lalu,
di views.py, saya membuat fungsi-fungsi yang bisa menampilkan data dalam format
HTMLL, XML, dan JSON. Setelah itu saya lakukan routing di urls.py, caranya adalah
dengan menambah path-path HTML, JSON, XML, dan format JSON yang berdasarkan ID-nya.
Setelah semuanya lengkap, tahap selanjutnya adalah add, commit, dan push kemudian
deploy applikasi mywatchlist ke heroku.



Berikut screenshot Postman:



















