import requests
from xml.dom.minidom import parseString

url = "http://gotracker.ca/GoTracker/web/GODataAPIProxy.svc/TripLocation/Service/Lang/31/en?_=1663888486410"
x = requests.get(url)

document = parseString(x.content)
out = document.getElementsByTagName("InServiceTripPublic")

kitchener_trains = [] 
for i in out:
    kitchener_trains.append(dict(i.attributes.items()))

print(len(kitchener_trains))


x = map(lambda x: (x["EquipmentCode"], x["Latitude"], x["Longitude"]), kitchener_trains)
print(list(x))


# import re

# with open("go_train_data/stops.txt") as file:
#     for line in file:
#         sp_l = line.split(",")[0:5]
#         pattern = re.compile("[A-Z][A-Z]")
#         if pattern.match(sp_l[0]):
#             print(sp_l)