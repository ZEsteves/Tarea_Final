
def add_task_to_list(task: str, todo_list: list, position: int=None):
    n=len(todo_list) #largo de la lista
    if position == None:
        todo_list.append(task)
    elif position >= 1 and position <= n+1:
        todo_list.insert(position-1, task) 
    else:
        raise IndexError(str(position) + " is an invalid position for to do list of size " + str(n))

def remove_task_from_list(position: int, todo_list: list):
    n=len(todo_list)
    if position >= 1 and position <= n:
        todo_list.pop(position-1)
    else:
        raise IndexError(str(position) + " is an invalid position for to do list of size " + str(n))
    
def move_task(position1: int, position2: int, todo_list: list):
    n=len(todo_list)
    if position1 >= 1 and position1 <= n:
        if position2 >= 1 and position2 <= n:
            temp = todo_list.pop(position1-1)
            todo_list.insert(position2-1,temp)
        else:
             raise IndexError(str(position1) + " is an invalid position 2 for to do list of size " + str(n))
    else:
        raise IndexError(str(position1) + " is an invalid position 1 for to do list of size " + str(n))

def move_task_to_other_list(position1: int, todo_list1: list, todo_list2: list, position2: int=None):
    n=len(todo_list1)
    m=len(todo_list2)
    if position1 >= 1 and position1 <= n:
        if position2==None:
            temp = todo_list1.pop(position1-1)
            todo_list2.append(temp)
        elif position2 >= 1 and position2 <= m:
            temp = todo_list1.pop(position1-1)
            todo_list2.insert(position2-1,temp)
        
def get_task(position: int, todo_list: list):
    return todo_list[position-1]

def show_list(todo_list: list):
    """Prints the content of the todo list in this format:
    _____________________
    | 1. Item1          |
    | 2. Item2          |
    | 3. Item3          |
    | 4. Item4          |
    | ...               |
    _____________________
    Parameters:
    todo_list: List with tasks
    """
    print("_"*34)
    for pos, task in enumerate(todo_list, start=1):
        task = str(pos) + ". " + task
        if len(task) > 30:
            task_str1 = task[:29]
            task_str2 = task[29:]
            while len(task_str2) > 30:
                print(f"| {task_str1}- |")
                task_str1 = task_str2[:29]
                task_str2 = task_str2[29:]
            print(f"| {task_str1}- |")
            wspace = " "*(30 - len(task_str2))
            print(f"| {task_str2}{wspace} |")
        else:
            wspace = " "*(30 - len(task))
            print(f"| {task}{wspace} |")
    print("_"*34)
