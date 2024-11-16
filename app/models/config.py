"""
Конфигурационный файл для SQLAlchemy
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# архитектура для бд
engine = create_engine("sqlite://", echo=True)

# Сессия для работы с бд
session = Session()
