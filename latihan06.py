print("====================================")
print("======program score kelulusan=======")
print("====================================")

nama = input('masukan nama mahasiswa : ')
nilai =input("inputkan nilai kelulusan : ")

if (nilai.isnumeric() == True):
    nilai_int = int(nilai)
    if nilai_int >=90:
        grade = "A"
        predikat = "dengan pujian"

    elif nilai_int >=80:
        grade = "B"
        predikat =  "sangat memuaskan"

    elif nilai_int >=70:
        grade = "C"
        predikat = "memuaskan"

    elif nilai_int >=60:
        grade = "D"
        predikat = "tidak memuaskan"

    elif nilai_int >=0:
        grade = 'E'
        predikat = "tidak lulus"

    print("\n============================")
    print("nama mahasiswa : ", nama)
    print("grade anda     : ", grade)
    print("predikat anda  : ", predikat)

else:
    print("\nmaaf input anda salah")