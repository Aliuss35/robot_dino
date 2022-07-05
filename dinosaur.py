class Dinosaur():

  def __init__(self, name, attack_power):
    self.name = name
    self.attack_power = attack_power
    self.health= 100


  def attack(self,robot):
    new_health_of_rob = robot.health - self.attack_power
    print(f"{self.name} hit {self.attack_power} with his claws")
    print(f"{robot.name}'s health is now {new_health_of_rob}")
    robot.health = new_health_of_rob

