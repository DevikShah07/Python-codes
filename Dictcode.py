mydict={
  "devik" : "maitri",
  "roshan" : "dhruti",
}
for x in mydict.items():
  print(x)

mydict={
  "devik" : "maitri",
  "roshan" : "dhruti",
}
thisdict=mydict.copy()
print(thisdict)

mydict={
  "devik" : "maitri",
  "roshan" : "dhruti",
}
thisdict=dict(mydict)
print(thisdict)

NESTED DICT
friends = {
    "one": {
        "name": "devik",
        "age": 20
    },
    "two": {
        "name": "manan",
        "age": 20
    },
    "three": {
        "name": "niheel",
        "age": 21
    },
    "four": {
        "name": "roshan",
        "age": 20
    }
}
for x in friends.items():
  print(x)


QUESTION
mydict={
  "devik" :["maitri","dhwani"],
  "roshan" : "dhruti"
}
# print(mydict.get("devik"[0]))
# for x in mydict.items:
#   print(x)
print(mydict.values())
