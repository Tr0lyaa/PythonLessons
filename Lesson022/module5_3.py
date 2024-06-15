class Building:
    def __init__(self,numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

b1 = Building(20, 'ЖК')
b2 = Building(20, 'ЖК')
b3 = Building(13, 'ЖК')

print(b1 == b2)
print(b2 == b3)
