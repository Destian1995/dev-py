import os, time
import numba

def main():
    while True:
        @njit(fastmath=True, cache=True, parallel=True)
        start = time.time()
        print('Мониторинг запущен')
        vv = '/home/vagrant/ansible-playbook'
        put = vv
        t = time.localtime()
        now = time.strftime("%H:%M:%S", t)
        mass = set()
        mass2 = set()
        # Делаем слепок 1 версии каталога
        path = len([name for name in os.listdir(put) if
                    os.path.isfile(os.path.join(put, name))])
        for root, dirs, files in os.walk(put):
            for filename in files:
                mass.add(filename)


        time.sleep(10)  # 10 секунд
        # Делаем слепок 2 версии каталога
        path2 = len([name for name in os.listdir(put) if
                     os.path.isfile(os.path.join(put, name))])
        for root, dirs, files in os.walk(put):
            for filename in files:
                mass2.add(filename)
        # Ищем отличия в 1 и 2 слепке
        res = list(set(mass) - set(mass2))
        res = str(res)

        # Если находим то формируем лог-файл.
        if path2 < path:
            with open(put + "_logs_sfs01.txt", "w") as file:
                file.write("Обнаружена пропажа файлов! В ")
                file.write(now)
                file.write(' МСК ')
                file.write('Список пропавших файлов - ')
                file.write(res)
                file.close()
            print('Лог-файл сформирован!')
        end = time.time()
        print("1 (множества) :",
              (end - start) * 10 ** 3, "ms")

        start = time.time()
        print('Вторая стадия...')
        vv2 = '/home/vagrant/ansible-playbook'
        put = vv2
        t = time.localtime()
        now = time.strftime("%H:%M:%S", t)
        mass = []
        mass2 = []
        # Делаем слепок 1 версии каталога
        path = len([name for name in os.listdir(put) if
                    os.path.isfile(os.path.join(put, name))])
        for root, dirs, files in os.walk(put):
            for filename in files:
                mass.append(filename)

        time.sleep(10)  # 10 секунд
        # Делаем слепок 2 версии каталога
        path2 = len([name for name in os.listdir(put) if
                     os.path.isfile(os.path.join(put, name))])
        for root, dirs, files in os.walk(put):
            for filename in files:
                mass2.append(filename)
        # Ищем отличия в 1 и 2 слепке
        res = list(set(mass) - set(mass2))
        res = str(res)
        # Если находим то формируем лог-файл.
        if path2 < path:
            with open(put + "_logs_sfs02.txt", "w") as file:
                file.write("Обнаружена пропажа файлов! В ")
                file.write(now)
                file.write(' МСК ')
                file.write('Список пропавших файлов - ')
                file.write(res)
                file.close()
            print('Лог-файл сформирован!')
        end = time.time()
        print("2 вариант(списки) :",
              (end - start) * 10 ** 3, "ms")
        input('нажмите для продолжения')
main()