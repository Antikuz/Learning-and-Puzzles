import os

SAVE = ""

def main():
    text = []
    filename = ""
    while True:
        print("List Keeper")
        print("Проверка сейв:", SAVE)
        if not filename:
            filename, text = find_lst(text)
        text = get_words(text)
        if do_action(filename, text):
            break
        
            

def do_action(filename, text):
    global SAVE
    if len(text) > 0: 
        delete = "[D]elete"
    else:
        delete = ""
    action = get_str("\n[A]dd {0} {1} [Q]uit [a]: ".format(delete, SAVE),
    condition={"a", "d", "s", "q"}, errMessage="AaDdSsQq")
    if action == "a":
        text.append(input("\nВведите слов(а): "))
        SAVE = "[S]ave"
    elif action == "d":
        a = get_int("\nВведите номер строки для удаления или 0 для отмены: ")
        if a != 0:
            text.pop(a - 1)
            SAVE = "[S]ave"
    elif action == "s":
        save_file(filename, text)
        SAVE = ""
    elif action == "q":
        if SAVE:
            answer = get_str("Остались несохраненние изменения, хотите сохранить? [y/n]", {"yes", "y", "no", "n"}, errMessage="да или нет")
            if answer in {"yes", "y"}: save_file(filename, text)
        return 1

            
def save_file(filename, text):
    count = ""
    file = open(filename, "w", encoding="utf8")
    for i in text:
        file.write(i)
    file.close()
    if len(text) == 1: count = "а"
    print("Сохранено {0} строк{1} в файле {2}".format(len(text), count, filename))
    input("\n---нажмите Enter для продолжения---")
    
    
def get_words(text):
    if not text:
        print ("\n---Not items in the list---")
    width = 1
    text = sorted(text)
    if 9 < len(text) < 100: width = 2
    elif len(text) > 99: width = 3
    for lino, line in enumerate(text):
        print ("{0:{wd}}: {1}".format(lino + 1, line,wd=width))
    return text
    
        
def find_lst(text):
    width = 1
    find_lst = [i for i in os.listdir() if i.endswith(".lst")]
    if 9 < len(find_lst) < 100: width = 2
    elif len(find_lst) > 99: width = 3
    if find_lst:
        print("\n")
        for lino, line in enumerate(find_lst):
            print("{0:{wd}}: {1}".format(lino + 1, line, wd=width)) 
        a = get_int("\nВыберите номер файла, или 0 для создания нового: ")
        if a != 0: 
            filename = find_lst[a - 1]
            for i in open(filename, encoding="utf8"):
                text.append(i)
            return filename, text
    filename = input("\nВыберите имя для файла: ")
    if not filename.endswith(".lst"): filename += ".lst" 
    return filename, text


def get_int(message):
    while True:
        answer = input(message)
        try:
            return int(answer)
        except RangeError as err:
            print("Ошибка", err)
        except ValueError as err:
            input("---ОШИБКА, нужно ввести цифру, нажмите Enter для продолжения---")
            continue
        

def get_str(message, condition, errMessage="буквы"):
    while True:
        answer = input(message).lower()
        try:
            if str(answer) in condition:
                return(answer)
            else:
                raise ValueError
        except ValueError as err:
            input("---ОШИБКА, нужно ввести {0}, нажмите Enter для продолжения---".format(errMessage))
            continue
        
main()