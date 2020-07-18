# Seconds
# This script convert numbers in hours 
# to seconds, in other words, change time
# units

convertion = 3600

def time_in_seconds(number):
    time_in_seconds = number*convertion
    print('{} hours equals to {} seconds'.format(number, time_in_seconds))
    return time_in_seconds 

if __name__ == "__main__":
    number = 12
    time_in_seconds(number)
