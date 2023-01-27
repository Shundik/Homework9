import time


class Auto:
    brand = 'kia'
    age = 8
    color = 'while'
    mark = 'rio'
    weight = 1500

    def move(self, brand, age, weight):
        self.brand = brand
        self.age = age
        self.weight = weight
        print('move')

    def stop(self, brand, age, weight):
        self.brand = brand
        self.age = age
        self.weight = weight
        print('stop')

    def birthday(self, brand, age, weight):
        self.brand = brand
        self.age = age
        self.weight = weight
        Auto.age += 1


r = Auto()

r.birthday('opel', 8, 1500)
print(Auto.__dict__)
print(r.__dict__)


class Truck(Auto):
    max_load = 500

    def move(self, brand, age, weight):
        print('Attention')
        super().move(brand, age, weight)

    def Load(self):
        time.sleep(1)
        print('Load')
        time.sleep(1)


class Car(Auto):
    max_speed = '160'

    def move(self, brand, age, weight):
        super().move(brand, age, weight)
        x = getattr(Car, 'max_speed')
        print('max speed is ' + x)


r1 = Truck()
r2 = Truck()
r1.move('opel', 15, 1500)
r2.Load()
c1 = Car()
c1.move('opel', 15, 1500)
