class Hero: #template

	def __init__(self,name,health,attackPower): #merupakan salh satu konstruktor, Metode __init__(sering disebut "the instaler"),
		                                    # melewati instance yang baru dibuat sebagai argumen disebut "self"
	  self.__name = name       #object/instance variabel (menginisialisasi name dari object secara otomatis) dan menjadikannya private
	  self.__health = health   #object/instance variabel (menginisialisasi health dari object secara otomatis) dan menjadikannya private
	  self.__attPower = attackPower #object/instance variabel (menginisialisasi attackpower dari object secara otomatis) dan menjadikannya private

	# getter
	def getName(self):         #method dengan return
		return self.__name #menginisialisai getname dari method dengan return

	def getHealth(self):         #method dengan return
		return self.__health #menginisialisai gethealth dari method dengan return

	# setter
	def diserang(self,serangPower):      #method dengan argumen, tanpa return
		self.__health -= serangPower #menginisialisai diserang dari method dengan argumen dan tanpa return

	def setAttPower(self,nilaibaru):     #method dengan argumen, tanpa return
		self.__attPower = nilaibaru  #menginisialisai setAttpoer dari method dengan argumen dan tanpa return

# awal dari game
earthshaker = Hero("earthshaker",50, 5) #menginputkan data atribut dari object (hero)

# game berjalan
print(earthshaker.getName())   #untuk mengakses dan menampilkan hasil dari method dengan return
print(earthshaker.getHealth()) #untuk mengakses dan menampilkan hasil dari method dengan return
print(earthshaker.diserang(5)  #untuk mengakses dan menampilkan hasil dari method dengan argumen dan tanpa return
print(earthshaker.getHealth()) #untuk mengakses dan menampilkan hasil dari method dengan argumen dan tanpa return
