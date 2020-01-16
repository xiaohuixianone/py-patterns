class CoffeineBeverage:

    def prepare_recipe(self):
        # 新的实现方法
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    def brew(self):
        # 需要在子类实现
        raise NotImplementedError

    def pour_in_cup(self):
        print("Pouring into cup")

    def add_condiments(self):
        # 这里其实是个钩子方法，子类可以视情况选择是否覆盖
        # 钩子方法是一个可选方法，也可以让钩子方法作为某些条件触发后的动作
        pass


# 茶的制作方法
class Tea(CoffeineBeverage):

    def brew(self):
        # 父类中声明了 raise NotImplementedError，这里必须要实现此方法
        print("Steeping the tea")

    # Tea 不需要 add_condiments 方法，所以这里不需要实现


# 咖啡的制作方法
class Coffee(CoffeineBeverage):

    def brew(self):
        # 父类中声明了 raise NotImplementedError，这里必须要实现此方法
        print("Dripping Coffee through filter")

    def add_condiments(self):
        print("Adding Sugar and Milk")