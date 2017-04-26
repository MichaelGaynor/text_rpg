class Monster(object):
  def __init__(self, name, health, power, xp_value):
    self.name = name
    self.health = health
    self.power = power
    self.xp_value = xp_value

  def take_damage(self, damage):
    self.health -= damage
  def is_alive(self):
    return self.health > 0


class Goblin(Monster):
  def __init__(self):
    super(Goblin, self).__init__("wretched Goblin", 6, 2, 5)
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


class Vampire(Monster):
  def __init__(self):
    super(Vampire, self).__init__("foul Vampire", 12, 5, 10)
  def print_image(self):
      print("                                                  ")
      print("           ``    `..-:+++///-..``                 ")
      print("          ` ``.-/+oossshmdsssso/:..``             ")
      print("          ````.-:+oyyyhdNNysosoo+/-.`             ")
      print("            .:+ssysoossymdo+//osyhs/.`            ")
      print("          .oddhyhdNms+shmhs+ohmNdhyys:`           ")
      print("         `/syhysyydds/:/oo/oyyyyooooo++`          ")
      print("         ./+/--..-::/-`./..::.....-:/o/-          ")
      print("         :/-`          -y-          ``.-`         ")
      print("         ...   Y O U   +mo   A R E   .```         ")
      print("         `./          `odo`         .:.`          ")
      print("          `:`    ..---.+ho-```.    `:-.`          ")
      print("           :hmddNho+:-.ydy:.-/sdysosyy-           ")
      print("          :+//oso:-`.-/yNd+.`-/osoo:-.--          ")
      print("         `..:ss+::+/-:+hNd/..-::/-:++//`          ")
      print("           ```:.``.-...:/:``.+y+::--..``          ")
      print("             `.```-/::-:/:---++:.````             ")
      print("              .``-/+osddddhs+/+o/` `.             ")
      print("               `..::::+ooo++/:--:.``              ")
      print("              `-:-:++/+oyyooo///:..               ")
      print("             `:/:.    `...``  `-/+/`              ")
      print("             ``    `.`../-::.`   `..              ")
      print("                 `.`.       .--`                  ")
      print("               ````           ``                  ")
      print("                    F O O D                       ")
      print("                                                  ")
      print("                  .``````...``                    ")
      print("                  ..`  `.--`.--                   ")
      print("                   .------:--.+:                  ")
      print("                     `.://.   .:`                 ")
      print("                      `  --   `-                  ")
      print("                `` `.----`.:/:-`                  ")
      print("               .:. `-+yNmh:` -`                   ")
      print("              .--.``.:hNNNs` -/:`                 ")
      print("               ``...--:dNh:``.:-.                 ")
      print("         `..`      `--.`-:`.``.-`` ``-:-`         ")
      print("      `.---..`    -+/-`` `..../sy+ `..//:.`       ")
      print("  `-:/+///:..`` `-:yhhs:` `.:/+o/.  .--:+oooo+-`  ")


class Witch(Monster):
  def __init__(self):
    super(Witch, self).__init__("unholy Witch", 20, 60, 150)
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




class Black_phillip(Monster):
  def __init__(self):
    super(Black_phillip, self).__init__("Black Phillip, King of All", 666, 666, 666)
  def print_image(self):
    print("`.....--:::://+ooossssoooooooooosssssssssyysssssss")
    print("...----:::://+ossssssssssssooossssssssssyyyyyyyyyy")
    print("-----::::///+oosssyyyyyyo/:-.``.-/oyyyyyyyyhhhhhhy")
    print("---::://///+oossyyyyyyyyyyyyyyo/.  .ohhyyyyyhhhhhh")
    print("::::////+++oossyyhhhhyhyyyhhhyyyyo. `:shhyhhhhhhhy")
    print("::://++++oosssyyhhhhhhhhhhhhhyhhhyy/  `odhhhhhhhhy")
    print(":://+++ooossyyhhhhhhhhhhhhhhhhhhhhhh:  `ymddho/-+y")
    print("////++ooossyyyhhhhhhhhhhhhhhhhhhhhhhy   .dmmmmo `s")
    print("///++ooosssyyhhhhhhhhhhhhho::/+osyhhs    :hdh-  .y")
    print("+o+oooossssyyhhhhhhhddddddho.    `-:`  ``-/+-` -yy")
    print("oooooossssyyhhhhhdddddddddddho:-.    .``...-.--hhy")
    print("ooooosssssyyhhhhhdddddddddddhhhs-         `.:.://o")
    print("ooossssssyyhhhhhdhhhddddddhhys:.          `:++..os")
    print("ooosssssyyyhhhhhhhhhhhhhhhs/-``        `` `./+//ys")
    print("oosssyyyyyhhhhhhhhhhhhyys/.`              ``.:+sss")
    print("osssyyyyyyhhhhhhhhhhyyo:`                  `-:+oss")
    print("ssssyyyyyhhhhhhhhhhys/.                    `  ``:o")
    print("oossyyyyyhhhhhhhhyyo-                           `+")
    print("ooossyyyyhhhhhhyyo:`                           `:+")
    print("ooossyyyhhhhyys/-`                   `         /o+")
    print("ooosyyyyyhhho+-`                              .oo+")
    print("osssyyyyyyy+-`                               .+o++")
    print("sssyyyyyys:`   ```                       `` `/oo++")
    print("syyyyyyys-   ````` ```                    `-+ooo++")
    print("yyyyyyys:```  ````                         -ssoo++")
    print("yyyyyys+`    `````                          /oo++/")
    print("yyyssss:     `                           `` `++++/")
    print("yyyyss+`                                 `` `/+///")
    print("ssyyyo.                                ````  :++//")
    print("ssyss-                                  ...` :///:")
    print("ssss+``                                 `.-` :/:::")
    print("ssoo.`                                  ``.` -:::-")
    print("ooo+`        ```       `                  `` -:::-")
    print("oo/.        -+:-`    ```                 ``  `:::-")
    print("o/`  ``    -oss+:. ` `.`                 `   `---.")

                                                  