class Bots:
    def __init__(self, name, health=50, speed=50, power=50): #out of 100
        self.name = name
        self.health = health
        self.speed = speed
        self.power = power
        self.arena = Arena(obstacle='razors', location='forest', crowd=0)
    def basic_attack(self, other_bot):
        other_bot.health -= 20
        if other_bot.health <= 0:
            print(f"Stop it {other_bot.name} loses")
        return self
    def special_attack(self, other_bot):
        if other_bot.health <= 0:
            print(f"Stop it {other_bot.name} loses")
            return self 
        if other_bot.health > 0:
            other_bot.health -= 30
            other_bot.speed -= 20
            if other_bot.health < 0:
                other_bot.health = 0
        elif other_bot.health <= 0:
            print(f"Stop it!! {other_bot.name} has lost.")
            return self
        print(f"{other_bot.name} was attacked")
        print(f"Name: {other_bot.name} | Power {other_bot.power} | Health {other_bot.health} | Speed {other_bot.speed}")
        return self
    def repair(self):
        self.health += 10
        print(f"{self.name} has been healed! New health: {self.health}")
        return self
    def Intro(self, other_bot, location):
        print(f"Welcome to Battle Bots! Featuring {self.name} vs. {other_bot.name}, at {location}")
        print(f"Opponent 1 Stats: {self.name} | Power {self.power} | Health {self.health} | Speed {self.speed}")
        print(f"Opponent 2 Stats: {other_bot.name} | Power {other_bot.power} | Health {other_bot.health} | Speed {other_bot.speed}")
        return other_bot
    def rematch(self, other_bot):
        print(f"{self.name} challenges {other_bot.name} to a rematch!")
        self.health=50
        self.power=50
        self.speed=50
        other_bot.health=50 
        other_bot.power=50 
        other_bot.speed=50
        print(f"{self.name} RESTORED! | Power {self.power} | Health {self.health} | Speed {self.speed}")
        print(f"{other_bot.name} RESTORED! | Power {other_bot.power} | Health {other_bot.health} | Speed {other_bot.speed}")
        return other_bot


class Arena:
    def __init__(self, obstacle='razors', location='forest', crowd= 0):
        self.obstacle = obstacle
        self.location = location
        self.crowd = 0

    def display_location(self):
        self.location
        print(f'This battle will take place at {self.location}!')
        return self
#     def cheer(self):
#         if crowd > 0:
#             print('The crowd went wild!') 

#     def obstacle(self):

#         print('Obstacles have entered the arena')        


blue = Bots("Bluebot")
red = Bots("Redbot")


# print(blue.name)
blue.Intro(red, 'Magic Forest')

blue.special_attack(red).special_attack(red).special_attack(red)
blue.rematch(red)
forest = Arena("Magic Forest")
forest.display_location()
blue.basic_attack(red).special_attack(red).special_attack(red)
blue.rematch(red)
#red.repair().repair().repair().repair().repair()

