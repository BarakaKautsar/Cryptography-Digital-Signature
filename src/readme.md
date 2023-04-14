# Tugas Kecil 3: Implementasi Program Tanda-tangan Digital dengan Menggunakan Algoritma RSA dan Fungsi hash SHA-3
## II4031 Kriptografi dan Koding
- 18220049 Rachmad Hidayat 
- 18220057 Muhammad Ardi Avicenna
- 18220095 Tubagus Baraka Kautsar

## 📖 PENDAHULUAN 📖
- tanda tangan digital menjadi salah satu solusi untuk mengatasi masalah kurangnya keamanan dan keaslian pada dokumen atau file digital yang ditransmisikan melalui internet.
- pembuat atau pengirim dokumen atau file dapat memberikan identitas elektronik yang unik pada dokumen atau file mereka dengan tanda tangan digital
- Pada tugas ini, algoritma dan fungsi hash yang dipakai yaitu fungsi hash SHA-3 dan algoritma RSA.
- Proses tanda tangan digital ini dibagi kedalam 3 proses utama 
  -  proses pembangkitan kunci publik dan kunci private,
  -  proses penandatanganan (signing), serta
  -  verifikasi tanda tangan (verifying)
-  Pada tugas ini, pengguna aplikasi dapat membangkitkan kunci dengan memasukan nilai p, q, dan e (private key) pada halaman "Generate Public Key and Private Key"
-  Lalu hasil kunci yang dibangkitkan dapat digunakan pada halaman "Signing Digital Signature"
-  Pada halaman tersebut akan menghasilkan tanda tangan digital yang diapit oleh "*** Begin of digital signature ****" dan "*** End of digital signature ****"
-  Terakhir pengguna dapat melakukan verifikasi keabsahan tanda tangan pada halaman "Verifying Digital Signature"

## ✅ SPESIFIKASI PROGRAM ✅
- Program merupakan aplikasi desktop dengan tampilan antarmuka dengan tools Tkinter
- Terdapat beberapa halaman pada program ini
  -  Halaman Generate Public Key and Private Key
  -  Halaman Signing Digital Signature
  -  Halaman Verifying Digital Signature
- Implementasi RSA tidak menggunakan library RSA yang sudah beredar melainkan melalui pemanfaat fungsi - fungsi primitif
- Format defaalt file fokumen yang ditanda-tangani adalah file teks dab tanda-tangan akan disisipkan pada akhir dokumen
- Bahasa pemrograman yang digunakan adalah Python 3

## 🏃‍♂️ TUTORIAL MENJALANKAN PROGRAM 🏃‍♂️
1. Clone repositori ini
2. Run file bernama "main.py"
3. Jika belum memiliki key, pada halaman Generate Public Key and Private Key, pilihlah nilai p, q yang bernilai prima dan nilai e yang relatif prima dengan nilai (p-1)*(q-1) 
4. Jika telah memiliki key, lakukan tanda tangan pada halaman Signing Digital Signature
5. Tanda tangan digital dapat diverifikasi keabsahannya pada halaman Verifying Digital Signature
