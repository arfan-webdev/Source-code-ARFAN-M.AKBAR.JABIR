def solve_pindahan_rumah():
    # 1. Definisi Data Barang Pindahan
    # Nama Barang, Berat (kg), Nilai Profit
    items = [
        {"nama": "Kasur Springbed", "berat": 80, "profit": 95},
        {"nama": "Kulkas 2 Pintu",  "berat": 70, "profit": 90},
        {"nama": "Mesin Cuci",      "berat": 50, "profit": 85},
        {"nama": "Lemari Pakaian",  "berat": 120, "profit": 70},
        {"nama": "Sofa Ruang Tamu", "berat": 100, "profit": 60},
        {"nama": "Meja Makan",      "berat": 60, "profit": 50},
        {"nama": "Televisi & Rak",  "berat": 30, "profit": 80},
        {"nama": "Box Pakaian",     "berat": 40, "profit": 85},
        {"nama": "Alat Masak",      "berat": 20, "profit": 75},
        {"nama": "AC (Indoor/Out)", "berat": 35, "profit": 80}
    ]
    
    kapasitas_mobil = 400 # kg
    n = len(items)
    
    # 2. Membuat tabel DP (Matriks)
    dp = [[0 for _ in range(kapasitas_mobil + 1)] for _ in range(n + 1)]

    # 3. Proses Pengisian Tabel DP (Tabulasi)
    for i in range(1, n + 1):
        berat_skrg = items[i-1]["berat"]
        profit_skrg = items[i-1]["profit"]
        
        for w in range(kapasitas_mobil + 1):
            if berat_skrg <= w:
                # Membandingkan profit jika barang diambil vs jika tidak diambil
                dp[i][w] = max(profit_skrg + dp[i-1][w - berat_skrg], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    # 4. Melacak Kembali Barang yang Terpilih (Backtracking)
    total_profit = dp[n][kapasitas_mobil]
    total_berat = 0
    barang_terpilih = []
    w_sisa = kapasitas_mobil
    
    for i in range(n, 0, -1):
        if dp[i][w_sisa] != dp[i-1][w_sisa]:
            barang_terpilih.append(items[i-1])
            total_berat += items[i-1]["berat"]
            w_sisa -= items[i-1]["berat"]

    # 5. Menampilkan Hasil Output Sesuai Instruksi Tugas
    print("="*45)
    print("HASIL OPTIMASI 0/1 KNAPSACK - PINDAHAN RUMAH")
    print("="*45)
    print(f"Kapasitas Maksimal Mobil : {kapasitas_mobil} kg")
    print(f"Total Berat Terpakai     : {total_berat} kg")
    print(f"Total Keuntungan (Profit): {total_profit}")
    print("-" * 45)
    print("Daftar Item yang Terpilih:")
    for b in barang_terpilih:
        print(f"- {b['nama']} ({b['berat']} kg) -> Profit: {b['profit']}")
    print("-" * 45)

if __name__ == "__main__":
    solve_pindahan_rumah()
    