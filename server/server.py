from flask import Flask, request
from flask.ext import restful
from pymongo import MongoClient
from tools.decorators import get_str_object_or_404

app = Flask(__name__)
api = restful.Api(app)

collection = MongoClient().db.coll

class MongoWorld(restful.Resource):
    @get_str_object_or_404
    def get(self, id):
        return collection.find_one({'mongo_id': id})

    def put(self, id):
        collection.update({'mongo_id': id}, {'mongo_id': id, 'data': request.form['data']}, upsert=True)
        return self.get(id)

    def post(self, id):
        self.put(id)

    def delete(self, id):
        return collection.remove({'mongo_id': id})

api.add_resource(MongoWorld, '/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
