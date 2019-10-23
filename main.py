from anytree import Node, RenderTree
from anytree import NodeMixin
from anytree import Resolver
from anytree import Walker


class MyBaseClass(object):  # Just an example of a base class
    foo = 4
    #separator = "."
class Node(MyBaseClass, NodeMixin):  # Add Node feature
    def __init__(self, name, length, width, parent=None, children=None):
        super(Node, self).__init__()

        self.name = name
        self.length = length
        self.width = width
        self.parent = parent

        self.pos = "0"
        self.text = "0"

        self.lpos = [1]


        if children:
            self.children = children

    def update_stringpos(self): #, list_pos, number):

        new_pos = ""
        for i in self.lpos:
            new_pos += str(i)
            if i != self.lpos[-1]:
                new_pos += str('.')

        self.pos = new_pos





class Tracker:
    def __init__(self):

        self.ALL_ID = 0
        self.ALL_POS = "1"
        #self.CURRENT_POS = "1"

        self.lALL_POS = [1]

    def update_stringpos(self):  # , list_pos, number):

        new_pos = ""
        for i in self.lALL_POS:
            new_pos += str(i)
            if i != self.lALL_POS[-1]:
                new_pos += str('.')

        self.ALL_POS = new_pos


def check_hure(node, user_input):
    for i in node.children:

        if i.text == user_input:
            print("gibts schon", i.text, i.name, i.pos, i.lpos)

            return True, i

    return False, 0

def debug_print(node):

    print("DEBUG:")
    for i in node.children:
        print(i.name, " ", i.lpos)



# TODO active_node in class active_node used in while
# TODO

track = Tracker()



start_room = Node("1", 0, 0)
#start_room.parent = start_room
start_room.text = "JO SEAS, WEN HOMMA DENN DO LOL"
start_room.lpos = [1]
print(start_room.text)



active_node = start_room
user_input = ""
while user_input != "end":

    print("TOP: ACTIVE NODE: ", active_node.name, active_node.lpos, active_node.text)

    user_input = input("lol: ")
    if user_input == "end":
        print("Exit")
        break

    if user_input == "back":
        active_node = active_node.parent
        #print("back jump back to: ", active_node.name, active_node.text, active_node.lpos)

    elif user_input == "start":
        active_node = start_room
        #print("start jump back to: ", active_node.name, active_node.text, active_node.lpos)

    else:

        found, found_node = check_hure(active_node, user_input)
        if found:
            active_node = found_node
            #print("found jump to: ", active_node.name, active_node.text, active_node.lpos)


        else:
            #if(user_input != "back" and user_input != "start"):

            # Check for new .1
            #print("LENGTH: ", len(track.lALL_POS)," ", len(active_node.lpos))
            if len(track.lALL_POS) == len(active_node.lpos):
                track.lALL_POS.append(1)


                # ERROR new_pos.append(1) appends on active_node.lpos too
                #new_pos = active_node.lpos
                #new_pos.append(1)
                new_pos = []
                for i in active_node.lpos:
                    new_pos.append(i)
                new_pos.append(1)

                name_numb = 1

            else:

                # TODO IN FUNKTION
                # TODO Mehr Funktionen? str int wechseln, rechnen und All.Pos handeln

                # pos handler

                new_pos = []
                for i in active_node.lpos:
                    new_pos.append(i)
                new_pos.append(1)


                #calc_pos = active_node.lpos

                print(new_pos, new_pos[-1])
                print(track.lALL_POS, track.lALL_POS[len(active_node.lpos) - 1])
                #active_node[-1] = track.lALL_POS[len(active_node.lpos)-1]+1
                new_pos[-1] = track.lALL_POS[len(new_pos) - 1] + 1
                print(new_pos)
                print(track.lALL_POS, track.lALL_POS[len(active_node.lpos) - 1])

                name_numb = new_pos[-1]




                #ret_numb = int(calc_pos[-1]) + 1 # Zahl für Node.name

                # Wenn größere Zahlen gefunden werden wird ALL.Pos überschrieben, damit größte bleibt.

                ka = 0
                for a,b in zip(new_pos, track.lALL_POS):
                    if a > b:
                        #print(a, ">", b)
                        track.lALL_POS[ka] = a

                    ka += 1



                #active_node.update_stringpos()
                track.update_stringpos()


            #print(new_pos)

            #new_entry = Node(str(ret_numb), 0,0, parent=active_node)
            new_entry = Node(name_numb, 0, 0, parent=active_node)
            #print("NEW ENTRYS: ", new_entry.name, new_entry.lpos)
            new_entry.lpos = new_pos
            #print(new_entry.lpos)
            #new_entry.update_stringpos()
            new_entry.text = user_input

            new_pos=[]
            active_node = new_entry




############# DEBUG ###################

for pre, fill, node in RenderTree(start_room):
    treestr = u"%s%s" % (pre, node.name)
    print(treestr.ljust(8), node.text, node.pos, node.lpos)

