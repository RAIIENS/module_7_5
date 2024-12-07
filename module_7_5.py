import os
import time
# Путь к каталогу
directory = "."
# Обход каталога
for root, dirs, files in os.walk(directory):
    for file in files:
# Формирование полного пути к файлу
        filepath = os.path.join(root, file)
# Получение времени последнего изменения файла
        filetime = os.path.getmtime(filepath)
# Форматирование времени
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
# Получение размера файла
        filesize = os.path.getsize(filepath)
# Получение родительской директории файла
        parent_dir = os.path.dirname(filepath)
# Вывод информации о файле
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

# Используем os.walk(directory) для обхода всех подкаталогов и файлов в указанном каталоге.
# Вложенный цикл for используется для обработки каждого файла в текущем каталоге.
# Полный путь для каждого файла формируется  с помощью os.path.join(root, file).
# Получаем время последнего изменения файла с помощью os.path.getmtime(filepath).
# Форматируем время в удобочитаемый вид.

