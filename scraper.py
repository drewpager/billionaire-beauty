import scraperwiki
import requests
import json

json_data = requests.get("https://www.forbes.com/ajax/list/data?year=2017&uri=billionaires&type=person").content
data = [item for item in json.loads(json_data)]

base_image_url = "http://i.forbesimg.com/media/lists/people/{}_100x100.jpg"

new_data = []

for item in data:
    result_dict = {}
    for entry, value in item.iteritems():
        if entry == 'imageUri' and not "no-pic" in value:
            print entry, value
            result_dict[entry] = base_image_url.format(item['imageUri'])
        else:
            result_dict[entry] = item[entry]
    new_data.append(result_dict)

scraperwiki.sqlite.save(['rank'], new_data)
