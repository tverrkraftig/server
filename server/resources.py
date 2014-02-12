from flask import request
from flask.ext import restful
from pymongo import MongoClient
from tools.decorators import get_str_object_or_404
from tools.helpers import get_microtime

mongodb = MongoClient().db

class Status(restful.Resource):
    def __init__(self):
        self.collection = mongodb.status

    @get_str_object_or_404
    def get(self, id):
        return self.collection.find_one({'device_id': id})

    def post(self, id):
        data = request.get_json(force=True, cache=False)
        data["device_id"] = id
        data["timestamp"] = get_microtime()

        self.collection.update({'device_id': id}, data, upsert=True)
        # TODO Return get commands
        return {}

class Data(restful.Resource):
    def __init__(self):
        self.collection = mongodb.data

    @get_str_object_or_404
    def get(self, id, sensor=None):
        if sensor != None:
            return self.collection.find_one({'device_id': id, 'sensor': sensor})
        else:
            return [sensor for sensor in self.collection.find({'device_id': id})]

    def post(self, id, sensor=None):
        data = request.get_json(force=True, cache=False)

        if sensor == None:
            for sensor_data in data:
                sensor_data["device_id"] = id
                sensor_data["timestamp"] = get_microtime()
                self.collection.update({'device_id': id, 'sensor': sensor_data['sensor']}, sensor_data, upsert=True)
        else:
            data["device_id"] = id
            data["timestamp"] = get_microtime()
            self.collection.update({'device_id': id, 'sensor': sensor}, data, upsert=True)

        # TODO Return get commands
        return {}

class Command(restful.Resource):
    def __init__(self):
        self.collection = mongodb.commands

    def get(self, id):
        # TODO Write this
        pass

    def post(self, id):
        data = request.get_json(force=True, cache=False)
        data["device_id"] = id
        data["timestamp"] = get_microtime()
        self.collection.insert(data)
        # TODO return something?
        return {}
