import math
points = [(1,2),(3,4),(10,20),(7,8)]
distances = []
def euclideanDistance(point1,point2):
    d = math.sqrt(((point1[0]-point2[0])**2) + (point1[1]-point2[1])**2)
    return d


for i in range(len(points)-1):
    element1 = points[i]
    element2 = points[i+1]
    print(euclideanDistance(element1,element2));
    