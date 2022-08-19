import copy
  

class NODE:
    def __init__(self, _state, _hval, _parent):
        self.state = _state
        self.hval = _hval
        self.parent = _parent

 
## pass only their states
def h(curr_state, goal_state):
    totalh = 0
    for i in range(len(curr_state)):
        if len(curr_state[i])>0:
            mn = min(len(curr_state[i]), len(goal_state[i]))
            for j in range(mn):
                if curr_state[i][j]!=goal_state[i][j]:
                    totalh-=(j+1)
                else:
                    totalh+=(j+1)
    return totalh


## pass whole nodes
def move_gen(start, first, last):
    neighbour = []
    curr_state = first.state
    goal_state = last.state
    h_val = first.hval
    s1 = copy.deepcopy(curr_state)
    for i in range(len(s1)):
        s2 = copy.deepcopy(s1)
        if len(s2[i])>0:
            ele = s2[i].pop()
            for j in range(len(s2)):
                if i!=j:
                    s3 = copy.deepcopy(s2)
                    s3[j].append(ele)
                    
                    now_h = h(s3, goal_state)
                    
                    if now_h > h_val and last.hval > start.hval:
                        n_node = NODE(s3, now_h, first)
                        neighbour.append(n_node)

                    elif now_h < h_val and last.hval < start.hval:
                        n_node = NODE(s3, now_h, first)
                        neighbour.append(n_node)

    
    return neighbour
      

def test_goal(_curr, _goal):
    return _curr.hval == _goal.hval



path = []
heuristic = []

def findPath(node):
    while node.parent!=None :
        path.append(node.state)
        heuristic.append(node.hval)
        node = node.parent
    

print("Initial State:       Final State:")
print("      d  ",                  "                 ")
print("      e  ",                  "             f  b")
print("   b  e  ",                  "             c  e")
print("a  c  f  ",                  "             a  d")
print()

_start = [['a'], ['c', 'b'], ['f', 'e', 'd'], []]
_goal = [['a', 'c', 'f'], ['d', 'e', 'b'], [], []]

hval_start = h(_start, _goal)
hval_goal = h(_goal, _goal)



start_node = NODE(_start, hval_start, None)
goal_node = NODE(_goal, hval_goal, None)



print("Initial state: ", start_node.state , "   Heuristic value: ", start_node.hval)
print("Final state: ", goal_node.state , "   Heuristic value: ", goal_node.hval)
print()


open = [start_node]
closed = []

check = False


while open:
    _curr = open.pop(0)
    #print("Current state : ", _curr.state , "   Heuristic value: ", _curr.hval)
    closed.append(_curr)
    
    if test_goal(_curr, goal_node):
        findPath(_curr)
        path.append(_start)
        heuristic.append(start_node.hval)
        path.reverse()
        heuristic.reverse()
        
        check = True
        break
    
    neighbour = move_gen(start_node, _curr, goal_node)
   
    for item in neighbour:
        if item not in closed:
            open.append(item)
            closed.append(item)


    


if check:
    print()
    #print("Solved!!!\n")
    print("Path from Initial state to end state: \n")
    for i in  range(len(path)):
        print("State : ", path[i] , "  Heuristic value: ", heuristic[i])
else:
    print()
    print("No solution")
