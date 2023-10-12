# Soal pertama
soal1 = "Siapakah presiden pertama Indonesia?"
A1 = "A. Soekarno"
B1 = "B. Soeharto"
C1 = "C. Megawati"
D1 = "D. Jokowi"
jawaban1 = "A"

# Soal kedua
soal2 = "Apa ibukota Indonesia?"
A2 = "A. Bandung"
B2 = "B. Jakarta"
C2 = "C. Bekasi"
D2 = "D. Jawa Barat"
jawaban2 = "B"

# Inisialisasi nilai
nilai = 0

# Pertanyaan pertama
print(soal1)
print(A1)
print(B1)
print(C1)
print(D1)

jawaban_user1 = input("Masukkan jawaban Anda (A, B, C, atau D) untuk soal pertama: ")

if jawaban_user1 == jawaban1:
    nilai += 50  # Jika benar soal pertama, tambahkan 50 poin ke nilai

# Pertanyaan kedua
print(soal2)
print(A2)
print(B2)
print(C2)
print(D2)

jawaban_user2 = input("Masukkan jawaban Anda (A, B, C, atau D) untuk soal kedua: ")

if jawaban_user2 == jawaban2:
    nilai += 50  # Jika benar soal kedua, tambahkan 50 poin ke nilai

# Menampilkan nilai akhir
print("Nilai akhir Anda:", nilai)
