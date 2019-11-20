from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return """<h1>Hello!</h1>
    <a href="/about">О сайте</a><a href="/test">Рыбный тест</a>
    """

@app.route('/about')
def about():
    A = random.randint(1, 10)
    return render_template('about.html', number=A)

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/answer')
def answer():
    name = request.args.get('name', '')
    age = int(request.args.get('age', 0))

    if len(name) < 6 and age < 20:
        return "<h1>Лещ</h1>"
    elif len(name) > 6 and age < 20:
        return "<h1>Форель</h1>"
    elif len(name) < 6 and age > 20:
        return """
        <h1>Язь!!!!</h1>
        <iframe width="560" height="315" src="https://www.youtube.com/embed/TY1ymotP0P0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
        """
    else:
        return "<h1>Вы - не рыба, вы - мясо</h1>"
# http://127.0.0.1:5000/answer?name=%D0%A0%D0%BE%D1%81%D1%82%D0%B8%D1%81%D0%BB%D0%B0%D0%B2&age=25

app.run(debug=True)