# Создаем пустой словарь для хранения данных о людях
slovar= {
"Leo":"ул.Гоголя д.68",
"Mark":"ул.Толстого 32",
"Kate":"ул.Суврова д.94"} 

while True:  # условие всегда будет истиным
    print("выберите действие:")
    print("1.показать все адреса")
    print("2.изменить адрес")
    print("3.удалить запись")
    print("4. выйти из системы")
    v = input("введите номер: ")  
    #Выбор номера
    if v =="1":
        print("все адреса:")
        for name, addres in slovar.items():   
            print(f"{name}:{addres}")
    elif v =="2":
        name = input('введите имя:')
        if name in slovar: #Ecли имя в словоре
            new_addres = input("введите адресс:")
            slovar[name]= new_addres   #изменить адресс
            print(f"адрес для{name} изменили на {new_addres}")
        else:
            print("erooooor найди ошибку")
    elif v == '3':
      name = input("Введите имя человека: ")
      if name in slovar:
          del slovar[name] # Удаляем человека из словаря
          print(f"Человек {name} удален из словаря.")
      else:
        print(f"Человека с именем {name} нет в словаре.")
    elif v == "4":
        break   
    else:
        print("неверный ввод попробуй снова")