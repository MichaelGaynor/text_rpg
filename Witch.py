class Witch(object):
  def __init__(self):
    self.health = 20
    self.power = 60
    self.name = "unholy Witch"
    self.xp_value = 150
    
  def take_damage(self, damage):
    self.health -= damage
  def is_alive(self):
    return self.health > 0