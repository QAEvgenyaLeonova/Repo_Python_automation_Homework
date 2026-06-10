from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

# Конфигурация базы данных
DATABASE_URL = "postgresql://postgres:123@localhost:5432/QA_Practice_1"

# Создание движка и сессии
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Student(Base):
    """
    Модель таблицы студентов.
    """
    __tablename__ = 'SNTUDENT'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String)
    age: int = Column(Integer)
    is_deleted: bool = Column(Boolean, default=False)  # для soft delete

    def __repr__(self) -> str:
        return f"<Student id={self.id} name={self.name} age={self.age}>"

# Создаем таблицы, если не существуют
Base.metadata.create_all(engine)

def add_student(name: str, age: int) -> int:
    """
    Добавляет нового студента.
    :param name: Имя студента
    :param age: Возраст студента
    :return: ID нового студента
    """
    session = Session()
    new_student = Student(name=name, age=age)
    session.add(new_student)
    session.commit()
    student_id = new_student.id
    session.close()
    return student_id

def update_student(student_id: int, new_name: str = None, new_age: int = None) -> None:
    """
    Обновляет данные студента.
    :param student_id: ID студента
    :param new_name: Новое имя (опционально)
    :param new_age: Новый возраст (опционально)
    """
    session = Session()
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        if new_name:
            student.name = new_name
        if new_age:
            student.age = new_age
        session.commit()
    session.close()

def delete_student(student_id: int) -> None:
    """
    Удаляет студента (soft delete).
    :param student_id: ID студента
    """
    session = Session()
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        student.is_deleted = True
        session.commit()
    session.close()