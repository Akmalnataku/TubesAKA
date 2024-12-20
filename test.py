import matplotlib.pyplot as plt
import time

# Data warung dan ratingnya
warungs = [
    {"name": "Warung Nasi Ayam", "rating": 4.2},
    {"name": "Warung Sate Kambing", "rating": 4.5},
    {"name": "Bakso Pak Slamet", "rating": 3.8},
    {"name": "Mie Ayam Enak", "rating": 4.7},
    {"name": "Warung Tegal", "rating": 4.0},
    {"name": "Sop Buntut Lezat", "rating": 5.0},
    {"name": "Warung Nasi Kucing", "rating": 3.2},
    {"name": "Warung Sate Ayam", "rating": 2.5},
    {"name": "Cuanki 66", "rating": 4.8},
    {"name": "Mie Yamin mas Budi", "rating": 4.6},
    {"name": "Warung Sego", "rating": 3.0},
    {"name": "Sop Kaki Kambing", "rating": 3.6},
]

# Fungsi iteratif untuk mencari warung dengan rating tertentu hingga maksimal
def search_iterative(warungs, start_rating):
    result = []
    for warung in sorted(warungs, key=lambda x: x["rating"], reverse=True):
        if warung["rating"] >= start_rating:
            result.append(warung)
    return result

# Fungsi rekursif untuk mencari warung dengan rating tertentu hingga maksimal
def search_recursive(warungs, start_rating, result=None):
    if result is None:
        result = []
    if not warungs:
        return result
    warung = warungs[0]
    if warung["rating"] >= start_rating:
        result.append(warung)
    return search_recursive(warungs[1:], start_rating, result)

# Fungsi untuk menampilkan hasil pencarian
def display_results(results):
    for warung in results:
        print(f"Rating: {warung['rating']} - Nama Warung: {warung['name']}")

# Fungsi untuk menghitung waktu eksekusi
def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    return result, end_time - start_time

# Menjalankan program
if __name__ == "__main__":
    # Meminta input rating dari pengguna
    start_rating = float(input("Masukkan rating minimum untuk pencarian: "))
    
    # Menjalankan pencarian iteratif
    sorted_warungs = sorted(warungs, key=lambda x: x["rating"], reverse=True)
    iter_results, iter_time = measure_execution_time(search_iterative, sorted_warungs, start_rating)
    print("\nHasil Pencarian Iteratif:")
    display_results(iter_results)

    # Menjalankan pencarian rekursif
    rec_results, rec_time = measure_execution_time(search_recursive, sorted_warungs, start_rating)
    print("\nHasil Pencarian Rekursif:")
    display_results(rec_results)

    # Menampilkan grafik waktu eksekusi
    algorithms = ["Iteratif", "Rekursif"]
    times = [iter_time, rec_time]

    plt.bar(algorithms, times, color=["blue", "green"])
    plt.xlabel("Algoritma")
    plt.ylabel("Waktu Eksekusi (detik)")
    plt.title("Perbandingan Waktu Eksekusi Algoritma Pencarian")
    plt.show()
