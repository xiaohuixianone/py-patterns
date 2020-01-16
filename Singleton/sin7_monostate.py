# 单态

class Borg:
    __shared_state = {}

    def __init__(self):

        self.x = 1

        print(self.__shared_state)

        self.__dict__ = self.__shared_state

        print(self.__dict__)


b = Borg()
b1 = Borg()
print(b._Borg__shared_state)
b.x = 4



print("--------------------")

print(b.__dict__)
print(b1.__dict__)