import json


class load:
    def save(obj, id):
        dic = dict()
        dic['num_ID'] = id        
        if type(obj) == list:
            re = []
            for item in obj:
                re.append(item.__dict__)
            dic['Books'] = re
            with open('Stor.json', 'w') as file:
                json.dump(dic, file, indent=4)
        else:
            with open('Stor.json', 'w') as file:
                json.dump(dic, file, indent=4)
