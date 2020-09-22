mydict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1955
}

for x in mydict:
  print(x, mydict[x])

for x in mydict.values():
  print(x)

for x, y in mydict.items():
  print(x,y)

child1 = {
  "name": "Emil",
  "age": 11
}
child2 = {
  "name": "Tobias",
  "age": 22
}
child3 = {
  "name": "Linux",
  "age": 33
}
myfamily = {
  "child1": child1,
  "child2": child2,
  "child3": child3
}

print(myfamily)
for c in myfamily.keys():
  print(c, myfamily[c]['name'])