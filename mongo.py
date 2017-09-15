# mongo.py

from flask import Flask
from flask import jsonify
from flask import request
from mongoengine import *
from models.framework import Framework
import json

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'iva-webservice'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/iva-webservice'
mongo = connect(host=app.config['MONGO_URI'])

@app.route('/get_example', methods=['GET'])
def get_test():
    # framework = mongo.db.framework
    output = []

    # for q in Framework.objects:
    #     # framework = Framework(**q)
    #     output.append(q)
    #     # print(q.to_json())
    return Framework.objects.to_json()
    # return jsonify(res=[q.to_json() for q in Framework.objects ])

@app.route('/post_example', methods=['POST'])
def post_test():
    # frameworkDB = mongo.db.framework
    # frameworkModel = Framework(request.json)
    # json_dict = json.loads(request.json)
    # print(request.json)
    framework = Framework(**request.json)
    print(framework.id)

    framework_id = framework.save()
    print(framework.id)
    framework_created = Framework.objects().with_id(framework.id)
    print(framework_created.id)


    # JSONEncoder().encode(framework)
    # jsonToPost = json.dumps(TypeError: 'str' object does not support item assignment
    # print({"name": framework.name, "language": framework.language})
    # name = request.json['name']
    # # language = request.json['language']
    # framework_id = frameworkDB.insert(framework.toDict())
    # print(framework_id)
    # new_framework = frameworkDB.find_one({'_id': framework_id})
    # print(new_framework)
    # # output = Framework(**new_framework)
    # return dumps(new_framework)
    return framework_created.to_json()


if __name__ == '__main__':
    app.run(debug=True)