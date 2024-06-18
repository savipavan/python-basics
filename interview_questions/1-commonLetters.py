'''
Write a Python program to find out common letters between two strings
'''


def common_letters():
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    s1 = set(str1)
    s2 = set(str2)
    result = s1 & s2
    print(result)


if __name__ == '__main__':
    common_letters()
