'''
Write a Python program to count the frequency of words appearing in a string

eg. Jhansi loves eating apple and mango and her sister loves apple
'''


def freq_words():
    str = input('Enter a string: ')
    s = str.split()
    d = {}

    for i in s:
        if i not in d.keys():
            d[i] = 0
        d[i] = d[i] + 1
    print(d)


if __name__ == '__main__':
    freq_words()