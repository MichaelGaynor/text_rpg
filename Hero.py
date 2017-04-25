class Hero(object):
  def __init__(self, name = "Incognito"):
    self.name = name
    self.health = 10
    self.power = 5

  def cheer_hero(self):
    print ("Fight hard, %s" % (self.name))

# This class method returns a boolean: True if hero is alive, False if dead
  def is_alive(self):
    if(self.health > 0):
      return True
    else:
      return False
    # This does the same thing as:
    # return self.health > 0