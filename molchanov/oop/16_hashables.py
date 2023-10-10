# Ключом в словарях могут быть только хэшируемые объекты.
# Эти объекты должны быть не изменяемыми, иначе хэш изменится.
# Нужна реализация двух дандер методов:
# __eq__ : сравнивать нужно только свойства чтения объекта (ro)
# __hash__ : собственно формирует хэш


import hashlib

class Person:
    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        """
        С помощью @property (так как нет сеттера) создаем ro свойство:
        """
        return self._name
    
    def __hash__(self) -> int:
        return hash(self.name)
    
    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, Person) and self.name == __value.name
    

p1 = Person('Ivan')
p2 = Person('Ivan')
p3 = Person('Ivan')
print(p1 == p2)
# Использование как ключа словаря:
d1 = {p1: 'person 1'}
print(d1[p1])
# Так как p1 == p2 == p3 они могут быть только единственным ключом,
# при попытке использовать их вместе, последующий затирает предыдущий:
d2 = {p1: 'person 1',
      p2: 'person 2',
      p3: 'person 3'}
print(f'{d2[p1]=}')
