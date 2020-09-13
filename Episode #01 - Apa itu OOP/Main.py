class Hero: # template / class
    pass # cara untuk membuat class Hero paling sederhana/simple


hero1 = Hero() # object 1 / instance (instansiate)
hero2 = Hero() # object 2 / instance 2
hero3 = Hero(); # object 3 / instance 3

hero1.name = "sniper" # attribute name,dari hero1 
hero1.health = 100    # attribute health,dari hero1

hero2.name = "sven" # attribute name,dari hero2
hero2.health = 200  # attribute health,dari hero2

hero3.name = "ucup" # attribute name,dari hero3
hero3.health = 1000 # attribute health,dari hero3

print(hero1) # untuk melihat apa object 1 (hero1) merupakan object atau tidak dari class Hero
print(hero1.__dict__) # untuk menampilkan atribut - atribut apa saja yang dimiliki object 1 (hero1)  
print(hero1.name) # untuk menampilkan/mengakses attribute name dari object 1 (hero1)
