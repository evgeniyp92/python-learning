user_prompt = "Type add/show/exit: "

todos = []

while True:
    user_action = input(user_prompt).strip().lower()
    match user_action:
        case 'add':
            todo = str(input('Enter a todo: '))
            todos.append(todo.capitalize())
        case 'show':
            for i in range(len(todos)):
                print(f'{i+1}. {todos[i]}')
        case 'exit':
            break