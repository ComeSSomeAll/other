from tkinter import *       # graphic interface
from decimal import *       # exact calculation

root = Tk()
root.title('Calculator')

buttons = (('7', '8', '9', '/', '4')        # create buttons
           ('4', '5', '6', '*', '4')
           ('3', '2', '1', '-', '4')
           ('0', '.', '=', '+', '4')
          )

activeStr = ''
stack = []

def calculate():            # this func will recieve inf from stack[]
    global stack
    global label
    result = 0
    operand2 = Decimal(stack.pop())
    operation = stack.pop()
    operand1 = Decimal(stack.pop())

    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
        result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2
    label.configure(text=str(result))

def click(text):            # processing of the pressed key
    global activeStr
    global stack
    if text == 'CE':
        stack.clear()
        activeStr = ''
        label.configure(text='0')
    elif '0' <= text <= '9':
        activeST

