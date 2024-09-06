
class Calculator:

    def __init__(self, number_1,number_2):
        """Конструктор который выполняеться при создание объекта"""
        self.number_1 = number_1
        self.number_2 = number_2

    def add(self):
        return self.number_1 + self.number_2

    def subtract(self):
        return self.number_1 - self.number_2

    def division(self):
        if number_2 != 0:
            return self.number_1 / self.number_2

class Logger:
    def __init__(self,filename):
        self.filename = filename

    def log_to_file(self,number_1,number_2,action):
        with open(self.filename, 'a', encoding='utf-8') as f:
            log_string = f'{number_1},{number_2}: {action} \n'
            f.write(log_string)
    def read_logs(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            print(f.read())

print('Введи два числа:')
number_1 = int(input('Первое число'))
number_2 = int(input('Второе число'))


print('1 сложить')
print('2 вычесть')
print('3 поделить')
print('4 прочитать логи')
ans = input('Выбери операцию:')

# Создали экземпляры нужных классов
calсulator = Calculator(number_1,number_2)
logger = Logger('logs.txt')
logger_new = Logger('logs_new.txt')

if ans == '1':
    res = calсulator.add()
    print(res)
    logger.log_to_file(number_1,number_2,'Сложение')
elif ans == '2':
    res = calсulator.subtract()
    print(res)
    logger_new.log_to_file(number_1,number_2,'Вычeтание')
elif ans == '3':
    res = calсulator.division()
    print(res)
    logger.log_to_file(number_1, number_2, 'Деление')
elif ans == '4':
    logger.read_logs()
    logger_new.read_logs()
else:
    print('Не верная операция')