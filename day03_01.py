# 6.1
# count = 1
# while count <= 5:
#     print(count)
#     count += 1
#
# # 6.1.1
# while True:
#     stuff = input("String to capitalize[type q to quit]: ")
#     if stuff == 'q':
#         break
#     else:
#         print(stuff.capitalize())
#
# while True:
#     stuff = input("String to capitalize[type q to quit]: ")
#     if stuff == 'q':
#         break
#     print(stuff.capitalize()) # break가 끝나도 수행

# 6.1.2
# 정수가 홀수이면 제곱을 출력, 짝수면 다음 반복으로 건너뜀, q 입력하면 종료
# while True:
#     value = input("정수를 입력[type q to quit]: ")
#     if value == 'q':
#         break
#
#     number = int(value)
#     if number % 2 == 1:
#         print(number * number)
#         # print(number, 'squared is', number*number)
#         break
#     else:
#         continue

# 6.1.3
# numbers = [1, 3, 5]
# position = 0
# while position < len(numbers):
#     number = numbers[position]
#     if number % 2 == 0:
#         print('found even number', number)
#         break
#     position += 1
# else:
#     print('no even number found')