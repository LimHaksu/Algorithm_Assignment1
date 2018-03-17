import heapq
class node:
    def __init__(self, x, y, from_node, g, h):
        self.from_node = from_node
        self.to = []
        self.x = x
        self.y = y
        self.g = g
        self.h = h
    def __gt__(a, b):
        if a.g + a.h > b.g + b.h:
            return True
        else:
            return False
    def __lt__(a, b):
        if a.g + a.h < b.g + b.h:
            return True
        else:
            return False

# 2차원 배열 생성 방법
# L = [[0 for cols in range(m)]for rows in range(n)]

def make_child_node(current_node, parrent_node, height, width, maze, tag):
    print(current_node.y,current_node.x)
    #print explored node
    if(current_node.y == height-1 and current_node.x == width-1):
        print_tree(current_node)
        return 0
    # the left node of current node
    x = current_node.x - 1
    y = current_node.y
    if not(x == parrent_node.x and y == parrent_node.y):
        if width > x >= 0 and height > y >= 0 and maze[y][x] == 0:
            h=width-x+height-y-2
            current_node.to.append(node(x,y,current_node, current_node.g, h))
            heapq.heappush(hq, node(x,y,current_node, current_node.g, h))
            #make_child_node(current_node.to[i], current_node, h, w, maze)

    # the right node of current node
    x = current_node.x
    y = current_node.y + 1
    if not(x == parrent_node.x and y == parrent_node.y):
        if width > x >= 0 and height > y >= 0 and maze[y][x] == 0:
            h=width-x+height-y-2
            current_node.to.append(node(x,y,current_node, current_node.g, h))
            heapq.heappush(hq, node(x,y,current_node, current_node.g, h))
            #make_child_node(current_node.to[i], current_node, h, w, maze)
    x = current_node.x + 1
    y = current_node.y
    if not(x == parrent_node.x and y == parrent_node.y):
        if width > x >= 0 and height > y >= 0 and maze[y][x] == 0:
            h=width-x+height-y-2
            current_node.to.append(node(x,y,current_node, current_node.g, h))
            heapq.heappush(hq, node(x,y,current_node, current_node.g, h))
            #make_child_node(current_node.to[i], current_node, h, w, maze)
    x = current_node.x
    y = current_node.y - 1
    if not(x == parrent_node.x and y == parrent_node.y):
        if width > x >= 0 and height > y >= 0 and maze[y][x] == 0:
            h=width-x+height-y-2
            current_node.to.append(node(x,y,current_node, current_node.g, h))
            heapq.heappush(hq, node(x,y,current_node, current_node.g, h))
            #make_child_node(current_node.to[i], current_node, h, w, maze)
    if hq:
        tag = 1
        q = heapq.heappop(hq)
        make_child_node(q, q.from_node, height, width, maze, tag)

def print_tree(leaf_node):
    node = leaf_node
    stack = []
    while not(node.x == 0 and node.y == 0):
        stack.append(node)
        node = node.from_node
    print("("+str(node.y)+", "+str(node.x)+")",end='')
    while stack:
        node = stack.pop()
        print("("+str(node.y)+", "+str(node.x)+")",end='')
    print('\n')

f = open("input.txt")
testcases = f.readline()
for i in range(0, int(testcases)):
    f.readline()
    line = f.readline().split(' ', 1)
    #line = line.split(' ', 1 )
    height = int(line[0]) # height of maze
    width = int(line[1]) # with of maze
    hq = []
    # make maze from the input file
    maze = [[0 for col in range(width)] for row in range(height)]
    for j in range(0, height):
        line = f.readline().split(',', width-1)
        for k in range(0, width):
            maze[j][k] = int(line[k])
    start_node = node(0,0,None, 0, width+height-2)
    tag = 0
    make_child_node(start_node, start_node, height, width, maze, tag)
    current_node = start_node

#    while(current_node != None):
#        print('(',current_node.y,',',current_node.x,',',current_node.g,',',current_node.h,')\n')
#        current_node = current_node.to[0]
f.close()
