import vehicles


def main():
  car = vehicles.Car('basic', 2007, 12500, 21500.00, 4)
  truck = vehicles.Truck('python', 2002, 40000, 12000.0, '4WD')
  suv = vehicles.SUV('classinheritance', 2000, 30000, 18500.0, 5)

  print('INVENTORY')
  print('=========')

  print('Make: ', car.get_make())
  print('Model: ', car.get_model())
  print('Mileage: ', car.get_mileage())
  print('Price: ', car.get_price())
  print('Number of doors: ', car.get_doors())
  print()

  print('Make: ', truck.get_make())
  print('Model: ', truck.get_model())
  print('Mileage: ', truck.get_mileage())
  print('Price: ', truck.get_price())
  print('Drive type: ', truck.get_drive_type())
  print()

  print('Make: ', suv.get_make())
  print('Model: ', suv.get_model())
  print('Mileage: ', suv.get_mileage())
  print('Price: ', suv.get_price())
  print('Passenger capacity: ', suv.get_pass_cap())
  print()


main()