import json
import hashlib

def hash_generator(filename):
    with open(filename, encoding='utf-8') as countries_data:
        data = countries_data.read()
        string = json.loads(data)
        start = 0
        end = len(string)
        for i in range(start, end):
            data = hashlib.md5(string[i]['name']['common'].encode()).hexdigest()
            yield data
            start += 1

for i in hash_generator('countries.json'):
    print(i)



