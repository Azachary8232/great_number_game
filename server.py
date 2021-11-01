from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.secret_key = "skittles"

@app.route('/')
def game_home():
    if 'random_num' not in session:
        session['random_num'] = random.randint(1,100)
    if 'count' not in session:
        session['count'] = 0
    if session['count'] == 10:
        if session['color'] != "green1": 
            session['color'] = "green2"
            print(session['color'])
            return render_template("index.html")
    print(session['random_num'])
    print(session['count'])
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    if int(request.form['guess']) > session['random_num']:
        session['color'] = "red1"
        session['count'] += 1
        print(session['color'])
        return redirect('/')
    elif int(request.form['guess']) < session['random_num']:
        session['color'] = "red2"
        session['count'] += 1
        print(session['color'])
        return redirect('/')
    else:
        session['color'] = "green1"
        session['count'] += 1
        print(session['color'])
        return redirect('/')
        
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')





if __name__ == "__main__":
    app.run(debug=True)