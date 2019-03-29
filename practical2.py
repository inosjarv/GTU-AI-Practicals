"""BFS for solving 8 puzzle problem"""
from node import *

def BFS(start,goal):
    queue = [start]
    visited = set()
    found = False
    depth = 50
    while queue:
        state = queue.pop()
        if state == goal:
            found = state
            break
        if state in visited or state.step > depth:
            continue
        visited.add(state)
        for s in state.next():
            queue.insert(0,s)
    if found:
        printPath(found)
        print("find solution")
    else:
        print("solution not found")

print("BFS for 8 puzzle")
start = Node([2,0,1,4,5,3,8,7,6])
goal = Node([1,2,3,4,5,6,7,8,0])

BFS(start,goal)
