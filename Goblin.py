class Goblin(object):
  def __init__(self):
    self.health = 6
    self.power = 2
    self.name = "Goblin"
    self.xp_value = 5

  def print_image(self):
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMmMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMohMMNdmMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMooM+.--sMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMM//hNs/-+mMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMmmNM/:omMN:+sMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMNy/.-:/:--+yMMs/+yMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMy``  H E  /:dms/-/+NMMMMMMMMMMMM")
    print("MMMMMMmdhyysoooo++` . S E E S   ---/dMMMMMMMMMMMMM")
    print("MMMMNhdhysssyo+/:-.`   Y O U  ..-:+mMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMmds.`.---:::``-+--mMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMo..````````.+o/oyMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMN/:-.`-```..-+:-ymMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMm:-..o---.::::-+MMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMh:--:M+`::.`:-`-NMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMd-.:Mo`.-.`-```sMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMM-.`:.`-----.`.-sMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMy..```-:ys/o-`.-oMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMs.`.--:/:-//o:..--/+shNMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMM+----:ssNMddMd.```hNNMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMyo:./dMMMMMMMMy```+MMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMdh+--mMMMMMMMm:``/MMMMMMMdhdNMMMM")
    print("MMMMMMMMMMMMMMMMNy/../dMMMMMMMy..-hMMMMMMMmddNMMMM")
    print("MMMMMMMMMMMMMMMMo.-sMMMMMMMMMMh-:-:oNMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMydMMMMMMMMMMMMM//-.sMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm:ssMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    
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