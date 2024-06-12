todos = []
awaiting_input = True
while awaiting_input:
    todo = str(input("Enter a todo or press q to quit: "))
    if todo == 'q':
        awaiting_input = False
        continue
    else:
        todos.append(todo.capitalize())
        continue
print(todos)
