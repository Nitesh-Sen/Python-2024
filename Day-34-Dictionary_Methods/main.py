ep1 = {874: 54, 889: 56, 564: 98, 958: 65}
ep2 = {1226: 51, 365: 32}
ep1.update(ep2)
# ep1.clear() # To make a empty dictionary.
# ep1.pop(1226) # To remove a iteam with pop.
ep1.popitem() # It will remove last iteam in dictionary.
# del ep1 # this will delete disctionary entirly.
del ep1[1226]
print(ep1) 