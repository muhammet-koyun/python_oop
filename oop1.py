class Kamera:

    def cek(self):

        print("Fotoğraf çekildi.")
class Telefon:

    def __init__(self):

        self.kamera = Kamera()



telefon = Telefon()

telefon.Kamera.cek()s