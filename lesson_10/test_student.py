import pytest
import allure
from main import add_student, update_student, delete_student, engine

@allure.title("Тест добавления студента")
@allure.description("Проверка добавления нового студента в базу данных")
@allure.feature("CRUD операции")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_student():
    with allure.step("Добавляем нового студента"):
        student_id = add_student("Тестовый студент", 20)
    with allure.step("Проверяем наличие студента в базе"):
        with engine.connect() as connection:
            result = connection.execute(f"SELECT * FROM SNTUDENT WHERE id = {student_id}").fetchone()
        assert result is not None, "Студент не добавился"
    # Очистка данных
    delete_student(student_id)

@allure.title("Тест обновления студента")
@allure.description("Проверка обновления данных студента")
@allure.feature("CRUD операции")
@allure.severity(allure.severity_level.NORMAL)
def test_update_student():
    student_id = add_student("Начальное имя", 25)
    with allure.step("Обновляем имя и возраст студента"):
        update_student(student_id, new_name="Обновленное имя", new_age=30)
    with engine.connect() as connection:
        result = connection.execute(f"SELECT name, age FROM SNTUDENT WHERE id = {student_id}").fetchone()
    assert result['name'] == "Обновленное имя", "Имя не обновилось"
    assert result['age'] == 30, "Возраст не обновился"
    delete_student(student_id)

@allure.title("Тест удаления студента")
@allure.description("Проверка soft delete студента")
@allure.feature("CRUD операции")
@allure.severity(allure.severity_level.MINOR)
def test_delete_student():
    student_id = add_student("Удаляемый студент", 22)
    delete_student(student_id)
    with engine.connect() as connection:
        result = connection.execute(f"SELECT is_deleted FROM SNTUDENT WHERE id = {student_id}").fetchone()
    assert result['is_deleted'] is True, "Студент не помечен как удаленный"