"""
一个众所周知的代理模式的例子就是引用计数的指针对象。

代理模式是结构设计模式的例子。这个模式的目的是要创建一个真实对象或类的代理。

代理模式有3个必要的元素：

真实的对象（执行业务逻辑，被代理的对象）
代理类（用户请求的一个接口，对真实目标的保护）
用户（获取任务的用户请求）

"""
from abc import ABCMeta,abstractmethod

class KindWoman(metaclass=ABCMeta):

    @abstractmethod
    def make_eyes_with_man(self):
        pass

    @abstractmethod
    def happy_with_man(self):
        pass



class PanjinLian(KindWoman):

    def make_eyes_with_man(self):
        print(f"{PanjinLian.__name__} make_eyes_with_man")

    def happy_with_man(self):
        print(f"{PanjinLian.__name__} happy_with_man")


class WangPo(KindWoman):
    """王婆这个人老聪明了，她太老了，
     是个男人都看不上她，
     但是她有智慧经验呀，
     他作为一类女人的代理！
    """
    def __init__(self):
        self.kind_woman = PanjinLian()

    def set_kindWoman(self,kindWoman):
        '''她可以是KindWomam的任何一个女人的代理，
           只要你是这一类型
        '''
        self.kind_woman = kindWoman

    def happy_with_man(self):
        '''自己老了，干不了了，但可以叫年轻的代替'''
        self.kind_woman.happy_with_man()


    def make_eyes_with_man(self):
        '''王婆年纪大了，谁看她抛媚眼啊'''
        self.kind_woman.make_eyes_with_man()


if __name__ == '__main__':

    p = PanjinLian()

    p.make_eyes_with_man()