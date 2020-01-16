class Singleton(object):
    """
    __new__ (构造函数)单独地创建一个对象，而 __init__ (初始化函数)负责初始化这个对象。
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"instance"):
            cls.instance = super(Singleton,cls).__new__(cls)

        return cls.instance


s = Singleton()

s1 = Singleton()

print(s)
print(s1)
