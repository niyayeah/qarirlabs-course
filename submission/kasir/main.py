# MAIN MENU
from registrasi import login_account, register, tampil
from tambah_menu import input_makanan
from kasir import hitung_kasir


#menu awal: sudah memiliki akun atau belum
def display_menu():
  status = input("Sudah memiliki akun? (y/n)?")
  if status == "y":
    login_account()
  elif status == "n":
    register()
  else:
    return status

def makanan():
  return input_makanan()

def kasir():
  return hitung_kasir()

ulang = True
while ulang:
    display_menu()
    pilih_menu = input("Pilih Menu:")
    if pilih_menu == "1":
      cek = makanan()
      if cek == False:
        tampil()
        pilih_menu = input("Pilih Menu:")
    elif pilih_menu == "2":
      cek = kasir()
      # print(cek)
      if cek == False:
        tampil()
        pilih_menu = input("Pilih Menu:")
    elif pilih_menu == "3":
      break
    else:
      print("menu tidak tersedia")
      ulang = True

