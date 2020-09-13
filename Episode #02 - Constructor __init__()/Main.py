class Hero: # template / class

    def __init__(self, inputName, inputHealth,inputPower, inputArmor): # merupakan salah satu konstruktor. Metode __init__(sering disebut "the initialiser"),
                                                                       # melewati instance yang baru dibuat sebagai argumen (secara konvensional disebut "self")
            
    	self.name = inputName     # menginisialisasi name dari object  secara otomatis
    	self.health = inputHealth # menginisialisasi health dari object secara otomatis
    	self.power = inputPower   # menginisialisasi power dari object secara otomatis
    	self.armor = inputArmor   # menginisialisasi armor dari object secara otomatis


hero1 = Hero("sniper",100, 10, 4) # menginputkan data atribut dari object 1 (hero1)
hero2 = Hero("mirana",100, 15, 1) # menginputkan data atribut dari object 2 (hero2)
hero3 = Hero("ucup",1000, 100, 0) # menginputkan data atribut dari object 3 (hero3)

print(hero1.__dict__) # menampilkan/melihat semua atribut dari object 1 (hero1)
print(hero2.__dict__) # menampilkan/melihat semua atribut dari object 2 (hero2)
print(hero3.__dict__) # menampilkan/melihat semua atribut dari object 3 (hero3)
