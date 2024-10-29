import pywhatkit as kit
import time

# Fungsi untuk mengirim pesan berulang
def kirim_pesan(nomor, pesan, jumlah, jam, menit):
    for _ in range(jumlah):
        kit.sendwhatmsg(nomor, pesan, jam, menit)
        time.sleep(60)  # Tunggu 60 detik sebelum mengirim pesan berikutnya

# Masukkan informasi
nomor_wa = input("Masukkan nomor WhatsApp (mis. +628123456789): ")
pesan_wa = input("Masukkan pesan yang ingin dikirim: ")
jumlah_pesan = int(input("Masukkan jumlah pesan yang ingin dikirim: "))
jam_kirim = int(input("Masukkan jam pengiriman (24h format): "))
menit_kirim = int(input("Masukkan menit pengiriman: "))

# Panggil fungsi kirim pesan
kirim_pesan(nomor_wa, pesan_wa, jumlah_pesan, jam_kirim, menit_kirim)
