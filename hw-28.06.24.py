import os

class Employee:
    def __init__(self, name, surname, age, position):
        self.name = name
        self.surname = surname
        self.age = age
        self.position = position

employees = []

def save_employees_to_file(file_path):
    with open(file_path, "w") as file:
        for employee in employees:
            file.write(f"{employee.name},{employee.surname},{employee.age},{employee.position}\n")

def load_employees_from_file(file_path):
    global employees
    employees = []
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            for line in file:
                name, surname, age, position = line.strip().split(",")
                employee = Employee(name, surname, int(age), position)
                employees.append(employee)

def add_employee():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    age = int(input("Введите возраст: "))
    position = input("Введите должность: ")
    employee = Employee(name, surname, age, position)
    employees.append(employee)

def edit_employee():
    surname = input("Введите фамилию сотрудника: ")
    for employee in employees:
        if employee.surname == surname:
            name = input(f"Введите новое имя (старое: {employee.name}): ")
            age = int(input(f"Введите новый возраст (старый: {employee.age}): "))
            position = input(f"Введите новую должность (старая: {employee.position}): ")
            employee.name = name
            employee.age = age
            employee.position = position
            print("Данные сотрудника успешно обновлены.")
            return
    print("Сотрудник с указанной фамилией не найден.")

def remove_employee():
    surname = input("Введите фамилию сотрудника: ")
    for i, employee in enumerate(employees):
        if employee.surname == surname:
            del employees[i]
            print("Сотрудник успешно удален.")
            return
    print("Сотрудник с указанной фамилией не найден.")

def search_employees_by_surname():
    surname = input("Введите фамилию: ")
    found_employees = [employee for employee in employees if employee.surname == surname]
    if found_employees:
        print("Найденные сотрудники:")
        for employee in found_employees:
            print(f"Имя: {employee.name}, Фамилия: {employee.surname}, Возраст: {employee.age}, Должность: {employee.position}")
    else:
        print("Сотрудники с указанной фамилией не найдены.")

def print_employees_by_age():
    age = int(input("Введите возраст: "))
    found_employees = [employee for employee in employees if employee.age == age]
    if found_employees:
        print(f"Сотрудники в возрасте {age} лет:")
        for employee in found_employees:
            print(f"Имя: {employee.name}, Фамилия: {employee.surname}, Возраст: {employee.age}, Должность: {employee.position}")
    else:
        print(f"Сотрудники в возрасте {age} лет не найдены.")

def print_employees_by_first_letter():
    letter = input("Введите букву: ")

    found_employees = [employee for employee in employees if employee.surname.startswith(letter)]
    if found_employees:
        print(f"Сотрудники, фамилия которых начинается на '{letter}':")
        for employee in found_employees:
            print(
                f"Имя: {employee.name}, Фамилия: {employee.surname}, Возраст: {employee.age}, Должность: {employee.position}")
    else:
        print(f"Сотрудники, фамилия которых начинается на '{letter}', не найдены.")

def save_found_employees_to_file():
    file_path = input("Введите путь к файлу: ")
    with open(file_path, "w") as file:
        file.write("Имя,Фамилия,Возраст,Должность\n")
        for employee in employees:
            file.write(f"{employee.name},{employee.surname},{employee.age},{employee.position}\n")
    print(f"Информация о сотрудниках сохранена в файл: {file_path}")

def main():
    file_path = input("Введите путь к файлу с данными о сотрудниках: ")
    load_employees_from_file(file_path)

    while True:
        print("\nМеню:")
        print("1. Добавить сотрудника")
        print("2. Редактировать данные сотрудника")
        print("3. Удалить сотрудника")
        print("4. Поиск сотрудника")
