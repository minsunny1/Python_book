# set
# 딕셔너리에서 키만 있음, 중복된 값을 삭제
# set()함수나 { , } 중괄호 안에 콤마로 구분된 값을 넣어
empty_set = set()
print(empty_set)
numbers = {1, 2, 5, 6}
print(numbers)

# 변환하기
print(set('letters'))  # 중복값 출력 안됨, 순서 보장 안됨
print(set(['가', '나', '다', '라']))
print(set(('김', '민', '선', '선')))
print(set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'}))

s = set((1,2,3))
print(s)
print(s.add(4))  # 리턴값이 없으므로 None
print(s.remove(3))  # 리턴값이 없으므로 None

s = set((1,2,3))
s.add(4)
print(s)
print(len(s))

# 딕셔너리 안에 value값이 set
drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahllua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

# name은 key, contents는 value
for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)

# set 교집합 &
# 하나라도 들어가 있으면 출력
for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:  # vermouth나 orange juice가 들어있다면
        print(name)

# 둘다 들어간 걸 출력하려면 부분집합
for name, contents in drinks.items():
    if contents >= {'vermouth', 'vodka'}:
        print(name)

# 재료 셋을 변수에 저장
bruss = drinks['black russian']
wruss = drinks['white russian']

# 교집합
print(bruss & wruss)
print(bruss.intersection(wruss))

# 합집합
print(bruss | wruss)
print(bruss.union(wruss))

# 차집합
print(bruss - wruss)
print(bruss.difference(wruss))

# ^ 연산자, symmetric_difference()
# 대칭 차집합 = 서로 다른거
print(bruss ^ wruss)
print(bruss.symmetric_difference(wruss))

# 부분집합
print(bruss <= wruss)

# 셋 컴프리헨션
a_set = {number for number in range(1,6) if number % 3 == 1} # 1~6까지
print(a_set)

# 불변 셋 frozenset()
print(frozenset([3, 2, 1]))
print(frozenset({1, 2, 3}))
print(frozenset((2, 3, 1)))
fs = frozenset([3, 2, 1])
# fs.add(4) // error


# 자료구조 결합
# 리스트
marxes = ['Groucho', 'Chico', 'Harpo']
pythons = ['CHapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe', 'Curly', 'Larry']
# 튜플의 요소가 리스트
tuple_of_lists = marxes, pythons, stooges
print(tuple_of_lists)
# 리스트의 요소가 리스트
list_of_lists = [marxes, pythons, stooges]
print(list_of_lists)
# 딕셔너리의 요소가 리스트 // 리스트 딕셔너리
dict_of_lists = {'Marxes': marxes, 'Pythons': pythons, 'Stooges': stooges}
print(dict_of_lists)



# 코드 재사용을 줄이기 위해 함수를 사용한다

# 함수 정의 def
def do_nothing():  # 괄호 안에 매개변수
    pass
do_nothing()  # 함수 호출
print(do_nothing())  # None // 아무것도 없음

mamamoo = ['화사', '솔라', '휘인', '문별']
print(mamamoo.pop())  # pop은 return 후에 삭제함
print(mamamoo)

mamamoo = ['화사', '솔라', '휘인', '문별']
print(mamamoo.remove('문별'))  # None // remove는 return 기능이 없이 삭제만 함


# def isprime(n):
#     """
#     매개변수로 받은 정수가 소수인지 여부를 판정하는 함수
#     :param n: integer number
#     :return: true or false
#     """
#     if n <= 1:
#         return False
#     for k in range(2, n):
#         if n % k == 0:
#             return False
#     else:
#         return True
#
# help(isprime)  # 주석으로 달았던 함수에 대한 정보를 출력
# print(isprime(19))
#
# start = int(input("input start number: "))
# end = int(input("input end number : "))
#
# if end < start:
#     start, end = end, start
#
# for i in range(start, end+1):
#     if isprime(i):
#         print(i, end=' ')



def echo(anything):
    return anything + " " + anything
print(echo('kadfu'))


# None
# None과 False는 다름
thing = None
if thing:
    print("It's some thing")
else:
    print("It's no thing")


thing = None
if thing is None:
    print("nothing")
else:
    print("something")


def whatis(thing):
    if thing is None:
        print(thing, "is None")
    elif thing:
        print(thing, "is True")
    else:
        print(thing, "is False")


# 위치 인수: 함수에 인수를 순서대로 넣는 방식
# 순서가 달라지면 잘못된 결과
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}
print(menu('chardonnay', 'chicken', 'cake'))

# 키워드 인수
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}
print(menu(entree='beef', dessert='bagel', wine='bordeaux'))

# 위치인수와 키워드인수를 섞어서 쓰면, 위치인수가 먼저 온다
def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}
print(menu('frontenac', dessert='flan', entree='fish'))

# 기본 매개변수 값 지정하기
# def menu(wine, entree, dessert='pudding'):
#     return {'wine':
#             }



def buggy(arg, result=[]):
    result.append(arg)
    print(result)
buggy('a')
buggy('b')


def works(arg):
    result = []
    result.append(arg)
    return result
print(works('a'))
print(works('b'))


# 위치 인수 분해하기/모으기
# 애스터리스크 *은 매개변수에서 위치 인수를 튜플로 묶는다
# 매개변수 개수가 확실하지 않을 때
# args는 argument
def print_args(*args):
    print('positional tuple:', args)

print_args()
print_args(3, 2, 1, 'wait!', 'uh...')




# list
# def calculate_fee(*args):  # error
def calculate_fee(args):
# def calculate_fee(args): -> list  // 라고 명시해도 됨
    '''
    놀이공원 요금 계산 프로그램
    :param args: ages in list
    :return: [전체 인원수, 어른수, 아이수, 총 입장료]
    '''
    total = 0
    adults = 0
    kids = 0
    for age in args:
        if 19 <= age:  # adult
            total += 10000
            adults += 1
        else:
            total += 3000
            kids += 1
    return [len(args), adults, kids, total]

import random
visitors = int(input('총 인원수: '))
age_visitors = [random.randint(1, 60) for age in range(0, visitors)]
results = calculate_fee(age_visitors)

print(f"{visitors}명 방문하였고, 어른수는 {results[1]}, 아이수는 {results[2]}명, 총요금은 {results[3]}입니다.")


# dictionary -> 키값이 중복되지 않을 때 사용
def calculate_fee(kwargs):
    # document string
    '''
    놀이공원 요금 계산 프로그램
    :param kwargs: ages in list
    :return: {'no_of_people':전체 인원수, 'no_of_adults':어른수, 'no_of_kids':아이수, 'fee':총 입장료}
    '''
    total = 0
    adults = 0
    kids = 0
    for age in kwargs:
        if 19 <= age:  # adult
            total += 10000
            adults += 1
        else:
            total += 3000
            kids += 1
    return {'no_of_people':len(kwargs), 'no_of_adults':adults, 'no_of_kids':kids, 'fee':total}

import random
visitors = int(input('총 인원수: '))
age_visitors = {random.randint(1, 60) for age in range(0, visitors)}
results = calculate_fee(age_visitors)

print(f"{results['no_of_people']}명 방문하였고, 어른수는 {results['no_of_adults']}, 아이수는 {results['no_of_kids']}명, 총요금은 {results['fee']}입니다.")




# print(calculate_fee(20, 20, 25))
# print(calculate_fee(45, 43, 10, 7))


# 키워드 인수를 딕셔너리로 묶기
# **
def print_kwargs(**kwargs):
    print('keyword arguments:', kwargs)




def print_data(data, *, start=0, end=100):
    for value in (data[start:end]):
        print(value)
data = ['a', 'b', 'c', 'd', 'e', 'f']
print_data(data)


# 함수는 변수, 인수, 반환 전부 가능
def answer():
    '''
    숫자 출력
    :return:
    '''
    print(42)
def run_something(func):
    '''
    매개변수로 함수를 넘겨받아 실행
    :param func: 매개변수가 함수
    :return:
    '''
    func()
run_something(answer)
print(type(run_something))




def add_args(arg1, arg2):
    print(arg1+arg2)
def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)
run_something_with_args(add_args, 5, 9)



# 내부함수
def outer(a, b):
    def inner(c, d):
        return c+d
    return inner(a, b)
print(outer(4, 7))


# 고차함수
# 이너함수는 클로저처럼 동작가능
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s" % saying
    return inner2
a = knights2('Duck')  # string이 아니라 함수
b = knights2('feffer')
print(a)
print(b)
print(a())
print(b())


# Closures
def calculate():
    x = 1
    y = 2
    temp = 0
    def add_sub(n):  # 외부 변수의 값을 기억하고 있다
        nonlocal temp  # 지역변수가 아니다 // 변경 가능
        # x = 11  # local variable
        temp = temp + x + n - y
        return temp
    return add_sub
c1 = calculate()
for i in range(5):
    print(c1(i))  # calculate는 한번만 돌아


# 익명 함수 lambda // 일회성 함수
# 임의의 수 제곱하는 값을 출력하는 코드
import random
def squares(num):
    '''
    제곱함수
    :param num: integer
    :return: integer
    '''
    return num * num

def process(no_lists, f):  # 첫번째는 리스트, 두번째는 함수를 변수로 받아
    for no in no_lists:
        print(f(no))

numbers = [random.randint(1, 100) for i in range(5)]
print(numbers)
process(numbers, squares)

# 위를 람다함수로 // 일회용
import random

def process(no_lists, f):  # 첫번째는 리스트, 두번째는 함수를 변수로 받아
    for no in no_lists:
        print(f(no))

numbers = [random.randint(1, 100) for i in range(5)]
print(numbers)
process(numbers, lambda x: x * x)

