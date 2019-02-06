from enemy import Enemy, Troll, Vampyre, VampyreKing

super_vamp = VampyreKing("Super Fang")

while super_vamp._alive:
    super_vamp.take_damage(20)
    print(super_vamp)

# ugly_troll = Troll("Pug")
# print("Ugly troll - {}".format(ugly_troll))

# another_troll = Troll("Ug")
# print("Another troll - {}".format(another_troll))

# brother = Troll("Urg")
# print(brother)

# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()

# ugly_troll.take_damage(10)
# ugly_troll.take_damage(10)
# ugly_troll.take_damage(10)
# ugly_troll.take_damage(10)
# ugly_troll.take_damage(10)


# dracula = Vampyre("Dracula")

# dracula.take_damage(13)
# print(dracula)

# dracula.take_damage(3)
# print(dracula)

# # while dracula._alive:
#     # dracula.take_damage(1)
#     # print(dracula)

# dracula._lives = 0
# dracula._current_hit_points = 1
# print(dracula)