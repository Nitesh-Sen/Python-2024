s1 =  {1, 2, 5, 7, 8}
s3 = {3, 7, 8}
print(s1.union(s3))
s1.update(s3)
print(s1, s3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)