import consoles


def main():
  ps_vita = consoles.PSVita()
  gba = consoles.GBA()

  ps_vita.make_sound()
  ps_vita.show_variant()

  gba.make_sound()
  gba.show_variant()


main()