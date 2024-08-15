from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        self.value = value

class Phone(Field):
    def __init__(self, value):
        if self.__is_phone__(value):
            raise ValueError("WrongPhone")
        self.value = value

    def __is_phone__(self, user_data):
        return not user_data.isnumeric() or len(user_data) != 10

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, user_data):
        phone = Phone(user_data)
        self.phones.append(phone)

    def remove_phone(self, user_data):
        for phone in self.phones:
            if phone.value == user_data:
                self.phones.remove(phone)
                break
        else:
            raise ValueError("NoSuchRecord")

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.remove(phone)
                self.add_phone(new_phone)
                break
        else:
            raise ValueError("NoSuchRecord")
    
    def find_phone(self, user_data):
        for phone in self.phones:
            if phone.value == user_data:
                return phone
        # else:
        #     raise ValueError("NoSuchRecord")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, user_data):
        if user_data in self.data:
            return self.data[user_data]
        # else:
        #     raise ValueError("NoSuchRecord")

    def delete(self, user_data):
        if user_data in self.data:
            del self.data[user_data]
        # else:
        #     raise ValueError("NoSuchRecord")

if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    print("== 1 ==")
    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    print("== 2 ==")
    # Додавання запису John до адресної книги
    book.add_record(john_record)

    print("== 3 ==")
    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    print("== 4 ==")
    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    print("== 5 ==")
    # Знаходження та редагування телефону для John
    john = book.find("John")
    print(f"john = {john}")
    john.edit_phone("1234567890", "1112223333")

    print("== 6 ==")
    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
    
    print("== 7 ==")
    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    print("== 8 ==")
    # Видалення запису Jane
    book.delete("Jane")