def is_multiple_of(number, factor):
    return (number % factor == 0)

def sum_multiples(target, factor1, factor2, even_flag):
    s = 0
    for i in range(target):
        if is_multiple_of(i, factor1) or is_multiple_of(i, factor2):
            if not even_flag or (even_flag and i %2 == 0):
                s+=i
                
    return s

print(sum_multiples(100000, 3, 5, False)) # 2333316668
print(sum_multiples(100000, 4, 7, False)) # 1785635717
print(sum_multiples(100000, 4, 7, True)) # 1428478574

