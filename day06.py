# 제너레이터
# 메모리를 확보할 필요없이 큰 시퀀스 순회 가능
# 이터레이터에 대한 데이터의 소스
# 리스트, 딕셔너리는 컴프리헨션이 있는데 튜플은 없고 제너레이터임
print(sum(range(1, 101)))  # 1+2=3, 3+3=6 마지막으로 호출된 항목을 기억하고 다음 값을 반환 -> 일반함수와 차이점
print('\n')

def my_range(first=0, last=10, step=1):  # keyword parameter
    number = first
    while number < last:
        yield number  # return이라면 종료되는데, yield는 끝까지 코드가 돌아
        number += step

ranger = my_range(1, 5)
print(ranger)  # generator는 for문을 이용하여 출력해야 됨
for x in ranger:
    print(x)



def a():  # generator
    yield 1
    yield 2
    yield 3

def b():  # nomal
    return 1  # end
    return 2
    return 3

print(a())
print(b())

for i in a():
    print(i)
for i in a():
    print(i)  # 순회를 마친 제너레이터는 메모리에 저장없어

# 제너레이터 컴프리헨션는 괄호로 묶어
genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))
print(genobj)
for i in genobj:
    print(i)



# 데커레이터
# 코드를 변경하지 않고, 함수를 수정
def sub_int(x, y):
    return x-y

# decorator
def document_info(func):  # 기존의 func 함수를 수정하지 않고 수정하고 싶을 때
    def new_function(*args, **kwargs):  # 가변인수
        print('실행중인 function:', func.__name__)  # 함수의 이름이 출력
        print('positional argument:', args)  # 튜플
        print('keyword argument:', kwargs)  # 딕셔너리
        result = func(*args, **kwargs)
        print('실행결과:', result)
        return result
    return new_function

print(sub_int(7, 3))

info_sub_int = document_info(sub_int)
info_sub_int(7, 3)

r = info_sub_int(6, 3)
print(r)
print('\n')


# 자동
@document_info
def sub_int(x, y):
    return x-y

@document_info
def squares(n):
    return n * n

print(sub_int(7, 3))
print(squares(5))
print('\n')


# 네임스페이스
g = 1  # 전역변수
def print_global():
    print(g)
print(g)
print_global()

print('\n')
def change_print_global():
    global g  # 전역변수 g를 참조
    print(g)
    g = 2
    print(g)
change_print_global()
print_global()
print(g)
print(globals())
print(locals())
print(__name__)
print('\n')


def something(n):
    a = 5
    a += n
    print(a)

something(1)
something(3)
print('\n')


# 재귀함수 : 함수가 자기자신을 호출
# 반복문
def factorial_iter(n):
    '''
    반복문을 사용한 팩토리얼 함수
    :param n: n!
    :return: 팩토리얼 계산 결과값
    '''
    result = 1
    for k in range(1, n+1):
        result = result * k
    return result

print(factorial_iter(5))


# 재귀함수
def factorial_recu(n):
    '''
    재귀함수을 사용한 팩토리얼 함수
    :param n: n!
    :return: 자기 자신을 호출 또는 1
    '''
    if n == 1:  # 끝나는 조건
        return 1
    else:
        return factorial_recu(n-1) * n

print(factorial_recu(5))
print('\n')



# 에러 처리하기
# 나누기 프로그램
try:
    # raise "쉬는시간!"
    raise Exception("쉬는 시간")
    expr = input('분자 문모 입력(띄어쓰기로 구분): ').split()
    print(int(expr[0]) / int(expr[1]))
    print(expr[2])
# value error
except ValueError as err:
    print(err)
    print(f'숫자를 입력하세요 ({err}).')
# zero division error as err
except ZeroDivisionError as err:
    print(f'분모에 0이 올 수 없습니다. ({err})')
# index error
except IndexError as err:
    print(f'입력 값의 범위에 문제가 있습니다. ({err})')
# except
except Exception as other:
    print(f'예외발생: {other}')
else:  # 예외가 발생하지 않았을 때
    print('프로그램 정상', end=' ')
finally:  # 예외 발생 여부와 상관 없이 무조건 실행
    print('종료')


groups = {
    '빅뱅': ['GD', '태양', '탑', '대성', '승리'],
    '마마무': ['문별', '솔라', '휘인', '화사']
}

# 리스트에서 승리를 빼기
for group, members in groups.items():
    print(f'{group}의 멤버')
    for member in members:
        if member != '승리':
            print(member)



# 객체와 클래스
class Cat():
    pass  # 클래스가 비어있음


# 매서드: class 안에 선언된 함수 = 멤버함수
class Cat:
    def __init__(self):  # 첫번째 매개변수의 이름은 self
        pass

# 초기화
class Cat:
    def __init__(self):  # __init__()은 초기화 매서드
        pass

class Pokemon:
    def __init__(self):  # 객체 생성시 동작
        print("포켓몬 객체 생성됨")

p1 = Pokemon()  # 객체 생성
p2 = Pokemon()
print(p1, p2)  # 두 객체의 메모리는 서로 다름
print('\n')


class Pokemon:
    def __init__(self, name, owner, skills):  # 객체 생성시 동작
        self.name = name  # 매개변수 이름이 속성의 이름이 된다
        self.owner = owner
        self.skills = skills.split('/')

        print(f"포켓몬 {name} 생성됨")

    def info(self):  # 멤버함수
        print(f'{self.owner}의 포켓몬은 {self.name}')
        for skill in self.skills:
            print(skill)

p1 = Pokemon('피카추', '한지우', '50만 볼트/100만 볼트/번개')
p2 = Pokemon('꼬부기', '오바람', '고속스핀/거품/몸통박치기/하이드로펌프')
print('\n')

print(p1.name)
print(p2.name)
print(p2.skills)
print('\n')

print(f'{p1.owner}의 포켓몬은 {p1.name}')
print(f'{p2.owner}의 포켓몬은 {p2.name}')
print('\n')

p1.info()
p2.info()
print('\n')


# 상속
class Pikachu(Pokemon):  # Pokemon은 부모클래스, Pikachu는 자식클래스
    pass

pi1 = Pikachu('피카추', '덴트', '번개')
pi1.info()





class Car():
    pass
class Yugo(Car):
    pass

print(issubclass(Yugo, Car))

# 각 클래스로부터 객체 생성
give_me_a_car = Car()
give_me_a_yugo = Yugo()















