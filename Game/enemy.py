import random

# class Enemy:
class Enemy(object):

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self._name = name
        self._base_hit_points = hit_points
        self._current_hit_points = hit_points
        self._lives = lives
        self._alive = True

    def take_damage(self, damage):
        if not self._alive:
            print("{} is dead".format(self._name))
            return

        remaining_points = self._current_hit_points - damage
        if remaining_points > 0:
            self._current_hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self._current_hit_points))
        else:
            self._lives -= 1
            if self._lives > 0:
                self._current_hit_points = self._base_hit_points

                print("I lost a life and have {} lives remaining".format(self._lives))
            else:
                self._alive = False
                print("{} died".format(self._name))

    def __str__(self):
        return "Name: {0._name}, Lives: {0._lives}, Hit points: {0._current_hit_points}".format(self)


class Troll(Enemy):
    
    def __init__(self, name):
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("Me {0._name}. {0._name} stomp you".format(self))


class Vampyre(Enemy):

    def __init__(self, name, hit_points=12):
        super().__init__(name=name, lives=3, hit_points=hit_points)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("***** {0._name} dodges *****".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage=damage)

class VampyreKing(Vampyre):

    def __init__(self, name):
        super().__init__(name=name, hit_points=140)

    def take_damage(self, damage):
        super().take_damage(damage // 4)
