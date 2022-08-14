a = [1, 2, 3]

b = list(a)

c = a[::]

print(id(a))
print(id(b))
print(id(c))

print(a)
print(b)
print(c)

my_list = list(range(100))

print(my_list)

double = [i*2 for i in my_list]
pairs = [i for i in my_list if i % 2 == 0]

print(pairs)