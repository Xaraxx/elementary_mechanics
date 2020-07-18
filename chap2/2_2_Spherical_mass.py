# This script calculate the mass from 
# a body with spherical shape.

import math

def spherical_mass(radius):
    rho = 7860 # is this the steel density in kg/m**3
    porportion = 4/3
    mass = math.pi*porportion*rho*(radius)**3
    print('the mass in kilograms is {} and the radius {} in meter'.format(mass, radius))
    return mass

def converter_to_meter_units(unit, number):
    
    if unit == 'M':
        milimeter_to_meter = (number)/ 1000
        spherical_mass(milimeter_to_meter)
        return milimeter_to_meter
    elif unit == 'C':
        centimeter_to_meter = (number)/ 100
        spherical_mass(centimeter_to_meter)
        return centimeter_to_meter
    elif unit == 'I':
        inches_to_meter = (number)/ 39.3701
        spherical_mass(inches_to_meter)
        return inches_to_meter
    else:
        foots_to_meter = (number)/ 3.28084
        spherical_mass(foots_to_meter)
        return foots_to_meter


def _print_welcome():
    message = 'Select from this list your current unit:'
    print(message)
    print('m[E]ters')
    print('[M]ilimeters')
    print('[C]entimeters')
    print('[I]nches')
    print('[F]oots')

def __command():
    command = input()
    command = command.upper()

    if command == 'M':
        number = int(input('Please write how many milimeters? '))
        converter_to_meter_units(command, number)
        return command, number
    elif command == 'E':
        number = int(input('Please write how many milimeters? '))
        spherical_mass(number)
        return command, number
    elif command == 'C':
        number = int(input('Please write how many centimeters? '))
        converter_to_meter_units(command, number)
        return command, number
    elif command == 'I':
        number = int(input('Please write how many inches? '))
        converter_to_meter_units(command, number)
        return command, number
    elif command == 'F':
        number = int(input('Please write the how many foots? '))
        converter_to_meter_units(command, number)
        return command, number    
    else:
        print('Invalid command')

if __name__ == "__main__":
    
    _print_welcome()
    __command()
    
    