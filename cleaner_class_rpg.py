# //////////////////////////////////////////////////////////////
# ////////////////////  THE GAME BEGINS  ///////////////////////
# //////////////////////////////////////////////////////////////


# ----------------------HERE WE IMPORT THE OTHER FILES--------------------------------
from Hero import Hero
from Monster import Monster
from Monster import Goblin
from Monster import Vampire
from Monster import Witch
from Monster import Goat_guy
# from Events import Events
# from random import randint


# ----------------------HERE WE SET SOME OF OUR GLOBAL VARIABLES----------------------
monsters = []
monster_types = ["goblins", "vampires", "witches", "Goat Guy"]
region_enemy = Goblin
region = 0
game_on = True
playing = True
soul_forfeited = False
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
print ("Welcome, %s. Wouldst thou like to live deliciously?  Y N" % (hero_name))
delicious_living = raw_input("> ")
if delicious_living != "Y" and delicious_living != "y":
  print (" ")
  print (" ")
  print (" ")
  print ("Thy reluctance does thee no favors.")
else:
  print (" ")
  print (" ")
  print (" ")
  print ("Well chosen, %s" % (hero_name))


# ----------------------HERE WE ASK FOR A REGION TO ENTER-----------------------------
# Event.choose_region()
def choose_region():
  global region
  global region_enemy
  print (" ")
  print (" ")
  print (" ")
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
    region_enemy = Goat_guy()


# ----------------------HERE WE ASK FOR THE NUMBER OF ENEMIES-------------------------
# Event.enemy_generator(region_enemy)
def enemy_generator(listspot):
  global game_on
  global monsters
  monsters = []
  game_on = True
  print (" ")
  print ("How many monsters dare you fight?")
  the_number = int(raw_input("> "))
  if the_number < 30 and region_enemy == Goat_guy:
    number_of_enemies = 1
  elif the_number < 30 and region_enemy != Goat_guy:
    number_of_enemies = the_number
  else:
    print("Don't be a dick")
  for i in range(0, number_of_enemies):
    if (monster_types[listspot] == "goblins"):
      monsters.append(Goblin())
    elif (monster_types[listspot] == "vampires"):
      monsters.append(Vampire())
    elif (monster_types[listspot] == "witches"):
      monsters.append(Witch())
    elif (monster_types[listspot] == "Goat Guy"):
      monsters.append(Goat_guy())


# ----------------------HERE WE TRULY ENTER THE GAME----------------------------------
while playing == True:


# ----------------------HERE WE INITIATE COMBAT---------------------------------------
  choose_region()
  enemy_generator(region)
  for monster in monsters:
    if game_on == True:
      print (" ")
      monster.print_image()
      print (" ")
      if monster.name == "Goat Guy, King of All":
        print ("Brave %s, thou hast encountered %s" % (hero_name, monster.name))
      else:
        print ("Brave %s, thou hast encountered a %s" % (hero_name, monster.name))
      while monster.health > 0 and the_hero.is_alive() and game_on == True:
        # print (" ")
        # print (" ")
        print ("Thou hast %d health and %d power." % (the_hero.health, the_hero.power))
        if monster.name == "Goat Guy, King of All":
          print ("%s has %d health and %d power." % (monster.name, monster.health, monster.power))
        else:
          print ("The %s has %d health and %d power." % (monster.name, monster.health, monster.power))
        print (" ")
        print (" ")
        print (" ")
        print ("What wouldst thou?")
        print ("1. Fight %s" % (monster.name))
        print ("2. Do nothing, I am sorely afrighted")
        print ("3. Flee")
        print ("4. Drink aqua vitae")
        global soul_forfeited
        if soul_forfeited:
          print ("---or---")
          print ("Type CONSUME to use His power")
        else:
          print ("5. Forfeit thy soul to acquire His power")
        user_input = raw_input("> ")

        if user_input == "1":
          monster.take_damage(the_hero.power)
          if monster.name == "Goat Guy, King of All":
            print ("Thou has done %d damage to %s" % (the_hero.power, monster.name))
            print ("He seems amused.")
          else:
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
          soul_forfeited = True
          print ("...")
          print ("The deal is struck,")
          print ("CONSUME those who oppose thee,")
          print ("and thou shalt have their power")
          print (" ")
          print (" ")
          print (" ")

        elif (user_input == "CONSUME"):
          soul_forfeited = True
          the_hero.max_health += monster.health
          the_hero.health += monster.health
          the_hero.power += monster.power
          monster.health -= monster.health
          if monster.name == "Goat Guy, King of All":
            print ("Thou acquired %s's strength" % (monster.name))
            print ("Thine health is now %d and thine power is now %d" % (the_hero.health, the_hero.power))
            print ("The world has grown darker, He is well pleased with thee")
          else:
            print ("Thou acquired the %s's strength" % (monster.name))
            print ("Thine health is now %d and thine power is now %d" % (the_hero.health, the_hero.power))
            print ("The world has grown darker, He is well pleased with thee")

        elif (user_input == "THERE CAN BE ONLY ONE!"):
          the_hero.max_health += 20000
          the_hero.health += the_hero.max_health
          the_hero.power += 1000

        else:
          print ("Those words mean naught here.")
          pass


    # ----------------------WHILE FIGHTING------------------------------------------------
        if monster.health <= 0 and monster.name == "Goat Guy, King of All":
          global monsters
          print (" ")
          print (" ")
          print (" ")
          print (" ")
          print ("Thou hast defeated %s" %(monster.name))
          print (" ")
          print (" ")
          if soul_forfeited == False:
            print ("Goat Guy: 'Thou art incorruptible. Be free, %s.'" % (hero_name))
            game_on = False
            playing = False
          elif soul_forfeited == True:
            print (" ")
            print ("Goat Guy: 'Didst thou truly think My power had no price?'")
            print (" ")
            print ("You forfeited your soul for the power to CONSUME.")
            print ("He has chosen to collect on thy debt now.")
            print ("You are defeated.")
            print (" ")
            game_on = False
            playing = False         

        if monster.health <= 0 and monster.name != "Goat Guy, King of All":
          global monsters
          print ("Thou hast defeated the %s" %(monster.name))
          the_hero.xp += monster.xp_value
          the_hero.check_level()
          monsters.remove(monster)
          if monsters == []:
            game_on = False

        if (monster.health > 0) and game_on == True:
          the_hero.health -= monster.power
          print ("The %s hits you for %d damage" % (monster.name, monster.power))
          if the_hero.is_alive() == False:
            print (" ")
            print (" ")
            print ("Thou hast been defeated by the %s" % (monster.name))
            print (" ")
            print (" ")
            print ("Thy game is ended, thy soul forfeit.")
            the_hero.health = the_hero.max_health
            game_on = False  
            playing = False
            



