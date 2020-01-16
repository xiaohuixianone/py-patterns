"""
门面设计模式  又叫外观设计
整个模式的执行方式就是，门面接收客户端的需求，去安排系统完成工作。用一个简单的例子举例：去快餐店，我们向服务员点了一份xx套餐，套餐里有一杯冰可乐，一个汉堡，一份薯条，这时服务员听到你的点餐后，扭头告诉后厨需要一份xx套餐，于是后厨有三个人开始行动，一个做可乐，一个做汉堡，一个做薯条。这个例子里，你就是客户端，服务员为门面，后厨的三个人做东西为三个子系统，他们组合合作完成这份套餐的制作。这样看来，门面模式的理解便非常简单了

原则：
1 最少知识原理 减少对象之间的交互
2

"""


class facade:

    def __init__(self):

        self.bell = bellRing()
        self.stu = stuSeat()
        self.teac = teacSeat()

    def runAll(self):
        self.bell.run()
        self.stu.run()
        self.teac.run()

class bellRing:
    def run(self):
        print ('铃声响')

class stuSeat:
    def run(self):
        print ('学生就坐')

class teacSeat():
    def run(self):
        print ('老师就坐')