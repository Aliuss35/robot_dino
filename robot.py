from weapon import Weapon

class Robot():
  def __init__(self, name):
    self.name = name
    self.health = 100
    self.active_weapon = Weapon("Katana", 15)


  def attack(self,dinosaur):
    
    dinos_health_after_attack = dinosaur.health - self.active_weapon.attack_power
    print(f"{self.name} hit {self.active_weapon.attack_power} with {self.active_weapon.name}")
    print(f"{dinosaur.name}'s health is {dinos_health_after_attack}")
    dinosaur.health = dinos_health_after_attack
    
