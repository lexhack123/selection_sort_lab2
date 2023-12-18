# -*- coding: utf-8 -*-

 #Описание:
    #Функция сохраняет отсортированные данные в указанный файл.

    #Аргументы:
    #- fname (str): Имя файла, в который нужно сохранить данные.
    #- sorted_data (list): Отсортированный список данных.

    #Примечание:
    #Если файл существует, он будет перезаписан данными.


def save_sorted_data_to_file(fname: str, sorted_data: list):
  
    try:
        with open(fname, 'w') as file:
            for data in sorted_data:
                file.write(str(data) + '\n')
        print(f"The sorted data is saved to the file '{fname}'.")
    except Exception as e:
        print(f"Error saving data to file '{fname}': {e}")
        
