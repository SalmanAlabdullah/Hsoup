import datetime

class friend :
    def __init__(self,names , levels):
        self.names = names
        self.levels = levels
    def get(self):
        return self.names + self.levels



class player:
    total = 0

    def __init__(self, name, level, weapon):
        self.name = name
        self.level = level
        self.weapon = weapon
        player.total += 1
        self.friend = None

    def __add__(self, other):
        return self.level * other.level




    def loss(self):
        return f' {self.level - 1}'

    def getf(self):
        return self.friend

    def weapon(self):
        return self.weapon

    @classmethod
    def group(cls):
        return cls.total

    @staticmethod
    def hello():
        return print("hello")

    @staticmethod
    def is_workday(day):
        if day.weekday() == 4 or day.weekday() == 5:
            return False
        return True, player.total


class bot(player):
    pass

    def __init__(self, name, level, weapon, strong, inventory):
        super().__init__(name, level, weapon)
        self.strong = strong
        self.inventory = inventory



    def inc(self):
        self.strong += 1

    def inv(self):
        print("  -- inventory --")
        print("=====================")
        inv_list = []
        for item in enumerate(self.inventory) :
            inv_list.append(item)
            print(f'item = {item}' )
        print("=====================")




boto = bot('sultan',12,'bow',5 , ['apple','sword'])
boto.inv()
print(boto.strong)
boto.inc()
print(boto.strong)

boto_friend = friend(['ahmed','khald'],[1,3])

boto.friend = boto_friend

print(boto.friend.get())


date = datetime.date(2004, 11, 2)

print(player.is_workday(date))

player_1 = player('salman', 12, 'sword')
player_2 = player('salman', 2, 'sword')


play = player_1 + player_2

print(play)

print(player_1)
# print(player_1._weapon())
player_1_friend = friend('sa','1')
player_1.friend = player_1_friend

# print(player_1.getf())
#
#
# print(player.group())
# one = player('khald', 5, 'sowrd')
#
# tow = player('salman ', 7, 'bow')
#
# three = player('salman ', 7, 'bow')

# print(player.group())



# print(one.level, 'sasa', one.name)
# print(one.loss())
# print(player.group())
# three = player('salman ', 7, 'bow')
# print(player.group())




