import pandas as pd
import numpy as np
from flask import Flask, render_template, request, redirect, url_for        ## Web 구현용

app = Flask(__name__)

@app.route('/')             # 이게 홈 화면으로 설정
def home():
    return render_template('index.html')

# @app.route('/input2')
# def input():
#     return render_template('input2.html')

# @app.route('/home3')
# def home3():
#     return render_template('home3.html')

# @app.route('/input2/meta2', methods = ['POST'])
# def meta2():
#     val1 = request.form['course_code']          # request.form이 데이터 받아오는 애
#     return render_template('meta2.html', result=None, resultData=((prediction, mileage_prop),), resultUPDATE=None)

if __name__ == '__main__':
    app.run(host='0.0.0.0')           # Flask를 실행해주는 친구. 앞에 있어도 되고 뒤에 있어도 된다.