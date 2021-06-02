import random
from enum import Enum

CarType=Enum("CarType","subcompact compact suv")

class Car:
    pool=dict()
    def __new__(cls,car_type:CarType):
        obj=cls.pool.get(car_type,None)
        if not obj:
            obj=object.__new__(cls)
            cls.pool[car_type]=obj
            obj.car_type=car_type
        return obj
    
    def render(self,color,x,y):
        type=self.car_type
        msg=f"render a car of type {type} and color {color} at({x},{y})"
        print(msg)

def main():
    rnd=random.Random()
    colors="white black silver".split(" ")
    min_point,max_point=0,100
    car_counter=0
    for _ in range(10):
        c1=Car(CarType.subcompact)
        
        
        c1.render(random.choice(colors),rnd.randint(min_point,max_point),
        rnd.randint(min_point,max_point)        
        )
        car_counter+=1