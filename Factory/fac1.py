class ShapeFactory(object):
    def getShape(self):
        return self.shape_name

class Circle(ShapeFactory):

    def __init__(self):
        self.shape_name = "Circle"
    def draw(self):
        print('draw circle')

class Rectangle(ShapeFactory):
    def __init__(self):
        self.shape_name = "Retangle"

    def draw(self):
        print('draw Rectangle')


class ShapeInterfaceFactory(object):
    '''
    接口基类
    '''
    def create(self):
        '''
        把要创建的工厂对象装配进来
        '''
        raise  NotImplementedError

class ShapeCircle(ShapeInterfaceFactory):
    def create(self):
        return Circle()


class ShapeRectangle(ShapeInterfaceFactory):
    def create(self):
        return Rectangle()


shape_interface = ShapeCircle()
obj = shape_interface.create()
obj.getShape()
obj.draw()

shape_interface2 = ShapeRectangle()
obj2 = shape_interface2.create()
obj2.draw()

"""

ShapeFactory（父类 or 基类）：提取出所有子类的重复方法代码
Circle（Shape子类 or 派生类）：作用为画圆形
Rectangle（Shape子类 or 派生类）：作用为画矩形
ShapeInterfaceFactory（父类 or 基类）：提取出所有子类的重复方法代码
ShapeCircle（ShapeInterfaceFactory的子类 or 派生类）：作用为创建指定的Circle对象
ShapeRectangle（ShapeInterfaceFactory的子类 or 派生类）：作用为创建指定的Rectangle对象

"""