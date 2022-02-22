import numpy as np

class Hero():
    def __init__(self,name,level,start_location,max_hp,hp,damage):
        self.name=name
        self.level=level
        self.start=start_location
        self.max_hp=max_hp
        self.hp=hp
        self.damage=damage
    def __str__(self):
        return(f'This is the hero of the world')

    # def battle(self,other):
    #     hero_attack=np.random.randint(1,6)*self.level
    #     monster_attack=np.random.randint(1,6)*other.level

    #     if hero_attack>monster_attack:
    #         print(f'{self.name} wins the battle')
    #         return True
    #     else:
    #         print(f'{other.name} wins the battle \n {self.name} must retreat for now')
    #         return False
    def attack(self,other):   
        other.hp-=self.damage
        if other.hp<=0:
            print(f'{other.name} is dead')
            other.hp=0

    def heal(self):
        self.hp+=int(10+self.level)
        if self.hp>self.max_hp:
            self.hp=self.max_hp

    def level_up(self,other):
        self.level+=other.level
        self.max_hp+=6
        self.hp=self.max_hp
        self.damage+=2
    
    def stats(self):
        print(f'{self.name}\nlevel:{self.level}\nhp:{self.hp}\nattack{self.damage}')

class Monster:
    def __init__(self,name,level,start_location,damage):
        self.name=name
        self.level=level
        self.start_location=start_location
        self.damage=damage
        
    def __str__(self):
        return (f'This is {self.name} level {self.level}')

    def attack(self,other):   
        other.hp-=self.damage
        if other.hp<=0:
            print(f'{other.name} is dead')
            other.hp=0

    def stats(self):
        print((f'{self.name}\nlevel:{self.level}\nhp:{self.hp}\nattack{self.damage}'))

    
class Enemy(Monster):
    def __init__(self,name,level,start_location,max_hp,hp,damage):
        super().__init__(name,level,start_location,damage)
        self.max_hp=max_hp
        self.hp=hp
        
    def random_generator(self):
        self.number_units=np.random.randint(1,3)
        return self.number_units

   
class Boss(Monster):
    def __init__(self,name,level,start_location,max_hp,hp,damage):
        super().__init__(name,level,start_location,damage)
        self.max_hp=max_hp
        self.hp=hp

    def attack(self,other):
        if self.level> 2*other.level:
            print(f"{other.name} is much weaker than {self.name}")
            multiplier=np.random.randint(0,3)
            other.hp-= self.damage*multiplier
            print(f'{other.name} received huge damage!!!\n{other.name} hp:{other.hp}')

        else:
            other.hp-=self.damage
            print(f"{other.name} received damage")
            print(f'{other.name} received huge damage!!!\n{other.name} hp:{other.hp}')
        
        if other.hp<=0:
            print(f'{other.name} is dead')
            other.hp=0

    def special_attack(self,other):
        hero_attack=np.random.randint(1,6)*other.level
        monster_attack=np.random.randint(1,6)*self.level
        print(f'{self.name} is preparing a special attack!!!\nDestiny will decide who wins')
        if monster_attack>hero_attack:
            print("Special Move cause Instant death!!")
            other.hp=0
        else:
            print(f"Luck is in {other.name} side!!!")
            self.hp=0

   

