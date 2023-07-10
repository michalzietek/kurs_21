import json
import pickle

with open("data.json") as file:
    data = json.load(file)

print(data)

dummy_set = [1, 2, 3, 4, 5]

with open("test1.pkl", mode="wb") as file:
    pickle.dump(dummy_set, file)

with open("test1.pkl", mode="rb") as file:
    pickle_data = pickle.load(file)

print(f"Dane z pickle: {pickle_data}")