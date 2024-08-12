from flask import Flask, request, jsonify, render_template
from models import Pessoa

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_person', methods=['POST'])
def add_person():
    data = request.get_json()
    pessoa = Pessoa(data['name'], data['age'])
    pessoa.save()
    return jsonify({'success': True})

@app.route('/get_people', methods=['GET'])
def get_people():
    pessoas = Pessoa.get_all()
    return jsonify([{'name': p[1], 'age': p[2]} for p in pessoas])

if __name__ == '__main__':
    app.run(debug=True)
