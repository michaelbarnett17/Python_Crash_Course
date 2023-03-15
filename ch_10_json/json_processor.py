from pathlib import Path
import json

class JsonProcessor:

    def __init__(self):
        pass

    def dump_json(self, input_data, dump_path):

        path = Path(dump_path)
        formatted_contents = json.dumps(input_data)
        path.write_text(formatted_contents)


    def load_json(self, load_path):

        path = Path(load_path)

        if path.exists():
            contents = path.read_text()
        else:
            print("Path does not exist")
            formatted_contents = []
            return formatted_contents

        formatted_contents = json.loads(contents)
        
        return formatted_contents