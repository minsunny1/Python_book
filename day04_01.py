# 구구단 거꾸로
number = int(input("단을 입력하세요: "))
i_list = []
for i in range(1, 10):
    i_list.append(i)

i_list2 = i_list[::-1]
for num in range(0, 9):
    print(f'{number} * {i_list2[num]} = {number * i_list2[num]}')



