# Возьмите любые 1-3 задания из прошлых домашних заданий. Добавьте к ним
# логирование ошибок и полезной информации. Также реализуйте возможность
# запуска из командной строки с передачей параметров.

import argparse
import logging


FORMAT = "%(asctime)s %(levelname)s %(message)s"
logging.basicConfig(format=FORMAT, filename='logs_for_Archive.log', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

class InvalidNumberError(ValueError):
    pass


class InvalidTextError(ValueError):
    pass


class Archive:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.archive_text = []
            cls._instance.archive_number = []
        else:
            cls._instance.archive_text.append(cls._instance.text)
            cls._instance.archive_number.append(cls._instance.number)
        return cls._instance

    def __init__(self, text: str, number: int):
        if len(text) == 0 or type(text) != str:
            raise InvalidTextError(f'Invalid text: {text}. Text should be a non-empty string.')
        self._text = text
        if number < 0 or type(number) == chr or type(number) == str:
            raise InvalidNumberError(f'Invalid number: {number}.Number should be a positive integer or float.')
        self._number = number

    @property
    def text(self):
        return self._text

    @property
    def number(self):
        return self._number

    def __str__(self):
        return f'Text is {self.text} and number is {self.number}. Also {self.archive_text} and {self.archive_number}'

    def __repr__(self):
        return f'Archive("{self.text}", {self.number})'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--text', type=str, help="Текст", default='')
    parser.add_argument('-n', '--num', type=int, help="Номер", default='')
    args = parser.parse_args()
    try:
        Archive(args.text, args.num)
    except InvalidTextError as err:
        print("Ошибка Invalid text")
        logging.error(f'{args.text} : Invalid text')
    except InvalidNumberError as err:
        print("Ошибка Invalid number")
        logging.error(f'{args.num} : Invalid number')
    print(Archive)
