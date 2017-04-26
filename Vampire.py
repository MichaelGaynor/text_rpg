class Vampire(object):
  def __init__(self):
    self.health = 12
    self.power = 5
    self.name = "foul Vampire"
    self.xp_value = 10

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
      print(":syyyyyysssyyso+:-..-++/--:.---.``.:oyhhhso+/++o/ ")
      print("ys+:.```..-:/osyhy:.` ```ss`   ```/hhs/-`       ..")
      print(":              `-osoos/:`+o.`-/++/++-     `.-:--.`")
      print("   `.-..````` ` `//+++/-` `  `.-://+/```..--:/::-.")
      print("`...--:-.......```.-::-`        `````.:::-::--...`")

  def take_damage(self, damage):
    self.health -= damage
  def is_alive(self):
    return self.health > 0