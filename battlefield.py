from dinosaur import Dinosaur
from robot import Robot


class Battlefield():

  def __init__(self):
    self.dinosaur = Dinosaur("Dino", 20)
    self.robot = Robot("Rob")

  def run_game(self):
    print("Let the fight begin!!")
    self.display_welcome()
    self.battle_phase()
    self.display_winner()

  def display_welcome(self):
    print("Be ready for the mass destruction in the city!!!")

  def battle_phase(self):
    
    while self.robot.health > 0 and self.dinosaur.health > 0:
      self.robot.attack(self.dinosaur)
      self.dinosaur.attack(self.robot)
    

 
  def display_winner(self):
    if self.robot.health <= 0:
      print(f"{self.dinosaur.name} won")

    else:
      print(f"{self.robot.name} won")
