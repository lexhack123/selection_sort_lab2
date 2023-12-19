# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

 #Описание:
    #Функция строит график для отсортированных данных.
    #Аргументы:
    #- sorted_data (list): Отсортированный список данных.

def save_plot(data: list, fname: str):
    
    try:
        plt.plot(data)
        plt.title('Sorted data')
        plt.xlabel('Index')
        plt.ylabel('Meaning')
        plt.savefig(fname)
        plt.close()
        print(f"The graph is saved to file '{fname}'.")
    except Exception as e:
        print(f"Error while plotting: {e}")
