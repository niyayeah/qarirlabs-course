#REGISTRASI

admin = {"admin": "admin"}

# function untuk menambahkan admin
def register():
    username = (input("Masukan username anda: "))
    password = (input("masukkan password anda: "))
    print("Akun berhasil dibuat")
    admin[username] = password
    login_account()

#function untuk login
def login_account():
    login = True 
    while login:
        username = input("Username anda: ")
        password = input("Password anda: ")
        if username in admin and admin[username] == password:
            login = False
            tampil()
        else:
            print("Username dan Password anda salah")
            login = True

def tampil():
    print("---SELAMAT DATANG---")
    print("-----------------")
    print(" 1. | Input Menu | ")
    print(" 2. | Kasir | ")
    print(" 3. | Keluar | ")
    print("-----------------")
