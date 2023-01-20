# 매서드 오버라이드
# 부모 클래스의 매서드를 자식 클래스에서 재정의하여 사용하는 것
class Car():
    def exclaim(self):
        print("I'm a car")

class Yugo(Car):
    def exclaim(self):
        print("I'm a yugo. Much like a Car, but more Yugo_ish.")  # exclaim() 매서드 오버라이드
    def push(self):  # 매서드 추가
        print('A little help here?')

print(issubclass(Yugo, Car))

give_me_a_car = Car()  # 각 클래스로부터 객체 생성
give_me_a_yugo = Yugo()


class Person():
    def __init__(self, name):
        self.name = name

print('\n')

class Pokemon:
    def __init__(self, owner, skills):
        self.owner = owner
        self.skills = skills.split('/')
        print(f"포켓몬 생성:", end=' ')

    def info(self):
        print(f'{self.owner}의 포켓몬이 가진 스킬')
        for skill in self.skills:
            print(skill)

    def attack(self, idx):
        print(f'{self.owner} {self.skills[idx]} 공격 시전')



class Pikachu(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)  # 부모의 생성자를 호출
        self.name = "피카추"
        print(f'{self.name}')

    def attack(self, idx):
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전')


class Ggoboogi(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)  # super() 부모의 생성자를 호출
        self.name = "꼬부기"
        print(f'{self.name}')

    def attack(self, idx):
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전')

    def swim(self):
        print(f'{self.name}가 수영을 합니다.')


p0 = Pokemon('아이리스', '어떤공격')
p0.attack(0)

pk1 = Pikachu('덴트', '번개')
pk1.info()
pk1.attack(0)

ggo1 = Ggoboogi('오바람', '고속스핀/거품/몸통박치기/하이드로펌프')
print(ggo1.skills)
ggo1.info()
ggo1.attack(2)
ggo1.swim()

print('\n')

# 다중 상속 - 여러 부모 클래스
# 권장하지는 않는다
class animal:
    def says(self):
        return 'I speak!'


class horse(animal):
    def says(self):
        return '말!'


class donkey(animal):
    def says(self):
        return '당나귀!'


class mule(donkey, horse):  # 다중상속 받음 (mule -> donkey -> horse -> animal)
    pass

class hinny(horse, donkey):  # (hinny -> horse -> donkey -> animal)
    def says(self):
        return '히니가 옵니다.'

m1 = mule()
h1 = hinny()
print(m1.says())
print(h1.says())

print(mule.mro())  # 뮬의 order 순서

print('\n')

# 믹스인
class PrettyMixin():
    def time_print(self):  # 날짜 출력
        import datetime
        print(datetime.date.today())

    def dump(self):
        import pprint
        pprint.pprint(vars(self))  # vars는 딕셔너리를 출력

class Thing(PrettyMixin):
    pass

t = Thing()
t.time_print()
t.name = "김민선"
t.feature = 'ichor'
t.age = 'eldritch'
t.dump()


# 속성 접근
# private 속성의 getter/setter 매서드 - 외부에서 직접 접근하지 못하도록 함
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):  # 이름을 꺼낸다 // getter
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):  # 이름을 저장한다  // setter
        print('inside the setter')
        self.hidden_name = input_name


don = Duck('Donald')
print(don.get_name())
don.set_name('Donna')
print(don.get_name())
don.hidden_name = '김인하'  # 직접접근을 막지 못함
print(don.get_name())


# 프로퍼티
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('inside the getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)  # 프로퍼티의 이름을 name으로 해서 hidden name을 감춘다

don = Duck('Donald')
print(don.get_name())
print(don.name)

don.set_name('Donna')
print(don.get_name())

don.name = 'Donna2'
print(don.name)
print('\n')


# 계산된 값의 프로퍼티
class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def duameter(self):
        return 2 * self.radius


# 클래스와 객체 속성
class Fruit:
    color = 'red'

blueberry = Fruit()
print(Fruit.color)  # 클래스 속성 // 객체 이름이 필요 없음
print(blueberry.color)  # 객체 속성

# 객체 속성을 변경해도 클래스 속성에 영향 없음
blueberry.color = 'blue'
print(blueberry.color)
print(Fruit.color)

# 클래스 속성을 변경해도 기존 자식 객체에는 영향 없음
Fruit.color = 'orange'
print(blueberry.color)
print(Fruit.color)

new_fruit = Fruit()  # 새로운 객체에는 영향을 줌
print(new_fruit.color)

print('\n')

# 클래스 매서드
class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm a A")
    @classmethod  # 다같이 공유하는거 -> 인하대학교 전체 재학생의 수
    def kids(cls):
        print(f'A has {cls.count} little objects.')


# 정적 매서드
# 클래스나 객체에 영향이 없고 단지 편의를 위해 존재
class CoyoteWeapon():
    @staticmethod
    def commercial():
        print("This coyoteweapon has been brought to you by Acme")

print(CoyoteWeapon.commercial())


# 덕 타이핑
# 다형성 -> 클래스에 상관없이 같은 동작을 다른 객체에 적용 (부피, 넓이)
import math
class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_area(self):
        print('면적을 출력합니다.')


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, x, y, width, length):
        super().__init__(x, y)

        self.width = width
        self.length = length

    def get_area(self):
        return math.pi * self.width * self.length

    def __repr__(self):  # 매직 메서드
        return f'사각형의 좌표는 x: {self.x}, y: {self.y}이고 넓이는 {self.get_area()}입니다.'

    def __add__(self, other):
        # 두 사작형 넓이의 합
        return (self.width * self.length) + (other.width * other.length)

        # 각 사각형의 width의 합과 length의 합을 곱
        # return Rectangle(0, 0, (self.width + other.width), (self.length + other.length))

class Cylinder(Circle):
    def __init__(self, x, y, radius, height):
        super().__init__(x, y, radius)
        self.height = height

    def get_area(self):
        return super().get_area() * self.height
    # def get_area(self):
    #     return math.pi * self.radius * self.radius * self.height


c1 = Circle(100, 100, 10.0)
c2 = Circle(50, 50, 2.0)
r1 = Rectangle(100, 50, 5, 2)
r2 = Rectangle(70, 30, 5, 2)
cy1 = Cylinder(20, 20, 10.0, 2)


print(c1.get_area())
print(c2.get_area())
print(r1)  # 매직 메서드
print(r2)
print(r1 + r2)
# 사각형의 넓이 비교
# 원기둥의 넓이 비교


# 매직 메서드
class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):  # == 연산자를 사용할 수 있음
        return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('HA')
third = Word('eh')
print(first == second)  # 대소문자 무시
print(first == third)


# 애그리게이션과 콤퍼지션
# 둘다 상속보다 약한 결합 관계
# 애그리게이션은 더 약하고, 콤퍼지션은 강해

