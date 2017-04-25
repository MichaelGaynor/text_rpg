#//////////////////////////////////////////////////////////////
#///////////////// CLASS INFO FOR MY EDIFICATION///////////////
#//////////////////////////////////////////////////////////////
# class Person(object):
#   def __init__(self, name, gender, number_of_arms = 2):
#     self.name = name
#     self.gender = gender
#     self.species = "Human"
#     self.number_of_arms = number_of_arms

# marissa = Person("Marissa", "female", 3)
# # print (marissa.name, marissa.gender)
# # print (marissa.species)
# # print (marissa.number_of_arms)

# merilee = Person("Merilee", "female")
# merilee.species = "Robot"
# # print (merilee.species)




# //////////////////////////////////////////////////////////////
# ////////////////////  THE GAME BEGINS  ///////////////////////
# //////////////////////////////////////////////////////////////


from Hero import Hero
from Goblin import Goblin
from Vampire import Vampire
from Witch import Witch


print ("Who are you, brave fool?")
hero_name = raw_input("> ")

the_hero = Hero(hero_name)
monsters = []
region_enemy = Goblin
# monsters.append(Goblin())
# monsters.append(Vampire())
# monsters.append(Witch())

def choose_region():
  global region_enemy
  print (" ")
  print ("In what region wouldst thou start?")
  print ("1. The Shimmering Vale")
  print ("2. The Dark Woods")
  print ("3. The Blasted Heath")
  region_choice = raw_input("> ")
  if region_choice == "1":
    region_enemy = Goblin
  elif region_choice == "2":
    region_enemy = Vampire
  elif region_choice == "3":
    region_enemy = Witch
  return region_enemy

choose_region()

def enemy_generator(region_enemy):
  global monsters
  monsters = []
  print (" ")
  print ("How many monsters dare you fight?")
  number_of_enemies = int(raw_input("> "))
  for i in range(0, number_of_enemies):
    monsters.append(region_enemy())

enemy_generator(region_enemy)


for monster in monsters:
# for i in range(0, len(monsters)-1):
  print ("Brave %s, thou hast encountered a %s" % (hero_name, monster.name))
  # Run game as long as BOTH characters have health
  while monster.health > 0 and the_hero.is_alive():
    print (" ")
    print (" ")
    print ("Thou hast %d health and %d power." % (the_hero.health, the_hero.power))
    print ("The %s has %d health and %d power." % (monster.name, monster.health, monster.power))
    print (" ")
    print ("What wouldst thou?")
    print ("1. fight %s" % (monster.name))
    print ("2. do nothing, I am sorely afrighted")
    print ("3. flee")
    print ("4. Drink aqua vitae")
    user_input = raw_input("> ")
    if user_input == "1":
      monster.take_damage(the_hero.power)
      print ("Thou hast done %d damage to the %s" % (the_hero.power, monster.name))

    elif (user_input == "2"):
      print ("To dare not is to fail.")
      pass
      
    elif (user_input == "3"):
      print ("You escape with thine soul intact.")
      print (" ")
      print ("Goodbye, coward.")
      choose_region()
      enemy_generator(region_enemy)

    elif (user_input == "4"):
      the_hero.increase_health(20)

    elif (user_input == "CONSUME"):
      the_hero.health += monster.health
      the_hero.power += monster.power
      monster.health -= monster.health
      print ("You lunge forward and devour the %s before it can react!" % (monster.name))
      print (" ")
      print ("You gain the %s's strength!" % (monster.name))
      print ("Thine health is now %d and thine power is now %d" % (the_hero.health, the_hero.power))
      
    else:
      print ("Those words mean naught here.")
      choose_region()
      enemy_generator(region_enemy)

    if monster.health <= 0:
      print ("Thou hast defeated the %s" %(monster.name))
      the_hero.xp += monster.xp_value
      the_hero.check_level()
      choose_region()
      enemy_generator(region_enemy)

    if (monster.health > 0):
      the_hero.health -= monster.power
      print ("The %s hits you for %d damage" % (monster.name, monster.power))
      if the_hero.is_alive() == False:
        print ("Thou hast been defeated by the %s" % (monster.name))
        choose_region()
        enemy_generator(region_enemy)















