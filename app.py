

from flask import Flask, render_template


app = Flask(__name__)
guesses = ['Python', 'Java', 'C++']
questions = ['Is it compiled?', 'Does it run a VM?']


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/guess/<int:id>')
def guess(id):
    return render_template('guess.html', guess=guesses[id])


@app.route('/question/<int:id>')
def question(id):
    return render_template('question.html', question=questions[id])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
