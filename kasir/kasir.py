#KASIR

#function untuk menampilkan menu
def list_menu():
  print("---Daftar Menu---")
  print("-----------------")
  print(" 1. | Nasi Goreng  | Rp. 12000")
  print(" 2. | Mie Tek Tek  | Rp. 10000")
  print(" 3. | Indomie Goreng/Rebus  | Rp.6000  ")
  print(" 4. | Kwetiauw  | Rp. 15000 ")
  print("-----------------")

#function untuk menghitung kasir
def hitung_kasir():
  global total
  ulang = True
  while ulang:
    list_menu()
    pesan = int(input("Pilih menu makanan: "))
    jumlah_pesanan = int(input("Jumlah dibeli: "))
    if pesan == 1 and pesan <= 5:
      nama = "Nasi Goreng"
      total = (12000*jumlah_pesanan)
    elif pesan == 2 and pesan <= 5:
      nama = "Mie Tek Tek"
      total = (10000*jumlah_pesanan)
    elif pesan == 3 and pesan <= 5:
      nama = "Indomie Goreng/Rebus"
      total = (6000*jumlah_pesanan)
    elif pesan == 4 and pesan <= 5:
      nama = "Kwetiauw"
      total = (15000*jumlah_pesanan)
    else:
      print("Maaf, Menu anda tidak ada di daftar.")

    print(" ------------------------------")
    print(" Menu :",nama)
    print(" Jumlah Pesanan :", jumlah_pesanan)
    print(" ------------------------------")
    print(" Total Pembayaran :", total)
    print(" ------------------------------")
    nota()

    lanjut_input = input("lanjut input menu? (y/n) ")
    if lanjut_input == "y" or lanjut_input == "Y":
        ulang = True
    else:
        ulang = False
        return False

#function untuk nota
def nota():
  bayar = int(input("masukan uang pembeli: Rp."))
  total1 = bayar - total
  print("uang kembalian anda Rp.", total1)


# hitung_kasir()
 
  