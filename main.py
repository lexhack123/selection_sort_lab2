# -*- coding: utf-8 -*
from os import mkdir, path
from array_generator import generate_random_array  # Инструмент для создания случайных массивов
from data_saver import save_sorted_data_to_file  # Инструмент для сохранения отсортированных данных в файл
from plot_saver import save_plot  # Инструмент для сохранения графиков
from selection_sort import selection_sort2  # Импорт функции сортировки выбором
from data_loader import load_data_from_file
#отображение главного меню
def display_menu():
    print("\nMenu:")
    print("1. Load data from a file")
    print("2. Generate random arrays")
    print("3. Manually input numbers")
    print("4. Quit")
#отображение подменю
def display_submenu():
    print("\nSub-menu:")
    print("1. Save sorted data to a file")
    print("2. Save plots")

def main_menu():
    arr = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")  # Введите ваш выбор (1-4):

        if choice == "1":
            # Загрузить данные из файла
            file_path = input("Enter the file path: ")  # Введите путь к файлу:
            arr = load_data_from_file(file_path)
            
            # Сортировка и отображение данных
            if arr:
                selection_sort2(arr)
                print("Sorted ", arr)  # Отсортированные и отображенные данные
        elif choice == "2":
            # Сгенерировать случайные массивы
            size = int(input("Enter the size of the array: "))  # Введите размер массива:
            min_value = int(input("Enter the minimum value: "))  # Введите минимальное значение:
            max_value = int(input("Enter the maximum value: "))  # Введите максимальное значение:
            arr = generate_random_array(size, min_value, max_value)
            
            # Сортировка и отображение данных
            if arr:
                selection_sort2(arr)
                print("Sorted ", arr)  # Отсортированные и отображенные данные
        elif choice == "3":
            # Ввести числа вручную
            manual_input = input("Enter numbers separated by spaces: ")  # Введите числа, разделенные пробелами:
            arr = [int(num) for num in manual_input.split()]
            
            # Сортировка и отображение данных
            if arr:
                selection_sort2(arr)
                print("Sorted ", arr)  # Отсортированные и отображенные данные
        elif choice == "4":
            # Выйти
            print("End of program.")  # Конец программы.
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")  # Неверный выбор. Введите число от 1 до 4.
            continue

        while True:
            display_submenu()
            sub_choice = input("Enter your choice (1-3) or 3 to go back to the main menu: ")  # Введите ваш выбор (1-2) или 3, чтобы вернуться в главное меню:

            if sub_choice == "5":
                # Сохранить отсортированные данные в файл
                sorted_dir = 'sorted/'
                if not path.exists(sorted_dir):
                    mkdir(sorted_dir)

                output_file = input("Enter the output file name for sorted data: ")  # Введите имя файла для сохранения отсортированных данных:
                save_sorted_data_to_file(path.join(sorted_dir, output_file), arr)
                print(f"Sorted data has been saved to {output_file}.")  # Отсортированные данные сохранены в {output_file}.
            elif sub_choice == "6":
                # Сохранить графики
                imgs_dir = 'imgs/'
                if not path.exists(imgs_dir):
                    mkdir(imgs_dir)

                output_image = input("Enter the output file name for the plot: ")  # Введите имя файла для сохранения графика:
                save_plot(arr, path.join(imgs_dir, output_image))
                print(f"The plot has been saved to {output_image}.")  # График сохранен в {output_image}.
            elif sub_choice == "4":
                # Вернуться в главное меню
                break
            else:
                print("Invalid choice. Please enter 4, 5, or 6.")  # Неверный выбор. Введите 4, 5 или 6.

if __name__ == "__main__":
    main_menu()

