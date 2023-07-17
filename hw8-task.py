# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.

import os
import json
import csv
import pickle

def traverse_directory(directory):
    result = []

    for root, dirs, files in os.walk(directory):
        current_dir_size = sum(os.path.getsize(os.path.join(root, file)) for file in files)
        current_obj = {
            'name': os.path.basename(root),
            'path': root,
            'type': 'directory',
            'size': current_dir_size
        }
        result.append(current_obj)

        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.path.getsize(file_path)
            file_obj = {
                'name': file,
                'path': file_path,
                'type': 'file',
                'size': file_size
            }
            result.append(file_obj)

    return result

def save_as_json(data, filename):
    with open(filename, 'w', encoding="utf-16") as json_file:
        json.dump(data, json_file, indent=4)

def save_as_csv(data, filename):
    keys = data[0].keys()
    with open(filename, 'w', newline='', encoding="utf-16") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

def save_as_pickle(data, filename):
    with open(filename, 'wb') as pickle_file:
        pickle.dump(data, pickle_file)


directory = 'E:\\MUSIC'
output_directory = 'E:\\MUSIC'

traversal_result = traverse_directory(directory)

json_file = os.path.join(output_directory, 'result.json')
save_as_json(traversal_result, json_file)

csv_file = os.path.join(output_directory, 'result.csv')
save_as_csv(traversal_result, csv_file)

pickle_file = os.path.join(output_directory, 'result.pickle')
save_as_pickle(traversal_result, pickle_file)