import json
import os.path
import datetime

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
    jsonDataFormat = '''
{
    "time": "",
	"data": [{
			"date": "5/27/2021",
			"hour": "17",
			"data": {
				"light": 30,
				"dry": 40,
				"ph": 10,
				"relay_ctrl": "ON",
				"node": "Device Not Connected"
			}
		}
        ]
}
    '''
    def write_json(self, new_data, filename='static/js/data.json'):
        
        if not os.path.exists(filename):
            newFile = open(filename, "w+")
            newFile.write(self.jsonDataFormat)

        with open(filename,'r+') as file:
            # First we load existing data into a dict.
            file_data = json.load(file)

            # # Join new_dat3a with file_data
            file_data["data"].append(new_data)

            unique = { each["hour"] : each for each in file_data["data"] }.values()
            # # print(list(unique))
            file_data["data"] = list(unique)
            file_data["time"] = str(datetime.datetime.now())

            json_formatted_st = json.dumps(file_data, indent=2)

            newFile = open(filename, "w+")
            newFile.write(json_formatted_st)

    
    def construct_data(self, data):
        jsonData = {
			"date": "5/27/2021",
			"hour": "17",
			"data": {
			}
        }

        today = datetime.date.today()
        jsonData["date"] = today.strftime("%m/%d/%Y")
        jsonData["data"] = data
        time = datetime.datetime.now()
        jsonData["hour"] = (time.strftime("%H"))
        self.write_json(jsonData)
        print("Append done")
        pass