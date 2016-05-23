from flask import Flask, render_template, request, abort, redirect, url_for, flash, jsonify
import json
from Cat import Cat

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cat', methods=['POST'])
def cat():
    data = json.loads(request.data)
    new_cat = Cat(name='test', **data)
    new_cat.describe()
    answer = jsonify({'base_color': new_cat.fenotype.base_color, 'torbie': new_cat.fenotype.torbie, 'albino':
        new_cat.fenotype.albino, 'pattern': new_cat.fenotype.pattern, 'spots': new_cat.fenotype.spots})
    return answer


if __name__ == '__main__':
    app.run(debug=True)
