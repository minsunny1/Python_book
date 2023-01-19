def sub_int(x, y):
    return x-y

def do_info(func):
    def new(*args, **kwargs):
        print('실행 함수: ', func.__name__)
        print('위치변수:', args)
        print('키워드 변수:', kwargs)
        result = func(*args, **kwargs)
        print('실행결과:', result)
        return result
    return new

info_sub_int = do_info(sub_int)
info_sub_int(7, 3)




def func():
    print('원본 함수이다')

# 함수 시작과 끝에 문장을 추가하는 데커레이터
def test(func):
    def new_function(*args, **kwargs):
        print('start!')
        result = func(*args, **kwargs)
        print('end')
        return result
    return new_function

test(func)()