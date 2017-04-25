class Black_phillip(object):
  def __init__(self):
    self.health = 1
    self.power = 666
    self.name = "Black Phillip"
    
  def take_damage(self, damage):
    self.health += damage
  def is_alive(self):
    return self.health > 0
  def dark_invitation(self):
    print ("Wouldst thou like to live deliciously?")