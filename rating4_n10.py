import time
import matplotlib.pyplot as plt

# Fungsi pencarian iteratif dengan algoritma linear search dan menggunakan insertion sort untuk pengurutan
def search_iteratif(data_restoran, target_rating):
    while target_rating <= 5: # Selama target_rating <= 5 
        hasil = [] #List yang akan menampung daftar restoran yang memenuhi syarat (rating >= target_rating)
        
        # Mencari restoran dengan rating >= target_rating
        for restoran in data_restoran:  
            if restoran['Rating'] >= target_rating: #jika rating restoran >= target_rating
                hasil.append(restoran) # Restoran yang memenuhi syarat ditambahkan ke dalam list

        # Jika ada hasil, sortir berdasarkan rating (Menggunakan insertion sort)
        if hasil:
            for i in range(1, len(hasil)):
                key = hasil[i]
                j = i - 1
                while j >= 0 and key['Rating'] > hasil[j]['Rating']:
                    hasil[j + 1] = hasil[j]
                    j -= 1
                hasil[j + 1] = key
            
            # Menampilkan hasil dengan format yang diinginkan
            print("\nHasil Pencarian Iteratif:")
            for restoran in hasil:
                print(f"Rating: {restoran['Rating']} - Nama Warung: {restoran['Nama']}")
            return hasil

        # Tingkatkan target_rating dan bulatkan ke 1 desimal
        target_rating += 0.1
        target_rating = round(target_rating, 1)
    
    return "Tidak ada restoran yang ditemukan"

# Fungsi pencarian rekursif dengan sorting di dalam fungsi (menggunakan insertion sort)
def search_rekursif(data_restoran, target_rating):
    # Basis: Jika target_rating lebih besar dari 5, kembalikan pesan "Tidak ada restoran yang ditemukan"
    if target_rating > 5:
        return "Tidak ada restoran yang ditemukan"
    
    hasil = []
    
    # Mencari restoran dengan rating >= target_rating
    for restoran in data_restoran:
        if restoran['Rating'] >= target_rating:
            hasil.append(restoran)
    
    # Jika ada hasil, sortir berdasarkan rating menggunakan insertion sort
    if hasil:
        for i in range(1, len(hasil)):
            key = hasil[i]
            j = i - 1
            while j >= 0 and key['Rating'] > hasil[j]['Rating']:
                hasil[j + 1] = hasil[j]
                j -= 1
            hasil[j + 1] = key

        # Menampilkan hasil dengan format yang diinginkan
        print("\nHasil Pencarian Rekursif:")
        for restoran in hasil:
            print(f"Rating: {restoran['Rating']} - Nama Warung: {restoran['Nama']}")
        return hasil
    
    # Panggil kembali fungsi dengan target_rating yang lebih tinggi
    return search_rekursif(data_restoran, round(target_rating + 0.1, 1))

# Fungsi untuk mengukur waktu eksekusi
def measure_time(search_func, data_restoran, target_rating):
    start_time = time.perf_counter() # Catat waktu mulai dengan presisi tinggi
    search_func(data_restoran, target_rating)
    end_time = time.perf_counter() # Catat waktu selesai
    return end_time - start_time # Hitung durasi

# Menentukan rating target yang dicari
target_rating = 4.0

# Dataset rating warung/restoran di sekitar telkom university berdasarkan google maps
# Ubah jumlah data menjadi 10, 20, 30, 50 dan 100 untuk mengetes skenario terbaik dan terburuk suatu algoritma
data_restoran = [ #10
    {'Nama': 'RM. PADANG MAHKOTA', 'Rating': 4.2},
    {'Nama': 'Warkop DJOEANG', 'Rating': 4.4},
    {'Nama': 'Baso Budi Mie Yamin & Mie Ayam Telkom', 'Rating': 4.8},
    {'Nama': 'Tansoe Mapan', 'Rating': 3.0},
    {'Nama': 'Diagram Coffee & Space', 'Rating': 4.8},
    {'Nama': 'Kopi Laka Laka Telkom Bandung', 'Rating': 3.9},
    {'Nama': 'HAUS! STT TELKOM', 'Rating': 4.3},
    {'Nama': 'Warung Makan Pondok Titis', 'Rating': 5.0},
    {'Nama': 'MOURISOL (Premium Risoles)', 'Rating': 5.0},
    {'Nama': 'APM PISANG CAB TELKOM', 'Rating': 4.5}
]

# Mengukur waktu eksekusi untuk algoritma iteratif dan rekursif
iteratif_time = measure_time(search_iteratif, data_restoran, target_rating)
rekursif_time = measure_time(search_rekursif, data_restoran, target_rating)

print()  # Menambahkan spasi kosong
# Menampilkan hasil pencarian dan waktu eksekusi
print(f"Waktu eksekusi pencarian iteratif: {iteratif_time:.6f} detik")
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