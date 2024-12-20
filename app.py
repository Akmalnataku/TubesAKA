import time
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')  # Backend interaktif dengan Tkinter
import matplotlib.pyplot as plt

# Dataset, Gantilah jumlah dataset ini dengan sekitar 10, 25, 50, 100(kalau ada)
#  untuk mengetes running time pada jumlah dataset yang berbeda ()
data = {
    'Nama Warung': ['Warung A', 'Warung B', 'Warung C', 'Warung D', 'Warung E', 'Warung B', 'Warung C', 'Warung D', 'Warung E'],
    'Rating': [4.5, 4.2, 4.8, 4.1, 4.3, 3.2, 3.8, 5.0, 4.3]
}

# Mengonversi dataset menjadi DataFrame
df = pd.DataFrame(data)

# Fungsi pencarian iteratif
def search_iteratif(data, target_rating):
    for i in range(len(data)):
        if data[i]['Rating'] == target_rating:
            return data[i]
    return None

# Fungsi pencarian rekursif
def search_rekursif(data, target_rating, index=0):
    if index == len(data):
        return None
    if data[index]['Rating'] == target_rating:
        return data[index]
    return search_rekursif(data, target_rating, index + 1)

# Fungsi untuk mengukur waktu eksekusi
def measure_time(search_func, data, target_rating):
    start_time = time.time()
    result = search_func(data, target_rating)
    end_time = time.time()
    return end_time - start_time

# Menentukan rating target yang dicari
target_rating = 4.0

# Mengukur waktu eksekusi untuk algoritma iteratif dan rekursif
iteratif_time = measure_time(search_iteratif, df.to_dict('records'), target_rating)
rekursif_time = measure_time(search_rekursif, df.to_dict('records'), target_rating)

# Menampilkan hasil
print(f"Waktu eksekusi pencarian iteratif: {iteratif_time:.6f} detik")
print(f"Waktu eksekusi pencarian rekursif: {rekursif_time:.6f} detik")

# Membuat grafik perbandingan
algorithms = ['Iteratif', 'Rekursif']
times = [iteratif_time, rekursif_time]

plt.bar(algorithms, times, color=['blue', 'green'])
plt.xlabel('Algoritma')
plt.ylabel('Waktu Eksekusi (detik)')
plt.title('Perbandingan Waktu Eksekusi Algoritma Pencarian')
plt.show()