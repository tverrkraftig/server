from flask import Flask
from flask.ext import restful
import resources

app = Flask(__name__)
api = restful.Api(app)

"""
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

api.add_resource(MongoWorld, '/<string:id>')"""

api.add_resource(resources.Status, '/status/<string:id>')
api.add_resource(resources.Data, '/data/<string:id>', '/data/<string:id>/<string:sensor>', defaults={'sensor':None})
#api.add_resource(resources.Data, '/data/<string:id>/<string:sensor>')
api.add_resource(resources.Command, '/command/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
