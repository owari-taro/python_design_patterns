from enum import Enum
import time
PizzaProgress = Enum("PizzaProgress", "queued preperation baking ready")
PizaDough = Enum("PizzaDough", "thin thick")
PizzaSauce = Enum("PizzaSauce", "tomato creme_fraiche")
PizzaTopping = Enum(
    "PizzaTopping", "mozzaraella double mozzarella bacon ham mushrooms red onion oregon")
STEP_DELAY = 3
