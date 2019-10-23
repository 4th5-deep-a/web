"""
https://gist.github.com/nwith > dictionary.py

난이도* 1. 지역(location)은 몇개 있나요? : list length
출력 예시)
2

난이도** 2. python standard library에 'requests'가 있나요? : 접근 및 list in
출력 예시)
false

난이도*** 3. mulcam에서 배우는 언어들을 출력하세요. : dictionary.keys() 반복
출력 예시)
python
web

난이도*** 4. mulcam 블록체인반의 강사와 매니저의 이름을 출력하세요. dictionary.values() 반복
출력 예시)
bing
문정연

난이도***** 5. framework들의 이름과 설명을 다음과 같이 출력하세요. : dictionary 반복 및 string interpolation
출력 예시)
flask는 micro이다.
django는 full-functioning이다.

난이도***** 6. 오늘 당번을 뽑기 위해 groups의 1조 중에 한명을 랜덤으로 뽑아주세요. : depth 있는 접근 + list 가지고 와서 random.
출력예시)
오늘의 당번은 한대건
"""

mulcam = {
    "location": ["역삼","선릉"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scraping": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "딥러닝":  {
            "lecturer": "junwoo",
            "manager": "민채원",
            "groups": {
                "1조": ["윤선재", "이정서", "한대건", "문금란", "이진호"],
                "2조": ["유승우", "이효정", "임채명", "박병규"],
                "3조": ["김지현", "박희현", "강강토"],
            }
        },
        "블록체인": {
            "lecturer": "bing",
            "manager": "문정연"
        }
    }
}

# 1.
print(len(mulcam.get('location'))) #=> 2

# 2.
print('requests' in mulcam.get('language').get('python').get('python standard library')) #=> [...]

# 3. 
for key in mulcam.get('language').keys(): #=> [key, key]
    print(key)

# 4.
for value in mulcam.get('classes').get('블록체인').values(): #=> [value, value]
    print(value)

# 5.
for key, value in mulcam.get('language').get('python').get('frameworks').items(): #=> [(key, value), (key, value)]
    print(f'{key}는 {value}이다.')

# 6.
import random
members = mulcam.get('classes').get('딥러닝').get('groups').get('1조') #=> [...]
result = random.choice(members)
print(result)