class Karyawan:
    def _init_(self, nama, umur):
        self.nama = nama
        self.umur = umur
        self.jenisKelamin = None
        self.upahPerHari = None

    def setJenisKelamin(self, jenisKelamin):
        self.jenisKelamin = jenisKelamin

    def setUpahPerHari(self, upahPerHari):
        self.upahPerHari = upahPerHari

    def printInfo(self):
        print("Info")
        print("Nama \t\t: {}".format(self.nama))
        print("Umur \t\t: {}".format(self.umur))
        print("Jenis Kelamin \t: {}".format(self.jenisKelamin))
        print("Upah per Hari \t: {}".format(self.upahPerHari))

    def hitungGajiBulanan(self, jumlahHari):
        if self.upahPerHari is None:
            print("ERROR!: Upah per hari belum diisi")
        else:
            gajiBulanan = self.upahPerHari * jumlahHari
            print("Gaji bulanan {} adalah: {}".format(self.nama, gajiBulanan))

orang1 = Karyawan("Haniif", 90)
orang1.printInfo()

orang2 = Karyawan("Sindu", 190)
orang2.setJenisKelamin("Laki-laki")
orang2.setUpahPerHari(30000)
orang2.printInfo()


orang1.hitungGajiBulanan(28)


orang2.hitungGajiBulanan(30)