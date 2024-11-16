"""
Файл с моделями для базы данных
"""

from database import *
from sqlalchemy.orm import Mapped


class Employee(Base):
    """
    Модель для сотрудников
    """

    id = Mapped[int_pk]
    first_name = Mapped[str_null_false]
    last_name = Mapped[str_null_false]
    patronymic = Mapped[str_null_false]
    email = Mapped[str_uniq]
    password = Mapped[str_null_false]

    @property
    def full_name(self) -> str:
        """
        Свойство для получения ФИО
        :return: lastname firstname patronymic -> str
        """
        fullname = [str(self.last_name), str(self.first_name)]
        if self.patronymic:
            fullname.append(str(self.patronymic))
        return str(" ".join(fullname))

    def __repr__(self):
        return f"Employee(last_name={self.last_name}, first_name={self.first_name}, email={self.email})"


class Ticket(Base):
    """
    Модель для талончиков
    """

    id = Mapped[int_pk] # id
    unique_id = Mapped[int] # Уникальный номер для талончика
    student_first_name = Mapped[str_null_false] # Имя
    student_last_name = Mapped[str_null_false] # Фамилия
    student_patronymic = Mapped[str_null_true] # Отчество
    group = Mapped[str_null_false] # Группа студента
    table = Mapped[str_null_true] # Назначенныц стол для консультации
    is_accepted = Mapped[bool]
    is_processed = Mapped[bool]
    is_waiting = Mapped[bool]

    @property
    def full_name(self) -> str:
        """
        Свойство для получения ФИО
        :return: lastname firstname patronymic -> str
        """
        fullname = [str(self.student_last_name), str(self.student_first_name)]
        if self.student_patronymic:
            fullname.append(str(self.student_patronymic))
        return str(" ".join(fullname))

    def __repr__(self) -> str:
        return f"Ticket(unique_id={self.unique_id}, last_name={self.student_last_name}, first_name={self.student_first_name}, table={self.table})"