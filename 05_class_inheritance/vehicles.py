# The Automobile class holds general data about an automobile in inventory.

class Automobile:
  # The __init__ method accepts arguments for the make, model, mileage, and price.
  #   It initializes the data attributes with these values.

  def __init__(self, make, model, mileage, price):
    self.__make = make
    self.__model = model
    self.__mileage = mileage
    self.__price = price

  def set_make(self, make):
    self.__make = make

  def set_model(self, model):
    self.__model = model

  def set_mileage(self, mileage):
    self.__mileage = mileage

  def set_price(self, price):
    self.__price = price

  def get_make(self):
    return self.__make

  def get_model(self):
    return self.__model

  def get_mileage(self):
    return self.__mileage

  def get_price(self):
    return self.__price


class Car(Automobile):
  def __init__(self, make, model, mileage, price, doors):
    Automobile.__init__(self, make, model, mileage, price)
    self.__doors = doors

  def set_doors(self, doors):
    self.__doors = doors

  def get_doors(self):
    return self.__doors
    