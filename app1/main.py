user_prompt = "Type add/show/edit/finish/exit > "

while True:
    # for index, item in enumerate(todos):
    #     print(f"{index + 1}. {item}")
    user_action = input(user_prompt).strip().lower()
    if 'add' in user_action:
        # Get input from user
        # todo = input('Enter a todo > ') + "\n"
        todo = user_action[4:] + "\n"

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

    elif 'show' in user_action:
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
            print(f'{index + 1}. {item}')

    elif 'edit' in user_action:
        index = int(user_action[5:])

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = str(input('Enter the edited todo > '))
        todos[index - 1] = new_todo.capitalize().title() + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'finish' in user_action:
        index = int(user_action[7:]) - 1

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        print('Todo finished successfully')

    elif 'exit' in user_action:
        break

    # default case handling
    else:
        print('You entered an invalid input')
        continue
