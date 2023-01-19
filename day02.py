# list mutable
math_values = (3.14, 2.71)
math_values = [3.14, 2.71]
print(f'원주율의 값은 {math_values[0]}이고 타입은 {type(math_values)}입니다.')
math_values[0] = 9.99
print(f'원주율의 값은 {math_values[0]}이고 타입은 {type(math_values)}입니다.')

y=13
x=y
print(x)

print(isinstance(x, int))
print(isinstance(x, bool))
x=[]
print(isinstance(x, list))

# ch3
print(2*2*2*2)
print(2**4)
print(pow(2, 4))
print(5 % 2)
print(5 // 2)
print(5 / 2)

# tuple
print(divmod(9, 5))
print(type(divmod(9, 5)))
print(type(1, 2))

test = 1, 2 # packing
print(type(test))
print(test)
print(test[1])
a, b = test # unpacking
print(a)
print(b)

# 진법
number = 0b10011010 # 2진수
print(number)
number2 = 0x9A # 8진수, 4bit씩 끊어서 계산
print(number2)
number3 = 0o232 # 16진수, 3bit씩 끊어서 계산
print(number3)

value = 154
print(bin(value))
print(oct(value))
print(hex(value))

# ASCII code
# 정수를 단일 문자열로
print(chr(65))

# 단일 문자열을 정수로
print(ord(" ")) # 10진수, sp에 대한 ascii code 값
print(hex(ord(" ")))

# type 변환
int(99)
int('99')
# int('99 bottles of beer on the wall')
int()

sum = 1+\
    2+\
    3+\
    4
print(sum)

disaster = True
if disaster:
    print("woe")
else:
    print("whee")

color = "red"
if color == "yellow":
    print("It's a banana")
else:
    print("color is ", color)
#논리연산자: and, or

# 비트 연산자
# x=7
# print(5<x & x<10)
# print(5<x | x<10)

# Ch4
print(bool([]))
print(bool(set()))
print(bool(dict()))

a = []
print(bool(a))
a.append((5))

vowels = 'aeiou'
letter = 'x'
if letter in vowels:
    print("실행 안됨")
else: print("없음")

vowels = 'aeiou'
letter = 'x'
if letter not in vowels:
    print("실행 안됨")

# 곱셈만 string과 연산이 가능
limits = 20
tweets = "pass" * 7
diff = limits - len(tweets)
if diff >= 0:
    print(tweets)
else:
    print(f'제한 글자 수 {abs(diff)} 초과')

#random 함수
import random
limits = 20
tweets = "pass" * random.randint(1,10) # 1~10사이의 난수
diff = limits - len(tweets)
if diff >= 0:
    print(tweets)
else:
    print(f'글자수 {abs(diff)} 초과')

# 과제
import random
