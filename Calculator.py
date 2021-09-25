import tkinter as tk

fun = '' 

# Функция проверяет строку на наличее числа
def isLnt(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Функция при отсутствии числа в конце списка не ставит знак
def znac(i):
    global fun
    if fun == '':
        return
    elif isLnt(str(fun[-1])) == False:
        return
    else:
        fun += i 
        label['text'] = f'{fun}'

##################
# Функции кнопок
##################

def clic0(): 
    global fun
    fun += '0'        
    label['text'] = f'{fun}'
    
def clic1():
    global fun
    fun += '1'        
    label['text'] = f'{fun}'
    
def clic2():
    global fun 
    fun += '2'        
    label['text'] = f'{fun}'
    
def clic3():
    global fun
    fun += '3'         
    label['text'] = f'{fun}'
    
def clic4(): 
    global fun
    fun += '4'
    label['text'] = f'{fun}'
    
def clic5():
    global fun 
    fun += '5'
    label['text'] = f'{fun}'
    
def clic6(): 
    global fun
    fun += '6'
    label['text'] = f'{fun}'
    
def clic7(): 
    global fun
    fun += '7'
    label['text'] = f'{fun}'
    
def clic8(): 
    global fun
    fun += '8'
    label['text'] = f'{fun}'
    
def clic9(): 
    global fun
    fun += '9'
    label['text'] = f'{fun}'
      
def clicRav():
    global fun  
    if fun == '':
        return
    else:       
        label['text'] = f'{eval(fun)}'
        fun = ''

def clicDell(): 
    global fun
    fun = ''
    label['text'] = f'{fun}'

def clicPlas():
    global fun
    if fun == '':
        return
    elif isLnt(str(fun[-1])) == False:
        return
    else:
        fun += '+' 
        label['text'] = f'{fun}'

def clicMin():
    global fun
    if fun == '':
        return
    elif isLnt(str(fun[-1])) == False:
        return
    else:
        fun += '-' 
        label['text'] = f'{fun}'
    
def clicDel():
    global fun
    if fun == '':
        return
    elif isLnt(str(fun[-1])) == False:
        return
    else:
        fun += '/' 
        label['text'] = f'{fun}'
    
def clicUm(): 
    global fun
    if fun == '':
        return
    elif isLnt(str(fun[-1])) == False:
        return
    else:
        fun += '*' 
        label['text'] = f'{fun}'

#
# Далее оболочуа
#

# Создаем окно   
window = tk.Tk()
window.title('Калькулятор')
# Рамка для дисплея
frame = tk.Frame(window)
frame.grid(row=0, column=0)

# Дисплей
label = tk.Label(frame, bg='white', text='0', width=26)
label.grid(row=0, column=0, padx=2, pady=2)

#Рамка для кнопок
frameButton = tk.Frame(window)
frameButton.grid(row=1, column=0)

# Задаем и ставим кнопки
button0 = tk.Button(frameButton, text='0', width=5, height=2, command=clic0)
button0.grid(row=3, column=0, padx=2, pady=2)
buttonRav = tk.Button(frameButton, text='=', width=5, height=2, command=clicRav)
buttonRav.grid(row=3, column=1, padx=2, pady=2)
buttonDell = tk.Button(frameButton, text='Dell', width=5, height=2, command=clicDell)
buttonDell.grid(row=3, column=2, padx=2, pady=2)
buttonMin = tk.Button(frameButton, text='-', width=5, height=2, command=clicMin)
buttonMin.grid(row=3, column=3, padx=2, pady=2)
button1 = tk.Button(frameButton, text='1', width=5, height=2, command=clic1)
button1.grid(row=2, column=0, padx=2, pady=2)
button2 = tk.Button(frameButton, text='2', width=5, height=2, command=clic2)
button2.grid(row=2, column=1, padx=2, pady=2)
button3 = tk.Button(frameButton, text='3', width=5, height=2, command=clic3)
button3.grid(row=2, column=2, padx=2, pady=2)
buttonPlas = tk.Button(frameButton, text='+', width=5, height=2, command=clicPlas)
buttonPlas.grid(row=2, column=3, padx=2, pady=2)
button4 = tk.Button(frameButton, text='4', width=5, height=2, command=clic4)
button4.grid(row=1, column=0, padx=2, pady=2)
button5 = tk.Button(frameButton, text='5', width=5, height=2, command=clic5)
button5.grid(row=1, column=1, padx=2, pady=2)
button6 = tk.Button(frameButton, text='6', width=5, height=2, command=clic6)
button6.grid(row=1, column=2, padx=2, pady=2)
buttonDel = tk.Button(frameButton, text='/', width=5, height=2, command=clicDel)
buttonDel.grid(row=1, column=3, padx=2, pady=2)
button7 = tk.Button(frameButton, text='7', width=5, height=2, command=clic7)
button7.grid(row=0, column=0, padx=2, pady=2)
button8 = tk.Button(frameButton, text='8', width=5, height=2, command=clic8)
button8.grid(row=0, column=1, padx=2, pady=2)
button9 = tk.Button(frameButton, text='9', width=5, height=2, command=clic9)
button9.grid(row=0, column=2, padx=2, pady=2)
buttonUm = tk.Button(frameButton, text='*', width=5, height=2, command=clicUm)
buttonUm.grid(row=0, column=3, padx=2, pady=2)

window.mainloop()
