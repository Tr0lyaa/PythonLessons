class Building:

    total = 0

    def __init__(self):
        Building.total += 1

list_of_buildings =[]
for i in range(40):
    building = Building()
    list_of_buildings.append(building)
    print('Building.total =', Building.total)

print()

for i in list_of_buildings:
    print(f'В {i} total = {i.total}')
