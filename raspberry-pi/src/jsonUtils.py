import json

import datetime

# {
# 	"data": [{
# 			"date": "5/27/2021",
# 			"time": "17",
# 			"data": {
# 				"light": 30,
# 				"dry": 40,
# 				"ph": 10,
# 				"relay_ctrl": "ON",
# 				"node": "Device Not Connected"
# 			}
# 		}
# }
class jsonUtils:

    def write_json(self, new_data, filename='static/js/data.json'):
        # print(new_data)
        with open(filename,'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)
            # Join new_dat3a with file_data
            file_data["data"].append(new_data)
            # # # Sets file's current position at offset.
            file.seek(0)
            # # # convert back to json.
            json.dump(file_data, file, indent = 4)

    
    def construct_data(self, data):
        jsonData = {
			"date": "5/27/2021",
			"time": "17",
			"data": {
			}
        }

        today = datetime.date.today()
        jsonData["date"] = today.strftime("%m/%d/%Y")
        jsonData["data"] = data
        time = datetime.datetime.now()
        jsonData["time"] = (time.strftime("%H"))
        self.write_json(jsonData)
        print("Append done")
        pass