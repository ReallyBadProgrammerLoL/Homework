import csv
import json
import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_columns', None)

LABEL_MASS = {
    '1': 'dos',
    'Podkatalog': 'u2r',
    '3': 'r2l',
    '4': 'r2l',
    '5': 'r2l',
    '6': 'probe',
    '7': 'dos',
    '8': 'u2r',
    '9': 'r2l',
    '10': 'dos',
    '11': 'probe',
    '12': 'u2r',
    '13': 'r2l',
    '14': 'dos',
    '15': 'probe',
    '16': 'u2r',
    '17': 'probe',
    '18': 'dos',
    '19': 'r2l',
    '20': 'dos',
    '21': 'r2l',
    '22': 'r2l'
}

METRIC_COLUMS = [
    'logged_in',
    'su_attempted',
    'root_shell',
    'num_root',
    'num_file_creations',
    'num_access_files',
    'num_outbound_cmds',
    'src_bytes',
    'dst_bytes'
]

file_path = "Field Names.csv"
file_out  = "out.json"

with open(file_path, 'r') as f:
    columns = [line.split(',')[0].strip() for line in f.readlines()]

columns += ['label_type', 'label_id']

file_path = "KDDTest+.csv"

with open(file_path, mode='r') as file:
    content_csv = list(csv.reader(file))
    df = pd.DataFrame(content_csv, columns = columns)

total = len(df)

print(f"#3. tcp={round(len(df[df['protocol_type'] == 'tcp']) / total, 3)}, udp={round(len(df[df['protocol_type'] == 'udp']) / total, 3)}")


print("\n#4. Кол-во сетевых содинений по категориям")
df_attacks = df[df['label_type'] != 'normal'].copy()
df_attacks['label_type_from_id'] = df_attacks['label_id'].map(LABEL_MASS)
print(df_attacks['label_type_from_id'].value_counts())


print(f"\n#5.\nTCP с атакой: {len(df[(df['protocol_type'] == 'tcp') & (df['label_type'] != 'normal')])}")
print(f"TCP без атаки: {len(df[(df['protocol_type'] == 'tcp') & (df['label_type'] == 'normal')])}")

print("\n#6. Доля каждой категории атаки среди всех сетевых соединений, имеющих признаки атаки")
print(df_attacks['label_type_from_id'].value_counts(normalize = True).round(3))

for col in METRIC_COLUMS:
    df_attacks[col] = pd.to_numeric(df_attacks[col], errors='coerce').fillna(0)

attack_metrics = df_attacks.groupby('label_type_from_id')[METRIC_COLUMS].agg({
    'logged_in': 'sum',
    'su_attempted': 'sum',
    'root_shell': 'sum',
    'num_root': 'sum',
    'num_file_creations': 'sum',
    'num_access_files': 'sum',
    'num_outbound_cmds': 'sum',
    'src_bytes': 'mean',
    'dst_bytes': 'mean'
})
attack_metrics = attack_metrics.rename(columns={
    'logged_in': 'Успешные авторизации (кол-во)',
    'su_attempted': 'Попытки входа под root (кол-во)',
    'root_shell': 'Входы под root (кол-во)',
    'num_root': 'Доступы суперпользователя (кол-во)',
    'num_file_creations': 'Создано файлов (кол-во)',
    'num_access_files': 'Обращений к файлам (кол-во)',
    'num_outbound_cmds': 'Исходящие FTP команды (кол-во)',
    'src_bytes': 'Средний исходящий трафик (байт)',
    'dst_bytes': 'Средний входящий трафик (байт)'
})
print("#7 для каждого вида атаки")
print(attack_metrics.head())

with open(file_out, mode='w', encoding='utf-8') as f:
    json.dump(attack_metrics.to_dict(orient='index'), f, indent= 4, ensure_ascii=False)

plt.figure()
df['protocol_type'].value_counts().plot.pie(autopct='%1.1f%%')
plt.savefig('protocols.jpg')
plt.close()

# Podkatalog. Типы атак (#4)
plt.figure()
df_attacks['label_type_from_id'].value_counts().plot.bar()
plt.savefig('attack_types.jpg')
plt.close()

# 3. TCP атаки vs нормальные (#5)
plt.figure()
pd.Series({
    'С атакой': len(df[(df['protocol_type'] == 'tcp') & (df['label_type'] != 'normal')]),
    'Без атаки': len(df[(df['protocol_type'] == 'tcp') & (df['label_type'] == 'normal')])
}).plot.bar()
plt.tight_layout()
plt.savefig('tcp_status.jpg')
plt.close()

# 4. Метрики атак (#7) - только 3 ключевых показателя
plt.figure()
attack_metrics[['Входы под root (кол-во)', 'Создано файлов (кол-во)', 'Средний исходящий трафик (байт)']].plot.bar()
plt.savefig('key_metrics.jpg')
plt.close()
