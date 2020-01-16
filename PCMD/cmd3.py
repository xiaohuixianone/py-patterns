"""
关于 __call__ 方法，不得不先提到一个概念，就是可调用对象（callable），我们平时自定义的函数、内置函数和类都属于可调用对象，但凡是可以把一对括号()应用到某个对象身上都可称之为可调用对象，判断对象是否为可调用对象可以用函数 callable

"""


class A:

    def __init__(self,name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print(self.name)


if __name__ == '__main__':


    commandStack = []


    commandStack.append(A("sb"))
    commandStack.append(A("sx"))

    print(commandStack)

    A("sd")()

    for cmd in commandStack:
        cmd()
