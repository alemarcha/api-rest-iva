from mongoengine import *

class Framework(Document):
    name = StringField(max_length=200, required=True)
    language = StringField(max_length=200, required=True)
    # def __init__(self, name, language, *args, **kwargs):
    #     # if **kwargs['id'] != None:
    #     #     self.id = args.id
    #     self.name = name
    #     self.language = language
    #
    # def serialize(self):
    #     return json.dumps(self)
    #
    # def toDict(self):
    #     return self.__dict__
