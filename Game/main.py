from player import Player

dave = Player("David")

print(dave.name)
print(dave.lives)
dave.lives -= 1
print(dave)

dave.lives -= 1
print(dave)

dave.lives -= 1
print(dave)

dave.lives -= 1
print(dave)

dave._lives = 9
print(dave)

dave.level = 2
print(dave)

dave.level += 5
print(dave)

dave.level = 3
print(dave)

dave.score = 500
print(dave)