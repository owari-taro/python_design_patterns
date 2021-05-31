from abc import ABCMeta, abstractmethod
from chap2.pizza_builder import PizaDough
import time
from dataclasses import dataclass
from enum import Enum
DELAY = 3

PizzaName = Enum("PizzaName", "margarita creamy_bacon")


class PizzaName(Enum):
    margarita = "margarita"
    creamy_bacon = "creamy_bacon"


class PizzaProgress(Enum):
    queued = "queued"
    preparation = "preparation"
    baking = "baking"
    ready = "ready"


class PizzaSauce(Enum):
    tomato = "tomato"
    cream_fraiche= "cream_fraiche"


class PizzaTopping(Enum):
    mozzarella = "mozzarella"
    double_mozzarella = "double_mozzarella"
    bacon = "bacon"
    ham = "ham"
    mashrooms = "mashrooms"
    red_onion = "red_onion"


PizzaDough = Enum("PizzaDough", "thin thick")


class Builder(ABCMeta):
    @abstractmethod
    def prepare_dough(self):
        pass

    @abstractmethod
    def add_souce(self):
        pass

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def add_topping(self):
        pass


class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder: Builder):
        self.builder = builder
        self.builder.prepare_dough()
        cself.builder.add_souce()
        self.builder.bake()

    @property
    def pizza(self):
        return self.builder.pizza


class MargaritaBuilder(Builder):
    def __init__(self):
        self.pizza = Pizza(PizzaName.margarita)
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizaDough.thin)

    def add_source(self):
        print("adding the tomato sauce margarita....")
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(DELAY)
        print("done with toimato sauce")

    def add_topping(self):
        topping_desc = "double mozzaralla,oregano"
        topping_items = [PizzaTopping.double_mozzarella, PizzaTopping.oregano]
        self.pizza.topping.extend(topping_items)
        time.sleep(DELAY)
        print(f"done with the topping{topping_desc}")


@dataclass
class Pizza:
    name: PizzaName
    dough = None
    sauce = None
    topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough: PizzaDough):
        self.dough = dough
        print(f"preparing the {self.dough.name} dough of your {self}")
        time.sleep(DELAY)
        print(f"done with the {self.dough.name} done")
