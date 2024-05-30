todos = []

while True:
    user_action = input("type add or show or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            # print(todos)
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case otherInput:
            print("You have chosen wrong input", ",try again")

print('bye!')