from flask import Flask, render_template, session
import random
app = Flask(__name__)
app.secret_key = "skittles"

@app.route('/')
def game_home():
    session['random_num'] = random.randint(1,100)
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)