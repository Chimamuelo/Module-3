import numpy as np
from random import shuffle
class Card:
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None,None, "Ace", "2", "3", "4", "5", "6", "7", 
              "8", "9", "10", "Jack", "Queen", "King"]
    
    
    def __init__(self,r,s):

      

        self.r=r
        self.s=s
    def __str__(self):
    #Returns a human-readable string representation."""
        return f'{Card.rank_names[self.r]} {Card.suit_names[self.s]}'

    def value(self):
        return Card.rank_names[self.r]

    
class Deck(Card):
    def __init__(self):
        
        self.cards=[]
        for r in range(2,15):
            for s in range(4):
                self.card=Card(r,s)
                self.cards.append(self.card)

    def mix(self):
        shuffle(self.cards)
    
    def get_card(self):
        if len(self.cards)==0:
            return
        return self.cards.pop()

    def __str__(self):
        s=[]
        for card in self.cards:
            s.append(str(card))
        return "\n".join(s)
    
     
       



class Player():
    def __init__(self,name):

        self.card=None
        self.name=name

    

##Simulate 21 Game
"""""
Each player draws two cards, the value on those cards must be as close as possible to 21
if the player wants to draw an additional card it is possible.
"""
class Game:
    
    special_card={"Queen":10,"Jack":10,"King":10,"Ace":[1,11]}

    def __init__(self):
        player_1=str(input("Player 1 name:"))
        player_2=str(input("Player 2 name:"))
        self.p_1=Player(player_1)
        self.p_2=Player(player_2)
        self.deck=Deck()
        self.deck.mix()
        
        


    
    
    
    
    
    def play_game(self):
        cards = self.deck.cards
        print(len(self.deck.cards))
        print("beginning War!")
        while len(cards) >= 2:
            m = "q to quit. Any " + \
                "key to play:"
            response = input(m)
            if response == 'q':
                break
            print(f'{self.p_1.name} draws')
            p1_cards=[]
            p1_card1 = self.deck.get_card()
            p1_val1=p1_card1.value()
            p1_card2 = self.deck.get_card()
            p1_val2=p1_card2.value()
            p1n = self.p_1.name
            p2n = self.p_2.name
            print(f'{p1_card1},{p1_card2}')
            print('Want to draw another card?')
            option=int(input("1:yes\n2:no"))
            if option==1:
                p1_card3=self.deck.get_card()
                p1_val3=p1_card3.value()
            elif option==2:
                p1_val3=0
            else:
                pass
            p1_cards.append(p1_val1)
            p1_cards.append(p1_val2)
            p1_cards.append(p1_val3)
            print(p1_cards)
            for i in range(len(p1_cards)):
                if p1_cards[i] == 'Queen' or p1_cards[i]=='Jack' or p1_cards[i]=='King':
                    p1_cards[i]=10
                elif p1_cards[i]=='Ace':
                    option=int(input("Choose Value\n1: 1\n 2: 11"))
                    if option==1:
                        p1_cards[i]=1
                    elif option==2:
                        p1_cards[i]=11
                    else:
                        pass
                else:
                    p1_cards[i]=int(p1_cards[i])
            
            p1_total=sum(p1_cards)
            print(f'{p1n} total is:{p1_total}')
            p2_cards=[]
            print(p2n+'draws')
            p2_card1=self.deck.get_card()
            p2_val1=p2_card1.value()
            p2_card2=self.deck.get_card()
            p2_val2=p2_card2.value()

            print(f'{p2_card1},{p2_card2}')
            print('Want to draw another card?')
            option=int(input("1:yes\n2:no"))
            if option==1:
                p2_card3=self.deck.get_card()
                p2_val3=p2_card3.value()
            elif option==2:
                p2_val3=0
            else:
                pass
            p2_cards.append(p2_val1)
            p2_cards.append(p2_val2)
            p2_cards.append(p2_val3)
            print(p2_cards)
            for i in range(len(p2_cards)):
                if p2_cards[i] == 'Queen' or p2_cards[i]=='Jack' or p2_cards[i]=='King':
                    p2_cards[i]=10
                elif p2_cards[i]=='Ace':
                    option=int(input("Choose Value\n1:1\n 2:11"))
                    if option==1:
                        p2_cards[i]=1
                    elif option==2:
                        p2_cards[i]=11
                    else:
                        pass
                else:
                    p2_cards[i]=int(p2_cards[i])
            
            p2_total=sum(p2_cards)
            print(f'{p2n} total is:{p2_total}')

            if p1_total>p2_total and p1_total<=21:
                print(f'{p1n} has won')
            elif p1_total==p2_total:
                print('draw')
            else:
                print(f'{p2n} has won')

   


g=Game()
g.play_game()