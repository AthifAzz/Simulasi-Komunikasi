# Simulasi Komunikasi Sistem Terdistribusi

## Deskripsi
Aplikasi ini merupakan simulasi interaktif untuk memahami dua model komunikasi dalam sistem terdistribusi:
- Request-Response
- Publish-Subscribe

Simulasi dilengkapi dengan animasi pergerakan pesan, multi client, multi subscriber, serta pengukuran latency.

## Fitur Utama
- Animasi pesan bergerak (visual interaktif)
- Multi client (3 client)
- Multi subscriber (2 subscriber)
- Slider kecepatan simulasi
- Perhitungan latency (ms)
- Log aktivitas sistem
- Perbandingan model komunikasi

## Teknologi
- Python 3
- Tkinter (GUI)

## Cara Menjalankan
1. Pastikan Python sudah terinstall
2. Jalankan file:
   python main_pro.py

## Cara Penggunaan
1. Masukkan pesan pada input
2. Pilih model komunikasi:
   - Request-Response → simulasi client ke server
   - Publish-Subscribe → simulasi broadcast ke subscriber
3. Atur kecepatan dengan slider
4. Lihat hasil di log dan animasi

## Penjelasan Model

### Request-Response
Client mengirim request ke server, lalu server memberikan response kembali ke client.

Karakteristik:
- Komunikasi langsung (1:1)
- Sederhana
- Tidak scalable untuk banyak client

### Publish-Subscribe
Client (publisher) mengirim pesan ke broker, lalu broker mendistribusikan ke subscriber.

Karakteristik:
- Komunikasi 1 ke banyak
- Lebih scalable
- Cocok untuk sistem real-time

## Kesimpulan
Model Publish-Subscribe lebih unggul dalam skalabilitas dan distribusi pesan ke banyak node, sedangkan Request-Response lebih sederhana dan cocok untuk komunikasi langsung.
