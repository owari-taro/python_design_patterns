class Frog:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

    def intercat_with(self, obstacle):
        act = obstacle.action()
        msg = f"{self} the Frog encounters {obstacle} and {act}"
        print(msg)


class Bug:
    def __init__(self):
        return "a bug"

    def action(self):
        return "eats it"


class FrogWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return "\n\n\t-----frog world--------"

    def make_character(self):
        return Frog(self.player_name)


class GameEnviroment:
    def __init__(self, factory):
        self.hero = factory.make_chatacter()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def valid_age(name):
    try:
        age = input(f"welcome {name},how old are you?")
        age = int(age)
    except ValueError as err:
        print(f"age {age} is invalid please try again")
        return (False, age)
    return (True, age)


class Wizard:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interacta_with(self, obstacle):
        act = obstacle.action()
        msg = f"{self} the wizard battles against {obstacle}"
        print(msg)


class Ork:
    def __str__(self):
        return "an evil ork"

    def action(self):
        return "kills it"


def main():
    name = input("hello,whats your name?")
    valid_input = False
    while not valid_input:
        valid_iknput, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    enviroment = GameEnviroment(game(name))
    enviroment.play()
