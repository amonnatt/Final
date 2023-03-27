import math
def chack_car (number):
    van=0
    car=0
    sum=0
    num_vans=0
    num_car=0
    while number>0:
        if number >= 11 :
            van=+1
            num_vans=math.ceil(number/11)
        else: 
            car=+1
            sum = number - num_vans*11
            num_car = math.ceil(sum/4)
        number=sum
        return ("van: %d"%van)+" "+("car: %d"%car)
    return "No Passenger"


def validate_number(number):
    if type(number) != int:
        if type(number) == str:
            return "input integer"
        elif number >= 0:
            return "input integer"
        else:
            return "out of range"
    elif number >= 1:
        return number
    else:
        return "out of range"