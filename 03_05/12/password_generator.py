import json
import random
import string
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("pylog.log", mode="w", encoding='utf-8'),
        logging.StreamHandler()
    ]
)

def gen_pass(min_length, max_length, min_digits, min_special_chars, special_chars):
    available_chars = {
        'lower': ''.join(c for c in string.ascii_lowercase if c not in 'lo'),
        'upper': ''.join(c for c in string.ascii_uppercase if c not in 'IO'),
        'digits': ''.join(c for c in string.digits if c not in '01'),
        'special': special_chars
    }

    required_length = min_digits + min_special_chars + 2
    if max_length < required_length:
        raise ValueError("Максимальная длина пароля слишком мала для заданных требований.")

    password_length = random.randint(max(required_length, min_length), max_length)

    password_chars = []
    password_chars.append(random.choice(available_chars['lower']))
    password_chars.append(random.choice(available_chars['upper']))
    password_chars.extend(random.choices(available_chars['digits'], k=min_digits))
    password_chars.extend(random.choices(available_chars['special'], k=min_special_chars))

    remaining_length = password_length - len(password_chars)
    all_available_chars = ''.join(available_chars.values())
    password_chars.extend(random.sample(all_available_chars, remaining_length))

    random.shuffle(password_chars)

    if len(set(password_chars)) != len(password_chars):
        logging.warning("Пароль содержит дубликаты. Генерация повторяется.")
        return gen_pass(min_length, max_length, min_digits, min_special_chars, special_chars)

    return ''.join(password_chars)

def generate_passwords(config):
    num_passwords = config['num_passwords']
    min_length = config['min_length']
    max_length = config['max_length']
    min_digits = config['min_digits']
    min_special_chars = config['min_special_chars']
    special_chars = config['special_chars']

    passwords = []
    for _ in range(num_passwords):
        try:
            password = gen_pass(min_length, max_length, min_digits, min_special_chars, special_chars)
            passwords.append(password)
            logging.info(f"Сгенерирован пароль: {password}")
        except Exception as e:
            logging.error(f"Ошибка при генерации пароля: {e}")
    return passwords


input_file = 'settings.json'
try:
    with open(input_file, 'r') as file:
        config = json.load(file)
        logging.info("Конфигурация успешно загружена.")
except Exception as e:
    logging.error(f"Ошибка при чтении конфигурации: {e}")


passwords = generate_passwords(config)


output_file = 'passwords.json'
try:
    with open(output_file, 'w') as file:
        json.dump({"passwords": passwords}, file, indent=4)
        logging.info("Пароли успешно сохранены в файл passwords.json.")
except Exception as e:
    logging.error(f"Ошибка при записи паролей в файл: {e}")
