# //////////////////////////////////////////////////////////////
# ////////////////////  THE GAME BEGINS  ///////////////////////
# //////////////////////////////////////////////////////////////


# ----------------------HERE WE IMPORT THE OTHER FILES--------------------------------
from Hero import Hero
from Monster import Monster
from Monster import Goblin
from Monster import Vampire
from Monster import Witch
from Monster import Black_phillip
# from Events import Events
# from random import randint


# ----------------------HERE WE SET SOME OF OUR GLOBAL VARIABLES----------------------
monsters = []
monster_types = ["goblins", "vampires", "witches", "black phillip"]
region_enemy = Goblin
region = 0
game_on = True
playing = True
# Event = Events()
# Goblin = Goblin()
# Vampire = Vampire()
# Witch = Witch()


# ----------------------HERE WE ASK FOR A NAME FOR OUR HERO AND GREET THEM------------
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
print (" ")
print (" ")
print (" ")
print ("Welcome, %s. Wouldst thou like to live deliciously?" % (hero_name))
print (" ")
print (" ")


# ----------------------HERE WE ASK FOR A REGION TO ENTER-----------------------------
# Event.choose_region()
def choose_region():
  global region
  # global region_enemy
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
    region = 0
    # region_enemy = Goblin()
  elif region_choice == "2":
    region = 1
    # region_enemy = Vampire()
  elif region_choice == "3":
    region = 2
    # region_enemy = Witch()
  elif region_choice == "4":
    region = 3
    print (" ")
    print (" ")
    print (" ")
    print ("You may not leave until you face me.")
    # region_enemy = Black_phillip()


# ----------------------HERE WE ASK FOR THE NUMBER OF ENEMIES-------------------------
# Event.enemy_generator(region_enemy)
def enemy_generator(listspot):
  global game_on
  global monsters
  monsters = []
  game_on = True
  print (" ")
  print ("How many monsters dare you fight?")
  number_of_enemies = int(raw_input("> "))
  for i in range(0, number_of_enemies):
    if (monster_types[listspot] == "goblins"):
      monsters.append(Goblin())
    elif (monster_types[listspot] == "vampires"):
      monsters.append(Vampire())
    elif (monster_types[listspot] == "witches"):
      monsters.append(Witch())
    elif (monster_types[listspot] == "black phillip"):
      monsters.append(Black_phillip())


# ----------------------HERE WE TRULY ENTER THE GAME----------------------------------
while playing == True:


# ----------------------HERE WE INITIATE COMBAT---------------------------------------
  choose_region()
  enemy_generator(region)
  for monster in monsters:
    print (" ")
    monster.print_image()
    print (" ")
    print ("Brave %s, thou hast encountered a %s" % (hero_name, monster.name))
    while monster.health > 0 and the_hero.is_alive() and game_on == True:
      # print (" ")
      # print (" ")
      print ("Thou hast %d health and %d power." % (the_hero.health, the_hero.power))
      print ("The %s has %d health and %d power." % (monster.name, monster.health, monster.power))
      print ("What wouldst thou?")
      print ("1. Fight %s" % (monster.name))
      print ("2. Do nothing, I am sorely afrighted")
      print ("3. Flee")
      print ("4. Drink aqua vitae")
      print ("5. Forfeit thy soul for His power")
      user_input = raw_input("> ")

      if user_input == "1":
        monster.take_damage(the_hero.power)
        print ("Thou hast done %d damage to the %s" % (the_hero.power, monster.name))

      elif (user_input == "2"):
        print ("To dare not is to fail.")
        pass

      elif (user_input == "3"):
        print ("Thou escapest with thine soul intact.")
        print (" ")
        print ("God speed thee on thy way, coward.")
        game_on = False

      elif (user_input == "4"):
        the_hero.increase_health(20)

      elif (user_input == "5"):
        print ("...")
        print ("The deal is struck,")
        print ("CONSUME those who oppose thee,")
        print ("and thou shalt have their power")

      elif (user_input == "CONSUME"):
        the_hero.max_health += monster.health
        the_hero.health += monster.health
        the_hero.power += monster.power
        monster.health -= monster.health
        print ("Thee acquired the %s's strength" % (monster.name))
        print ("Thine health is now %d and thine power is now %d" % (the_hero.health, the_hero.power))
        print ("The world has grown darker, He is well pleased with thee")

      else:
        print ("Those words mean naught here.")
        pass


  # ----------------------WHILE FIGHTING------------------------------------------------
      if monster.health <= 0:
        global monsters
        print ("Thou hast defeated the %s" %(monster.name))
        the_hero.xp += monster.xp_value
        the_hero.check_level()
        monsters.remove(monster)
        if monsters == []:
          game_on = False

      if (monster.health > 0):
        the_hero.health -= monster.power
        print ("The %s hits you for %d damage" % (monster.name, monster.power))
        if the_hero.is_alive() == False:
          print ("Thou hast been defeated by the %s" % (monster.name))
          the_hero.health = the_hero.max_health
          game_on = False  
          playing = False
          



