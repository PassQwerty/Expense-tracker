categories = ["продукты", "одежда", "развлечения", "больница", "другое"]

products = []
clothes = []
entertainments = []
hospital = []
other = []


def sumList():
    sum = 0
    allSumList = []
    allList = [products, clothes, entertainments, hospital, other]
    for item in allList:
        if len(item) > 0:
            allSumList.append(item)

    if len(allSumList) != 0:
        for list in allSumList:
            for item in list:
                sum += int(item[1])
        print('Общая сумма товаров равна: ', sum)
    else:
        print('Товары еще не были добавлены!')

    choice = input("Дальнейшие действия?('назад'|'отмена'): ")
    if choice.lower() == 'назад':
        main()
    elif choice.lower() == 'отмена':
        exit()


def getList(user_choice):
    formatText = None
    if user_choice.lower() == 'продукты':
        formatText = products
    elif user_choice.lower() == 'одежда':
        formatText = clothes
    elif user_choice.lower() == 'развлечения':
        formatText = entertainments
    elif user_choice.lower() == 'hospital':
        formatText = entertainments
    else:
        formatText = other
    return formatText


def setList(list, name, price):
    list.append([name, price])


def setItem():
    while True:
        user_choice = input(
            "Введите категорию расходов -\
            \n('продукты', 'одежда', 'развлечения', 'больница', 'другое') ('отмена'): ")
        if user_choice.lower() == 'отмена':
            print('Вы успешно вышли с программы.')
            break

        elif user_choice.lower() in categories:
            expenditure = input("Введите название расхода: ")
            price = int(input("Введите цену(руб): "))
            answer = getList(user_choice)
            setList(answer, expenditure, str(price))

            user_choice = input(
                "Хотите ввести еще один товар?('д'|'н'|'назад'): ")
            if user_choice.lower() == 'назад':
                main()
            elif user_choice.lower() == 'н':
                print('Вы успешно вышли с программы.')
                exit()
        else:
            print("Введите корректную категорию расходов!")


def sumCategories():
    while True:
        sum = 0
        user_choice = input(
            "Получить сумму с категорию расходов -\
            \n('продукты', 'одежда', 'развлечения', 'больница', 'другое') ('отмена'): ")
        if user_choice.lower() == 'отмена':
            print('Вы успешно вышли с программы.')
            exit()
        elif user_choice.lower() in categories:
            currentList = getList(user_choice)
            if len(currentList) > 0:
                for item in currentList:
                    sum += int(item[1])
                print(f'Сумма категории {user_choice} = {sum}')
            else:
                print("Выбранная категория не содержит товаров")

            user_choice = input(
                "Хотите узнать сумму другой категории?('д'|'н'|'назад'): ")
            if user_choice.lower() == 'назад':
                main()
            elif user_choice.lower() == 'н':
                print('Вы успешно вышли с программы.')
                exit()
        else:
            print("Введите корректную категорию расходов!")


def main():
    choice = input("Введите операцию... \
        \n(Добавить расход - 'расход')\
        \n(Посчитать сумму всех расходов - 'сумма')\
        \n(Посчитать сумму определенной категории - 'категория')\
        \n(Выход из программы - 'отмена'): ")
    if choice.lower() == 'расход':
        setItem()
    elif choice.lower() == 'сумма':
        sumList()
    elif choice.lower() == 'категория':
        sumCategories()
    else:
        print('Вы успешно вышли с программы.')


if __name__ == main():
    main()
