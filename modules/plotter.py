# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


    #Описание:
    #Функция сохраняет построенный график в файл.

    #Аргументы:
    #- data (list): Данные для построения графика.
    #- fname (str): Имя файла для сохранения графика.

    #Примечание:
    #Формат файла будет определен на основе расширения имени файла.
    

def plot_sorted_data(sorted_data: list):
   
    try:
        plt.plot(sorted_data)
        plt.title('Sorted data')
        plt.xlabel('Index')
        plt.ylabel('Meaning')
        plt.show()
    except Exception as e:
        print(f"Er ror while plotting: {e}")
