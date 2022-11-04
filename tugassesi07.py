print(12*"="+ "aplikasi sederhana" +12*"=")

while(True):
    print("menu")
    print("1.menghitung luass segitiga")
    print("2.menghitung luas persegi panjang")
    print("3.menentukan bilangan ganjil genap")
    print("4.Quit")

    listmenu = input("masukan pilihan : ")

    if listmenu == "1":
        print("menu--hitung lias segitiga")
        alas =int(input("masukan panjang alas : "))
        tinggi =int(input("masukan tinggi : "))

        rumus1 =1/2 * alas * tinggi
        print("luas segitiga : ",rumus1)
        print("===========================")

    elif listmenu == "2":
        print("menu -- hitung luas persegi panjang")
        panjang = int(input("masukan panjang : "))
        lebar = int(input("masukan lebar : "))

        rumus2 =  panjang * lebar 
        print("luas persegi panjang : ", rumus2)
        print(("==============================="))

    elif listmenu == "3" :
        print("menu -- tentukan number ganjil genap.")
        angka = int(input("masukan angka : "))

        if (angka % 2 == 0):
            print("angka", angka, "merupakan angka genap")
        else:
            print("angka", angka, "merupakan angka ganjil")

        print("=========================")

    else:
        menu = input("tanks you ... byabcd")
        print("--------------------------------")
        break
