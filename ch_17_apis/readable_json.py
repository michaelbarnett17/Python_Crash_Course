import json

class ReadableJson:

    # Constructor method
    def __init__(self, unformatted_json):

        self._unformatted_json = unformatted_json


    def formatted_json(self):
        return json.dumps(self._unformatted_json, indent=4)
        
        

