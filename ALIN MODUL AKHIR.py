import numpy as np
from prettytable import PrettyTable

latsol = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20LS.csv", delimiter = ",", dtype = 'str')
kuis = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Kuis.csv", delimiter = ",", dtype = 'str')
lab = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Lab.csv", delimiter = ",", dtype = 'str')
proyek = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Proyek.csv", delimiter = ",", dtype = 'str')
jurnal = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Jurnal.csv", delimiter = ",", dtype = 'str')
ujian = np.genfromtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Ujian.csv", delimiter = ",", dtype = 'str')
nilai_ls= latsol[1:, 1:].astype(float) * 1/100
nilai_kuis = kuis[1:, 1:].astype(float) * 2/100
nilai_lab = lab[1:, 1:].astype(float) * 4/100
nilai_proyek = proyek[1:, 1:].astype(float) * 7.50/100
nilai_jurnal = jurnal[1:, 1:].astype(float) * 3/100
nilai_ujian = ujian[1:, 1:].astype(float) * 25/100
nim = kuis[1: , 0:1]

Nilai = np.block([[nilai_ls, nilai_kuis, nilai_lab, nilai_proyek, nilai_jurnal, nilai_ujian ]])
Nilai = np.sum(Nilai, axis = 1)
Nilai = Nilai.reshape((101, 1))
[jumlah_mahasiswa, banyak_materi] = np.shape(nilai_ls)


grade = ""
list_hasil = []
for i in range(jumlah_mahasiswa):
    if Nilai[i] > 90 and Nilai[i] <= 100:
        grade = "A"
    elif Nilai[i] > 85 and Nilai[i] <= 90:
        grade = "A-"
    elif Nilai[i] > 80 and Nilai[i] <= 85:
        grade = "B+"
    elif Nilai[i] > 75 and Nilai[i] <= 80:
        grade = "B"
    elif Nilai[i] > 70 and Nilai[i] <= 75:
        grade = "B-"
    elif Nilai[i] > 60 and Nilai[i] <= 70:
        grade = "C+"
    elif Nilai[i] > 50 and Nilai[i] <= 60:
        grade = "C"
    elif Nilai[i] > 45 and Nilai[i] <= 50:
        grade = "C-"
    elif Nilai[i] > 40 and Nilai[i] <= 45:
        grade = "D"
    elif Nilai[i] >= 0 and Nilai[i] <= 41:
        grade = "F"
    list_hasil.append(grade)

columns = ["NIM", "Nilai akhir", "Index Prestasi"]
table = PrettyTable()

table.add_column(columns[0], nim)
table.add_column(columns[1], Nilai )
table.add_column(columns[2], list_hasil )
print("Tabel nilai\n", table)

#Tugas 2 dan Tugas 3
print("Nilai rata rata proyek: ", np.mean(latsol[1:,1:].astype(float), axis = 0))
print("Nilai rata rata kuis: ", np.mean(kuis[1:, 1:].astype(float), axis = 0))
print("Nilai rata rata lab: ", np.mean(lab[1:,1:].astype(float), axis = 0))
print("Nilai rata rata jurnal: ", np.mean(jurnal[1:, 1:].astype(float), axis = 0))
print("Nilai rata rata proyek: ", np.mean(proyek[1:, 1:].astype(float), axis = 0))
print("Nilai rata rata ujian: ", np.mean(ujian[1:,1:].astype(float), axis = 0))

#karna kita tahu bahwa nilai rata rata tertinggi adalah jurnal, terutama jurnal 1, kita mau menaikan bobot nilai jurnal 
nilai_ls2= latsol[1:, 1:].astype(float) * 0/100
nilai_kuis2 = kuis[1:, 1:].astype(float) * 0/100
nilai_lab2 = lab[1:, 1:2].astype(float) * 0/100
nilai_lab21 = lab[1:, 2:3].astype(float) * 0/100
nilai_proyek2 = proyek[1:, 1:].astype(float) * 0/100
nilai_jurnal2 = jurnal[1:, 1:2].astype(float) * 70/100
nilai_jurnal21 = jurnal[1:, 2:3].astype(float) * 0/100
nilai_ujian2 = ujian[1:, 1:].astype(float) * 15/100


Nilai2 = np.block([[nilai_ls2, nilai_kuis2, nilai_lab2, nilai_proyek2, nilai_jurnal2,nilai_jurnal21, nilai_ujian2 ]])
Nilai2 = np.sum(Nilai2, axis = 1)
Nilai2 = Nilai2.reshape((101, 1))

grade = ""
list_hasil2 = []
for i in range(jumlah_mahasiswa):
    if Nilai2[i] > 90 and Nilai2[i] <= 100:
        grade = "A"
    elif Nilai2[i] > 85 and Nilai2[i] <= 90:
        grade = "A-"
    elif Nilai2[i] > 80 and Nilai2[i] <= 85:
        grade = "B+"
    elif Nilai2[i] > 75 and Nilai2[i] <= 80:
        grade = "B"
    elif Nilai2[i] > 70 and Nilai2[i] <= 75:
        grade = "B-"
    elif Nilai2[i] > 60 and Nilai2[i] <= 70:
        grade = "C+"
    elif Nilai2[i] > 50 and Nilai2[i] <= 60:
        grade = "C"
    elif Nilai2[i] > 45 and Nilai2[i] <= 50:
        grade = "C-"
    elif Nilai2[i] > 40 and Nilai2[i] <= 45:
        grade = "D"
    elif Nilai2[i] >= 0 and Nilai2[i] <= 41:
        grade = "F"
    list_hasil2.append(grade)

table2 = PrettyTable()
table2.add_column(columns[0], nim)
table2.add_column(columns[1], Nilai2 )
table2.add_column(columns[2], list_hasil2 )
print("Tabel Baru\n",table2)

print("Jumlah nilai 'A' lama: ", list_hasil.count("A")) 
print("Jumlah nilai 'A' baru: ", list_hasil2.count("A")) 
print("Jumlah nilai 'F' lama: ", list_hasil.count("F"))
print("Jumlah nilai 'F' baru: ", list_hasil2.count("F")) 
print("Rata rata nilai akhir: ", np.mean(Nilai))
print("Rata rata nilai akhir baru: ", np.mean(Nilai2))
print()





