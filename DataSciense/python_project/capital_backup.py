import json

person = input("Countries")
with open('countries_capitals_100.json','r') as Capitals:
    cap = json.load(Capitals)
    for data in cap:
        if data['country'] == person.capitalize():
            print(data["capital"])