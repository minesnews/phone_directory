def write_file(data):
    second_name = input("Введите фамилию\n")
    name = input("Введите имя\n")
    last_name = input("Введите отчество\n")
    phone = input("Введите телефон\n")
    data.write(f'second_name: {second_name}\n')
    data.write(f'name: {name}\n')
    data.write(f'last_name: {last_name}\n')
    data.write(f'phone: {phone}\n')
        
    print("Файл записан")
    
def read_file(data):
    for line in data:
        print(line)
        
def transformations_data(res, find, option, finds, data):
    print('\n')
    count = 0
    id = 0
    while True:
        if option == 2:
            count = 0
        for line in res:
            if find == 1:
                    if line == f"second_name: {finds}":
                        count +=1
            if find == 2:
                    if line == f"name: {finds}":
                        count +=1
            if find == 3:
                    if line == f"last_name: {finds}":
                        count += 1
            if find == 4:
                    if line == f"phone: {finds}":
                        count += 1
        for line in range(len(res)):
            if option == 1:
                if find == 1:                    
                    if res[line] == f"second_name: {finds}":
                            print(res[line])
                            print(res[line+1])
                            print(res[line+2])
                            print(res[line+3])
                            count -=1
                elif find == 2:
                    if res[line] == f"name: {finds}":
                            print(res[line-1])
                            print(res[line])
                            print(res[line+1])
                            print(res[line+2])
                            count -=1
                elif find == 3:
                    if res[line] == f"last_name: {finds}":
                            print(res[line-2])
                            print(res[line-1])
                            print(res[line])
                            print(res[line+1])
                            count -=1
                elif find == 4:
                    if res[line] == f"phone: {finds}":
                            print(res[line-3])
                            print(res[line-2])
                            print(res[line-1])
                            print(res[line])
                            count -=1
            elif option == 2:
                if find == 1:
                    if res[line] == f"second_name: {finds}":                            
                            print(res[line])
                            print(res[line+1])
                            print(res[line+2])
                            print(res[line+3])
                            del res[line: line+4]
                            break
                elif find == 2:
                    if res[line] == f"name: {finds}":
                            print(res[line-1])
                            print(res[line])
                            print(res[line+1])
                            print(res[line+2])
                            del res[line-1: line+3]
                            break
                elif find == 3:
                    if res[line] == f"last_name: {finds}":
                            print(res[line-2])
                            print(res[line-1])
                            print(res[line])
                            print(res[line+1])
                            del res[line-2: line+2]
                            break
                elif find == 4:
                    if res[line] == f"phone: {finds}":
                            print(res[line-3])
                            print(res[line-2])
                            print(res[line-1])
                            print(res[line])
                            del res[line-3: line+1]
                            break
            elif option == 3:
                if find == 1:
                    if res[line] == f"second_name: {finds}":                            
                            print(f"Id {id}")
                            print(res[line])
                            print(res[line+1])
                            print(res[line+2])
                            print(res[line+3])
                            count -= 1
                            id+=1
                elif find == 2:
                    if res[line] == f"name: {finds}":
                            print(f"Id {id}")
                            print(res[line-1])
                            print(res[line])
                            print(res[line+1])
                            print(res[line+2])
                            
                            count -= 1
                            id+=1
                elif find == 3:
                    if res[line] == f"last_name: {finds}":
                            print(f"Id {id}")
                            print(res[line-2])
                            print(res[line-1])
                            print(res[line])
                            print(res[line+1])
                            count -= 1
                            id+=1
                elif find == 4:
                    if res[line] == f"phone: {finds}":
                            print(f"Id {id}")
                            print(res[line-3])
                            print(res[line-2])
                            print(res[line-1])
                            print(res[line])
                            count -= 1
                            id+=1
        if count == 0:
                break
    print('\n')
    if option == 2:
        itog_res =[]
        res1 = []
        for i in range(len(res)):
            if res[i].startswith("second_name:"):
                itog_res = res[i].split(' ')
                for j in range(len(itog_res)):
                    res1.append(itog_res[j])
            if res[i].startswith("name:"):
                itog_res = res[i].split(' ')
                for j in range(len(itog_res)):
                    res1.append(itog_res[j])
            if res[i].startswith("last_name:"):
                itog_res =res[i].split(' ')
                for j in range(len(itog_res)):
                    res1.append(itog_res[j])
            if res[i].startswith("phone:"):
                itog_res =res[i].split(' ')
                for j in range(len(itog_res)):
                    res1.append(itog_res[j])
        open_file('w', "data1", 0, res1)
        
    elif option == 3:
        if(id>1):
            id = 0
            s = int(input("Введите ID для изменения"))
            while True:
                print('входим в true')
                for line in range(len(res)):
                    if find == 1:
                        if res[line] == f"second_name: {finds}":
                            
                            if id == s:
                                print(id)
                                second_name = input("Введите фамилию (Нажмите ENTER, если хотите оставить текущую)")
                                if second_name != '':
                                    res[line] = f"second_name: {second_name}"
                                name = input("Введите имя (Нажмите ENTER, если хотите оставить текущую)")
                                if name != '':
                                    res[line+1] = f"name: {name}"
                                last_name = input("Введите отчество (Нажмите ENTER, если хотите оставить текущую)")
                                if last_name != '':
                                    res[line+2] = f"last_name: {last_name}"
                                phone = input("Введите телефон (Нажмите ENTER, если хотите оставить текущий)")
                                if phone != '':
                                    res[line+3] = f"phone: {phone}"
                                break
                            else:
                                id+=1
                    elif find == 2:
                        if res[line] == f"name: {finds}":
                            
                            if id == s:
                                print(id)
                                name = input("Введите имя (Нажмите ENTER, если хотите оставить текущую)")
                                if name != '':
                                    res[line] = f"name: {name}"
                                second_name = input("Введите фамилию (Нажмите ENTER, если хотите оставить текущую)")
                                if second_name != '':
                                    res[line-1] = f"second_name: {second_name}"
                                last_name = input("Введите отчество (Нажмите ENTER, если хотите оставить текущую)")
                                if last_name != '':
                                    res[line+1] = f"last_name: {last_name}"
                                phone = input("Введите телефон (Нажмите ENTER, если хотите оставить текущий)")
                                if phone != '':
                                    res[line+2] = f"phone: {phone}"
                                break
                            else:
                                id+=1
                    elif find == 3:
                        if res[line] == f"last_name: {finds}":
                            
                            if id == s:
                                print(id)
                                last_name = input("Введите Отчество (Нажмите ENTER, если хотите оставить текущую)")
                                if last_name != '':
                                    res[line] = f"last_name: {last_name}"
                                second_name = input("Введите фамилию (Нажмите ENTER, если хотите оставить текущую)")
                                if second_name != '':
                                    res[line-2] = f"second_name: {second_name}"
                                name = input("Введите имя (Нажмите ENTER, если хотите оставить текущую)")
                                if name != '':
                                    res[line-1] = f"name: {name}"
                                phone = input("Введите телефон (Нажмите ENTER, если хотите оставить текущий)")
                                if phone != '':
                                    res[line+1] = f"phone: {phone}"
                                break
                            else:
                                id+=1
                                
                    elif find == 4:
                        if res[line] == f"phone: {phone}":
                            
                            if id == s:
                                print(id)
                                phone = input("Введите телефон (Нажмите ENTER, если хотите оставить текущий)")
                                if phone != '':
                                    res[line] = f"phone: {phone}"
                                second_name = input("Введите фамилию (Нажмите ENTER, если хотите оставить текущую)")
                                if second_name != '':
                                    res[line-3] = f"second_name: {second_name}"
                                name = input("Введите имя (Нажмите ENTER, если хотите оставить текущую)")
                                if name != '':
                                    res[line-2] = f"name: {name}"
                                last_name = input("Введите Отчество (Нажмите ENTER, если хотите оставить текущую)")
                                if last_name  != '':
                                    res[line-1] = f"last_name: {last_name}"
                                break
                            else:
                                id+=1        
                            
                if id == s:                    
                    break
        else:
            for line in range(len(res)):
                    if find == 1:
                        if res[line] == f"second_name: {finds}":
                                second_name = input("Введите фамилию (Нажмите ENTER, если хотите оставить текущую)")
                                if second_name != '':
                                    res[line] = f"second_name: {second_name}"
                                name = input("Введите имя (Нажмите ENTER, если хотите оставить текущую)")
                                if name != '':
                                    res[line+1] = f"name: {name}"
                                last_name = input("Введите имя (Нажмите ENTER, если хотите оставить текущую)")
                                if last_name != '':
                                    res[line+2] = f"last_name: {last_name}"
                                phone = input("Введите телефон (Нажмите ENTER, если хотите оставить текущий)")
                                if phone != '':
                                    res[line+3] = f"phone: {phone}"    
                                break
                    if find == 2:
                        if res[line] == f"name: {finds}":
                                # second_name = input("Введите имя (Нажмите ENTER, если хотите оставить текущую)")
                                name = input("Введите имя (Нажмите ENTER, если хотите оставить текущую)")
                                if name != '':
                                    res[line] = f"name: {name}"
                                second_name = input("Введите фамилию (Нажмите ENTER, если хотите оставить текущую)")
                                if second_name != '':
                                    res[line-1] = f"second_name: {second_name}"
                                last_name = input("Введите отчество (Нажмите ENTER, если хотите оставить текущую)")
                                if last_name != '':
                                    res[line+1] = f"last_name: {last_name}"
                                phone = input("Введите телефон (Нажмите ENTER, если хотите оставить текущий)")
                                if phone != '':
                                    res[line+2] = f"phone: {phone}"
                                break
                    if find == 3:
                        if res[line] == f"last_name: {finds}":
                                last_name = input("Введите Отчество (Нажмите ENTER, если хотите оставить текущую)")
                                if last_name != '':
                                    res[line] = f"last_name: {last_name}"
                                second_name = input("Введите фамилию (Нажмите ENTER, если хотите оставить текущую)")
                                if second_name != '':
                                    res[line-2] = f"second_name: {second_name}"
                                name = input("Введите имя (Нажмите ENTER, если хотите оставить текущую)")
                                if name != '':
                                    res[line-1] = f"name: {name}"
                                phone = input("Введите телефон (Нажмите ENTER, если хотите оставить текущий)")
                                if phone != '':
                                    res[line+1] = f"phone: {phone}"
                                break
                    if find == 4:
                        if res[line] == f"phone: {finds}":
                            
                            if res[line] == f"phone: {finds}":
                                phone = input("Введите телефон (Нажмите ENTER, если хотите оставить текущий)")
                                if phone != '':
                                    res[line] = f"phone: {phone}"
                                second_name = input("Введите фамилию (Нажмите ENTER, если хотите оставить текущую)")
                                if second_name != '':
                                    res[line-3] = f"second_name: {second_name}"
                                name = input("Введите имя (Нажмите ENTER, если хотите оставить текущую)")
                                if name != '':
                                    res[line-2] = f"name: {name}"
                                last_name = input("Введите Отчество (Нажмите ENTER, если хотите оставить текущую)")
                                if last_name  != '':
                                    res[line-1] = f"last_name: {last_name}"
                                break
        itog_res =[]    
        data.close
        res1 = []

        for i in range(len(res)):
            if res[i].startswith("second_name:"):
                # print(i)
                itog_res = res[i].split(' ')
                for j in range(len(itog_res)):
                    res1.append(itog_res[j])
            if res[i].startswith("name:"):
                # print(i)
                itog_res = res[i].split(' ')
                for j in range(len(itog_res)):
                    res1.append(itog_res[j])
            if res[i].startswith("last_name:"):
                # print(i)
                itog_res =res[i].split(' ')
                for j in range(len(itog_res)):
                    res1.append(itog_res[j])
            if res[i].startswith("phone:"):
                # print(i)
                itog_res =res[i].split(' ')
                for j in range(len(itog_res)):
                    res1.append(itog_res[j])
        open_file('w', "data1", 1, res1)
    
        
        
def deleting_data(data, res):
    # print(res)
    for i in range(0, len(res), 2):
            data.write(f"{res[i]} {res[i+1]}\n")
            
def editing_data(data, res):
    # print(res)
    for i in range(0, len(res), 2):
        
            data.write(f"{res[i]} {res[i+1]}\n")    
      
        
def open_file_and_find(find, finds, data):
    s = int(input("Выберите режим: 1 - просмотр данных, 2 - удаление данных, 3 - изменение данных"))
    res = data.read()
    res = res.split('\n')
    if s == 1:
        count = 0
        transformations_data(res, find, s, finds, data)
    if s == 2:
        print("Идем удалять")
        transformations_data(res, find, s, finds, data)
    if s == 3:
        print("Идем изменять данные")
        transformations_data(res, find, s, finds, data)
        
def find_data(data):
    print("Перешли в поиск")
    bool_fio = False
    bool_name = False
    bool_last_name = False
    bool_telephone = False
    while True:
        find = int(input("Введите цифру для поиска по определенной категории: 1 - по фамилии, 2 - по имени, 3 - по отчеству, 4 - по телефону\n"))
        
        if find == 1:
            bool_fio = True
            break
        elif find == 2:
            bool_name = True
            break
        elif find == 3:
            bool_last_name = True
            break
        elif find == 4:
            bool_telephone = True
            break
        else:
            print("Неправильный ввод данных")      
    
    find_str = "Введите "
    if bool_fio:
        find_str += "фамилию: "
    elif bool_name:
        find_str += "имя: "
    elif bool_last_name:
        find_str += "отчество: "
    elif bool_telephone:
        find_str += "телефон: "
    finds = input(find_str)
    open_file_and_find(find, finds, data)
    

def open_file(mode, data, option, res):
    with open('file.txt', mode, encoding='UTF-8') as data:
        if mode == 'a':
            print("Переходим в функцию записи файла")
            write_file(data)
        if mode == 'r' and option == 0:
            print("Переходим в функцию чтения файла")
            read_file(data)            
        if mode == 'r' and option == 1:
            print("Переходим в функцию поиска в файле")
            find_data(data)
        if mode == 'w' and option == 0 and res != []:
            deleting_data(data, res)
            print("Удаляем найденные данные")
        if mode == 'w' and option == 1 and res != []:
            editing_data(data, res)
            print("Изменяем найденные данные")
            
        
            

while True:
    
    s = input("Введите цифру 1 - для записи файла, 2 - для чтения файла, 3 - поиск по ключевому слову, 4 - выход из программы \n")

    if s == "1":
        print("Переходим в функцию открытия файла")
        open_file('a', "data", 0, [])
    elif s == "2":
        print("Переходим в функцию открытия файла")
        open_file('r', "data", 0, [])
    elif s == "3":
        print("Инициализирую поиск данных...")
        open_file('r', "data", 1, [])
    elif s == "4":
        print("Инициализирую выход")
        break
    else:
        print("Вы ввели неправильные данные, введите снова")