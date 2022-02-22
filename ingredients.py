from distutils import command
import webbrowser
import requests
from pprint import pprint

##API KEYS IN txt file



class Ingredient:
    """Models a food item used as an ingredient."""

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def expire(self):
        """Expires the ingredient."""
        print(f"whoops, these {self.name} went bad...")
        self.name = "expired " + self.name

    def __add__(self, other):
        """Combines two ingredients."""
        new_name = self.name + other.name
        quantity=other.amount
        return Ingredient(name=new_name, amount=min(self.amount,quantity))
    
    def __str__(self):
        return f"{self.name} ({self.amount})"
    
    def __repr__(self):
        return f"Ingredient(name={self.name}, amount={self.amount})"

    def get_info(self):
        url="https://en.wikipedia.org/wiki/"
        webbrowser.open_new(url+self.name)


class Spice(Ingredient):
    
    def grind(self):
        print(f'you have {self.amount} of ground {self.name} ')
    
    def expire(self):
        if self.name=='salt':
            print('salt never expires!')
        else:
            print(f'Your {self.name} expired')
            self.name= 'old ' + self.name

class Soup():
    def __init__(self,ingredients,app_id,app_key):
        
        self.ingredients=ingredients
        self.app_id=app_id
        self.app_key=app_key 

    def cook(self):
        if len(self.ingredients)>1:
             list_ingredients=[]
             for ingredient in self.ingredients:
                 list_ingredients.append(ingredient.name)
        else:
            pass
        
        all_ing=' '.join(list_ingredients)
        query={"type": "public","q": all_ing, "app_id": self.app_id, "app_key": self.app_key}
        response=requests.get("https://api.edamam.com/api/recipes/v2",params=query)
        print(response)
        data=response.json()
        data=data["hits"]
        self.recipes=[]
        self.url=[]
        for i in range(0,len(data)):
            self.recipes.append(data[i]['recipe']['label'])
            self.url.append(data[i]['recipe']['url'])
        
        self.__get_info()

    def __get_info(self):
        index=0
        for recipe in enumerate(self.recipes):
            
            print('Select:')
            print(recipe)
        option=int(input())
        webbrowser.open_new(self.url[option])


        



if __name__ == '__main__':
    
    try:
        with open(r'C:\Users\alber\Desktop\Coding Nomads\python-301-main\03_inheritance\Login.txt') as f:
            lines=[]
            for line in f.read().splitlines():
                lines.append(line)
    except FileNotFoundError:
        print('File not found')
    except FileExistsError:
        print('File does not exist')    

    API_ID=lines[0]
    API_KEY=lines[1]


    c = Ingredient("carrot", 5)
    p = Ingredient("salt", 2)
   
    #c.get_info()
    #s.get_info()
    spice=Spice('tomatoe',5)
  

    all_ing=[]
    all_ing.append([c,p,spice])
    print(spice.name)
    recipe=Soup(*all_ing,API_ID,API_KEY)
    recipe.cook()
    