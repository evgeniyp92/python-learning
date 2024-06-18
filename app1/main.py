user_prompt = "Type add/show/edit/finish/exit > "

while True:
    # for index, item in enumerate(todos):
    #     print(f"{index + 1}. {item}")
    user_action = input(user_prompt).strip().lower()
    match user_action:
        case 'add':
            # Get input from user
            todo = input('Enter a todo > ') + "\n"

            # Using context manager, no need to close files
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # Append the new todo
            todos.append(todo.capitalize().title())

            # Open the file again in write mode and write lines again
            # basic modes: w-write (blowaway), r-read
            # refactored with context manager
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show' | 'display':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # Cleaning up a list via a for loop
            new_todos = []
            for item in todos:
                new_todos.append(item.strip('\n'))

            # Cleaning up using list comprehension
            new_todos2 = [item.strip('\n') for item in todos]

            # for i in range(len(new_todos)):
            #     print(f'{i+1}. {new_todos[i]}')

            for index, item in enumerate(new_todos):
                print(f'{index+1}. {item}')

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
