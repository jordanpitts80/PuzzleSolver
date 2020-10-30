import re
import itertools
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    

@app.route('/solve', methods=['POST'])
def solve():
    if request.method == 'POST':

        crypt = request.form['nm']


        regex = r'\w+'
        words = re.findall(regex,crypt)
        char = set(''.join(words))
        firstlet = set()
        for w in words:
            firstlet.add(w[0])
        n = len(firstlet)
        sort = ""
        sort = sort.join(firstlet) + sort.join(char - firstlet)
        characters = tuple()
        digits = tuple()
        for c in sort:
            charnum = ord(c)
            characters = characters + (charnum,)
        for d in '0123456789':
            num = ord(d)
            digits = digits + (num,)
        zero = digits[0]
        for perm in itertools.permutations(digits, len(characters)):
            if zero not in perm[:n]:
                equation = crypt.translate(dict(zip(characters, perm)))
                if eval(equation):
                    result = equation
                    return render_template('index.html', result=result)
    else:
        return render_template('index.html')
        

if __name__ == "__main__":
    app.debug = True
    app.run()

