import consoles


def main():
  ps_vita = consoles.PSVita()
  gba = consoles.GBA()

  display_data(ps_vita)
  print()
  display_data(gba)
  print()
  display_data('stringvalue')
  print()


def display_data(variant):
  if isinstance(variant, consoles.Portable):
    variant.show_variant()
    variant.make_sound()
  else:
    print('That\'s not a portable console.')


main()