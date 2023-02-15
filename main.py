import json,difflib
data = json.load(open("data.json"))
def getDefinitionOf(obj):
    if obj in data:
        for definition in data[obj]:
            print(definition)
    elif len(difflib.get_close_matches(obj,data.keys()))>0:
        yn = True if "yes".__contains__(input(f"Do you mean {difflib.get_close_matches(obj,data.keys(),n=1)} instead? type Y if Yes: ").lower()) else False
        if yn:
            for definition in data[difflib.get_close_matches(obj,data.keys(),n=1)[0]]:
                print(definition)
            else:
                print("We didn't understand your entry.")
    else:
        print("Word doesn't exist. Double check and try again.")
while True:
    getDefinitionOf(input("Search for a definition: ").lower())