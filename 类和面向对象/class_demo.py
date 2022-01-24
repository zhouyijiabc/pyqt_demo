# 1. 函数式编程和面向对象对比
# 2. 面向对象代码如何编写
# 3. 面向对象三大特性：封装/继承/多态


"""
变量：
     - 实例变量（字段）
        - 公有实例变量（字段）  内外都能调用
        - 私有实例变量（字段）  不会继承到子类，子类不可访问
     - 类变量（静态字段）
        - 公有类变量
        - 私有类变量  不会继承到子类，子类不可访问
        - 当所有对象种有共同的字段且要改都改要删都删的时候，可以将实例变量（字段）提取到类变量（静态字段）

方法：
    - 实例方法  在调用构造方法数据的时候用实例方法
    - 静态方法  私有方法加方法名前加__
    - 类方法

属性：
    - 属性前面加@property   调用不需要加括号  属性不能加参数，只能有一个self
    - 应用场景： 对于简单的方法，当无需传参且有返回值时，可以用 @property
    - 属性也有 公有属性和私有属性，编写时前面加__


"""


def new_fun(*arg):
    print(arg)


class Foo:
    age = 1  # 类变量（静态字段）

    def __init__(self, **kwargs):
        self.l1 = kwargs['l1']
        self.l2 = kwargs['l2']
        self.l3 = kwargs['l3']  # 公有实例变量（字段）外部可访问，可调用
        self.__name = 'hello'  # 私有实例变量（字段） 外部不能访问不能调用，只能内部调用

    def func(self):  # 实例方法
        print(self.__name)

    @staticmethod        # 静态方法， 带上@staticmethod   不用写self,方法参数可有可无
    def hello():  # 静态方法直接通过类调用不需要实例化调用， 不需要调用对象中已封装的值时用静态方法
        print('hello')

    @classmethod
    def hello_class(cls):  # 类方法 想用当前类的时候用类方法，cls为当前类__main__
        print('hello class')

    @property   # 属性前面加@property   调用不需要加括号  属性不能加参数，只能有一个self
    def start(self):
        return 1

    @property
    def end(self):
        return 20


obj = Foo(l1=33, l2=52, l3=44)
new_fun(obj.l1, obj.l2, obj.l3)
Foo.age = 12
print(obj.age)
# print(obj._Foo__name)  # 强行访问私有变量
Foo.hello()  # 调用静态方法
Foo.hello_class()  # 调用类方法
print(obj.start)  # 调用属性
print(obj.end)

