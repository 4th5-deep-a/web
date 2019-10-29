class Person(): # 클래스 (집단)
    name = '사람의 고유한 속성' # 멤버 변수 (속성)
    age = '출생 이후부터 삶을 마감할 때까지의 기간'

    def greeting(self): # 멤버 메서드 (행동)
        print(f'{self.name}이 인사합니다. 안녕하세요.')

    def eating(self):
        print(f'{self.name}은 밥을 먹고 있습니다.')

junwoo = Person() # 인스턴스 생성
print(junwoo.name)
print(junwoo.age)
junwoo.name = 'junwoo'
junwoo.age = '50'
print(junwoo.name)
print(junwoo.age)
print(Person.name)
print(Person.age)
junwoo.greeting()
