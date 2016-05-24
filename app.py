from flask import Flask, render_template, request, abort, redirect, url_for, flash, jsonify
import json
from Cat import Cat
from Population import Population

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
    answer = jsonify(new_cat.serialize())
    return answer


@app.route('/population', methods=['POST'])
def population():
    data = json.loads(request.data)
    population = Population()
    for new_cat in data:
        population.add_cat_from_data(new_cat)
    next_population = population.breed_population()
    answer = json.dumps(next_population.to_json())
    return answer


if __name__ == '__main__':
    app.run(debug=True)
