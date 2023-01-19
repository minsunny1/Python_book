# tuple -> ,로 연결되거나 비거나
# tuple은 수정이 안됨 -> 수정하려면 튜플을 리스트로 형변환
a = 'harry',
b = ('harry',)
c = ()  # empty tuple
d = 'harry', 'ron'  # packing
e = ('harry')  # str
f = ('harry', 'ron')  # packing
print(f[1])
x, y = f  # unpacking
print(x, y)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

password = 'swordfish'
icecream = 'tutti'
password, icecream = icecream, password  # tuple unpacking
print(password)
print(icecream)


# 튜플로 형변환
marx_list = ['groucho', 'chico', 'harpo']
print(tuple(marx_list))


# 결합하기
print(('groucho',) + ('chico', 'harpo'))

# 복제하기
print(('yada',) * 3)

# 순회하기
words = ('fresh', 'out', 'of', 'ideas')
for word in words:
    print(word)

# 수정하기
# 결합해서 새튜플을 만들 수 있음
t1 = ('fee', 'fie', 'foe')
t2 = ('flop',)
print(t1 + t2)
print(id(t1))
t1 += t2
print(t1)
print(id(t1))  # id값도 달라짐


# 리스트
empty_list = []
ramdomness = ['lemon', {'groundhog' : 'phi'}, 'Deb. 2']
first_names = ['jenny', 'rohi', 'slkj', 'jenny']  # 리스트는 고유한 값이 아니어도 됨

print(list('cat'))

# 튜플을 형변환
tuple_ = ('kim', 'min', 'sun')
print(list(tuple_))

# 튜플의 값을 변경하려면 리스트로 형변환을 하면 된다
scores = ('B+', 'A+', 'C+')
print(scores[1], scores[2])
temp = list(scores)
temp[1] = 'C+'
temp[2] = 'A+'
scores = tuple(temp)
print(scores[1], scores[2])
# scores[1] = 'C+' // error // 튜플은 값을 대입할 수 없음


# split()
# 문자열을 특정 문자 단위로 분할하여 리스트를 생성
day = '8/19/2019'
print(day.split('/'))

# 슬라이스 : 원소를 잘라내서 추출
# [start:end]
bigbang = ['gd', '태양', '대성', '탑', '승리']
print(bigbang[0])
print(bigbang[:])
print(bigbang[2:])
print(bigbang[2:4])
print(bigbang[::2])
print(bigbang[::-2])
print(bigbang[::-1])
print(bigbang[-1::])

bigbang.reverse()
print(bigbang)

# 항목을 추가하는 append(), insert()
bigbang = ['gd', '태양', '대성', '탑', '승리']
exo = ['백현', '수호']
bigbang.append('인하')  # 뒤에 삽입
print(bigbang)
bigbang.insert(1, '인하')  # 1 위치에 삽입
print(bigbang * 3)  # 복제

# 병합하기 extend()
bigbang.extend(exo)
print(bigbang)
exo.extend(bigbang)
print(exo)

bigbang = ['gd', '태양', '대성', '탑', '승리']
exo = ['백현', '수호']
exo = exo + bigbang
print(exo)


bigbang = ['gd', '태양', '대성', '탑', '승리']
exo = ['백현', '수호']
exo.append(bigbang)  # 1번방 exo 리스트 안에 2번방 bigbang 리트스
print(exo)
print(exo[2][1])  # 태양 // 특정 항목 추출
print(exo[-1][-4])

exo[-2] = '시우민'  # 수호자리에 시우민으로 변경
print(exo)

# 특정 항목 삭제
# print(exo.pop())  # 빅뱅 pop
# print(exo[2].pop())  # 승리 pop
# print(exo)
#
# print(exo[2].pop(-2))  # 승리 pop
# print(exo)  # 탑 pop
#
# del exo[2][-2]
# print(exo)  # 대성 delete
#
# exo.remove('인하') # not in exo
# exo[2].remove('인하')
# print(exo)
# exo.clear()
# print(exo)


primes = [2, 12, 5.0, 5, 7, 11]
print(primes)
primes.sort()
print(primes)

# mixed = [6, 4, 5, 'A', '트와이스', 'B', 'c', '마마무']
# mixed.sort()
# TypeError: '<' not supported between instances of 'str' and 'int'

mixed = ['6', '4', '5', 'A', '트와이스', 'B', 'c', '마마무']
mixed.sort()
print(mixed)

mixed.sort(reverse = True)
print(mixed)

primes = [2, 12, 5.0, 5, 7, 11]
primes_cp = primes
print(primes)
print(primes_cp)
primes[-1] = 'lunch time'
print(primes)
print(primes_cp)
primes_cp[0] ='morning coffee'
print(primes)
print(primes_cp)


# 복제
# imutable은 완전한 copy 안됨
a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]
a[2] = 'sw'
print(a, b, c, d)


import copy
a = [1, 2, [5, -9]]  # deep copy // mutable한 타입은 copy시에 전부 다 바뀜
b = copy.deepcopy(a)
b2 = a.copy()
c = list(a)
d = a[:]
a[1] = -77
a[2][1] = 7  # mutable, deepcopy
print(a, b, b2, c, d)

# days = ['monday', 'tuesday', 'wednesday']
# fruits = ['banana', 'orange', 'peach']
# drinks = ['coffee', 'tea', 'beer']
# desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
# for day, fruit, drink, dessert in (days, fruits, drinks, desserts):
#     print(day, ": drink", drink, "-eat", "")


number_list = []
for number in range(1, 6):
    number_list.append(number)
print(number_list)

number_list = [number for number in range(1,6)]
print(number_list)

a_list=[number for number in (1, 6) if number%2 ==1]
print(a_list)

rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print(row, col)


# list comprehension
# odd_list = []
# for i in range(1, 11):
#     if i % 2 == 1:
#         odd_list.append(i)
# print(odd_list)
odd_lists = [i for i in range(1, 11) if i % 2 == 1]
odd_tuples = (i for i in range(1, 11) if i % 2 == 1)  # 튜플은 컴프리헨션이 없다
print(odd_lists)
print(odd_tuples)  # generator는 메모리 공간을 버리지 않는다


# 딕셔너리
students = {'name': 'kiminha', 'age': '23', 'eyes': [0.9, 1.1]}
#for k in students:
#for k in students.keys():
#for k in students.values():
for k, v in students.items():
    # print(k)
    print(f'{k} : {v}')
print(f"이름은 {students['name']}, 나이는 {students['age']}세", end=' ')
print(f"시력은 좌: {students['eyes'][0]}, 우: {students['eyes'][1]}")


# # 술안주 추천 프로그램
# import random
# alcohol_foods = {
#     '맥주': '치킨',
#     '소주': '골뱅이소면',
#     '와인': '치즈',
#     '고량주': '짬뽕'
# }
# alcohol_list = list(alcohol_foods)  # keys만 추출
# while True:
#     alcohol = input(f'술을 선택하세요. 1) {alcohol_list[0]} 2) {alcohol_list[1]} 3) {alcohol_list[2]} 4) {alcohol_list[3]} 5) 계산: ')
#     print(alcohol)
#     if alcohol == '5':
#         print('다음에 또 오세요')
#         break
#     elif alcohol == '1':
#         print(f'{alcohol_list[0]}에 어울리는 안주는 {alcohol_foods[alcohol_list[0]]}입니다.')
#     elif alcohol == '2':
#         print(f'{alcohol_list[1]}에 어울리는 안주는 {alcohol_foods[alcohol_list[1]]}입니다.')
#     elif alcohol == '3':
#         print(f'{alcohol_list[2]}에 어울리는 안주는 {alcohol_foods[alcohol_list[2]]}입니다.')
#     elif alcohol == '4':
#         print(f'{alcohol_list[3]}에 어울리는 안주는 {alcohol_foods[alcohol_list[3]]}입니다.')
#     elif alcohol == '아무거나':
#         ran = alcohol_list[random.randint(0, 3)]
#         print(f'추천하는 술은 {ran}')
#         print(f'추천하는 안주는 {alcohol_foods[ran]}')
#     else:
#         print('메뉴에서 골라주세요.')
#
#
# 술안주 추천 프로그램
import random
alcohol_foods = {
    '맥주': '치킨',
    '소주': '골뱅이소면',
    '와인': '치즈',
    '고량주': '짬뽕'
}
alcohol_list = list(alcohol_foods)  # keys만 추출
food_list = [food for food in alcohol_foods.values()]
# print(alcohol_list, food_list)

# for i in range(len(food_list)):
#     print(food_list[i])

#for food in food_list:
#print(food)

for food in enumerate(food_list):  # tuple return
    print(food[1])

while True:
    alcohol = input(f'술을 선택하세요. 1) {alcohol_list[0]} 2) {alcohol_list[1]} 3) {alcohol_list[2]} 4) {alcohol_list[3]} 5) 아무거나 6) 계산: ')
    # print(alcohol)
    if alcohol == '6':
        print('다음에 또 오세요')
        break
    elif alcohol == '1':
        print(f'{alcohol_list[0]}에 어울리는 안주는 {alcohol_foods[alcohol_list[0]]}입니다.')
    elif alcohol == '2':
        print(f'{alcohol_list[1]}에 어울리는 안주는 {alcohol_foods[alcohol_list[1]]}입니다.')
    elif alcohol == '3':
        print(f'{alcohol_list[2]}에 어울리는 안주는 {alcohol_foods[alcohol_list[2]]}입니다.')
    elif alcohol == '4':
        print(f'{alcohol_list[3]}에 어울리는 안주는 {alcohol_foods[alcohol_list[3]]}입니다.')
    elif alcohol == '5':
        print(f'{random.choice(alcohol_list)}에 어울리는 안주는 {random.choice(food_list)}입니다.')
    else:
        print('메뉴에서 골라주세요.')


# # list -> dict 변환하기
# lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
# print(dict(lol))
#
# first = {'a': 'agony', 'b': 'bliss'}
# second = {'b': 'bagels', 'c': 'candy'}
# print({**first, **second})
#
# # 딕셔너리는 컴프레헨서가 있음
# word = 'letters'
# letters = {letter: word.count(letter) for letter in set(word):
# {}


