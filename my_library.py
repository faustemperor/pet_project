def option_one():
    print("Вы выбрали пункт 1")

def option_two():
    print("Вы выбрали пункт 2")

def option_three():
    print("Вы выбрали пункт 3")

def option_four():
    print("Вы выбрали пункт 4")

def main():
    while True:
        print("\nГлавное меню:")
        print("1. Пункт 1")
        print("2. Пункт 2")
        print("3. Пункт 3")
        print("4. Пункт 4")
        print("0. Выход")

        choice = input("Выберите пункт меню: ")
        if choice == '1':
            option_one()
        elif choice == '2':
            option_two()
        elif choice == '3':
            option_three()
        elif choice == '4':
            option_four()
        elif choice == '0':
            break
        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()