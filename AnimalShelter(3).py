from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,username,password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
            self.client = MongoClient('mongodb://%s:%s@localhost:54623/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
            self.database = self.client['test']
            
    def create(self, data):
        #Checks to see if the data is null or empty and returns false in either case
        if data is not None: 
            if data:
                self.database.animals.insert_one(data)
                return True
        else:
            return False
    def read_all(self,data):
        cursor = self.database.animals.find(data, {'_id':False})
        return cursor
    
    # The method to implement the R in CRUD.
    def read(self, search):
        #Checks to see if the data is null or empty and returns exception in either case
        if search is not None: 
            if search:
                searchResult = self.database.animals.find(search)
                return searchResult
        else:
            exception = "Nothing to search, because search parameter is empty"
            return exception

    # The method to implement the U in CRUD.
    def update(self, save):
        if save is not None:
        # the save() method updates the document if this has an _id property 
        # which appears in the collection, otherwise it saves the data
        # as a new document in the collection
            if save:
                saveResult = self.database.animals.insert_one(save)
            return saveResult
        else:
            exception = "Nothing to update, because save parameter is None"

    # The method to implement the D in CRUD.
    def delete(self, remove):
        if remove is not None:
            if remove:
                removeResult = self.database.animals.delete_one(remove)
            return removeResult
        else:
            exception: "Nothing to delete, because remove parameter is None"
                
    def deleteAll(self, remove):
        if remove is not None:
            if remove:
                removeResult = self.database.animals.remove({})
            return removeResult
        else:
            exception: "Nothing to delete, because remove parameter is None"