import os
import shutil
from pathlib import Path
import time

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


shutil.unpack_archive("'../../../3/dearchive/some.zip", "extracted_files")

try:
    shutil.unpack_archive("../../../3/dearchive/test.7z", "extracted_files")
except IOError as e:
    print(e)


temp_dir = "temp_pack_dir"
os.makedirs(temp_dir, exist_ok=True)

for root, dirs, files in os.walk('../../..'):
    for file in files:
        if file.startswith('a'):
            src_path = os.path.join(root, file)
            dst_path = os.path.join(temp_dir, file)
            try:
                for attempt in range(3):
                    try:
                        shutil.copy2(src_path, dst_path)
                        print(f"Добавлен: {src_path}")
                        break
                    except PermissionError:
                        if attempt == 2:
                            print(f"Ошибка: файл {src_path} занят. Пропускаем.")
                            continue
                        time.sleep(1)
            except Exception as e:
                print(f"Неизвестная ошибка с {src_path}: {e}")

if os.listdir(temp_dir):
    shutil.make_archive("archive_name", 'zip', temp_dir)
    print(f"\nАрхив создан: {"archive_name"}.zip")
else:
    print("\nФайлы по маске не найдены!")

for attempt in range(3):
    try:
        shutil.rmtree(temp_dir)
        break
    except PermissionError:
        if attempt == 2:
            print(f"Не удалось удалить {temp_dir}. Удалите вручную.")
        time.sleep(1)

print(os.path.abspath("archive_name.zip"))
print(os.path.exists("C:/Users/Руслан/PycharmProjects/PythonProject1"))