import re

go_train_lines = {
    "kitchener": [],
    "barrie": [],
    "lakeshore_east": [],
    "lakeshore_west": [],
    "milton": [],
    "richmond_hill": [],
    "stouffville_line": []
}

go_train_stations = []

with open("go_train_stops_on_routes") as file:
    for line in file:
        line_split = line.strip().split(",")
        go_train_lines[line_split[0]] = line_split[1:]

print(go_train_lines)

with open("go_train_data/stops.txt") as file:
    for line in file:
        sp_l = line.split(",")
        pattern = re.compile("[A-Z][A-Z]")
        if pattern.match(sp_l[0]):
            print(sp_l[0:3])
            # go_train_stations.append(sp_l[0:4])

# print(go_train_stations)