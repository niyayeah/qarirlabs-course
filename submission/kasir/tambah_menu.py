#TAMBAH MAKANAN
menus = []
prices = []

#function input makanan
def input_makanan():
    ulang1 = True
    while ulang1:
        menu = input("Masukan menu:")
        menus.append(menu)
        price = int(input("Masukan harga:"))
        prices.append(price)
        lanjut_input = input("lanjut input menu? (y/n) ")
        if lanjut_input == "y" or lanjut_input == "Y":
            ulang1 = True
        else:
            ulang1 = False
            return False

# input_makanan()