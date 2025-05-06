class NotFound(Exception):
    pass

class EmptyError(Exception):
    pass

class Tdl: #singkatan dari to do list
    def __init__(self):
        self.list_tugas = []
    
    def tambah_tugas(self):
        try:
            tugas = input("Masukkan tugas yang ingin ditambahkan: ")
            if not tugas.strip(): #fungsi strip() untuk menghapus spasi dan tab yang berlebih. 
                raise EmptyError("Input tidak boleh kosong.")
            self.list_tugas.append(tugas)
            print("Tugas berhasil ditambahkan!")
        except EmptyError as e:
            print(f"Error: {e}")
    
    def hapus_tugas(self):
        try:
            if not self.list_tugas:
                raise EmptyError("Daftar tugas kosong.")
            
            self.tampilkan_tugas()
            pilihan = input("Masukkan nomor tugas yang ingin dihapus: ")
            
            if not pilihan.strip():
                raise EmptyError("Input tidak boleh kosong.")
            
            try:
                pilihan = int(pilihan)#mengubah inputan menjadi tipe data integer
                pilihan = pilihan-1 #mencari nomor tugas tetapi dikurangi 1 karena index set dimulai dari 0 
            except ValueError:
                raise ValueError("Input harus berupa angka.")
            
            if pilihan < 0 or pilihan >= len(self.list_tugas):
                raise NotFound(f"Tugas dengan nomor {pilihan+1} tidak ditemukan.")
            
            del self.list_tugas[pilihan]
            print(f"Tugas dengan nomor {pilihan+1} berhasil dihapus.")
        except (EmptyError, ValueError, NotFound) as e:
            print(f"Error: {e}")
    
    def tampilkan_tugas(self):
        try:
            if not self.list_tugas:
                raise EmptyError("Daftar tugas kosong.")
            
            print("Daftar Tugas:")
            for i, tugas in enumerate(self.list_tugas):
                print(f"{i+1}. {tugas}")#menampilkan daftartugas dengan urutan dari 1
        except EmptyError as e:
            print(f"Error: {e}")


todo = Tdl()
    
while True:
    try:
        print("\nPilih aksi:")
        print("1. Tambah tugas")
        print("2. Hapus tugas")
        print("3. Tampilkan daftar tugas")
        print("4. Keluar")
            
        pilihan = input("Masukkan pilihan (1/2/3/4): ")
            
        if not pilihan.strip():
            raise EmptyError("Input tidak boleh kosong.") #akan menyebabkan exception error EmptyError
            
        try:
            pilihan = int(pilihan)
        except ValueError:
            raise ValueError("Input harus berupa angka 1-4.")#jika inputan bukan 1/2/3/4 maka akan menyebabkan Value Error
            
        if pilihan == 1:
            todo.tambah_tugas()
        elif pilihan == 2:
            todo.hapus_tugas()
        elif pilihan == 3:
            todo.tampilkan_tugas()
        elif pilihan == 4:
            print("Keluar dari program.")
            break
        else:
            raise ValueError("Pilihan harus antara 1-4.")
                
    except (EmptyError, ValueError) as e:
        print(f"Error: {e}")
