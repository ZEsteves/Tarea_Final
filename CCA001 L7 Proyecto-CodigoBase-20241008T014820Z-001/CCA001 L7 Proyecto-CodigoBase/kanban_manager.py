# Este import esta para el metodo show_kanban()
# Pueden dejarlo o eliminarlo dependiendo como quieran organizar sus imports
from todo_list_manager import show_list
kanban = {
    "backlog":[],
    "doing":[],
    "review":[],
    "done":[]
}


def move_task_up(current_position: int, list_name: str, new_position: int=None):
    n=len(kanban[list_name])
    if list_name=="backlog":
        if current_position >= 1 and current_position <= n:
            temp= kanban[list_name].pop(current_position)
            m= len(kanban["doing"])
        
            if new_position==None:
                kanban["doing"].append(temp)
            elif new_position >= 1 and new_position <= m:
                kanban["doing"].insert(new_position-1,temp)
            else:
                raise IndexError(str(new_position) + " is an invalid position for kanban doing list of size " + str(m))

        else:
            raise IndexError(str(current_position) + " is an invalid position for kanban " + list_name + " list of size " + str(n))
    
    elif list_name=="doing":
        if current_position >= 1 and current_position <= n:
            temp= kanban[list_name].pop(current_position)
            m= len(kanban["review"])

            if new_position==None:
                kanban["review"].append(temp)
            elif new_position >=1 and new_position <= m:
                kanban["review"].insert(new_position-1, temp)
            else: 
                raise IndexError(str(new_position) + " is an invalid position for kanban review list of size " + str(m))
        else:
            raise IndexError(str(current_position) + " is an invalid position for kanban " + list_name + " list of size " + str(n))

    elif list_name=="review":
        if current_position >=1 and current_position <= n:
            temp= kanban[list_name].pop(current_position)
            m= len(kanban["done"])

            if new_position==None:
                kanban["done"].append(temp)
            elif new_position >=1 and new_position <= m:
                kanban["done"].insert(new_position-1, temp)
            else: 
                raise IndexError(str(new_position) + " is an invalid position for kanban done list of size " + str(m))
        else:
            raise IndexError(str(current_position) + " is an invalid position for kanban " + list_name + " list of size " + str(n))
    
    elif list_name=="done":
        pass
    else:
        raise KeyError(list_name) + "is an invalid name for kanban"
    
def move_task_down(current_position: int, list_name: str, new_position: int=None):
    n=len(kanban[list_name])
    if list_name=="backlog":
       pass
    elif list_name=="doing":
        if current_position >= 1 and current_position <= n:
            temp= kanban[list_name].pop(current_position)
            m= len(kanban["backlog"])

            if new_position==None:
                kanban["backlog"].append(temp)
            elif new_position >=1 and new_position <= m:
                kanban["backlog"].insert(new_position-1, temp)
            else: 
                raise IndexError(str(new_position) + " is an invalid position for kanban backlog list of size " + str(m))
        else:
            raise IndexError(str(current_position) + " is an invalid position for kanban " + list_name + " list of size " + str(n))

    elif list_name=="review":
        if current_position >=1 and current_position <= n:
            temp= kanban[list_name].pop(current_position)
            m= len(kanban["doing"])

            if new_position==None:
                kanban["doing"].append(temp)
            elif new_position >=1 and new_position <= m:
                kanban["doing"].insert(new_position-1, temp)
            else: 
                raise IndexError(str(new_position) + " is an invalid position for kanban doing list of size " + str(m))
        else:
            raise IndexError(str(current_position) + " is an invalid position for kanban " + list_name + " list of size " + str(n))
    
    elif list_name=="done":
        if current_position >= 1 and current_position <= n:
            temp= kanban[list_name].pop(current_position)
            m= len(kanban["review"])
        
            if new_position==None:
                kanban["review"].append(temp)
            elif new_position >= 1 and new_position <= m:
                kanban["review"].insert(new_position-1,temp)
            else:
                raise IndexError(str(new_position) + " is an invalid position for kanban review list of size " + str(m))

        else:
            raise IndexError(str(current_position) + " is an invalid position for kanban " + list_name + " list of size " + str(n))
    
    else:
        raise KeyError(list_name) + "is an invalid name for kanban"

def change_task_priority(current_position: int, new_position: int, list_name: str):
    pass

def add_new_task(task: str):
     kanban["backlog"].append(task)

def remove_task(position: int, list_name: str):
    pass
def get_kanban():
    pass
def show_kanban():
    print("Backlog")
    show_list(kanban["backlog"])
    print("\nDoing")
    show_list(kanban["doing"])
    print("\nReview")
    show_list(kanban["review"])
    print("\nDone")
    show_list(kanban["done"])
    