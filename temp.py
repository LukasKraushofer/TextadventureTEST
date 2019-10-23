# for i in range(20):
#
#     position = []
#
#     x = randint(1,5)
#     for i in range(x):
#         pos = randint(0, 2000)
#         position.append(pos)
#
#     print(position)

# list1 = []
# list2 = []
# list3 = []
#
# list1.append(5)
# list1.append(list2)
# list1[1].append(2)
# list1[1].append(3)
# print(list1[1])


myfamily = {
  "child1" : {

    "child11" : {
      "name" : "arschi",
      "year" : 204
    },

    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

#EINFACH ID-LISTE UND DANACH AURFUFEN? ZU LANGSAM?

# 0 immer data, Rest neue dict?
entries = {
  "data": "0 text",
  "1" : {
      "data" : "text",
      "1" : 1.1,
      "2" : {
            "data" : "text 1.2",
            "1" : "1.1.2",
            "2" : "1.1.2",
            "3" : "1.1.3",
          },

      "3" : "1.3",
      "4" : "1.4",
  },
  "2" : "0.2",
  "3" : "0.3",
  "4" : "0.3",
}



print(myfamily["child1"])

x = myfamily["child2"]
print(x)



"""
class Tree(dict):
    def __init__(self):
        self = {}

    def add(self, node, child):
        if self.get(int(node)):
            childs = self.get(int(node))
            childs.append(int(child))
            self.update({int(node):childs})
        else:
            self.update({int(int(node)):[int(child)]})

def main():
    tot = int(input("Cantidad de relaciones: "))
    t = Tree()
    for i in range (0, tot):
        for i in range (0,1):
            a = []
            a.extend(input().split())
        t.add(a[0], a[1])
    print(t)


#################

a = {
    'a': [1, 2, 3],
    'b': {
        'c': [33, 44, 55]
        'd': 123,
    }
}

FALSCH pos 1.2.120.34 muss eine var sein
dict = {
  1 [entry1, entry2, entry3
  2 
  3
  4
  5

1 - 1,..
  1.1 - 1,..
    1.1.1 - 1,...
  
pos=[1,2,120,34]
for i in pos:
  
  

"""

# String in Liste zum addieren und zurück nach String
key2 = ""
key = "4.2.1.3"
# Instead of using a string, split it into a list:
key = key.split(".")
print(key)
key[-1] = int(key[-1]) + 1
print(key)

print(len(key))

for i in key:
    key2 += str(i)
    print(i, " ", key[-1])

    if i != key[-1]:
        key2 += str('.')
print(key2)

print('\n')


tree = []


# def fetch_field(subtree, key_list):
#     if not key_list:
#         return subtree["data"]
#
#     return fetch_field(subtree[key_list[0]], key_list[1:])
#
# key = "1.2.1.3"
# # Instead of using a string, split it into a list:
# key = key.split(".")
# fetch_field(tree, key)

print(tree)

li_1 = [1,2,3,4,5,6,7,8,9,10]
li_2 = [1,2,3,4]

print(len(li_1))
print(len(li_2))
print("")
print(li_2[-1])
print(li_1[len(li_2)])

li_2[-1] = li_1[len(li_2)-1] +1

print(li_2)