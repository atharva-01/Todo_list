import PySimpleGUI as sg 

sg.theme('Dark Blue')
priority = list()
def read_file():
    tasks = []
    with open('todo_1_list.txt','r') as fw:
        item = fw.readline()
        while item != '':
            tasks.append(item.strip('\n'))
            item = fw.readline()
    return tasks

def write_file():
    with open('todo_1_list.txt','w') as fw:
        for x in todo_list:
            fw.write(x+'\n')
    for line in todo_list:
        pri , tas  = line.split('-')
        priority.append(pri)
        priority.append(tas)

        

def addtotask(values):
    task = values['taskname']
    todo_list.append(task)
    window.FindElement('taskname').Update(value='')
    window.FindElement('todolist').Update(values=todo_list)
    window.FindElement('add_save').Update('Add')

def edit_task(values):
    edit_val =values['todolist'][0]
    window.FindElement('taskname').Update(value=edit_val)
    todo_list.remove(edit_val)
    window.FindElement('add_save').Update('Save')

def delete_task(values):
    del_val = values['todolist'][0]
    todo_list.remove(del_val)
    window.FindElement('todolist').Update(values=todo_list)




layout = [
    [sg.Text('Enter Your Task*',font=('Arial',14)),
    sg.InputText('',font=('Arial',14),size=(25,1),key='taskname'),
    sg.Button('ADD',font=('Arial',14),key='add_save')],
    [sg.Text('*Give priority to the task by assigning number to it in the form :(number-task) ',font=('Arial',10),)],
    [sg.Listbox('',size=(40,10),font=('Arial',14),key='todolist'),
    sg.Button('Edit',font=('Arial',14)),sg.Button('Delete',font=('Arial',14))]
]
todo_list=read_file()
window = sg.Window('Week 1 Tasks',layout)
while True:
    event , values = window.Read()
    if event == 'add_save':
        addtotask(values)
    elif event == 'Edit':
        edit_task(values)
    elif event == 'Delete':
        delete_task(values)
    else :
        break

window.Close()
write_file()
print(todo_list)