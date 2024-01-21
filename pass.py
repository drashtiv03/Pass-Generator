import random
import array as arr
import PySimpleGUI as sg
sg.theme('BluePurple')   
layout = [  [sg.Text('Enter the length of password(greater than 4 and non-negative for strong password )'), sg.InputText(key='str')],
            [sg.Text('Enter the number of password'), sg.InputText(key='tim')],
            [sg.Button('Submit'), sg.Button('Cancel')],
            [sg.Multiline(size=(50, 10), key='output_area', autoscroll=True)],]



window = sg.Window('Password Generator', layout,resizable=True,finalize=True)

while True:
    event, values = window.read()
    def process_input(str,tim):
        num=['0','1','2','3','4','5','6','7','8','9']
        alphaupper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        alphalower=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        special= ["!","@","#","$","%","^","&","*","(",")","_","{","}","|",":",";","<",">","?","/"]
        result_list=[]

        for j in range(tim):
            a=''
            for i in range(str):
                    if i%4==0:
                        ch=random.choice(num)
                    elif i%4==1:
                        ch=random.choice(alphaupper)
                    elif i%4==2:
                        ch=random.choice(alphalower)
                    else:
                        ch=random.choice(special)
                    
                    a+=ch
            result_list.append(a)
        return result_list
    def print_list_elements(my_list):
        for element in my_list:
            print(element)
    
    if event == sg.WINDOW_CLOSED or event == 'Cancel':
        break
    if event == 'Submit':
        length = int(values['str'])
        noofpass=int(values['tim'])
        result=process_input(length,noofpass)
        passwords_str = '\n\n'.join(result)
        window['output_area'].update(value=f'Passwords are:\n{passwords_str}')
    if event=='cancel':
        continue
window.close()
