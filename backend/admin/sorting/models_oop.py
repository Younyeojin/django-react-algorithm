from dataclasses import dataclass


@dataclass
class Calculator(object):
    num1 = int
    num2 = int

    @property
    def num1(self) -> int: return self._num1

    @num1.setter
    def num1(self, num1): self._num1 = num1

    @property
    def num2(self) -> int: return self._num2

    @num2.setter
    def num2(self, num2): self._num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiple(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2


@dataclass
class Grade(object):
    def __init__(self, kor, eng, math, name):
        self.kor = kor
        self.eng = eng
        self.math = math
        self.name = name

    @property
    def name(self): return self._name
    @name.setter
    def name(self, name): self._name = name
    @property
    def kor(self) -> int: return self._kor
    @kor.setter
    def kor(self, kor: int): self._kor = kor
    @property
    def eng(self) -> int: return self._eng
    @eng.setter
    def eng(self, eng: int): self._eng = eng
    @property
    def math(self) -> int: return self._math
    @math.setter
    def math(self, math: int): self._math = math

    def sum(self): return self.kor + self.eng + self.math
    def avg(self): return self.sum() / 3

    def return_grade(self) -> str:
        avg = self.avg()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        elif avg >= 50:
            return 'E'
        else:
            return 'F'


@dataclass
class Contacts(object):

    # @staticmethod
    # def set contact(name, phone, email, address) -> object:
    #     return Contacts(name, phone, email, address)
    @staticmethod
    def get_contacts(ls):
        for i in ls:
            i.to_string()
        return ls
    @staticmethod
    def del_contact(ls, name):
        for i, j in enumerate(ls):
            if name == j.name:
                del ls[i]
        return
