"""
Основная настройка базы данных
"""


from typing import Annotated
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, declared_attr, mapped_column, Mapped
from sqlalchemy import func


int_pk = Annotated[int, mapped_column(primary_key=True)]
str_uniq = Annotated[str, mapped_column(unique=True, nullable=False)]
str_null_true = Annotated[str, mapped_column(nullable=True)]
str_null_false = Annotated[str, mapped_column(nullable=False)]
created_at = Annotated[datetime, mapped_column(server_default=func.now())]
updated_at = Annotated[datetime, mapped_column(server_default=func.now(), onupdate=datetime.now())]


class Base(DeclarativeBase):
    """
    Настройка базовой модели
    """
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    created_at = Mapped[created_at]
    updated_at = Mapped[updated_at]