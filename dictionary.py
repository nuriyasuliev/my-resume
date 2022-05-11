car = {
    'brand': 'Honda',
    'year': 2020,
    'color': 'white',
    'available': True 
    }
for key in car.keys():
    print(key)

for values in car.values():
    print(values)    
for key, values in car.items():
    print(f'{key} of the car is {values}')
