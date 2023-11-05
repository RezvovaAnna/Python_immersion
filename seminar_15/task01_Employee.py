# Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним
# логирование ошибок и полезной информации. Также реализуйте возможность
# запуска из командной строки с передачей параметров.

import argparse
import logging

FORMAT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(format=FORMAT, filename='logs_for_Person.log', filemode='w', encoding='utf-8', level=logging.ERROR)
logger = logging.getLogger(__name__)


class InvalidNameError(Exception):
    pass


class InvalidAgeError(Exception):
    pass


class InvalidIdError(Exception):
    pass


class Person:
    def __init__(self, surname: str, name: str, patronymic: str, age: int):
        if len(surname) == 0:
            raise InvalidNameError(f'Invalid name: {surname}. Name should be a non-empty string.')
        self.surname = surname
        if len(name) == 0:
            raise InvalidNameError(f'Invalid name: {name}. Name should be a non-empty string.')
        self.name = name
        if len(patronymic) == 0:
            raise InvalidNameError(f'Invalid name: {patronymic}. Name should be a non-empty string.')
        self.patronymic = patronymic
        if age < 0:
            raise InvalidAgeError(f'Invalid age: {age}. Age should be a positive integer.')
        self.age = age

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic} возраст: {self.age}'

    def get_age(self):
        return self.age

    def birthday(self):
        return self.age + 1


class Employee(Person):
    _lst_id = None

    def __init__(self, surname, name, patronymic, age, num_id):
        super().__init__(surname, name, patronymic, age)
        if type(num_id) != int or num_id < 100000 or num_id > 999999:
            raise InvalidIdError(f'Invalid id: {num_id}. Id should be a 6-digit positive integer between 100000 and 999999.')
        self.num_id = num_id

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic} возраст: {self.age} id: {self.num_id} level: {self.get_level()}'

    def get_level(self):
        return sum(map(int, str(self.num_id))) % 7


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--surname', type=str, help= "Фамилия", default='')
    parser.add_argument('-n', '--name', type=str, help= "Имя", default='')
    parser.add_argument('-p', '--patronymic', type=str, help= "Отчество", default='')
    parser.add_argument('-a', '--age', type=int, help= "Возраст")
    parser.add_argument('-id', '--num_id', type=int, help="ID")
    args = parser.parse_args()
    try:
        Employee(args.surname, args.name, args.patronymic, args.age, args.num_id)
    except InvalidAgeError as err:
        print("Ошибка Invalid age")
        logging.error(f'{args.age} : Invalid age')
    except InvalidNameError as err:
        print("Ошибка InvalidNameError")
        logging.error(f'{args.surname}, {args.name}, {args.patronymic} : Invalid surname/name/patronymic format.')
    except InvalidIdError as err:
        print("Ошибка InvalidIdError")
        logging.error(f'{args.num_id} : Invalid id')
    print(Employee)