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
from Monster import Monster
from Monster import Goblin
from Monster import Vampire
from Monster import Witch
from random import randint


print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNh+.`/ymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdo-`    `./yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdo-`          `-+hNMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMNds:`               ``-odNMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMms:`          `````      ``-odNMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMmy:.`         ```````````      ``:smMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMmy/.`         ````````````````       `.:ymMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMNh+.`         ``````````````````````        ./hNMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMNh+-``         `````````  A N  ```````````        `-+hNMMMMMMMMMM")
print("MMMMMMMMMMNdo-```        ```````````         `````````````        `-odNMMMMMMM")
print("MMMMMMMNdo-````       `````````` A D V E N T U R E ``````````        `:smMMMMM")
print("MMMMNms:`````     ``````````````                   ````````````        ./yNMMM")
print("MMMNo-```````` ``````````````````````````````````````````````````        `-+mM")
print("MMMMNds:.```````````````````````````````````````````````````````````     `-sNM")
print("MMMMMMMMmy/-.``````````````````````````````````.--:--```````````````   `-sNMMM")
print("MMMMMMMMMMMNh-`````````````````````````````````.:::::``````````````` `-yNMMMMM")
print("MMMMMMMMMMMMM:`````````````````````````````````.:::::```````````````-yNMMMMMMM")
print("MMMMMMMMMMMMM:`````````````````````````````````-//:::.``````````````hMMMMMMMMM")
print("MMMMMMMMMMMMM-`````````````````````````````````-:/:::.``````````````hMMMMMMMMM")
print("MMMMMMMMMMMMM-``````````````````````````````````.--..```````````````hMMMMMMMMM")
print("MMMMMMMMMMMMM-````````````````````````````````````..````````````````hMMMMMMMNM")
print("MMMMMMMMMMMMM.```````````````````````````````````....```````````````yNNmmNMMMM")
print("MMMMMMMMMMMNN.```````````````````````````````````````````````````.-/hNNMMMMMMM")
print("MMMMMNNNNNNdd````````````````````````````````````````````..-:+syhmNMMMMMMMMMMM")
print("NMMNNmdhyyhoo````````````````````````````````````...-:+sydmNMMMMMMMMMMMMMMMMMM")
print("sss++/::/::::````````````````````````````...-/+syhdmNMMMMMMMMMMMMMMMMMMMMMMMMM")
print("//:::--:--::/`````````````````````..-/+sydmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print(":/o/:-..../+o````````````````.:+shdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("/oo/:-...`./+``````````../oydNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("+yh+/+/+osydd`````.-/ohmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("NMMMMMMMMMMMN-:+shmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
print ("Who are you, brave fool?")
hero_name = raw_input("> ")

the_hero = Hero(hero_name)
monsters = []
# monsters_types = ["vampire", "goblin"]

# for i in range(0, number_of_enemies):
#   rand_num = randint(0,len(monsters_types)-1)
#   if(monsters_types[i] == "vampire"):
#     monsters.append(Vampire())
#   elif(monsters_types[i] == "goblin"):
#     monsters.append(Goblin())

region_enemy = Goblin
game_on = True


while game_on == True:

  def choose_region():
    global region_enemy
    global game_on
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMMhy+sosMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMNs++o/oMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMNNmmNmmmmmmmmmddsso+++yyyysyyssyyhdNMMMMMMM")
    print("MMMMMMMNdys     S H I M M E R I N G      ++omMMMMM")
    print("MMMMMMmyoosyoo        V A L E        ++++oshNMMMMM")
    print("MMMMMMMNNNNNNNNdhhsssso/:/+//sysyyhhyyyydNMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMm:-----mMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMm+:+-::NMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMNNNmmmmdhs+o//:syssssoooossMMMMMMMMM")
    print("MMMMMMMMMmyys+////:::://::----------:--:/NMMMMMMMM")
    print("MMMMMMNyo/:  D A R K  --::-:  W O O D S .---mMMMMM")
    print("MMMMMMho/:--.---:-....---.-.-:--........:hMMMMMMMM")
    print("MMMMMMMMNmy+/:::/::/:::......++oo+++ooossmMMMMMMMM")
    print("MMMMMMMMMMMMNmNNNNNNNNd.```..MMMMMMMMMMMMMMMMMMMMM")
    print("MMMNmmmmmddddddhyyhhhhy////:/yyyyyyyyysyysssssydMM")
    print("MMdssooooo+//-:::::/+//oosso++///+//:/:--..---/hMM")
    print("MMNmhs+//+/::---   B L A S T E D    ---------:yMMM")
    print("MMMMMdso++//::::-    H E A T H    //:::/+++ohhmMMM")
    print("MMMNhyso++::/::::::-:/:++o////+//:/::///+oohMMMMMM")
    print("MMMMNdo++++/+/::::::+/++oo++///+/::--////yhMMMMMMM")
    print("MMMMMMdhsooo++oooo++oosooo+++oo+oooo+o+/dMMMMMMMMM")
    print("MMMMMMNNNNNNNNNNNNNNNNd:-..-sNNNNNNNNMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMm+.../hMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMms--.:dMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMN+:..-dMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMNo/..-dMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMN+//..yMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMNo::--oMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMNo-/:.oMMMMMMMMMMMMMMMMMMMMM")
    print("MMMMMMMMMMMMMMMMMMMMMMmo:+::sMMMMMMMMMMMMMMMMMMMMM")
    print (" ")
    print ("In what region wouldst thou start?")
    print ("1. The Shimmering Vale")
    print ("2. The Dark Woods")
    print ("3. The Blasted Heath")
    print ("4. Noplace, I wouldst leave this accursed realm")
    region_choice = raw_input("> ")
    if region_choice == "1":
      region_enemy = Goblin
    elif region_choice == "2":
      region_enemy = Vampire
    elif region_choice == "3":
      region_enemy = Witch
    elif region_choice == "4":
      # game_on = False
      region_enemy = Black_phillip
    return region_enemy

  choose_region()

  def enemy_generator(region_enemy):
    global monsters
    monsters = []
    print (" ")
    print ("How many monsters dare you fight?")
    number_of_enemies = int(raw_input("> "))
    for i in range(0, number_of_enemies + 1):
      # rand_num = randint(0,len(monsters_types)-1)
      # if(monsters_types[i] == "vampire"):
      #   monsters.append(Vampire())
      # elif(monsters_types[i] == "goblin"):
      #   monsters.append(Goblin())
      monsters.append(region_enemy())

  enemy_generator(region_enemy)

  for monster in monsters:
  # for i in range(0, len(monsters)-1):
    print ("Brave %s, thou hast encountered a %s" % (hero_name, monster.name))
    monster.print_image()

    # Run game as long as BOTH characters have health
    while monster.health > 0 and the_hero.is_alive():
      print (" ")
      print (" ")
      print ("Thou hast %d health and %d power." % (the_hero.health, the_hero.power))
      print ("The %s has %d health and %d power." % (monster.name, monster.health, monster.power))
      print ("What wouldst thou?")
      print ("1. fight %s" % (monster.name))
      print ("2. do nothing, I am sorely afrighted")
      print ("3. flee")
      print ("4. Drink aqua vitae")
      # print ("5. I wouldst leave this wretched game for good!")
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

      # elif (user_input == "5"):
      #   game_on = False
      #   break

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
        monsters.remove(monster)
        if monsters == []:
          choose_region()
          enemy_generator(region_enemy)

      if (monster.health > 0):
        the_hero.health -= monster.power
        print ("The %s hits you for %d damage" % (monster.name, monster.power))
        if the_hero.is_alive() == False:
          print ("Thou hast been defeated by the %s" % (monster.name))
          the_hero.health = the_hero.max_health
          choose_region()
          enemy_generator(region_enemy)











