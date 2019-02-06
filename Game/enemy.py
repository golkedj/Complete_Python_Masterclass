# class Enemy:
class Enemy(object):

    def __init__(self, name="Enemy", hit_points=0, lives=1):
        self.name = name
        self.base_hit_points = hit_points
        self.current_hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        if not self.alive:
            print("{} is not alive".format(self.name))
            return

        remaining_points = self.current_hit_points - damage
        if remaining_points > 0:
            self.current_hit_points = remaining_points
            print("I took {} points damage and have {} left".format(damage, self.current_hit_points))
        else:
            self.lives -= 1
            if self.lives > 0:
                self.current_hit_points = self.base_hit_points

                print("I lost a life and have {} lives remaining".format(self.lives))
            else:
                self.alive = False
                print("{} died".format(self.name))

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Hit points: {0.current_hit_points}".format(self)


class Troll(Enemy):
    
    def __init__(self, name):
        # super(Troll, self).__init__(name=name, lives=1, hit_points=23)
        super().__init__(name=name, lives=1, hit_points=23)

    def grunt(self):
        print("Me {0.name}. {0.name} stomp you".format(self))


class Vampyre(Enemy):

    def __init__(self, name):
        super().__init__(name=name, lives=3, hit_points=12)
