from enemy import Enemy, Troll, Vampyre

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

ugly_troll.take_damage(10)
ugly_troll.take_damage(10)
ugly_troll.take_damage(10)
ugly_troll.take_damage(10)
ugly_troll.take_damage(10)


dracula = Vampyre("Dracula")

dracula.take_damage(13)
print(dracula)

dracula.take_damage(3)
print(dracula)

while dracula.alive:
    dracula.take_damage(1)