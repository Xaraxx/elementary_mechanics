import math

def unit_vector(theta):    
    x = math.cos(theta)
    y = math.sin(theta)

    print('x = {} y = {}'.format(x, y))

    return([x, y])



def degrees_to_radians(angle_in_degrees):
    angle_in_radians = angle_in_degrees*(math.pi/180)
    print(angle_in_radians)
    return angle_in_radians


def _print_wellcome():
    message = 'Select the angle unit that you would prefer: '
    print(message)
    print('[R]adians')
    print('[D]egrees')



def __command():
    command = input()
    command = command.upper()
    
    if command == 'R':
        angle_in_radians = int(input('Write the angle magnitude: '))
        unit_vector(angle_in_radians)
    elif command == 'D':
        angle_in_degrees = int(input('Write the angle magnitude: '))

# Note; it is absolutely necesary to convert the angle from degrees to radians because 
# the trigonometical functions in python only recive angles in radians! never introduce 
# angles in degrees in this functions

        angle_in_radians = degrees_to_radians(angle_in_degrees)
        u_vector = unit_vector(angle_in_radians)
        x_in_degrees = math.degrees(u_vector[0])
        y_in_degrees = math.degrees(u_vector[1])
        print('x = {} y = {}'.format(x_in_degrees, y_in_degrees)) 





if __name__ == "__main__":
    _print_wellcome()
    __command()

    # theta = [0 , (math.pi/6), (math.pi/3), (math.pi/2), ((3*math.pi)/2)]
    # for i in theta:
    #     unit_vector(i)



    
