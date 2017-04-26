class Hero(object):
  def __init__(self, name = "Incognito"):
    self.name = name
    self.health = 10
    self.power = 5
    self.max_health = 10
    self.xp = 0
    self.level = 1

  def cheer_hero(self):
    print ("Fight hard, %s" % (self.name))

# This class method returns a boolean: True if hero is alive, False if dead
  def is_alive(self):
    return self.health > 0

  def increase_health(self, amount):
    self.health += amount
    if self.health > self.max_health:
      self.health = self.max_health

  def check_level(self):
    if (self.xp > (self.level * 5)):
      self.level += 1
      self.level_up()

  def level_up(self):
    self.max_health += 10
    self.health = self.max_health
    self.power += 5
    print("Thou hast leveled up %s! Thy max health is now %d and thy power is now %d" % (self.name, self.max_health, self.power))