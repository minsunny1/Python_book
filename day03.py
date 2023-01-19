print("I'm a boy")
print('''Boom''')
print("""Eek!""")

print('''여러줄을 쓰기 위해
따옴표를 3개를 사용한다.
트리플 홑따옴표''')

print('우리는 국가와 국민에 충성을 다하는 대한민국 육군이다.'
      '이렇게하면 에러가 안날까?')

print('우리는 국가와 국민에 충성을 다하는 대한민국 육군이다.\n 이렇게하면 에러가 안날까?')

print('우리는 국가와 국민에 충성을 다하는 대한민국 육군이다.\t 이렇게하면 에러가 안날까?')

print(str(98.6))
print(str(True))

# 문자열에서 \' 또는 \"를 사용하면 따옴표를 그대로 표현할 수 있다.
print('\" I did not nothing!\"')
print('The backslash \\ bends over backwards to please you.')

start = 'Na ' * 4 + '\n'
middle = 'hey ' * 3 + '\n'
end = 'goodbye.'
print(start + start + middle + end)

# 문자열에서 한 문자를 얻기 위해 문자열 이름 뒤에 대괄호와 오프셋을 지정한다.
# 가장 왼쪽의 오프셋은 0이고 가장 오른쪽의 오프셋은 -1이다.
letters = 'abcdefg'
print(letters[0])
# print(letters[10]) -> 오프셋을 문자열의 길이을 넘어가게 지정하면 에러

# 문자열은 불변함. 변경하고 싶으면 replace() 함수나 슬라이스를 사용해야한다
name = 'Henny'
name.replace('H', 'P')
print(name)
print(name.replace('H', 'P'))
print('P' + name[1:]) # P + name의 1번부터 끝까지

#슬라이스로 부분 문자열 추출
univ = 'Inha University' # 0~14글자
print(univ[:])
print(univ[5:])
print(univ[5:14])
print(univ[5:15])
print(univ[5:-6])
print(univ[-10:])
print(univ[5:15:2]) # univ[start:end:step]
print(univ[::2]) # 스텝(폭)을 이용하여 건더가면서 출력
print(univ[-10:-6])
print(univ[6::2])
print(univ[:15:2])
print(univ[-1::-1])
print(univ[::-1])
print(univ[:70])

#문자열의 길이 len()함수
print(len(univ))

# 문자열을 나누는 split() 함수
print(univ.split())
print(univ.split(', '))

# 문자열을 결합하는 join() 함수
poketmons_list = ['피카츄', '꼬부기', '이상해', '파이리']
poketmons_string = ', '.join(poketmons_list)
print(poketmons_string)

# 문자열을 대체하는 replace() 함수
setup = 'a duck goes into a bar...'
print(setup.replace('duck', 'marmoset'))
print(setup)
print(setup.replace('a', 'a famous', 100)) # 100회까지 a를 a famous로 대체
print(setup.replace('a', 'a famous', 1))

# 문자열 삭제 strip() 함수
# 왼쪽을 제거하고 싶으면 lstrip(), 오른쪽 제거하고 싶으면 rstrip()
word = "   python, database, data structure    "
print(word.strip())
print(word.lstrip())
print(word.rstrip())
print(word.strip('!'))

word2 = "   $  python, database, data structure    "
print(word2.strip('$'))

word3 = "What the ...!!?"
print(word3.strip('.!?'))
print(word3.strip('.?!'))

# ~로 시작하는지 물어보는 startswith()
print(word3.startswith('What'))
# ~로 끝나는지 물어보는 endswith()
print(word3.endswith('?'))

# 문자열 검색하는 find()
subjects = "   python, database, data structure    "
print(subjects.find('data'), subjects.index('data'))
print(subjects.find('inha')) # find는 문자열이 없을 때 -1을 출력
# print(subjects.index('inha')) # index는 문자열이 없을 때 에러

print(subjects.rfind('data')) # 문자열 끝에서 찾아
print(subjects.index('data'))

print(subjects.count('data'))
print(subjects.isalnum()) # 문자열이 모두 알파벳 또는 숫자로 이루어져 있는가

# 대소문자
print(subjects.title()) # 모든 글자의 첫번째를 대문자로

print('앞글자가 m인 단어의 m을 대문자로 바꾸자')
song = '''song = When an eel grabs your arm,
And it causes great harm,
That's - a moray!'''
idx = song.rfind('m')
print(idx)
song = song.replace(song[idx], song[idx].upper())
#print(idx, song[idx.upper()])

song_list = song.split()
print(song_list)
print(len(song_list))
song_list[14] = song_list[14].title()
song_string = ' '.join(song_list)
print(song_string)

#print(song.replace(idx, 'M'))
print(song)

# 포매팅
print('%s' % 42)
print('%d%%' % 100)

thing = 'wraith'
place = 'window'
print('The {} is the []'.format(thing, place))

# 5.3
print("My kitty cat likes %s" % ('roast beef'))

# while문
# while True:
#     dan = int(input('Dan: '))
#     if 1 < dan < 10:
#         i = 1
#         while i < 10:
#             print(f'{dan} * {i} = {dan * i}')
#             print('{0} * {1} = {2}'.format(dan, i, dan*i))
#             i += 1
#         break
#     else:
#         print('2~9 사이의 값을 입력하세요.')

# do {
#     dan = int(input('Dan: '))
# } while(dan < 1 || dan > 10);

# while True:
#     dan = int(input('Dan (0 to quit): '))
#     if dan == 0:
#         break
#     if 1 < dan < 10:
#         i = 1
#         while i < 10:
#             print(f'{dan} * {i} = {dan * i}')
#             i += 1
#     else:
#         print('2~9 사이의 값을 입력하세요.')

# while True:
#     dan = int(input('Dan (0 to quit): '))
#     if dan == 0:
#         break
#     if 1 < dan < 10:
#         for i in range(1, 10):
#             print(f'{dan} * {i} = {dan * i}')
#     else:
#         print('2~9 사이의 값을 입력하세요.')



# 이해 안됨
numbers = [1, 3, 5]
position = 0
print(len(numbers))
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('found even number', number)
        break
    position += 1
else:
    print('no even number found')



word = "thud"
for letter in word:
    if letter == 'u':
        break
    print(letter)

for i in range(2, -1, -1):
    print(i)

# 소수인지 아닌지 판별 (prime number)
# 1과 자신만 나눴을 때만 나머지가 0
# while
# number = int(input("정수 입력: "))
# counts = 0
#
# k = 1
# while k <= number:
#     if number % k == 0:
#         counts += 1
#     k += 1
# if counts == 2:
#     print(f'{number} is prime number!')
# else:
#     print(f'{number} is not prime number.')
#
# # for
# number = int(input('정수입력: '))
# counts = 0
#
# for k in range(1, number + 1):
#     if number % k == 0:
#         counts += 1
# if counts == 2:
#     print(f'{number} is prime number!')
# else:
#     print(f'{number} is not prime number.')
#
# # for
# number = int(input('정수입력: '))
# counts = 0
#
# for k in range(2, number): # 1과 자기자신이 아닐때
#     if number % k == 0:
#         counts += 1
# if counts:
#     print(f'{number} is not prime number.')
# else:
#     print(f'{number} is prime number.')

# for
number = int(input('정수입력: '))
is_prime = True

for k in range(2, number):
    if number % k == 0:
        is_prime = False
        break
    print(k) # 약수가 나오면 결과가 이미 결정된건데, break 없으면 의미없이 나머지 코드가 계속 돌아감.
if is_prime:
    print(f'{number} is prime number.')
else:
    print(f'{number} is not prime number.')


# 숫자 2개 입력하고, 그 범위 내에 소수만 가로로 출력되게
num1 = int(input("num1: "))
num2 = int(input("num2: "))
print(num1, num2)
is_Prime = True

for i in range(num1, num2+1):
    # is_Prime = True


    for k in range(2, i):
        if i % k == 0:
            is_Prime = False
            break
    else:
        print(i, end=' 5')


# start_end = int(input("start and end number: ")).split() # int로 타입 변환
# print(start_end)
# print(start_end[0], start_end[1])


# 6.1
for k in [3, 2, 1, 0]:
    print(k)








