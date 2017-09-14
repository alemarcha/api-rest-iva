# mongo.py

from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'iva-webservice'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/iva-webservice'
mongo = PyMongo(app)

@app.route('/get_example', methods=['GET'])
def get_test():
    framework = mongo.db.framework
    output = []

    for q in framework.find():
        print(q['name'])
        output.append({'name': q['name'], 'language': q['language']})

    return jsonify({'result': output})

@app.route('/post_example', methods=['POST'])
def post_test():
    framework = mongo.db.framework
    name = request.json['name']
    language = request.json['language']
    framework_id = framework.insert({'name': name, 'language': language})
    new_framework = framework.find_one({'_id': framework_id})
    output = {'name': new_framework['name'], 'language': new_framework['language']}
    return jsonify({'result': output})

if __name__ == '__main__':
    app.run(debug=True)