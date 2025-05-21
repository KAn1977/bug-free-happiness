class MyDict(dict):  # исправлено название класса согласно PEP 8
    def get(self, key, default=0):  # исправлен пробел после default
        return super().get(key, default)  # используем super() вместо dict

a = dict(a=1, b=2)
b = MyDict(a=1, b=2)

b['c'] = 4
print(b)  # {'a': 1, 'b': 2, 'c': 4}
print(a)

print(a.get('key'))  # None
print(b.get('v'))  # 0