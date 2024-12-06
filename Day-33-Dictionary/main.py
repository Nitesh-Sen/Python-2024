dic = {
    34: "Neon",
    43: "Shubham",
    544: "Zakir",
    9889: "Nikita"
}

print(dic[9889])

info = {'name': "Karan", 'age': 19, 'elegibel': True}
print(info)
print(info.keys())
# print(info['name2']) # it will throw error. if key not exists.
print(info.get('name2')) # It will show you none. if key not exists.

print()
for keya in info.keys():
    print(f"The value corresponding to the key {keya} is {info[keya]} ")

print()
for keya, valuea in info.items():
    print(f"The value corresponding to the key {keya} is {valuea}")