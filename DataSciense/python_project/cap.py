import json

person = input("Countries: ")
with open('countries_population_2024.json',"r") as cap_population:
    cappop = json.load(cap_population)
    for data in cappop:
        if data['country'] == person:
            print(f"{person}: {data['population']}")