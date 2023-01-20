# 포켓몬 프로그램
class Pokemon:
    def __init__(self, owner, skills):
        self.owner = owner
        self.skills = skills.split('/')
        print(f"포켓몬 생성:", end=' ')

    def info(self):
        print(f'{self.owner}의 포켓몬이 가진 스킬')
        for skill in self.skills:
            print(skill)
        for i in range(len(self.skills)):
            print(f'{i+1} : {self.skills[i]}')
        # for skill in self.skills:
        #     print(f'{skill}')

    def attack(self, idx):
        print(f'{self.skills[idx]} 공격 시전!')



class Pikachu(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)  # 부모의 생성자를 호출
        self.name = "피카추"
        print(f'{self.name}')

    def attack(self, idx):  # override
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전')


class Ggoboogi(Pokemon):  # inheritance
    def __init__(self, owner, skills):
        super().__init__(owner, skills)  # super() 부모의 생성자를 호출
        self.name = "꼬부기"
        print(f'{self.name}')

    def attack(self, idx):
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전')

    def swim(self):
        print(f'{self.name}가 수영을 합니다.')


class Pairi(Pokemon):
    def __init__(self, owner, skills):
        super().__init__(owner, skills)  # super() 부모의 생성자를 호출
        self.name = "파이리"
        print(f'{self.name}')

    def attack(self, idx):  # override
        print(f'{self.owner}의 {self.name}가 {self.skills[idx]} 공격 시전')

while True:
    menu = input('1) 포켓몬 생성  2) 프로그램 종료: ')
    if menu == '2':
        print('프로그램 종료')
        break
    elif menu == '1':
        poketmon = input('1) 피카추  2) 꼬부기  3) 파이리: ')
        if poketmon == '1':
            n = input('플레이어 이름 입력: ')
            s = input('사용 가능한 기술 입력(/로 구분하여 입력): ')
            p = Pikachu(n, s)
        elif poketmon == '2':
            n = input('플레이어 이름 입력: ')
            s = input('사용 가능한 기술 입력(/로 구분하여 입력): ')
            p = Ggoboogi(n, s)
        elif poketmon == '3':
            n = input('플레이어 이름 입력: ')
            s = input('사용 가능한 기술 입력(/로 구분하여 입력): ')
            p = Pairi(n, s)
        else:
            print('메뉴에서 골라주세요')
        info_attack = input('1) 정보조회  2) 공격: ')
        if info_attack == 1:
            p.info()
        elif info_attack == 2:
            p.info()
            attack_menu = input('공격 번호 선택: ')
            p.attack(int(attack_menu) - 1)
        else:
            print('메뉴에서 골라주세요')
    else:
        print('메뉴에서 골라주세요.')