import random
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename="logs11.log", filemode="a",
                    format="We have next logging message: "
                           "%(asctime)s:%(levelname)s-%(message)s"
                    )

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None, phone=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        self.phone = phone

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_phone(self):
        self.phone = Phone(phone_list)


    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def playing_games(self):
        if self.phone:
            self.gladness += self.phone.gladness
            self.money -= 5
        else:
            pass




    def eat(self):
        if self.home.food <=0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            logging.info("bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            print("Bought food")
            logging.info("bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            print("Hooray! Delicious!")
            logging.info("Delicious time")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f" Today the {day} of {self.name}'s life "
        print(f"{day:=^50}", "\n")
        logging.info("Days")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}", "\n")
        logging.info("human indexes")
        print(f"Money – {self.money}")
        logging.info("money")
        print(f"Satiety – {self.satiety}")
        logging.info("satiety")
        print(f"Gladness – {self.gladness}")
        logging.info("gladness")
        home_indexes = "Home indexes"
        print(f"{home_indexes:^50}", "\n")
        logging.info("home indexes")
        print(f"Food – {self.home.food}")
        logging.info("food")
        print(f"Mess – {self.home.mess}")
        logging.info("mess")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        logging.info("car indexes")
        print(f"Fuel – {self.car.fuel}")
        logging.info("fuel")
        print(f"Strength – {self.car.strength}")
        logging.info("car strength")

    def is_alive(self):
        if self.gladness < 0:
            print("Depression…")
            logging.info("depression")
            return False
        if self.satiety < 0:
            print("Dead…")
            logging.info("dead")
            return False
        if self.money < -500:
            print("Bankrupt…")
            logging.info("bankrupt")
            return False

    def live(self, day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            print("Settled in the house")
            logging.info("bought a house")
            self.get_home()
        if self.car is None:
            self.get_car()
            print(f"I bought a car {self.car.brand}")
            logging.info("bought a car")
        if self.job is None:
            self.get_job()
            print(f"I don't have a job, I'm going to get a job "
                  f"{self.job.job} with salary {self.job.salary}")
            logging.info("got a job")
        if self.phone is None:
            self.get_phone()
            print(f"I bought a phone {self.phone.phone} for {self.phone.salary_less}" )
            logging.info("bought a phone")
        self.days_indexes(day)
        dice = random.randint(1, 5)
        if self.satiety < 20:
            print("I'll go eat")
            logging.info("needs to eat")
            self.eat()
        elif self.gladness < 20:
            print("I'll play some games!")
            logging.info("playing games")
            self.phone()
            if self.home.mess > 15:
                print("I want to chill, but there is so much mess…")
                logging.info("mess in the house")
                print("So I will clean the house")
                logging.info("cleaning the house")
                self.clean_home()
            else:
                print("Let`s chill!")
                logging.info("chilling")
                self.chill()
        elif self.money < 0:
            print("Start working")
            logging.info("working")
            self.work()
        elif self.car.strength < 15:
            print("I need to repair my car")
            logging.info("need to repair a car")
            self.to_repair()
        elif dice == 1:
            print("Let`s chill!")
            logging.info("need to chill")
            self.chill()
        elif dice == 2:
            print("Start working")
            logging.info("working")
            self.work()
        elif dice == 3:
            print("Cleaning time!")
            logging.info("cleaning")
            self.clean_home()
        elif dice == 4:
            print("Time for treats!")
            logging.info("Time for treats")
            self.shopping(manage="delicacies")
        elif dice == 5:
            print("Playing games!")
            logging.info("Playing games")
            self.playing_games()

brands_of_car = {
    "BMW":{"fuel":100, "strength":100, "consumption": 6},
    "Lada":{"fuel":50, "strength":40, "consumption": 10},
    "Volvo":{"fuel":70, "strength":150, "consumption": 8},
    "Ferrari":{"fuel":80, "strength":120, "consumption": 14} }


class Auto:
    def __init__(self, brand_list):
        self.brand=random.choice(list (brand_list))
        self.fuel=brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption=brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move")
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

job_list = {
 "Java developer":
                {"salary":50, "gladness_less": 10 },
 "Python developer":
                {"salary":40, "gladness_less": 3 },
 "C++ developer":
                {"salary":45, "gladness_less": 25 },
 "Rust developer":
                {"salary":70, "gladness_less": 1 },
 }


class Job:
    def __init__(self, job_list):
        self.job=random.choice(list(job_list))
        self.salary=job_list[self.job]["salary"]
        self.gladness_less=job_list[self.job]["gladness_less"]

phone_list = {
 "Iphone":
                {"salary_less":50, "gladness": 25 },
 "Samsung":
                {"salary_less":40, "gladness": 5 },
 "Redmi":
                {"salary_less":30, "gladness": 3 },
 "Google Pixel":
                {"salary_less":45, "gladness": 10 },
 }


class Phone:
    def __init__(self, phone_list):
        self.phone=random.choice(list(phone_list))
        self.salary_less=phone_list[self.phone]["salary_less"]
        self.gladness=phone_list[self.phone]["gladness"]

nick = Human(name="Nick")
for day in range(1,800):
    if nick.live(day) == False:
        break