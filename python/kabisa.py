yil = int(input("Yilni kiriting:"))

if (yil % 400 == 0) or ( yil % 4 == 0 and yil % 100 != 0):
    print("Kabisa yili") 
else:
    print("Kabisa yili emas")
