class Kendaraan:
    def __init__(self,jenis, kecepatan_maksimum):
        self.jenis=jenis
        self.kecepatan_maksimum=kecepatan_maksimum
    def info_kendaraan(self):
        return f"{self.jenis} adalah {jenis}"
    def bergerak(self):
        return f"{self.jenis} bergerak dengan kecepatan {kecepatan_maksimum}"
class Mobil(Kendaraan):

class MobilSport(Mobil):

