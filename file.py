import os
import os.path


def main():
    while True:
        print(os.getcwd())
        print('1. Просмотр каталога\n' +\
              '2. На уровень вверх\n' +\
              '3. На уровень вниз\n' +\
              '4. Колличество файлов и каталогов\n' +\
              '5. Размер всех файлов в текущем каталоге\n' +\
              '6. Поиск файла\n' +\
              '7. Выход из программы\n' +\
              'Выберете пункт меню:')
        command = acceptCommand()
        runCommand(command)
        if command == 7:
            print('Работа программы завершена.')
            break


def acceptCommand():
    while True:
        command = int(input())
        if command in range(1, 8):
            break
    return command


def runCommand(command):
    if command == 1:
        print(catalog())
    if command == 2:
        moveUp()
    if command == 3:
        current = input('Введите имя нужного подкаталога: ')
        moveDown(current)
    if command == 4:
        path = os.getcwd()
        print(countFiles(path))
        os.chdir(path)
    if command == 5:
        path = os.getcwd()
        print(countBytes(path))
        os.chdir(path)
    if command == 6:
        target = input('Введите название файла: ')
        path = os.getcwd()
        a = findFiles(target, path)
        if a is True:
            print('Такой файл существует.')
        else:
            print('Такого файла нет.')


def catalog():
    dic_now = os.getcwd()
    return os.listdir(dic_now)


def moveUp():
    dic_now = os.getcwd()
    num = dic_now.rfind('\\')
    return os.chdir(dic_now[:num])


def moveDown(current):
    try:
        dic_now = os.getcwd()
        dic_now = os.path.join(dic_now, current)
        return os.chdir(dic_now)
    except FileNotFoundError:
        print('Такого файла нет.')


def moveDown_1(current):
    try:
        dic_now = os.getcwd()
        dic_now = os.path.join(dic_now, current)
        return os.chdir(dic_now)
    except FileNotFoundError:
        return


def countFiles(path):
    global counter
    for file in catalog():
        if os.path.isfile(path + '\\' + file):
            counter += 1
        if os.path.isdir(path + '\\' + file):
            moveDown_1(file)
            countFiles(path + '\\' + file)
    return counter


def countBytes(path):
    global bytes
    for file in catalog():
        if os.path.isfile(path + '\\' + file):
            bytes += os.path.getsize(path + '\\' + file)
        if os.path.isdir(path + '\\' + file):
            moveDown_1(file)
            countBytes(path + '\\' + file)
    return bytes


def findFiles(target, path):
    if target in catalog():
        return True
    for file in catalog():
        if os.path.isdir(path + '\\' + file):
            moveDown_1(file)
            findFiles(os.getcwd(), target)


counter = 0
bytes = 0

if __name__ == '__main__':
    main()
