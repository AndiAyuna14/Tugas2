# TUGAS 6

# Jelaskan perbedaan antara *asynchronus programming* dengan *synchronus programming*

- Asynchronus programming → user masih dapat berinteraksi dengan website ketika server sedang memproses data sehingga memungkinkan untuk menjalankan beberapa proses secara bersamaan tanpa menunggu server memberikan respons
- Synchronus programming → user harus menunggu respons dari user tiap kali user memberikan request atau event tertentu.

# ****Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.****

Event-Driven Programming adalah paradigma pemrograman di mana objek dapat berkomunikasi dengan mengirimkan pesan satu sama lain melalui perantara. Pengiriman pesan tersebut melalui event stream. Dan ini bergantung pada event dengan memperhatikan operasi apa yang akan diimplementasikan dari adanya event. Salah satu contoh dalam tugas ini ada pada implementasi tombol untuk Save Change dalam form tambah task yang terletak dalam modal.

```jsx
document.getElementById("button").onclick = addTodolist
```

Pada kode di atas, task baru akan ditambahkan jika ada event dari user berupa mouse click pada button Save Change.

# Jelaskan penerapan asynchronus pada AJAX.

Penerapannya yaitu ketika suatu event terjadi, JavaScript akan membuat XMLHttpRequest. Request ini akan diproses dan direspon kembali ke halaman web. Respon tersebut akan diterima dan diproses oleh JavaScript. Dengan adanya AJAX, data dapat diperbaharui tanpa harus menunggu halaman web direload. Sehingga, halaman web dapat diupdate secara asynchronus

# Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

Pertama saya membuat dua fungsi baru di views. Fungsi yang pertama yaitu add yang digunkan untuk menambahkan task baru melalui form. Fungsi yang kedua adalah show_json yang gunanya adalah untuk mengambil data dalam bentu json yang nantinya data ini dipakai di script untuk menampilkan data-data task di web. Langkah selanjutnya adalah routing di [url.py](http://url.py) dengan menambahkan path untuk fungsi views yang telah dibuat sebelumnya. Lalu selanjutnya saya membuat modal yang di dalamnya terdapat form dan agar bisa diakses dari script nanti, saya menambahkan id. Setelah itu saya membuat table. Lalu membuat script yang berisi fungsi-fungsi untuk menambahkan task dan juga menampilkannya. Di dalam script ini terdapat implementasi asynchronus programming. Lalu, agar dapat terhubung ke views, saya menggunakan fetch bserta url ke masing-masing fungsi views. Lalu melakukan looping untuk menampilkan data-data, dan juga fungsi addTodolist dengan method post untuk memproses form. Terakhir, saya menggunakan kode yang merupakan event-triggered agas task baru yang diinput user dapat disimpan.
