class Kendaraan:
    def __init__(self, jenis, kecepatan_maksimum):
        self.jenis = jenis
        self.kecepatan_maksimum = kecepatan_maksimum

    def info_kendaraan(self) :
        print(f"mobil jenis {self.jenis} memiliki kecepatan maksimum {self.kecepatan_maksimum} km/jam")
    def bergerak(self):
        print(f"mobil {self.merk} bergerak dengan kecepatan maksimum {self.kecepatan_maksimum} km/jam")

class Mobil(Kendaraan):
    def __init__(self,jenis, kecepatan_maksimum,merk,jumlah_pintu):
        super().__init__(jenis, kecepatan_maksimum)
        self.merk = merk
        self.jumlah_pintu = jumlah_pintu

    def info_mobil(self):
        print(f"Jenis : {self.jenis}, Merk : {self.merk}, Kecepatan maksimum : {self.kecepatan_maksimum} km/jam, Jumlah pintu : {self.jumlah_pintu}")

    def bunyikan_klakson(self):
        print(f"{self.merk} membunyikan klakson : Beep.. Beep...")

class MobilSport(Mobil):
    def __init__(self,jenis,kecepatan_maksimum,merk,jumlah_pintu, tenaga_kuda, harga):
        super().__init__(jenis,kecepatan_maksimum,merk,jumlah_pintu)
        self.__tenaga_kuda = tenaga_kuda
        self.__harga = harga

    def get_tenaga_kuda(self):
        return f"tenaga kuda = {self.__tenaga_kuda}"

    def set_tenaga_kuda (self,value):
        self.__tenaga_kuda =value

    def get_harga(self):
        return f"harga = {self.__harga}"

    def set_harga(self, value):
        self.__harga = value
    
    def info_mobil_sport(self):
        print(f"Jenis : {self.jenis}, Merk : {self.merk}, Tenaga Kuda : {self.__tenaga_kuda}, Kecepatan maksimum : {self.kecepatan_maksimum} km/jam, Jumlah pintu : {self.jumlah_pintu}, Harga : {self.__harga}")

    def mode_balap(self):
        return f"Mobil {self.merk} memasuki mode balap"

mobil = MobilSport("Darat",300,"ferrari", 2, 2000,3000000)
mobil.info_mobil_sport()
mobil.get_tenaga_kuda()
mobil.get_harga()
mobil.info_mobil_sport()
mobil.mode_balap()
mobil.bergerak()
mobil.set_tenaga_kuda(100)
mobil.set_harga(1000000)
mobil.info_mobil_sport()
