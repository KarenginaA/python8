import csv
import os.path


def load_contacts(filename):
    contacts = []
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                contacts.append(row)
    return contacts


def save_contacts(filename, contacts):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(contacts)


def add_contact(contacts):
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    email = input("Введите адрес электронной почты: ")
    contacts.append([name, phone, email])
    print("Контакт успешно добавлен!")


def find_contact(contacts, search_name):
    found_contacts = []
    for contact in contacts:
        if search_name.lower() in contact[0].lower():
            found_contacts.append(contact)
    return found_contacts


def edit_contact(contacts):
    search_name = input("Введите имя или фамилию контакта, которого хотите изменить: ")
    found_contacts = find_contact(contacts, search_name)
    if len(found_contacts) == 0:
        print("Контакт не найден.")
        return
    print("Найденные контакты:")
    for i, contact in enumerate(found_contacts):
        print(f"{i + 1}. {contact[0]}")
    choice = int(input("Выберите номер контакта для редактирования: "))
    if choice < 1 or choice > len(found_contacts):
        print("Некорректный выбор.")
        return
    contact = found_contacts[choice - 1]
    print("Текущая информация:")
    print(f"Имя: {contact[0]}")
    print(f"Номер телефона: {contact[1]}")
    print(f"Адрес электронной почты: {contact[2]}")
    new_name = input("Введите новое имя (оставьте пустым, если не хотите изменять): ")
    new_phone = input("Введите новый номер телефона (оставьте пустым, если не хотите изменять): ")
    new_email = input("Введите новый адрес электронной почты (оставьте пустым, если не хотите изменять): ")
    if new_name:
        contact[0] = new_name
    if new_phone:
        contact[1] = new_phone
    if new_email:
        contact[2] = new_email
    print("Контакт успешно изменен!")


def delete_contact(contacts):
    search_name = input("Введите имя или фамилию контакта, которого хотите удалить: ")
    found_contacts = find_contact(contacts, search_name)
    if len(found_contacts) == 0:
        print("Контакт не найден.")
        return
    print("Найденные контакты:")
    for i, contact in enumerate(found_contacts):
        print(f"{i + 1}. {contact[0]}")
    choice = int(input("Выберите номер контакта для удаления: "))
    if choice < 1 or choice > len(found_contacts):
        print("Некорректный выбор.")
        return
    contact = found_contacts[choice - 1]
    contacts.remove(contact)
    print("Контакт успешно удален!")