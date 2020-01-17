"""访问者模式"""


class Node(object):
    pass


class A(Node):
    pass


class B(Node):
    pass


class C(A, B):
    pass


class Visitor(object):
    def visit(self, node, *args, **kwargs):
        meth = None
        """python支持多重继承，在解析父类的__init__时，定义解析顺序的是子类的__mro__属性，内容为一个存储要解析类顺序的元组。"""
        """观察到，super的执行路径和类的__mro__列举的类顺序吻合；而__mro__的顺序可以看作是深搜的结果"""


        for cls in node.__class__.__mro__:
            """方法名"""
            meth_name = 'visit_' + cls.__name__
            """getattr()函数是Python自省的核心函数，具体使用大体如下：
             获取对象引用getattr,Getattr用于返回一个对象属性，或者方法
      
             如果Visitor对象中有属性meth_name则获得方法返回的值，否则赋值None
            """
            meth = getattr(self, meth_name, None)
            if meth:
                break

        if not meth:
            meth = self.generic_visit
        return meth(node, *args, **kwargs)

    def generic_visit(self, node, *args, **kwargs):
        print('通常访问: ' + node.__class__.__name__)

    def visit_B(self, node, *args, **kwargs):
        print('访问_B ' + node.__class__.__name__)


a = A()
b = B()
c = C()
visitor = Visitor()
visitor.visit(a)
visitor.visit(b)
visitor.visit(c)