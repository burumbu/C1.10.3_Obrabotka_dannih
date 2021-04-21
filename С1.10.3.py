
class Client:
    def __init__(self, first_name, last_name, city="", balance=0.0, status=""):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.status = status
        self.balance = balance

    def get_info(self):
        return f"Клиент {self.first_name} {self.last_name}, {self.city}. Баланс: {self.balance} руб."

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_city(self):
        return self.city

if __name__ == '__main__':
    client_1 = Client("Иван", "Петров", "Курск", 50)
    print(client_1.get_info())
    print(client_1.get_first_name())
    print(client_1.get_last_name())
    print(client_1.get_city())

if __name__ == '__main__':
    client_2 = Client("Николай", "Иванов","Бабруйск", 12)
    print(client_2.get_info())