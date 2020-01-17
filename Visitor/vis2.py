# 访问者模式，数据结构中保存着许多元素，当改变一种对元素的处理方式，我们避免重复的修改数据类的结构，那我们在设计之初就将数据的处理分离，即数据类只提供一个数据处理的接口，而数据类的处理方法我们叫它访问者，那么相同结构的数据面临不同的处理结果时，我们只需要创建不同的访问者。


class Finance:
    """财务数据结构类"""

    def __init__(self):
        self.salesvolume = None  # 销售额
        self.cost = None  # 成本
        self.history_salesvolume = None  # 历史销售额
        self.history_cost = None  # 历史成本

    def set_salesvolume(self, value):
        self.salesvolume = value

    def set_cost(self, value):
        self.cost = value

    def set_history_salesvolume(self, value):
        self.history_salesvolume = value

    def set_history_cost(self, value):
        self.history_cost = value

    def accept(self, visitor):
        pass


class Finance_year(Finance):
    def __init__(self,year):

        Finance.__init__(self)
        self.work = []
        self.year = year

    def add_work(self,work):
        self.work.append(work)

    def accept(self):
        for obj in self.work:
            obj.visit(self)


class Accounting:
    """会计类"""

    def __init__(self):
        self.ID = "会计"
        self.Duty = "计算报表"

    def visit(self,table):
        print('会计年度： {}'.format(table.year))
        print("我的身份是： {} 职责： {}".format(self.ID, self.Duty))
        print('本年度纯利润： {}'.format(table.salesvolume - table.cost))
        print('------------------')


class Audit:
    """财务总监类"""

    def __init__(self):
        self.ID = "财务总监"
        self.Duty = "分析业绩"

    def visit(self, table):
        print('会计总监年度： {}'.format(table.year))
        print("我的身份是： {} 职责： {}".format(self.ID, self.Duty))
        if table.salesvolume - table.cost > table.history_salesvolume - table.history_cost:
            msg = "较同期上涨"
        else:
            msg = "较同期下跌"
        print('本年度公司业绩： {}'.format(msg))
        print('------------------')


class Adviser:
    """战略顾问"""
    def __init__(self):
        self.ID = "战略顾问"
        self.Duty = "制定明年战略"

    def visit(self, table):
        print('战略顾问年度： {}'.format(table.year))
        print("我的身份是： {} 职责： {}".format(self.ID, self.Duty))
        if table.salesvolume > table.history_salesvolume:
            msg = "行业上行，扩大生产规模"
        else:
            msg = "行业下行，减小生产规模"
        print('本年度公司业绩： {}'.format(msg))
        print('------------------')


class Work:
    def __init__(self):
        self.works = []

    def add_work(self,obj):
        self.works.append(obj)

    def remove_work(self,obj):
        self.works.remove(obj)

    def visit(self):
        for obj in self.works:
            obj.accept()



if __name__ == '__main__':

    work = Work()


    finance_2018 = Finance_year(2018)

    finance_2018.set_salesvolume(200)
    finance_2018.set_cost(100)
    finance_2018.set_history_salesvolume(180)
    finance_2018.set_history_cost(90)

    accounting = Accounting() #  实例化会计
    audit = Audit() # 实例化总监
    adviser = Adviser() # 实例化顾问

    finance_2018.add_work(accounting)
    finance_2018.add_work(audit)
    finance_2018.add_work(adviser)


    work.add_work(finance_2018) # 添加2018年财务工作安排
    work.visit()



