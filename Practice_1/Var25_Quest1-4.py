import math

def first(x, y, z):
    first = 47 * (math.pow((math.sin(z) - math.sin(z)), 6))
    second = 31 * math.pow(y, 8)
    third_chisl = math.fabs(78 * math.pow(x, 3)) - math.sin(z)
    third_znam = math.pow(x, 8) + math.cos(y) - 27
    third = math.fmod(third_chisl, third_znam)
    fourth_chisl = math.pow(x, 4) - math.fmod(math.pow(x, 7), 18)
    fourth_znam = 89 * math.pow(x, 4) - 29 * math.pow(x, 8)
    fourth = math.fmod(fourth_chisl, fourth_znam)
    res = first + second - third + fourth
    return ('%.2e' % res)


print(first(-51, -22, 61))
print(first(41, 98, -64))


def second(x):
    if (x <= 6):
        res_1 = math.sin(x) - math.sin(x) - 31 * math.pow(x, 2)
        return ('%.2e' % res_1)
    elif ((-6 <= x) and (x < 67)):
        res_2 = math.fabs(math.pow(x, 5) + math.cos(x) - 38) - 95 * math.pow(x, 7)
        return ('%.2e' % res_2)
    elif ((67 <= x) and (x < 92)):
        res_3 = math.sin((math.pow(x, 2) - 5 * math.pow(x, 5))) + math.pow(x, 5)
        return ('%.2e' % res_3)
    elif ((92 <= x) and (x < 147)):
        res_4 = 99 * x - 19 * pow(x, 7)
        return ('%.2e' % res_4)
    elif (147 <= x):
        res_5 = 17 * math.pow((math.fmod(x ** 3, 52) - x ** 8), 2) + x ** 7
        return ('%.2e' % res_5)


print(second(68))
print(second(216))

def third(n, m):
    pervoe = 0
    vtoroe = 0
    for i in range (n):
        for j in range (m):
            pervoe += 47*math.pow((j+1), 6) + 5*math.pow((i+1), 8)
            vtoroe += 67*math.pow((i+1), 2) + math.fmod(((j+1)**4), 27) - 13

    result = pervoe - vtoroe
    return ('%.2e' % result)

print(third(26,83))
print(third(84,17))

def chetire(num):
    if (num==0):
        return 6
    elif (num==1):
        return 5
    else:
        return (1/16*chetire(num-1)-1/20*chetire(num-2)**3)

print('%.2e' % chetire(13))
print('%.2e' % chetire(7))