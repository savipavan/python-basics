# filename: mobiledata.py
filename = "mobiledata.txt"


# reading phonebook data
def readBook(book):
    import os
    if os.path.exists(filename):
        store = open(filename, 'r')
        for line in store:
            name = line.split()[0]
            mobile = line.split()[1]
            book[name] = mobile
        store.close()


# storing item to phonebook
def saveBook(book):
    store = open(filename, 'w')
    for name, mobile in book.items():
        store.write(name + ' ')
        store.write(mobile + '\n')
    store.close()

# taking user input
def addEntry(book):
    name = input('Enter a name: ')
    mobile = input('Enter a mobile: ')
    book[name]=mobile

#remove entry from phonebook
def removeEntry(book):
    name = input('Enter a name : ')
    del(book[name])

#search for an entry
def findEntry(book):
    name = input('Enter a name : ')
    if name in book:
        print(name, book[name])
    else:
        print('Sorry! no entry for : ', name)

# Display all items from phonebook
def displayAll(book):
    import os
    if os.path.exists(filename):
        store=open(filename,'r')
        for line in store:
            name=line.split()[0]
            mobile=line.split()[1]
            print('Name = ',name, ' and Mobile No = ', mobile)
        store.close()

# Memu for the user
def getChoice(menu):
    print(menu)
    choice = int(input('Enter your choice(1-5)'))
    return choice

# The main function
def main():
    themenu = '''
    1. Add Entry
    2. Remove Entry
    3. Find Entry
    4. Display All
    5. Quit
    '''

    phonebook = {} #Dictionary to store name and number
    readBook(phonebook)
    choice=getChoice(themenu)
    while choice < 5:
        if choice==1:
            addEntry(phonebook)
        elif choice==2:
            removeEntry(phonebook)
        elif choice==3:
            findEntry(phonebook)
        elif choice==4:
            saveBook(phonebook)
            displayAll(phonebook)
        choice=int(input('Enter your choice (1-5): '))
    saveBook(phonebook)

if __name__ == '__main__':
    main()
