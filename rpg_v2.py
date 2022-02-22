from re import A
import char_rpg_v2 as char
import numpy as np
import time

class Game():
    def __init__(self,hero,enemies):
        self.hero=hero
        self.enemies=enemies

    def game_loop(self):
        pass
        playing=True

        while playing:
            if self.enemies and self.hero.hp>0:
            
                self.movement()

                print(board)

            
                
            
            else:
                if self.hero.hp>0:
                
                    playing=False
                    print(f'{self.hero.name} has defeated all enemies\n The land is free!!!')
                else:
                    print(f'{self.hero.name} has been defeated!!\nThe land will face a reigin of terror')
                    playing=False

            
    def movement(self):
        print('Move with the wasd keys')
        print('w:up\na:left\ns:down\nd:right')

        move=str(input('Move\n'))
        while move not in ['w','s','a','d']:
            print("Not Valid, Choose again")
            print('w:up\na:left\ns:down\nd:right')
            move=str(input('Move'))

        #Movement logic
        if move=='a':
            board[self.hero.start[0]][self.hero.start[1]]=''
            self.hero.start[1]-=1
            if self.hero.start[1]<=0:
                self.hero.start[1]=0

            x=self.check_board(self.hero,self.enemies)
            if x:
                board[self.hero.start[0]][self.hero.start[1]]=f'{self.hero.name}'
               
            else:
                self.hero.start[1]+=1
                board[self.hero.start[0]][self.hero.start[1]]=f'{self.hero.name}'
            
        elif move=='d':
            board[self.hero.start[0]][self.hero.start[1]]=''
            self.hero.start[1]+=1
            if self.hero.start[1]>=4:
                self.hero.start[1]=4

            x=self.check_board(self.hero,self.enemies)
            if x:
                
                board[self.hero.start[0]][self.hero.start[1]]=f'{self.hero.name}'
                
            else:
               
                self.hero.start[1]-=1
                board[self.hero.start[0]][self.hero.start[1]]=f'{self.hero.name}'

            
            
        elif move=='w':
            board[self.hero.start[0]][self.hero.start[1]]=''
            self.hero.start[0]-=1
            if self.hero.start[0]<=0:
                self.hero.start[0]=0
            x=self.check_board(self.hero,self.enemies)
            if x:
                board[self.hero.start[0]][self.hero.start[1]]=f'{self.hero.name}'
               
            else:
                self.hero.start[0]+=1
                board[self.hero.start[0]][self.hero.start[1]]=f'{self.hero.name}'
            
            
        elif move=='s':
            board[self.hero.start[0]][self.hero.start[1]]=''
            self.hero.start[0]+=1
            if self.hero.start[0]>=4:
                self.hero.start[0]=4
            x=self.check_board(self.hero,self.enemies)
            if x:
                board[self.hero.start[0]][self.hero.start[1]]=f'{self.hero.name}'
                
            else:
                self.hero.start[0]-=1
                board[self.hero.start[0]][self.hero.start[1]]=f'{self.hero.name}'
            



    def check_board(self,hero,enemies):
        enemy=[l for l in enemies if l.start_location==hero.start]
        
        if enemy:
            
            print(f'{enemy[0].name} is in your way!!!')
            
            if(enemy[0].name=='King of Evil'):
                win,level=self.boss_combat(hero,enemy[0])
                if win:
                    enemies.remove(enemy[0])
                
                
            else:
                units=enemy[0].random_generator()
                number_enemy=[enemy[0]]*units
                print(len(number_enemy))
                win,level=self.combat(hero,number_enemy)
                if win:
                    enemies.remove(enemy[0])
            
                

        else:
            win=True
            level=False
            print('Free path')
        if level:
            hero.level_up(enemy[0])
        time.sleep(.5)
        

        return win


    def combat(self,hero,enemies):
        playing=True
        while playing:
            hero.stats()
            self.hero_turn(hero,enemies)

           
            for enemy in enemies:
                enemy.stats()
                self.enemy_turn(hero,enemy)

            if hero.hp<=0:
                playing =False
                win=False
                level_up=False
            
            if enemies:
                pass
            else:
                playing=False
                win=True
                level_up=True


        print(playing)
        return win,level_up
            


           
    
    def hero_turn(self,hero,enemies):
        print(f'{hero.name} turn')

        valid=True
        while valid:          
            print('Choose your objective:')
            for i in range(0,len(enemies)):
                print(str(i)+':'+enemies[i].name)
            objective=int(input())

           
            while objective not in range(len(enemies)):
                print("Not Valid, Choose again")
                for i in range(0,len(enemies)):
                    print(str(i)+':'+enemies[i].name)
                objective=int(input("Choose your objective"))
            
            decision=int(input("Choose your action:1 attack the enemy, 2:Recover health"))
            print('\n')
            if decision==1:
                hero.attack(enemies[objective])

                
            elif decision==2:
                hero.heal()
            if enemies[objective].hp<=0:
                enemies.remove(enemies[objective])
            valid=False
            


    def enemy_turn(self,hero,enemy):
        print(f'{enemy.name} is going to attack!!')
        valid=True
        while valid:
            if hero.hp>0:  
                enemy.attack(hero)
                valid=False
            else:
                valid=False
        print(f'{hero.name} has received damage!!!, {hero.hp} life points')

    def boss_combat(self,hero,enemy):
        playing=True
        while playing:
            hero.stats()
            self.hero_turn_boss(hero,enemy)

           
            enemy.stats()
            self.boss_turn(hero,enemy)

            if hero.hp<=0:
                playing =False
                win=False
                level_up=False
            
            if enemy.hp>0:
                pass
            else:
                playing=False
                win=True
                level_up=True
                

            print(playing)
        return win,level_up
        
    def hero_turn_boss(self,hero,enemy):
        print(f'{hero.name} turn')

        valid=True
        while valid:          

            
            decision=int(input("Choose your action:1 attack the enemy, 2:Recover health"))
            print('\n')
            if decision==1:
                hero.attack(enemy)

                
            elif decision==2:
                hero.heal()
            if enemy.hp<=0:
                enemy=False
            valid=False

    def boss_turn(self,hero,enemy):
        prob_1=np.random.randint(0,5)*enemy.level
        prob_2=np.random.randint(0,5)*.2*enemy.level
        if prob_2>prob_1:
            enemy.special_attack(hero)
        else:
            enemy.attack(hero)
            





    
            

board=np.zeros((6,6),dtype=str)

for i in range(len(board[0])):
    for j in range(len(board[1])):
        board[i][j]=''



def start_location():
    start_xlocation=np.random.randint(0,4)
    start_ylocation=np.random.randint(0,4)
    start=[start_xlocation,start_ylocation]
    return start

enemies=[
    char.Enemy('Dragon',20,start_location(),25,25,5),
    char.Enemy('Goblin',1,start_location(),2,2,2),
    char.Enemy('Bandit',2,start_location(),4,4,4),
    char.Boss('King of Evil',30,start_location(),50,50,10),

    
    ]
hero=char.Hero('Hero',1,start_location(),10,10,2)
board[hero.start[0]][hero.start[1]]= f'{hero.name}'
for enemy in enemies:
    if board[enemy.start_location[0]][enemy.start_location[1]]:
        new_loc=start_location()
        enemy.start_location=new_loc
        board[new_loc[0],new_loc[1]]=f'{enemy.name}'
    else:
        board[enemy.start_location[0]][enemy.start_location[1]]=f'{enemy.name}'



print(board)
game=Game(hero,enemies)
game.game_loop()





