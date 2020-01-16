# 懒汉式

class Singeleton:
    # 定义私有成员
    __instance = None

    def __init__(self):
        if not Singeleton.__instance:
            print("Instance begin create")
        else:
            print("Instance already create")

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singeleton()

        return cls.__instance


s1 = Singeleton().getInstance()
s2 = Singeleton().getInstance()

print(s1,s2)
print(Singeleton._Singeleton__instance)

s3 = Singeleton()
print(s3._Singeleton__instance)
s4 = Singeleton()
print(s3,s4)
