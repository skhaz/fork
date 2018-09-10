import sys
import life

from family import Camila as Mommy
from family import Rodrigo as Daddy


class Baby(Mommy, Daddy):

  def __init__(baby):
    baby.name = '???'
    
  def run(baby):
    with life.World() as world:
      while True:
        try:
          baby.eat()
          baby.play()
          baby.sleep()
        except Exception as cry:
          print(cry, file=sys.stderr)

