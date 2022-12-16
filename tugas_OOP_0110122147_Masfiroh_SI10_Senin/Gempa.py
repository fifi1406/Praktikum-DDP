class Gempa:
    #member1 variabel
    lokasi = ""
    skala = 0
    #member2 konstruktor
    def __init__(self,lokasi,skala):
        self.lokasi = lokasi
        self.skala = skala

    #member3 method
    def dampak(self):
        if( self.skala < 2):
            keterangan = 'Tidak berasa'
        elif(self.skala >= 2 and self.skala < 4):
            keterangan = 'Bangunan retak-retak'
        elif(self.skala >= 4 and self.skala < 6):
            keterangan = 'Bangunan roboh'
        else:
            keterangan = 'Bangunan roboh dan berpotensi tsunami'

        print(
            "Lokasi Gempa\t:",self.lokasi,
            "\nSkala\t\t\t:",self.skala,"richter"
            "\nDampak\t\t\t:",keterangan,
            "\n==================================")
        
    

    