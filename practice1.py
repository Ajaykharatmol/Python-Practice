import random
list = []
for i in range(5):
    list.append(random.random())
print(list)

dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
double_val = {k:v*2 for (k,v) in dict.items()}
print(double_val)

def is_arithmetic(n):
    delta = n[1] - n[0]
    for i in range(len(n) - 1):
        if not (n[i + 1] - n[i] == delta):
             return False
    return True

print(is_arithmetic([5, 7, 9, 11]))
print(is_arithmetic([5, 8, 9, 11]))