#import pygame
import time
import random

#pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 30
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
"""
# Initialize Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Age of Empires-like Game Simulation")
clock = pygame.time.Clock()"""

class init_resources:
    def __init__(self):
        self.resources = {"Wood": 200,"Food": 200, "Gold": 100,  "Stone": 100}
        self.init_berries()
        self.init_sheep()
        self.init_gold()
        self.init_stone()
        self.init_wood()
    
    def init_berries(self):
        self.bushes = 6
        self.berry_resource = 125*self.bushes
        
    def init_sheep(self):
        self.sheep = 8
        self.sheep_food = self.sheep*100
        
    def init_gold(self):
        self.primary_gold_tiles = 7
        self.primary_gold_resources = self.primary_gold_tiles*800

    def init_stone(self):
        self.primary_stone_tiles = 5
        self.primary_stone_resources = self.primary_stone_tiles*800
    
    def init_wood(self):
        self.trees = 20
        self.wood_resources = self.trees*100
    
    def print_resources(self):
        print("Player resources: ")
        print(self.resources)
        print("Map resources: ")
        print("Wood: " + str(self.wood_resources))
        print("Sheep food: " + str(self.sheep_food))
        print("Gold: " + str(self.primary_gold_resources))
        print("Stone: " + str(self.primary_stone_resources))
    

resources = init_resources()
resources.print_resources()


class Resource:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class Villager:
    def __init__(self, name, x, y):
        self.name = name
        self.resources = {"Gold": 0, "Stone": 0, "Wood": 0, "Food": 0}
        self.location = (x, y)

    def gather_resource(self, resource, amount):
        print(f"{self.name} is gathering {amount} {resource}.")
        time.sleep(1)  # Simulate time taken to gather resources
        self.resources[resource] += amount

    def walk_to_location(self, x, y):
        print(f"{self.name} is walking to location.")
        time.sleep(2 * max(abs(x - self.location[0]), abs(y - self.location[1])))
        self.location = (x, y)

class Building:
    def __init__(self, name, x, y):
        self.name = name
        self.location = (x, y)

    def upgrade(self):
        print(f"{self.name} is being upgraded.")
        time.sleep(3)  # Simulate time taken to upgrade

class Barracks(Building):
    def create_unit(self, unit_name):
        print(f"{self.name} is creating {unit_name}.")
        time.sleep(5)  # Simulate time taken to create a unit
        return Unit(unit_name)

class Stable(Building):
    def create_unit(self, unit_name):
        print(f"{self.name} is creating {unit_name}.")
        time.sleep(5)  # Simulate time taken to create a unit
        return Unit(unit_name)

class Blacksmith(Building):
    def upgrade(self, technology_name):
        print(f"{self.name} is upgrading {technology_name}.")
        time.sleep(4)  # Simulate time taken to upgrade

class Unit:
    def __init__(self, name):
        self.name = name

"""# Draw functions
def draw_villager(villager):
    pygame.draw.circle(screen, GREEN, villager.location, 20)

def draw_building(building):
    pygame.draw.rect(screen, RED, (building.location[0] - 30, building.location[1] - 30, 60, 60))"""

# Build order functions
def execute_build_order():
    villagers = []

    for _ in range(2):
        villager = Villager(f"Villager {_+1}", random.randint(50, 100), random.randint(50, 100))
        villagers.append(villager)
        #draw_villager(villager)

    build_house(villagers[0])
    build_house(villagers[1])

    for villager in villagers:
        scout_area(villager)

    gather_herdables(villagers[0], 6)

    build_lumber_camp(villagers[1])

    for _ in range(4):
        build_house(villagers[0])
        gather_berries(villagers[1])

    gather_boars(villagers)

    gather_farms(villagers)

    gather_gold(villagers[0], 3)
    acquire_loom(villagers[0])

    for _ in range(6):
        build_house(villagers[0])
        gather_wood(villagers[1])

    advance_to_feudal_age(villagers[0])

    build_barracks(villagers[1])

    advance_to_feudal_age(villagers[0])  # Advance to Castle Age

    build_stable(villagers[1])
    build_blacksmith(villagers[0])

    advance_to_feudal_age(villagers[0])  # Advance to Castle Age

    build_stable(villagers[1])

    for _ in range(4):
        create_knight(villagers[1])

# Individual build order steps
def build_house(villager):
    print(f"{villager.name} is building a house.")
    time.sleep(4)  # Simulate time taken to build a house

def scout_area(villager):
    print(f"{villager.name} is scouting the area.")
    time.sleep(3)  # Simulate time taken to scout

def gather_herdables(villager, num_villagers):
    print(f"{villager.name} is gathering herdable animals.")
    time.sleep(2 * num_villagers)  # Simulate time taken to gather herdables

def build_lumber_camp(villager):
    print(f"{villager.name} is building a lumber camp.")
    time.sleep(5)  # Simulate time taken to build a lumber camp

def gather_berries(villager):
    print(f"{villager.name} is gathering berries.")
    time.sleep(3)  # Simulate time taken to gather berries

def gather_boars(villagers):
    print("Villagers are gathering boars.")
    time.sleep(2 * len(villagers))  # Simulate time taken to gather boars

def gather_farms(villagers):
    print("Villagers are moving to farms.")
    time.sleep(2 * len(villagers))  # Simulate time taken to move to farms

def gather_gold(villager, num_villagers):
    print(f"{villager.name} is gathering gold.")
    time.sleep(2 * num_villagers)  # Simulate time taken to gather gold

def acquire_loom(villager):
    print(f"{villager.name} is acquiring Loom.")
    time.sleep(4)  # Simulate time taken to acquire Loom

def gather_wood(villager):
    print(f"{villager.name} is gathering wood.")
    time.sleep(3)  # Simulate time taken to gather wood

def advance_to_feudal_age(villager):
    print(f"{villager.name} is advancing to Feudal Age.")
    time.sleep(6)  # Simulate time taken to advance to Feudal Age

def build_barracks(villager):
    print(f"{villager.name} is building a Barracks.")
    time.sleep(5)  # Simulate time taken to build a Barracks

def build_stable(villager):
    print(f"{villager.name} is building a Stable.")
    time.sleep(5)  # Simulate time taken to build a Stable

def build_blacksmith(villager):
    print(f"{villager.name} is building a blacksmith.")
