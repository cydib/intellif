class Meta(type):
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        d = {}
        for k, v in attrs.items():
            if k.startswith('__'):
                d[k] = v
            else:
                d[k.upper()] = v
        print(d)
        return type(class_name, bases, d)


class Dog(metaclass=Meta):
    x = 5
    y = 9

    def hi(self):
        print('hi')


d = Dog()
print(d.X)
