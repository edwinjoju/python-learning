print("TODO LIST")

print("Enter a command. Type 'h' for help:")
todo = []
task = None
count=0

while(task!="q"):
    n=1
    task = input(">")

    if(task=='h'):
        print("TODO LIST help")
        print("Type 'q' to quit")
        print("To add task, type it and hit enter")
        print("TO complete todo enter its number")
    elif task =='q':
        print(f'You have {count} tasks...')
        for x in todo:
            print(f'{n}. {x}')
            n+=1
    else:
        todo.append(task)
        count+=1
        for x in todo:
            print(f'{n}. {x}')
            n+=1

