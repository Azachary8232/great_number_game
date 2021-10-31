from flask import Flask, render_template, session, redirect, request
import random
app = Flask(__name__)
app.secret_key = "skittles"

@app.route('/')
def game_home():
    session['random_num'] = random.randint(1,100)
    print(session['random_num'])
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    if int(request.form['guess']) > session['random_num']:
        return redirect('/')
        






if __name__ == "__main__":
    app.run(debug=True)