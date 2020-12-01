graph = {
    'a' : ['b', 'c', 'e'],
    'b' : ['d', 'f'],
    'c' : ['g','a'],
    'e' : ['f'],
    'f' : ['e'],
}


def DLS(node, goal, depth):
    print ("NODE: %s, GOAL %s, DEPTH: %i" % (node, goal, depth))
    if depth == 0 and node == goal:
        print( "GOAL FOUND ,RETURN TO")
        return node
    elif depth > 0:
        print ("LOOPING THROUGH CHILD NODES: %s" % (graph.get(node, [])))


        for child in graph.get(node, []):
            if goal == DLS(child, goal, depth-1):
                return goal

DLS('a', 'g', 0)
