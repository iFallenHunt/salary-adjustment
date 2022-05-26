job = int(input('Type the title: '))
salary = float(input('Type salary: '))
readjustment = float
increase = float

if job == 1:
  print('General Services')
  increase = salary * (50/100)
  readjustment = salary + increase
  print('The raise is: ', increase)
  print('The new salary is: ', readjustment)
else:
  if job == 2:
    print('Watchman')
    increase = salary * (30/100)
    readjustment = salary + increase
    print('The raise is: ', increase)
    print('The new salary is: ', readjustment)
  else:
    if job == 3:
      print('Receptionist')
      increase = salary * (25/100)
      readjustment = salary + increase
      print('The raise is: ', increase)
      print('The new salary is: ', readjustment)
    else:
      if job == 4:
        print('salesperson')
        increase = salary * (15/100)
        readjustment = salary + increase
        print('The raise is: ', increase)
        print('The new salary is: ', readjustment)
