# app.py
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    try:
        mail = request.form['mail']
        parola = request.form['parola']
        with open('mailuri', 'a') as file:
            file.write(f"[{mail},{parola}]\n")
        return render_template('log in.html')
    except:
        return "Error occurred."

@app.route('/log in', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        mail = request.form['mail']
        parola = request.form['parola']
        
        with open('mailuri', 'r') as file:
            for line in file:
                if f"[{mail},{parola}]" in line:
                    return render_template('logged.html', mail=mail)
        return "Invalid credentials. Please check your email and password."
    return render_template('log in.html')
if __name__ == '__main__':
    app.run(debug=True, port=80,host="0.0.0.0")
