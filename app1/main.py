user_prompt = "Type add/show/edit/finish/exit > "

todos = []

while True:
    for index, item in enumerate(todos):
        print(f"{index + 1}. {item}")
    user_action = input(user_prompt).strip().lower()
    match user_action:
        case 'add':
            todo = str(input('Enter a todo > '))
            todos.append(todo.capitalize().title())
        case 'show' | 'display':
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
