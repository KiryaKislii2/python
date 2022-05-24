from book import book

class repair:
    def parse(obj):
        mas = []
        id = 1
        if type(obj) == dict:
            id = obj['num_ID']
            if 'Books' in obj:
                print(obj['Books'])
                for x in obj['Books']:
                    mas.append(book(x['name'],x['author'],x['year'],x['number'],x['id']))
        tu = id, mas
        return tu
