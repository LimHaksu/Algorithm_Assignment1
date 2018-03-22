import heapq
class node:
    def __init__(self, x, y, from_node, g, h):
        self.from_node = from_node # the parrent node which is previous node of the current node
        self.to = [] # the children nodes which are next explored nodes
        self.x = x # the x coordinates of current node (y, x)
        self.y = y # the y coordinates of current node (y, x)
        self.g = g # the Uniform Cost Function of current node
        self.h = h # the heuristic function of current node
    def __gt__(a, b): # operator > overloading for heap queue which is used by Astar algorithm
        if a.g + a.h > b.g + b.h:
            return True
        else:
            return False
    def __lt__(a, b): # operator < overloading for heap queue which is used by Astar algorithm
        if a.g + a.h < b.g + b.h:
            return True
        else:
            return False

def make_child_node(current_node, parrent_node, height, width, maze):
    print_str = str(current_node.y)+" "+str(current_node.x)+"\n"
    f_out.write(str(print_str))
    # if the node reaches to the goal, print explored node
    if(current_node.y == height-1 and current_node.x == width-1):
        print_tree(current_node)
        return 0

    # the lower node of the current node
    x = current_node.x
    y = current_node.y + 1
    if not(x == parrent_node.x and y == parrent_node.y):
        if width > x >= 0 and height > y >= 0 and maze[y][x] == 0 and check[y][x] == 0:
            h=width-x+height-y-2
            current_node.to.append(node(x,y,current_node, current_node.g+1, h)) # make child node
            heapq.heappush(hq, node(x,y,current_node, current_node.g+1, h)) # and push the child node to the heap queue
            check[y][x] = 1 # check array is for checking if the node of coodinates (y,x) has been visited

    # the right node of the current node
    x = current_node.x + 1
    y = current_node.y
    if not(x == parrent_node.x and y == parrent_node.y):
        if width > x >= 0 and height > y >= 0 and maze[y][x] == 0 and check[y][x] == 0:
            h=width-x+height-y-2
            current_node.to.append(node(x,y,current_node, current_node.g+1, h))
            heapq.heappush(hq, node(x,y,current_node, current_node.g+1, h))
            check[y][x] = 1

    # the left node of the current node
    x = current_node.x - 1
    y = current_node.y
    if not(x == parrent_node.x and y == parrent_node.y):
        if width > x >= 0 and height > y >= 0 and maze[y][x] == 0 and check[y][x] == 0:
            h=width-x+height-y-2
            current_node.to.append(node(x,y,current_node, current_node.g+1, h))
            heapq.heappush(hq, node(x,y,current_node, current_node.g+1, h))
            check[y][x] = 1

    # the upper node of the current node
    x = current_node.x
    y = current_node.y - 1
    if not(x == parrent_node.x and y == parrent_node.y):
        if width > x >= 0 and height > y >= 0 and maze[y][x] == 0 and check[y][x] == 0:
            h=width-x+height-y-2
            current_node.to.append(node(x,y,current_node, current_node.g+1, h))
            heapq.heappush(hq, node(x,y,current_node, current_node.g+1, h))
            check[y][x] = 1
    if hq: # if hq is not empty
        q = heapq.heappop(hq)
        make_child_node(q, q.from_node, height, width, maze)

def print_tree(leaf_node):
    node = leaf_node
    stack = []
    while not(node.x == 0 and node.y == 0): # push the nodes from node of final state to node of start state(0,0)
        stack.append(node)
        node = node.from_node
    stack.append(node)
    while stack:
        node = stack.pop()
        print_str = "("+str(node.y)+", "+str(node.x)+")"
        f_out.write(print_str)
    f_out.write("\n\n")

f_in = open("input.txt", 'r')
f_out = open('output.txt', 'w')
testcases = f_in.readline()
for i in range(0, int(testcases)):
    f_in.readline()
    line = f_in.readline().split(' ', 1)
    height = int(line[0]) # height of maze
    width = int(line[1]) # with of maze
    hq = []

    # make maze from the input file
    check = [[0 for col in range(width)] for row in range(height)]
    maze = [[0 for col in range(width)] for row in range(height)]
    for j in range(0, height):
        line = f_in.readline().split(',', width-1)
        for k in range(0, width):
            maze[j][k] = int(line[k])
    start_node = node(0,0,None, 0, width+height-2)
    make_child_node(start_node, start_node, height, width, maze)
f_in.close()
f_out.close()
