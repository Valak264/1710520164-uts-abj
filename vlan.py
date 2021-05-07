while True:
    x = input("Input data VLAN baru (y/t)?")
    if x == "y" or x == "Y":
        file = open("/home/devasc/labs/devnet-src/python/vlan-database.txt", "a")
        b = input("Masukkan VLAN ID: ")
        c = input("Masukkan Nama VLAN: ")
        d = "VLAN ID " + b +", " + "Name: " + c
        file.write(d + "\n")
        file.close()
    else:
        file = open("/home/devasc/labs/devnet-src/python/vlan-database.txt", "r")
        for item in file:
            print(item)
        exit()
