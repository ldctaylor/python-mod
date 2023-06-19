#Dictionaries
#Unlike lists, dictionaries are not ordered

#Lists have INDEX and VALUE
#Dictionaries have KEY and VALUE
#Dictionaries use {squiggly brackets} unlike [lists]

#Keys must be immutable i.e. not lists, other dictionaries
#Keys must be UNIQUE.

mixed_dict = {
    "integer": 3,
    "float": 4.0,
    "string": "Hello",
    "boolean": True,
    "none": None,
    "list": [1,"i", False],
    "dictonary": {"a": 1, "b": 2, "c": 3}
}

print(mixed_dict)
print(type(mixed_dict))

dict_mixed = {
    "abc": "a string",
    1: "integer",
    2.0: "a float",
    False: "A boolean",
    None: "none"
}

print(dict_mixed)

#Accessing values in a list:
float_example = dict_mixed[2.0]
print(float_example)

ingredients = {
    "flour": "1 cup",
    "eggs": 2,
    "milk": "1 cup"
}

flour = ingredients["flour"]
eggs = ingredients["eggs"]
milk = ingredients["milk"]

print(f"To make a pancake you need {flour} of flour, {eggs} eggs and {milk} of milk")

ingredients["sugar"] = "1 tsp"

print(ingredients)
del ingredients["sugar"]
print(ingredients)

#Iterating

#METHOD .keys()

for _ in ingredients.keys():
    print(_)

#METHOD .values()

for _ in ingredients.values():
    print(_)

for i,j in ingredients.items():
    print(i,j)
#can be written as:
for key,value in ingredients.items():
    print(key,value)