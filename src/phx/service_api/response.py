import json
import copy


class Response:
    def __init__(self, raw_json_data):
        self.raw_json_data = raw_json_data

    def get_response(self, exclude_metadata=False):
        json_object = copy.deepcopy(self.raw_json_data)

        if exclude_metadata:
            json_object.pop("metadata")

        return json_object
    
    def get_metadata(self):
        json_object = json.loads(self.raw_json_data['metadata'])
        return json_object
