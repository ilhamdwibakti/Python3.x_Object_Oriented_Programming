class Hero: #template

def __init__(self,name,health,attackPower,armorNumber): # merupakan salh satu konstruktor, Metode __init__(sering disebut "the instaler")
		                                        # melewati instance yang baru dibuat sebagai argumen disebut "self"
		#instance variabel
		self.name = name               #object/instance variabel (menginisialisasi name dari object secara otomatis)
		self.health = health           #object/instance variabel (menginisialisasi health dari object secara otomatis)
		self.attackPower = attackPower #object/instance variabel (menginisialisasi attackPower dari object secara otomatis)
		self.armorNumber = armorNumber #object/instance variabel (menginisialisasi armorNumber dari object secara otomatis)

	def serang(self, lawan):                               #method dengan argumen, tanpa return
		print(self.name + ' menyerang ' + lawan.name ) #menampilan output dari method
		lawan.diserang(self, self.attackPower)         #method dengan argumen, tanpa return

	def diserang(self, lawan, attackPower_lawan):                        #method dengan argumen, tanpa return
		print(self.name + ' diserang ' + lawan.name)                 #menampilan output dari method
		attack_diterima = attackPower_lawan/self.armorNumber         #method dengan argumen, tanpa return
		print('serangan terasa : ' + str(attack_diterima))           #menampilan output dari method
		self.health -= attack_diterima                               #method dengan argumen, tanpa return
		print('darah ' + self.name + ' tersisa ' + str(self.health)) #menampilan output dari method

sniper = Hero('sniper',100,10,5)      #menginputkan data atribut dari object 1 (hero1)
rikimaru = Hero('rikimaru',100,20,10) #menginputkan data atribut dari object 2 (hero2)

sniper.serang(rikimaru) #untuk mengakses dan menampilkan hasil dari method yang telah dideklarasikan
print("\n") #spasi
rikimaru.serang(sniper) #untuk mengakses dan menampilkan hasil dari method yang telah dideklarasikan
print("\n") #spasi
rikimaru.serang(sniper) #untuk mengakses dan menampilkan hasil dari method yang telah dideklarasikan
print("\n") #spasi
rikimaru.serang(sniper) #untuk mengakses dan menampilkan hasil dari method yang telah dideklarasikan
print("\n") #spasi
rikimaru.serang(sniper) #untuk mengakses dan menampilkan hasil dari method yang telah dideklarasikan
print("\n") #spasi
rikimaru.serang(sniper) #untuk mengakses dan menampilkan hasil dari method yang telah dideklarasikan
