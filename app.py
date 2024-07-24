from flask import Flask, render_template, request
from waitress import serve
from werkzeug.security import generate_password_hash

import uuid
import hashlib
import random

app = Flask(__name__)

symbols = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=','[',']','{','}','|',':',';','\'','\"',',','<','>','.','/','?','`','~']

@app.route('/', methods = ['GET','POST'])
def home():
    if request.method == 'POST':
        e = ''
        if 'code' in request.form:
            e = hash(request.form['code'])
        else:
            e = hash()
        e = add_symbols(e)
        return render_template('index.html', e = e)
    return render_template('index.html')

def hash(code = uuid.uuid4().hex) -> str:
    seed = generate_password_hash(code)
    sha256 = hashlib.sha256()
    sha256.update(seed.encode('utf-8'))
    return sha256.hexdigest()

def add_symbols(text: str):
    for i in range(20):
        rand = random.randrange(0,len(symbols)-1)
        char = symbols[rand]
        index = random.randrange(0,len(text)-1)
        text = text[:index] + char + text[index:]
    return text

if __name__ == "__main__":
    serve(app, host = '0.0.0.0', port = 8000)