class Hero:
	# class variabel
	jumlah_hero = 0 #class variabel / statik variable

	def __init__(self, inputName, inputHealth, inputPower, inputArmor):#merupakan salh satu konstruktor, Metode __init__(sering disebut "the instaler"),
		                                                        # melewati instance yang baru dibuat sebagai argumen disebut "self"
		#instance variabel
		self.name = inputName     #object/instance variabel (menginisialisasi name dari object secara otomatis)
		self.health = inputHealth #object/instance variabel (menginisialisasi health dari object secara otomatis)
		self.power = inputPower   #object/instance variabel (menginisialisasi power dari object secara otomatis)
		self.armor = inputArmor   #object/instance variabel (menginisialisasi armor dari object secara otomatis)
		Hero.jumlah_hero += 1     #untuk mengakses variabel class/statik yang sudah dibuat

	# void function, method tanpa return, tanpa argumen
	def siapa(self):                            #void function / method tanpa return dan tanpa argumen
		print("namaku adalah " + self.name) #menampilan output dari method "self.name"

	# method dengan argumen, tanpa return
	def healthUp(self,up):     #method dengan argumen, tanpa return
		self.health += up  #menginisialisai healthUp dari method dengan argumen dan tanpa return

	# method dengan return
	def getHealth(self):       #method dengan return
		return self.health #menginisialisai gethealth dari method dengan return

 
hero1 = Hero('sniper', 100, 10, 5)    #menginputkan data atribut dari object 1 (hero1)
hero2 = Hero('mario bros', 90, 5, 10) #menginputkan data atribut dari object 2 (hero2)

hero1.siapa()      #untuk mengakses method tanpa return dan argumen
hero1.healthUp(10) #untuk mengakses method dengan argumen dan tanpa return

print(hero1.getHealth()) #untuk mengakses dan menampilkan hasil dari method dengan return
