from flask import Flask, jsonify, request

app = Flask(__name__)

persons = [
    {'id': '1', 'name': 'Max', 'work': 'Lime'},
    {'id': '2', 'name': 'Tommy', 'work': 'Nurse'},
    {'id': '3', 'name': 'Jane', 'work': 'Stuntwoman'}
]


@app.route('/', methods=['GET'])
def index():
    return 'Basic REST API'


class PersonEndpoints:
    @app.route('/person', methods=['GET'])
    def get_all():
        return jsonify(persons)

    @app.route('/person/<personid>', methods=['GET'])
    def get(personid):
        person = next((p for p in persons if p['id'] == personid), None)
        return jsonify(person)

    @app.route('/person', methods=['POST'])
    def add():
        persons.append(request.json)
        return jsonify(persons)

    @app.route('/person', methods=['PUT'])
    def update():
        person = next((p for p in persons if p['id'] == request.json['id']), None)
        person.update(request.json)
        return jsonify(person)

    @app.route('/person/<personid>', methods=['DELETE'])
    def delete(personid):
        person = next((p for p in persons if p['id'] == personid), None)
        persons.remove(person)
        return jsonify(persons)
