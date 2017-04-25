class Goblin(object):
  def __init__(self):
    self.health = 6
    self.power = 2
    self.name = "Goblin"
    self.xp_value = 5
    
  def take_damage(self, damage):
    self.health -= damage
  def is_alive(self):
    return self.health > 0

# class Goblin_Guard(object):
#   def __init__(self):
#     self.health = 8
#     self.power = 3
#     self.name = "Goblin Guard"


# class Goblin_King(object):
#   def __init__(self):
#     self.health = 10
#     self.power = 5
#     self.name = "Goblin King"
#     self.items = {
#       "gold": 100
#     }