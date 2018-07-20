import json
import './test.json' as json_data

json_parsed = json.loads(json_data)
print json_parsed['faces']
