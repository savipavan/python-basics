# filter method
alphabets = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'}
vowels = ['a', 'e', 'i', 'o', 'u']

filteredVowels = filter(lambda alpha: alpha in vowels, alphabets)
print('The filtered vowels are: ')
for vowel in filteredVowels:
    print(vowel)
