class MyClass:
    class_attribute = "I am a class attribute"

    def __init__(self, value):
        self.instance_attribute = value

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")
        print(f"Class attribute: {cls.class_attribute}")

# 通过类调用
MyClass.class_method()

# 通过实例调用
obj = MyClass("test")
obj.class_method()