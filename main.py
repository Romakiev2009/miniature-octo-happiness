import random


class Car:
    def __init__(self, model, fuel=100, condition=100):
        self.model = model
        self.fuel = fuel
        self.condition = condition

    def drive(self, distance):
        fuel_consumed = distance * 0.1
        if self.fuel >= fuel_consumed:
            self.fuel -= fuel_consumed
            print(f"The {self.model} drove {distance} km.")
            self.condition -= random.randint(1, 5)
        else:
            print(f"Not enough fuel to drive {distance} km.")
            return False

        return True
    def refuel(self, amount):
        self.fuel += amount
        if self.fuel > 100:
            self.fuel = 100
        print(f"The {self.model} was refueled. Current fuel: {self.fuel}")

    def repair(self):
        self.condition = 100
        print(f"The {self.model} has been repaired. Condition restored to 100.")

    def check_condition(self):
        if self.condition < 50:
            print(f"Warning: The {self.model} is in poor condition and needs repair.")

    def check_fuel(self):
        if self.fuel < 20:
            print(f"Warning: The {self.model} is low on fuel.")


class Driver:
    def __init__(self, name, car):
        self.name = name
        self.car = car

    def drive(self, distance):
        print(f"{self.name} is trying to drive the car.")
        if not self.car.drive(distance):
            print(f"{self.name} couldn't drive due to insufficient fuel.")
            return False
        self.check_conditions()
        return True

    def check_conditions(self):
        self.car.check_condition()
        self.car.check_fuel()

    def random_event(self):
        events = [
            ("You got a flat tire!", self.car.repair),
            ("You found a gas station!", lambda: self.car.refuel(random.randint(20, 50))),
            ("You were stopped by the police and fined $100.", lambda: print(f"{self.name} received a fine!")),
            ("You had a smooth ride with no incidents.", lambda: print(f"{self.name} had a smooth drive.")),
            ("You met a friend on the road!", lambda: print(f"{self.name} had a nice chat with a friend.")),
            ("You encountered heavy traffic!", lambda: print(f"{self.name} was stuck in traffic for an hour.")),
            ("You found a beautiful scenic spot!", lambda: print(f"{self.name} stopped to enjoy the view.")),
        ]
        event = random.choice(events)
        print(f"Event: {event[0]}")
        event[1]()

    def live_day(self):
        distance = random.randint(10, 100)
        if not self.drive(distance):
            return False
        self.random_event()
        return True


my_car = Car("Toyota Corolla")
driver = Driver("Vasya", my_car)

for day in range(1, 366):
    print(f"\nDay {day}:")
    if not driver.live_day():
        print(f"{driver.name} cannot continue driving. Simulation ended.")
        break  # Exit the loop if the driver can't continue
