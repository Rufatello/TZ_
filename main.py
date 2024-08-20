# Функция создает множество всех возможных услуг, а также словарь, где ключ это месяц, а значения услуги
def read_services(file_path):
    paid_services = {}
    all_services = set()
    with open(file_path, encoding='utf-8-sig') as file:
        for line in file:
            parts = line.strip().split("_")
            service_name = parts[0]
            month = parts[1].replace('.pdf', '')
            all_services.add(service_name)
            if month not in paid_services:
                paid_services[month] = set()
            paid_services[month].add(service_name)
    return paid_services, all_services


# создает файл "Чеки по папкам"и записывает значения в виде пути
def write_organized_services(file_path):
    with open(file_path, encoding='utf-8-sig') as file:
        with open("чеки_по_папкам.txt", "w+", encoding='utf-8-sig') as my_file:
            for f in file:
                a = f.strip().split('_')
                folder_name = a[1].replace('.pdf', '')
                my_file.write(f'{folder_name}/{f}')
            my_file.write(f'\n\n\nНе оплачены:\n')


# записывает информацию о неоплаченных услугах в файл чеки_по_папкам.txt
def write_unpaid_services(file_path, paid_services, all_services):
    with open(file_path, "a", encoding='utf-8-sig') as my_file:
        for month in paid_services:
            unpaid_services = all_services - paid_services[month]
            if unpaid_services:
                my_file.write(f"\n{month}:\n")
                my_file.write("\n".join(unpaid_services) + "\n")


def main():
    paid_services, all_services = read_services('чеки.txt')
    write_organized_services('чеки.txt')
    write_unpaid_services("чеки_по_папкам.txt", paid_services, all_services)


if __name__ == "__main__":
    main()
