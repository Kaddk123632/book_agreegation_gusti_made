class Buku:
    def __init__(self, judul, pengarang, harga):
        self.judul = judul
        self.pengarang = pengarang
        self.harga = harga

    def tampilkan_info(self):
        print("Judul:", self.judul)
        print("Pengarang:", self.pengarang)
        print("Harga:", self.harga)


class TokoBuku:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def tampilkan_daftar_buku(self):
        print(f"Daftar Buku di {self.nama}:")
        for buku in self.daftar_buku:
            buku.tampilkan_info()
            print("------------------------")


# Membuat objek TokoBuku
nama_toko = input("Masukkan nama toko buku: ")
toko_buku = TokoBuku(nama_toko)

# Menambahkan buku ke dalam daftar buku toko
jumlah_buku = int(input("Masukkan jumlah buku yang ingin ditambahkan: "))

for i in range(jumlah_buku):
    print(f"\nMasukkan informasi buku ke-{i+1}:")
    judul = input("Judul buku: ")
    pengarang = input("Pengarang buku: ")
    harga = float(input("Harga buku: "))

    buku = Buku(judul, pengarang, harga)
    toko_buku.tambah_buku(buku)

# Menampilkan daftar buku yang tersedia di toko
toko_buku.tampilkan_daftar_buku()