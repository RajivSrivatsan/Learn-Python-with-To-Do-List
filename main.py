todos = []

while True:
    user_action = input("Enter add, show, edit or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'edit':
            number = int(input("Number of to-do item to edit: "))
            number -= 1
            new_todo = input("Enter new to-do: ")
            todos[number] = new_todo
        case 'exit':
            break
        case _:
            print("hey you entered an unknown command")

print("Bye!")
