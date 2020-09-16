class Hero: #template
	#class variabel
	jumlah = 0 #class variabel / statik variable

	def __init__(self,inputName,inputHealth,inputPower,inputArmor): #merupakan salh satu konstruktor, Metode __init__(sering disebut "the instaler"),
		                                                        # melewati instance yang baru dibuat sebagai argumen disebut "self"
		#instance variabel
		self.name = inputName     #object/instance variabel (menginisialisasi name dari object secara otomatis)
		self.health = inputHealth #object/instance variabel (menginisialisasi health dari object secara otomatis)
		self.power = inputPower   #object/instance variabel (menginisialisasi power dari object secara otomatis)
		self.armor = inputArmor   #object/instance variabel (menginisialisasi armor dari object secara otomatis
		Hero.jumlah += 1          #untuk mengakses variabel class/statik yang sudah dibuat
		print("membuat Hero dengan nama " + inputName) #untuk menampilkan output dari "input name" pada variabel instance/object


hero1 = Hero("sniper",100, 10, 4) #menginputkan data atribut dari object 1 (hero1)
print(Hero.jumlah)                #untuk menampilkan jumlah dari hero/object yang telah dibuat, dari variabel class/statik
hero2 = Hero("mirana",100, 15, 1) #menginputkan data atribut dari object 2 (hero2)
print(Hero.jumlah)                #untuk menampilkan jumlah dari hero/object yang telah dibuat, dari variabel class/statik
hero3 = Hero("ucup",1000, 100, 0) #menginputkan data atribut dari object 2 (hero2)
print(Hero.jumlah)                #untuk menampilkan jumlah dari hero/object yang telah dibuat, dari variabel class/statik

