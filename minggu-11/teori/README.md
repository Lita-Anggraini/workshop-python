# Flask 
merupakan sebuah library yang disediakan Python yang khusus diperuntukkan oleh para pengembang perangkat lunak maupun pengelolaan website di berbagai industri. Dengan menggunakan Flask dan bahasa Python, pengembang dapat membuat sebuah web yang terstruktur dan dapat mengatur behaviour suatu web dengan lebih mudah. Bagi sahabat data tentunya belum familiar dengan library flask ini.
#  Cara instalasi flask
Web framework Flask ditulis menggunakan bahasa Python, sehingga sebelum Flask dapat digunakan, maka developer harus menginstall Python pada perangkat yang akan digunakan. Oleh sebab itu, web developer yang akan menggunakan Flask sebagai web framework untuk web development harus setidaknya mempelajari bahasa pemrograman Python terlebih dahulu, sebelum dapat menggunakan Flask seutuhnya.dalam melakukan instalasi Flask pada sebuah perangkat, dibutuhkan PIP yang biasanya sudah terinstall pada Python versi 3.4 ke atas. PIP adalah sebuah package management system yang biasa digunakan untuk mengatur dan menginstall package yang berisi modul-modul Python. PIP digunakan untuk menginstall Flask karena Flask ditulis dan dikembangkan dengan bahasa dan modul-modul pemrograman Python.
# Objek tertentu di Flask 
adalah objek global, tetapi bukan dari jenis yang biasa. Objek-objek ini sebenarnya adalah proxy untuk objek yang lokal untuk konteks tertentu. Apa seteguk. Tapi itu sebenarnya cukup mudah dipahami.bayangkan konteksnya menjadi utas penanganan. Permintaan masuk dan server web memutuskan untuk menelurkan utas baru (atau sesuatu yang lain, objek yang mendasarinya mampu menangani sistem konkurensi selain utas). Ketika Flask memulai penanganan permintaan internalnya, ia mengetahui bahwa utas saat ini adalah konteks aktif dan mengikat aplikasi saat ini dan lingkungan WSGI ke konteks (utas) itu. Itu dilakukan dengan cara yang cerdas sehingga satu aplikasi dapat memanggil aplikasi lain tanpa putus. Solusinya adalah membuat objek permintaan sendiri dan mengikatnya ke konteks. Solusi termudah untuk pengujian unit adalah dengan menggunakan manajer konteks test_request_context(). Dalam kombinasi dengan pernyataan with itu akan mengikat permintaan pengujian sehingga Anda dapat berinteraksi dengannya