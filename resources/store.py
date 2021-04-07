from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store = StoreModel.find_by_name(name)

        if store:
            return store.json()
        return {'message': 'Store Not Found'}, 404

    def post(self,name):
        store = StoreModel.find_by_name(name)

        if store:
            return {"message': 'Store with name {} Already Exists.".format(name)}, 400
        #return {'message': 'Store Not Found'}, 404

        store = StoreModel(name)
        try:
            StoreModel.save_to_db(store)
        except:
            return {'message': "An error is occurred while creating store"}, 500

        return store.json(), 201


    def delete(self,name):
        store = StoreModel.find_by_name(name)

        if store:
            StoreModel.delete_from_db(store)

        return {'message': 'Store deleted'}

class StoreList(Resource):
    def get(self):
        return {'Stores': [store.json() for store in StoreModel.query.all()]}
