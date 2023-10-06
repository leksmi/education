class Person:
    """
    Пример реализации вычисляемого атрибута,
    full_name вычисляется при каждом запросе,
    таким образом, после любого изменения name, surname -
    full_name подставляется с актуальными значениями
    """

    def __init__(self, name, surname) -> None:
        self._name = name
        self._surname = surname
        # устанавливаем атрибут для кэширования:
        self._full_name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        # сбрасываем full_name при каждом вызове setter
        self._full_name = None

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value
        # сбрасываем full_name при каждом вызове setter
        self._full_name = None

    @property
    def full_name(self):
        """
        Если name или surname менялись -
        Вычисляем атрибут full_name при обращении к нему.
        Иначе просто возвращаем текущий
        """
        if self._full_name is None:
            self._full_name = f"{self._name} {self._surname}"
        return self._full_name


p = Person(name="Kolya", surname="Krasnov")
print(f"Полное имя: {p.full_name}")
p.surname = "Perov"  # вносим изменение
print(f"Полное имя: {p.full_name}")
