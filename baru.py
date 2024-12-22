import time
import matplotlib.pyplot as plt

# Fungsi pencarian iteratif dengan sorting di dalam fungsi
def search_iteratif(data, target_rating):
    while target_rating <= 5:
        hasil = []
        
        # Mencari restoran dengan rating >= target_rating
        for restoran in data:
            if restoran['Rating'] >= target_rating:
                hasil.append(restoran)

        # Jika ada hasil, sortir berdasarkan rating
        if hasil:
            hasil_sorted = sorted(hasil, key=lambda x: x['Rating'], reverse=True)
            # Menampilkan hasil dengan format yang diinginkan
            print("\nHasil Pencarian Iteratif:")
            for restoran in hasil_sorted:
                print(f"Rating: {restoran['Rating']} - Nama Warung: {restoran['Nama']}")
            return hasil_sorted


        # Tingkatkan target_rating dan bulatkan ke 1 desimal
        target_rating += 0.1
        target_rating = round(target_rating, 1)
    
    return "Tidak ada restoran yang ditemukan"

# Fungsi pencarian rekursif dengan sorting di dalam fungsi
def search_rekursif(data, target_rating):
    # Basis: Jika target_rating lebih besar dari 5, kembalikan pesan "Tidak ada restoran yang ditemukan"
    if target_rating > 5:
        return "Tidak ada restoran yang ditemukan"
    
    hasil = []
    
    # Mencari restoran dengan rating >= target_rating
    for restoran in data:
        if restoran['Rating'] >= target_rating:
            hasil.append(restoran)
    
    # Jika ada hasil, sortir berdasarkan rating dan kembalikan hasilnya
    if hasil:
        hasil_sorted = sorted(hasil, key=lambda x: x['Rating'], reverse=True)

        # Menampilkan hasil dengan format yang diinginkan
        print("\nHasil Pencarian Rekursif:")
        for restoran in hasil_sorted:
            print(f"Rating: {restoran['Rating']} - Nama Warung: {restoran['Nama']}")
        return hasil_sorted
    
    # Panggil kembali fungsi dengan target_rating yang lebih tinggi
    return search_rekursif(data, round(target_rating + 0.1, 1))

# Fungsi untuk mengukur waktu eksekusi
def measure_time(search_func, data, target_rating):
    start_time = time.time()
    result = search_func(data, target_rating)
    end_time = time.time()
    return end_time - start_time

# Menentukan rating target yang dicari
target_rating = 4.0

# Contoh data restoran
data_restoran = [
    {'Nama': 'Warung A', 'Rating': 4.5},
    {'Nama': 'Warung B', 'Rating': 3.9},
    {'Nama': 'Warung C', 'Rating': 4.0},
    {'Nama': 'Warung D', 'Rating': 5.0}
]

# Mengukur waktu eksekusi untuk algoritma iteratif dan rekursif
iteratif_time = measure_time(search_iteratif, data_restoran, target_rating)
rekursif_time = measure_time(search_rekursif, data_restoran, target_rating)

print()  # Menambahkan spasi kosong
# Menampilkan hasil pencarian dan waktu eksekusi
# print(f"\nHasil Pencarian Iteratif:")
# print(search_iteratif(data_restoran, target_rating))
print(f"Waktu eksekusi pencarian iteratif: {iteratif_time:.6f} detik")

# print(f"\nHasil Pencarian Rekursif:")
# print(search_rekursif(data_restoran, target_rating))
print(f"Waktu eksekusi pencarian rekursif: {rekursif_time:.6f} detik")

# Visualisasi grafik waktu eksekusi
algorithms = ["Iteratif", "Rekursif"]
times = [iteratif_time, rekursif_time]

plt.figure(figsize=(6, 4))
plt.bar(algorithms, times, color=['blue', 'green'])
plt.xlabel('Algoritma')
plt.ylabel('Waktu Eksekusi (detik)')
plt.title('Perbandingan Waktu Eksekusi Pencarian Iteratif vs Rekursif')
plt.show()