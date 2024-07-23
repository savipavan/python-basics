### Filter
def is_it_even(num):
    return num % 2 == 0
print(is_it_even(4))

print(list(filter(is_it_even, range(1,11))))

# Similar to:
print(list(filter(lambda x: x % 2 == 0, range(1, 11))))
even_nums = [x for x in range[1,11] if x % 2 == 0]
print(even_nums)