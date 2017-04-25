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

hero_name = raw_input("Greetings hero, what is your name? ")
the_hero = Hero(hero_name)
# the_hero.cheer_hero()
the_goblin = Goblin()

# Run game as long as BOTH characters have health
while the_goblin.health > 0 and the_hero.is_alive():
  print "You have %d health and %d power." % (the_hero.health, the_hero.power)
  print "The goblin has %d health and %d power." % (the_goblin.health, the_goblin.power)
  print "What do you want to do?"
  print "1. fight goblin"
  print "2. do nothing"
  print "3. flee"
  print "> ",
  user_input = raw_input()
  if user_input == "1":
    the_goblin.health -= the_hero.power
    print ("you have done %d damage to the goblin" % (the_hero.power))

  elif (user_input == "2"):
    print ("Great job at doing nothing.")
    pass
    
  elif (user_input == "3"):
    print ("Goodbye, coward")
    break
    
  else:
    print ("INVALID INPUT: %s" %user_input)
    print ("INITIALIZE COMPUTER REFORMATTING...")
    print ("...................................")
    print ("---------                        20")
    print ("...................................")
    print ("------------------------         80")
    print ("...................................")
    print ("--------------------------------100")
    print ("...................................")
    print ("...................................")
    print ("-------REFORMATTING COMPLETE-------")
    print ("...................................")
    print ("...................................")
    print ("WELCOME: RESTART?   Y     N")

  if the_goblin.health <= 0:
    print ("You have defeated the goblin")

  if (the_goblin.health > 0):
    the_hero.health -= the_goblin.power
    print ("The goblin hits you for %d damage" % the_goblin.power)
    if the_hero.is_alive() == False:
      print ("You have been defeated by the goblin")
















