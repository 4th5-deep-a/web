from flask import Flask, escape, request, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'

@app.route('/mulcam')
def mulcam():
    return 'This is mulcam!!!!!!!'

# Path Variable / Variable Routing
@app.route('/greeting/<string:name>')
def greeting(name):
    return f'Hi, {name}' # 'Hi, {}'.format(name)

@app.route('/cube/<int:num>')
def cube(num):
    result = num ** 3
    return f'{num}의 세제곱은 {result}입니다.'

import random
# 사람 수를 route를 통해 받아, 사람 수 만큼 메뉴 추천
@app.route('/dinner/<int:person>')
def dinner(person):
    menu = ['치킨','피자','돈까스','초밥','국밥']
    result = random.sample(menu, person) 
    # ['치킨', '피자']
    return ','.join(result) #=> '치킨,피자'


@app.route('/html')
def html():
    multiline = """
        <h1>Hi, Hello</h1>
        <p>만나서 반갑습니다!</p>
    """
    return multiline

@app.route('/html_file')
def html_file():
    return render_template('file.html')

# Template Variable
@app.route('/hi/<string:name>')
def hi(name):
    # ...
    return render_template('hi.html', your_name=name)

@app.route('/list')
def list():
    menu = ['치킨','피자','돈까스','초밥','국밥']
    return render_template('list.html', menu=menu)


# def a(one, two, three):
#     return one, two, three

# a(1,three=2,two=3)






if __name__ == '__main__':
    app.run(debug=True)
