from abc import abstractmethod
from enum import Enum
import time
PizzaProgress = Enum("PizzaProgress", "queued preperation baking ready")
PizaDough = Enum("PizzaDough", "thin thick")
PizzaSauce = Enum("PizzaSauce", "tomato creme_fraiche")
PizzaTopping = Enum(
    "PizzaTopping",
    "mozzaraella double mozzarella bacon ham mushrooms red onion oregon")
STEP_DELAY = 3


class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []
    def __str__(self):
        return self.name
    def prepared_dough(self,dough):
        self.dough=dough
        time.sleep(STEP_DELAY)
        print(f"done with the {self.dough.name}" dough)

    d
