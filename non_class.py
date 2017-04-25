# This is a procedural approach to a text-based rpg game
# The hero is fighting a goblin
# He has the options to:

# 1. fight
# 2. do nothing
# 3. flee

def main():
  hero_health = 10
  hero_power = 5
  goblin_health = 6
  goblin_power = 2

  while goblin_health > 0 and hero_health > 0:
    print "You have %d health and %d power." % (hero_health, hero_power)
    print "The goblin has %d health and %d power." % (goblin_health, goblin_power)
    print "What do you want to do?"
    print "1. fight goblin"
    print "2. do nothing"
    print "3. flee"
    print "> ",
    user_input = raw_input()
    if (user_input == "1"):
      goblin_health -= hero_power
      print ("you have done %d damage to the goblin" % (hero_power))
 
    elif (user_input == "2"):
      # print ("Great job at doing nothing.")
      pass
    
    elif (user_input == "3"):
      print ("Goodbye, coward")
      break
    
    else:
      print ("INVALID INPUT: %s" %user_input)
      print ("INITIALIZE COMPUTER REFORMATTING...")
      print ("------------ 20")
      print ("------------ 80")
      print ("------------100")
      print ("REFORMATTING COMPLETE")
      print ("WELCOME: RESTART? Y N")

    if goblin_health <= 0:
      print ("You have defeated the goblin")

    if (goblin_health > 0):
      hero_health -= goblin_power
      print ("The goblin hits you for %d damage" % goblin_power)
      if hero_health <= 0:
        print ("You have been defeated by the goblin")

main()

