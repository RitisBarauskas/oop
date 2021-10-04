class Mammals:
    """
    Класс - млекопитающие
    """
    def __init__(self, age):
        self.age = age


class Monkey(Mammals):
    """
    Класс - обезьяна
    """
    def __init__(self, age):
        super().__init__(age)
        self.tail = True


class Dog(Mammals):
    """
    Класс - собака
    """
    def __init__(self, age):
        super().__init__(age)
        self.tail = True

    def _is_old(self):
        if self.age > 1:
            return True
        else:
            return False

    def __repr__(self):
        return 'Собака с хвостом'


class Bulldog(Dog):
    def __init__(self, name, age):
        super().__init__(age)
        self.name = name

    def info(self):
        if self._is_old():
            return f'{self.name} уже взрослый, делает "ррррр-гав"'
        else:
            return f'{self.name} еще щенок, делает "тяф-тяф"'

    def __repr__(self):
        return f'{self.name} - бульдог'


class Human(Monkey):
    """
    Класс - человек
    """
    def __init__(self, name, age):
        super().__init__(age)
        self.name = name
        self.tail = False

    def __repr__(self):
        return f'{self.name} - человек'


class Friend(Human):
    """
    Класс - друг
    """
    def __init__(self, name, age, phone):
        super().__init__(name, age)
        self.phone = phone


class Car:
    def __init__(self, fuel):
        self.fuel = fuel


class Toyota(Car):
    def __init__(self, fuel):
        super().__init__(fuel)

    def distance(self):
        result = self.fuel / 10
        return f'Toyota проедет на {self.fuel} около {result} километров'


class Tesla(Car):
    def __init__(self, fuel):
        super().__init__(fuel)

    def distance(self):
        return f'Если ты попытаешься залить в Tesla {self.fuel} бензина, то далеко не уедешь'
