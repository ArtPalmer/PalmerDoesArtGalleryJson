import json
with open('/json/discord_database.json', 'r') as json_file:
    json_load = json.load(json_file)
one = json_load['gallery']['data'][1]['url']
print("One")