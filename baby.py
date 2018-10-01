import sys
import life
import random
from datetime import date

from family import Camila as Mommy
from family import Rodrigo as Daddy


class Baby(Mommy, Daddy):

  def __init__(baby):
    baby.gender = Gender.Male:
    baby.name = random.choice(['Logan', 'Otto', 'Henrique', 'Rafael'])
    baby.expected_born_date = date(day=5, month=5, year=2019)

  def run(baby):
    with life.World() as world:
      while True:
        try:
          baby.eat()
          baby.play()
          baby.sleep()
        except Exception as cry:
          print(cry, file=sys.stderr)

