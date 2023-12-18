# -*- coding: utf-8 -*-

#Описание:
    #Функция загружает данные из указанного файла.

    #Аргументы:
    #- fname (str): Имя файла, из которого нужно загрузить данные.

    #Возвращает:
    #- list: Список строк, содержащих данные из файла.

    #Примечание:
    #Если файл не найден, функция возвращает пустой список.


def load_data_from_file(fname: str) -> list:
    
    try:
        with open(fname, 'r') as file:
            lines = file.readlines()
            data = []
            for line in lines:
                numbers = line.split()  # Разделяем строку на числа
                for num in numbers:
                    # Преобразуем каждое число в float и добавляем в список
                    data.append(float(num))
            return data
    except FileNotFoundError:
        print(f"File '{fname}' not found.")
        return []
    except ValueError as e:
        print(f"Error reading numeric values ​​from file '{fname}': {e}")
        return []
