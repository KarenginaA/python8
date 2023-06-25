from contacts import *


def main():
    filename = 'contacts.csv'
    contacts = load_contacts(filename)

    while True:
        print("\nТелефонный справочник")
        print("1. Просмотреть контакты")
        print("2. Добавить контакт")
        print("3. Изменить контакт")
        print("4. Удалить контакт")
        print("5. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            print("\nКонтакты:")
            if len(contacts) == 0:
                print("Нет контактов.")
            else:
                for contact in contacts:
                    print(f"Имя: {contact[0]}")
                    print(f"Номер телефона: {contact[1]}")
                    print(f"Адрес электронной почты: {contact[2]}")
                    print()

        elif choice == '2':
            add_contact(contacts)

        elif choice == '3':
            edit_contact(contacts)

        elif choice == '4':
            delete_contact(contacts)

        elif choice == '5':
            save_contacts(filename, contacts)
            print("Спасибо за использование справочника!")
            break

        else:
            print("Некорректный выбор. Попробуйте снова.")
