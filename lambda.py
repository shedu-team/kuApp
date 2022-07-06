people = [
        {"name": "Mohammad", "city": "Najaf"},
        {"name": "Ali", "city": "Basra"},
        {"name": "Karrar", "city": "Baghdad"},
        {"name": "Zaidon", "city": "Kut"},
        {"name": "Mahdi", "city": "Amman"}

        ]
#def f(person):
#    return person["city"]

people.sort(key = lambda person: person["name"])

print(people)
