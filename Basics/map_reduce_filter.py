from functools import reduce
# map and filtered can be used without importing

my_list = [1,2,3,4,5,6]
new_list = list(map(lambda x: x ** 2, my_list))
print(new_list)
filtered = list(filter(lambda x: x <= 20, new_list))
print(filtered)
reduced = reduce(lambda x, y: x + y, filtered)
print(reduced)