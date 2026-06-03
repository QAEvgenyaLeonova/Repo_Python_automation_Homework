from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:123@localhost:5432/QA_Practice_1"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Student(Base):
    __tablename__ = 'SNTUDENT'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    is_deleted = Column(Boolean, default=False)  # для soft delete

Base.metadata.create_all(engine)

def add_student(name, age):
    session = Session()
    new_student = Student(name=name, age=age)
    session.add(new_student)
    session.commit()
    student_id = new_student.id
    session.close()
    return student_id

def update_student(student_id, new_name=None, new_age=None):
    session = Session()
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        if new_name:
            student.name = new_name
        if new_age:
            student.age = new_age
        session.commit()
    session.close()

def delete_student(student_id):
    session = Session()
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        # soft delete
        student.is_deleted = True
        session.commit()
    session.close()