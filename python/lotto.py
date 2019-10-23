import requests

n = input('회차를 입력하세요: ')

url = f'https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={n}'
response = requests.get(url)
# response.text #=> string
lotto = response.json() #=> dict

# winner = []
# for i in range(1, 7):
#     winner.append(lotto[f'drwtNo{i}'])

winner = [lotto[f'drwtNo{i}'] for i in range(1, 7)]

bonus = lotto['bnusNo']

print(f'당첨 번호는 {winner} + {bonus}입니다.')