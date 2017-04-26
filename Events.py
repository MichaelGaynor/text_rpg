from Monster import Monster
from Monster import Goblin
from Monster import Vampire
from Monster import Witch

# ---------------------THIS IS WHERE WE CREATE OUR EVENTS---------
class Events(object):

# ---------------------THIS IS WHERE WE CHOOSE OUR REGION---------
    # def choose_region(self):
    #     global region_enemy
    #     print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    #     print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    #     print("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")
    #     print("MMMMMMMMMMMMMMMMMMMMMMMhy+sosMMMMMMMMMMMMMMMMMMMMM")
    #     print("MMMMMMMMMMMMMMMMMMMMMMNs++o/oMMMMMMMMMMMMMMMMMMMMM")
    #     print("MMMMMMMNNmmNmmmmmmmmmddsso+++yyyysyyssyyhdNMMMMMMM")
    #     print("MMMMMMMNdys     S H I M M E R I N G      ++omMMMMM")
    #     print("MMMMMMmyoosyoo        V A L E        ++++oshNMMMMM")
    #     print("MMMMMMMNNNNNNNNdhhsssso/:/+//sysyyhhyyyydNMMMMMMMM")
    #     print("MMMMMMMMMMMMMMMMMMMMMMm:-----mMMMMMMMMMMMMMMMMMMMM")
    #     print("MMMMMMMMMMMMMMMMMMMMMMm+:+-::NMMMMMMMMMMMMMMMMMMMM")
    #     print("MMMMMMMMMMMMMMNNNmmmmdhs+o//:syssssoooossMMMMMMMMM")
    #     print("MMMMMMMMMmyys+////:::://::----------:--:/NMMMMMMMM")
    #     print("MMMMMMNyo/:  D A R K  --::-:  W O O D S .---mMMMMM")
    #     print("MMMMMMho/:--.---:-....---.-.-:--........:hMMMMMMMM")
    #     print("MMMMMMMMNmy+/:::/::/:::......++oo+++ooossmMMMMMMMM")
    #     print("MMMMMMMMMMMMNmNNNNNNNNd.```..MMMMMMMMMMMMMMMMMMMMM")
    #     print("MMMNmmmmmddddddhyyhhhhy////:/yyyyyyyyysyysssssydMM")
    #     print("MMdssooooo+//-:::::/+//oosso++///+//:/:--..---/hMM")
    #     print("MMNmhs+//+/::---   B L A S T E D    ---------:yMMM")
    #     print("MMMMMdso++//::::-    H E A T H    //:::/+++ohhmMMM")
    #     print("MMMNhyso++::/::::::-:/:++o////+//:/::///+oohMMMMMM")
    #     print("MMMMNdo++++/+/::::::+/++oo++///+/::--////yhMMMMMMM")
    #     print("MMMMMMdhsooo++oooo++oosooo+++oo+oooo+o+/dMMMMMMMMM")
    #     print("MMMMMMNNNNNNNNNNNNNNNNd:-..-sNNNNNNNNMMMMMMMMMMMMM")
    #     print("MMMMMMMMMMMMMMMMMMMMMMm+.../hMMMMMMMMMMMMMMMMMMMMM")
    #     print("MMMMMMMMMMMMMMMMMMMMMMms--.:dMMMMMMMMMMMMMMMMMMMMM")
    #     print("MMMMMMMMMMMMMMMMMMMMMMN+:..-dMMMMMMMMMMMMMMMMMMMMM")
    #     print("MMMMMMMMMMMMMMMMMMMMMMNo/..-dMMMMMMMMMMMMMMMMMMMMM")
    #     print("MMMMMMMMMMMMMMMMMMMMMMN+//..yMMMMMMMMMMMMMMMMMMMMM")
    #     print("MMMMMMMMMMMMMMMMMMMMMMNo::--oMMMMMMMMMMMMMMMMMMMMM")
    #     print("MMMMMMMMMMMMMMMMMMMMMMNo-/:.oMMMMMMMMMMMMMMMMMMMMM")
    #     print("MMMMMMMMMMMMMMMMMMMMMMmo:+::sMMMMMMMMMMMMMMMMMMMMM")
    #     print (" ")
    #     print ("In what region wouldst thou start?")
    #     print ("1. The Shimmering Vale")
    #     print ("2. The Dark Woods")
    #     print ("3. The Blasted Heath")
    #     print ("4. Noplace, I wouldst leave this accursed realm")
    #     region_choice = raw_input("> ")
    #     if region_choice == "1":
    #       region_enemy = Goblin()
    #     elif region_choice == "2":
    #       region_enemy = Vampire()
    #     elif region_choice == "3":
    #       region_enemy = Witch()
    #     elif region_choice == "4":
    #       region_enemy = Black_phillip()


# ---------------------THIS IS WHERE WE CHOOSE NUMBER OF ENEMIES--
    # def enemy_generator(self, baddies):
    #     global game_on
    #     global monsters
    #     monsters = []
    #     game_on = True
    #     print (" ")
    #     print ("How many monsters dare you fight?")
    #     number_of_enemies = int(raw_input("> "))
    #     for i in range(0, number_of_enemies):
    #       monsters.append(baddies)
