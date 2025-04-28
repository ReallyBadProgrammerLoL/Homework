def find_failures(f):
    with open(f, 'r', encoding='utf-8') as file:
        for line in file:
            if 'Failure' in line:
                yield line

def process_logs(inp, outp):
    total, errors = 0, 0
    with open(outp, 'w', encoding='utf-8') as out_f, open(inp, 'r', encoding='utf-8') as in_f:
        for line in in_f:
            total += 1
            if 'Failure' in line:
                out_f.write(line)
                errors += 1
    print(f"Всего: {total}, Ошибок: {errors}, Процент: {errors/total*100:.2f}%" if total else "Файл пуст")

process_logs('Syslog-2019_01_21-12_40.log', 'errors.log')
