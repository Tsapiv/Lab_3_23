from flask import Flask, render_template, request
import logic

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        logic.give_me_map(name)
        logic.add_button()
        return render_template("map.html")
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
