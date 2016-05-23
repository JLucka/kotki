from flask import Flask, render_template, request, abort, redirect, url_for, flash, jsonify
import json
from Cat import Cat
from CatCreator import CatCreator

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cat', methods=['POST'])
def cat():
    gender = json.loads(request.args.get('gender'))[0] if request.args.get('gender') else 0
    orange = json.loads(request.args.get('orange')) if request.args.get('orange') else None
    black = json.loads(request.args.get('black')) if request.args.get('black') else None
    density = json.loads(request.args.get('density')) if request.args.get('density') else None
    dilute = json.loads(request.args.get('dilute')) if request.args.get('dilute') else None
    agouti = json.loads(request.args.get('agouti')) if request.args.get('agouti') else None
    mackarel = json.loads(request.args.get('mackarel')) if request.args.get('mackarel') else None
    ticked = json.loads(request.args.get('ticked')) if request.args.get('ticked') else None
    albino = json.loads(request.args.get('albino')) if request.args.get('albino') else None
    white = json.loads(request.args.get('white')) if request.args.get('white') else None
    spots = json.loads(request.args.get('spots')) if request.args.get('spots') else None
    new_cat = Cat(gender=gender, orange=orange, black=black, density=density, dilute=dilute, agouti=agouti, \
                                                                                               mackarel=mackarel,
                ticked=ticked, albino=albino, white=white, spots=spots)
    new_cat.describe()
    return jsonify({'base_color': new_cat.fenotype.base_color, 'torbie': new_cat.fenotype.torbie, 'albino':
        new_cat.fenotype.albino, 'pattern': new_cat.fenotype.pattern, 'spots': new_cat.fenotype.spots});


if __name__ == '__main__':
    app.run(debug=True)
