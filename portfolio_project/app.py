
python
from flask import Flask, render_template, request

app = Flask(_name_)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"Message from {name} ({email}): {message}")
        return "Thanks for contacting!"
    return render_template('contact.html')

if _name_ == '_main_':
    app.run(debug=True)


