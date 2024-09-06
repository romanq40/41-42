class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.health = 50
        self.food_to_eat = ['мясо','корм','печеньки']
        self.friend = None
        self.human = None




    def eat(self,food):
        if food in self.food_to_eat:
            self.health += 5
            print('Спасибо')
        else:
            print('Я такое не ем')

    def walk(self):
        yes = input('Пойдем гулять?')
        if yes == 'да':
            self.health +=10
            print('гаф,гаф,гаф')
        elif yes == 'нет':
            self.health -=20
            print('пись,пись')
        else:
            print('Неправильно')
    def age_of_people(self):
        return self.age * 7

    def get_friend(self,dog):
        if abs(dog.age - self.age) < 3:
            self.friend = dog
            dog.friend = self
            print('Ура мы друзья')
        else:
            print('Не получиться')

class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.health = 60
        self.dog = None

    def add_dog(self,dog):
        if not dog.human:
            self.dog = dog
            dog.human = self
            print('Мы подружились')
        else:
            print('Не получиться')


dog1 = Dog(name='Тузик',age= 2)
dog2 = Dog(name='Вареник',age= 3)

human1 = Human('Джек',23)
human1.add_dog(dog1)
human1.add_dog(dog2)
human2 = Human('Джек',23)
human2.add_dog(dog1)
human2.add_dog(dog2)
dog1.get_friend(dog2)
print(dog1.friend.name)
print(dog2.friend.name)
dog1.eat('мясо')
dog1.eat('салфетка')
print(dog1.health)
dog1.walk()
print(dog1.health)
print(dog1.age_of_people())
