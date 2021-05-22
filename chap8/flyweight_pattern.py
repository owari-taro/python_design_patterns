from enum import Enum

CarType = Enum('CarType', 'subcompact compact suv')


class Car:
    pool = dict()

    def __new__(cls, car_type):
        print(cls.pool)
        obj = cls.pool.get(car_type, None)
        if not obj:
            obj = object.__new__(cls)
            cls.pool[car_type] = obj
            obj.car_type = car_type
        return obj

    def render(self, color, x, y):
        type = self.car_type
        msg = f'render a car of type {type} and color {color} at ({x},{y})'
        print(msg)
