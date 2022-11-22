import json

API_KEY = 'd1526a9039658a6f76950cff21823aff'


s = '{"coord":{"lon":5.2861,"lat":52.1183},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"base":"stations","main":{"temp":4.59,"feels_like":2.65,"temp_min":3.77,"temp_max":5.97,"pressure":990,"humidity":93},"visibility":10000,"wind":{"speed":2.24,"deg":166,"gust":7.15},"clouds":{"all":55},"dt":1669103746,"sys":{"type":2,"id":2009129,"country":"NL","sunrise":1669101058,"sunset":1669131556},"timezone":3600,"id":2747030,"name":"Soesterberg","cod":200}'

d = json.loads(s)

print(d['weather'][0]['description'])