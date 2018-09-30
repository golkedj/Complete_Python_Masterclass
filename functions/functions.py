def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(*args, sep=' '):
    text = ""
    for arg in args:
        text += str(arg) + sep
    text = text[:-1]
    left_margin = (80 - len(text)) // 2
    return " " * left_margin + text


# with open('centered', mode='w') as centered_file:
    # call the function
# s1 = center_text("spam and eggs")
# print(s1)
# s2 = center_text("spam, spam and eggs")
# s3 = center_text(12)
# print(s3)
# s4 = center_text("spam, spam, spam and spam")
# print(s4)
# s5 = center_text("first", "second", 3, 4, "spam", sep=':')
# print(s5)

with open('menu', 'w') as menu:
    s1 = center_text("spam and eggs")
    print(s1, file=menu)
    s2 = center_text("spam, spam and eggs")
    print(center_text(12), file=menu)
    print(center_text("spam, spam, spam and spam"), file=menu)
    s5 = center_text("first", "second", 3, 4, "spam", sep=':')
    print(s5, file=menu)
