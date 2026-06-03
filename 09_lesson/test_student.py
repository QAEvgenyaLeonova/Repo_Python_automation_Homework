import pytest
from main import add_student, update_student, delete_student, Student, engine

@pytest.fixture(autouse=True)
def clean_db():
    with engine.connect() as connection:
        connection.execute("UPDATE SNTUDENT SET is_deleted = FALSE")
    yield

def test_add_student():
    student_id = add_student("Тестовый студент", 20)
    session = engine.connect()
    result = session.execute(f"SELECT * FROM SNTUDENT WHERE id = {student_id}").fetchone()
    session.close()
    assert result is not None

    delete_student(student_id)

def test_update_student():
    student_id = add_student("Начальное имя", 25)
    update_student(student_id, new_name="Обновленное имя", new_age=30)
    session = engine.connect()
    result = session.execute(f"SELECT name, age FROM SNTUDENT WHERE id = {student_id}").fetchone()
    session.close()
    assert result['name'] == "Обновленное имя"
    assert result['age'] == 30
    delete_student(student_id)

def test_delete_student():
    student_id = add_student("Удаляемый студент", 22)
    delete_student(student_id)
    session = engine.connect()
    result = session.execute(f"SELECT is_deleted FROM SNTUDENT WHERE id = {student_id}").fetchone()
    session.close()
    assert result['is_deleted'] is True