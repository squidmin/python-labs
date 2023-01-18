class Console:
  def __init__(self, variant):
    self.__variant = variant

  def show_variant(self):
    print('I am a', self.__variant)

  def make_sound(self):
    print('hodl!')


class PSVita(Console):
  def __init__(self):
    Console.__init__(self, 'PS Vita')

  def make_sound(self):
    print('I can run PS1 classic titles')


class GBA(Console):
  def __init__(self):
    Console.__init__(self, 'GBA')

  def make_sound(self):
    print('I\'m backwards compatible with original GB titles')