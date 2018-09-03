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
# try:
#     import tkinter
# except ImportError:  # python 2
#     import Tkinter as tkinter

# import json

# main_window = tkinter.Tk()

# main_window.title('Calculator')
# main_window.geometry('640x480+400+200')
# main_window_padding = 8
# main_window['padx'] = main_window_padding

# result = tkinter.Entry(main_window)
# result.grid(row=0, column=0, sticky='nsew')

# keypad = tkinter.Frame(main_window)
# keypad.grid(row=1, column=0, sticky='nsew')
# with open('calculator_buttons.json') as buttons_file:
#     button_configurations = json.load(buttons_file)
# for button_configuration in button_configurations:
#     button = tkinter.Button(keypad, text=button_configuration['text'])
#     button.grid(
#         row=button_configuration['row'],
#         column=button_configuration['column'],
#         rowspan=button_configuration['rowspan'],
#         columnspan=button_configuration['columnspan'],
#         sticky=button_configuration['sticky']
#     )

# main_window.update()
# total_width = main_window_padding + keypad.winfo_width()
# total_height = result.winfo_height() + keypad.winfo_height()
# main_window.minsize(total_width, total_height)
# main_window.maxsize(total_width, total_height)

# main_window.mainloop()

# Professor Solution
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 2), ('/', 1)],
        ]

mainWindowPadding = 8
mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('640x480-8-200')
mainWindow['padx'] = mainWindowPadding

result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, sticky='nsew')

keyPad = tkinter.Frame(mainWindow)
keyPad.grid(row=1, column=0, sticky='nsew')

row = 0
for keyRow in keys:
    col = 0
    for key in keyRow:
        tkinter.Button(keyPad, text=key[0]).grid(row=row, column=col, columnspan=key[1], sticky=tkinter.E + tkinter.W)
        col += key[1]
    row += 1

mainWindow.update()
mainWindow.minsize(keyPad.winfo_width() + mainWindowPadding, result.winfo_height() + keyPad.winfo_height())
mainWindow.maxsize(keyPad.winfo_width() + 50 + mainWindowPadding, result.winfo_height() + 50 + keyPad.winfo_height())

mainWindow.mainloop()
