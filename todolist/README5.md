READ.me TUGAS 5

link aplikasi : https://katalog-ayuna.herokuapp.com/todolist/login/?next=/todolist/

**Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?**
- Inline : kode CSS dituliskan langsung sebagai atribut elemen HTML. Setiap elemen HTML mempunya atribut style, sehingga jika ingin menggunakan inline style ini, kita dapat menulis CSS dalam atribut ini.
    
    Kelebihan inline CSS adalah kita dapat melihat perubahan pada satu elemen dan ini berguna ketika kita ingin memperbaiki kode dengan cepat. Tak hanya itu, proses load juga akan lebih cepat. Namun, inline CSS kurang efisien untuk kita terapkan karena kita harus menerapkan CSS pada tiap satu elemen HTML.
    
- Internal CSS : kode CSS dituliskan di dalam tag <style> tanpa mengganggu kode HTML yang ada.
    
    Kelebihan Internal CSS adalah kita tidak perlu mengupload beberapa file karena CSS sudah ada pada file HTML dan juga pada internal CSS, class dan IS bisa digunakan oleh internal stylesheet. Namun, kekurangan dari internal CSS adalah kurang efisien ketika kita ingin menggunakan CSS yang sama dalam beberapa file. 
    
- External CSS : kode CSS ditulis terpisah dengan kode HTML dimana kode CSS dituliskan pada sebuah file khusus dengan ekstensi .css
    
    Kelebihannya adalah ukuran file html menjadi lebih kecil dan loading website juga akan lebih cepat. Namun, halaman akan bisa berantakan apabila file css yang dipanggil oleh HTML itu gagal. Hal ini disebabkan oleh koneksi internet yang buruk.

**Jelaskan tag HTML5 yang kamu ketahui.**
 - Tag header digunakan untuk mendefisikan header untuk section yang berisi informasi seperti judul konten.
 - Tag footer digunakan untuk mendefinisikan footer atau bagian catatan kaki dari sebuah halaman.
 - Tag nav, digunakan untuk mendefinisikan section yang menyediakan link navigation.
  
  
**Jelaskan tipe-tipe CSS selector yang kamu ketahui.**
 - Element Selector : tipe selector yang menggunakan tag elemen sebagai selectornya. Misalnya kita ingin memilih tag (h1) pada HTML. maka pada CSS selectornya cukup kita tuliskan dengan h1, tanpa ada tambahan tanda (#) ataupun (.).
 - Class Selector : tipe selector yang menggunakan atribut class pada elemen HTML sebagai selectornya. Misalnya kita ingin memilih class (h1 class=”pacil”), maka pada CSS selector kita dapat memanggilnya dengan tanda titik di awal nama classnya seperti .pacil{…}.
 - ID Selector : tipe selector yang menggunakan atribut id sebagai selectornya. Misalnya kita ingin memilih (h1 id=”bakung”), maka pada CSS kita dapat memanggilnya dengan menuliskan #bakung (diawali dengan tanda #). Dan ID ini sifatnya harus bersifat unik.
