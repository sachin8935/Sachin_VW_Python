class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating new instance")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value):
        if not hasattr(self, "initialized"):
            self.value = value
            self.initialized = True

s1 = Singleton(10)
s2 = Singleton(20)

print(s1.value)
print(id(s1))
print(id(s2))
print(s1 is s2)