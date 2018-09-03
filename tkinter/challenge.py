# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok if you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# If you are using Windows you will probably find that the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

# My Solution
try:
    import tkinter
except ImportError:  # python 2
    import Tkinter as tkinter

import os
import json

main_window = tkinter.Tk()

main_window.title('Calculator')
main_window.geometry('640x480+400+200')
main_window['padx'] = 8

main_window.columnconfigure(0, weight=100)
main_window.columnconfigure(1, weight=90)
main_window.rowconfigure(0, weight=100)
main_window.rowconfigure(1, weight=90)

result_frame = tkinter.LabelFrame(main_window)
result_frame.grid(row=0, column=0)
result = tkinter.Entry(result_frame)
result.grid(row=0, column=0, columnspan=4, sticky='new')

keypad_frame = tkinter.Frame(main_window)
keypad_frame.grid(row=1, column=0)
with open('calculator_buttons.json') as buttons_file:
    button_configurations = json.load(buttons_file)
for button_configuration in button_configurations:
    button = tkinter.Button(keypad_frame, text=button_configuration['text'])
    button.grid(
        row=button_configuration['row'],
        column=button_configuration['column'],
        rowspan=button_configuration['rowspan'],
        columnspan=button_configuration['columnspan'],
        sticky=button_configuration['sticky']
    )
# buttons = [
#     {

#     }
# ]
# tkinter.Button(main_window, text='C')
# buttons[0].grid(row=1, column=0, sticky='nw')

main_window.mainloop()