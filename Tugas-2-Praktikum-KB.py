import statistics
import sys
from colorama import Fore, Style

nilai_mahasiswa ={}

def hitung_nilai_akhir(kuis, uts, uas, projek):
    return round((kuis*0.1)+(uts*0.2)+(uas*0.1)+(projek*0.5),2)

def tentukan_grade_status(nilai):
    if nilai >= 85:
        return "A", "Lulus", Fore.GREEN
    elif nilai >= 75:
        return "B", "Lulus", Fore.GREEN
    elif nilai >= 60:
        return "C", "Lulus", Fore.GREEN
    else:
        return "D", "Tidak Lulus/ Mengulang", Fore.RED
    
print("=====================================")
print("= Kalukulator Nilai Akhir Mahasiswa =")
print("=====================================")

while True:
    nama=input("Masukkan Nama Mahasiswa: ")
    kuis=float(input("Masukkan Nilai Kuis: "))
    uts=float(input("Masukkan Nilai UTS: "))
    uas=float(input("Masukkan Nilai UAS: "))
    projek=float(input("Masukkan Nilai Projek: "))

    nilai_akhir=hitung_nilai_akhir(kuis, uts, uas, projek)
    grade, status, warna=tentukan_grade_status(nilai_akhir)

    nilai_mahasiswa[nama]={"Kuis": kuis, "UTS": uts, "UAS":uas, "Projek": projek, "Nilai Akhir": nilai_akhir, "Grade": grade, "Status": status}

    print("\n--------------------------------------")
    print(nama)
    print("Nilai Akhir: ", nilai_akhir)
    print("Grade: ", grade)
    print("Status: ", warna + status + Style.RESET_ALL)
    print("--------------------------------------\n")
    
    lanjut = input("Tambah mahasiswa lagi? (y/n): ").lower()
    if lanjut != 'y':
        break

print("\n")
print("=====================================")
print("=      Daftar Nilai Mahasiswa       =")
print("=====================================")
for mahasiswa, nilai in nilai_mahasiswa.items():
    warna = Fore.GREEN if nilai["Status"] == "Lulus" else Fore.RED
    print("\n--------------------------------------")
    print(mahasiswa)
    print("Nilai Akhir: ", nilai["Nilai Akhir"])
    print("Grade: ", nilai["Grade"])
    print("Status: ", warna + nilai["Status"] + Style.RESET_ALL)
    print("--------------------------------------")

sys.exit()

