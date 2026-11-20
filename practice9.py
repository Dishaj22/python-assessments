class Car:
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0

    def accelerate(self, amount):
        self.speed = self.speed + amount
        print("Current speed:", self.speed)

    def brake(self, amount):
        self.speed = self.speed - amount

        if self.speed < 0:
            self.speed = 0

        print("Current speed:", self.speed)


car1 = Car("BMW")

car1.accelerate(50)
car1.accelerate(20)
car1.brake(30)
car1.brake(100)