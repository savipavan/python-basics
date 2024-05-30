todos = []

while True:
    user_action = input("type add, show, edit or exit: ")
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
        case 'edit':
            number = int(input("enter the number to edit "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'exit':
            break
        case otherInput:
            print("You have chosen wrong input", ",try again")

print('bye!')