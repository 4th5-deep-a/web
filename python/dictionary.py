lunch = {
    '중국집': '양자강',
    '한식집': '시래기', # trailing comma
}
# lunch = dict(중국집='양자강')
lunch['분식집'] = '김밥카페'
lunch['중국집'] #=> '양자강'

dinner = {
    '한식집': { # string, interger, float, boolean
        '고갯마루': '02-3476-7006',
        '순남시래기': '02-1234-1234',
    }
}

dinner['한식집']['고갯마루'] #=> 02-...
dinner.get('한식집').get('고갯마루')

# 기본 활용
for key in lunch:
    print(key)
    print(lunch.get(key))

# key 가져오기
for key in lunch.keys(): # [key, key, ...]
    print(key)

# value 가져오기
for value in lunch.values(): # [value, value, ...]
    print(value)

# key, value 가져오기
for key, value in lunch.items(): # [(key, value), (key, value), ...]
    print(key)
    print(value)