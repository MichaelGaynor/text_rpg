class Witch(object):
  def __init__(self):
    self.health = 20
    self.power = 60
    self.name = "unholy Witch"
    self.xp_value = 150

  def print_image(self):
    print("MMMMMMMMMMMMmoyy++sysyydmNNmdmNNNmmddhhhhyyyo++++/")
    print("MMMMMMMMMMMdy:-`.``````` `.`.:+hmmmdddhhhhyooo++//")
    print("MMMMMMMMMMy`````.`....```````  `-dmmdddhhsooo+++//")
    print("MMMMMMMMMs````-+sydmdhddhys+/.`` /dddddhsoso+++++/")
    print("MMMMMMMM+ ``-yNMMMMMMMNNNNmhyo:.` -hdhssysoo++++//")
    print("MMMMMMMd``./mMMMMMMMMNNNmmdysoo+-` `oyyysooo+++///")
    print("MMMMMMMs..:NNMMMMMMMNNNmmdhsso++/.  .sysssso++////")
    print("MMMMMMM/--yNNNMMMMMMdyNNmmdhyoo/:-`  :syssoo+++///")
    print("MMMMMMh--.do-.:+ymNd:-shy+-`   ``.   `+soo+++++///")
    print("MMMMMM+-``....``  ````           `    .+oooo+++///")
    print("MMMMMN:. `` Y O U R ``:. E N D     `   .:///++////")
    print("MMMMMN-. `-:-.`../+-+-  ...``          .-/++/:////")
    print("MMMMMh.. `:/++ydNd:+o+:`.ss+:.`        `:./+++/://")
    print("MMNMMs-.`./syMMMNdmNNmy/.:mmdy:.`       ---/+++///")
    print("MMMMmo-``/smNMMMMNsos:` `.sdhs/.``      --/:/+///:")
    print("MMMMd+.` `/mmNNNMMMMNmhsssys+:.``    `-..///:////:")
    print("MMMMm-.` `.d A P P R O A C H E S````  .---/+/:///:")
    print("MMMNm-` ``.+mmmdhyshoos+:.`.````     `----//-/::/:")
    print("NNNmd-` ` ` /hhhhhyo/-:-..`````      `-...-:::://:")
    print("NNNmh/:  `   .sshdmmNmdhs:.`        `.-. ``-/::///")
    print("mmmys//  .`` `ys::+oso+/.`          .``.`  .//:///")
    print("mmdsoo/ ``..` /dsh+.``              `````.:///////")
    print("dds///:  `./. `ssmdhs/.          ```::``::::/+////")
    print("+:++/--`  `//  ./hddhys/-` .--:::..:o-`o+-:-`///::")
    print("mdo..--.```.:.  `+hyyso++/.  `-:-.-:o.-oo/--::::--")
    print("dho` .-.    `    .oyooooso..://++:-::/:///-://:---")
    print("s/.   ``         ./ysosyho/:/oss:..-/o:+//:-----..")
    print("-`               //osooyhy++-`` `::-so:+s//-.`````")
    print("``               -//ossyyoy/```-/+.o//../---`     ")
    print(".                `/:oyyyss+.--o+/-.o:-` ` ` ````  ")
    print("``               `:/syyyso:` `::--`.-/      ````  ")
    print(" `                -+oyyys+. --..-`  :/    ` ````  ")
    print("                  :/+ssss: ``````   `        `    ")
    print(" `                -s//+o+.  ``                    ")
    print("       `          -++-++/`  `:``                  ")
    print("                  .//:/+:  `//-`                  ")
    print("                  `:/-:/-` -+//.                  ")
    
  def take_damage(self, damage):
    self.health -= damage
  def is_alive(self):
    return self.health > 0