import os
import shutil
from pathlib import Path

print(f"#1. {os.name}")

env_vars = os.environ

env_name = {}
for k, v in env_vars.items():
    if 'python' in k.lower():
        env_name[k] = v

print("\n#Podkatalog. Переменные окружения, связанные с Python:")
for k, v in env_name.items():
    print(f"{k}: {v}")


os.environ['PYTHONMY'] = 'ABOBA'
"""Ответы на вопросы:
1.Переменная окружения сущетсвует только в рамках текущего процесса
Podkatalog.Для хранения ифнормации конфигурации, например API ключ
3.Создать можно при помощи панели управления или cmd
"""
for k, v in env_vars.items():
    if 'python' in k.lower():
        env_name[k] = v

print("\n#3. Переменные окружения, связанные с Python:")
for k, v in env_name.items():
    print(f"{k}: {v}")

print("\n#4. Содержание каталога:")
for root, dirs, files in os.walk('../../..'):
    print(f"Каталог: {root}")
    for file in files:
        print(f"  Файл: {file}")
    for dir in dirs:
        print(f"  Подкаталог: {dir}")

target_dir = Path(__file__).parent.parent.parent

if os.path.exists(str(target_dir) + '\\renamed_file.txt'):
    os.remove(str(target_dir) + '\\renamed_file.txt')

if os.path.exists('test_file.txt'):
    os.remove('test_file.txt')

if os.path.exists('copied_file.txt'):
    os.remove('copied_file.txt')

if os.path.exists('renamed_file.txt'):
    os.remove('renamed_file.txt')

with open('test_file.txt', 'w') as f:
    f.write("Тестовый файл")

shutil.copy('test_file.txt', 'copied_file.txt')

os.rename('copied_file.txt', 'renamed_file.txt')

shutil.move('renamed_file.txt', target_dir)

"""6. UNIX специфичные:
1. Их можно использовать и в Windows, но повдение может отличаться
Например os.unlink() - вызывает os.remove
Другие и вовсе недоступны как 
os.getgrouplist 
os.getgid
"""

print("\n#7 Поддерживаемые типы архивов\n", shutil.get_archive_formats())


shutil.unpack_archive("C:\\Users\\Руслан\\PycharmProjects\\PythonProject1\\04_02\\1\\Podkatalog\\3\\dearchive\\some.zip", "extracted_files")
try:
    shutil.unpack_archive("C:\\Users\\Руслан\\PycharmProjects\\PythonProject1\\04_02\\1\\Podkatalog\\3\\dearchive\\test.7z", "extracted_files")
except IOError as e:
    print(e)




