import PySimpleGUI as sg 
from file_reader import file_write ,file_read

sg.theme('Dark Blue')
file_name = 'tasks.txt'
tasks = file_read(file_name)
        

def addtotask(values):
     newtask = values['todo_item'].strip()
     priority = values['priority']
     tasks.append([newtask,priority])
     window.FindElement('todo_item').Update(value="")
     window.FindElement('items').Update(values=tasks)
     window.FindElement('add_save').Update("Add")
     window.FindElement('add_save').Update(disabled=True)


def edit_task(values):
     edit_val = values["items"][0]
     print(edit_val)
     tasks.remove(edit_val)
     window.FindElement('todo_item').Update(value=edit_val[0])
     window.FindElement('priority').Update(value=edit_val[1])
     window.FindElement('add_save').Update("Save")

def delete_task(values):
     tasks.remove(values["items"][0])
     window.FindElement('items').Update(values=tasks)

def check_enable_buttons():
    if values["items"]:
        window.FindElement('delete').Update(disabled=False)
        window.FindElement('edit').Update(disabled=False)
    if values["todo_item"].strip() != '':
        window.FindElement('add_save').Update(disabled=False)


layout = [
    [sg.Text('Enter Your Task',font=('Arial',14)),
    sg.InputText('',font=('Arial',14),size=(25,1),key='todo_item', enable_events=True)],
    [sg.Text('Prioirity:',font=('Arial',14)),sg.Combo(['high','medium','low'],font=('Arial',14),key='priority'),sg.Button('ADD',bind_return_key=True,font=('Arial',14),key='add_save',disabled=True )],
    [sg.Listbox(values=tasks, size=(40,10), font=('Arial',14), key='items', enable_events=True),
    sg.Button('Edit',key='edit',font=('Arial',14),disabled=True),sg.Button('Delete',key='delete',font=('Arial',14),disabled=True)]
]
if __name__ == '__main__':
    window = sg.Window('Week1 App', layout)
    while True:
        event , values = window.Read()
        if event == sg.WINDOW_CLOSED:
            break
        else:
            check_enable_buttons()
        if event == "add_save":
            addtotask(values)
        elif event == "delete":
            delete_task(values)
        elif event == "edit":
            edit_task(values)

    file_write(file_name, tasks)
    window.Close()