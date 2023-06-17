
array1 = [24, 36, 48, 60]
array2 = [12, 18, 24, 36, 72]


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def gcd_array(array):
    result = array[0]
    for i in range(1, len(array)):
        result = gcd(result, array[i])
    return result


def gcd_of_arrays(array1, array2):
    gcd1 = gcd_array(array1)
    gcd2 = gcd_array(array2)
    return gcd(gcd1, gcd2)


result = gcd_of_arrays(array1, array2)