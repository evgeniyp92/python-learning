user_prompt = "Type add/show/edit/finish/exit > "

while True:
    # for index, item in enumerate(todos):
    #     print(f"{index + 1}. {item}")
    user_action = input(user_prompt).strip().lower()
    match user_action:
        case 'add':
            # Get input from user
            todo = input('Enter a todo > ') + "\n"
            # Open the file and read lines, copy the todos into state, and close the file again
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            # Append the new todo
            todos.append(todo.capitalize().title())
            # Open the file again in write mode and write lines again
            # basic modes: w-write (blowaway), r-read
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show' | 'display':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            print(todos)
            for i in range(len(todos)):
                print(f'{i+1}. {todos[i]}')
        case 'edit':
            index = int(input('Enter the number of the todo to edit > '))
            new_todo = str(input('Enter the edited todo > '))
            todos[index - 1] = new_todo.capitalize().title()
        case 'finish':
            index = int(input('Enter the number of the todo to finish > ')) - 1
            todos.pop(index)
        case 'exit':
            break
        # default case handling
        case _:
            print('You entered an invalid input')
            continue
