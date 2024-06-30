import time
start = time.time()
from Hanoi.aima import PriorityQueue
from hanoi_states import StatesHanoi, ProblemHanoi
from tree_hanoi import NodeHanoi

initial_state = StatesHanoi([5, 4, 3, 2, 1], [], [], max_disks=5)
goal_state = StatesHanoi([], [], [5, 4, 3, 2, 1], max_disks=5)

problem = ProblemHanoi(initial=initial_state, goal=goal_state)

frontier = [NodeHanoi(problem.initial)]
explored = set()

# good_order = [[5,4,3,2,1],[5,4,3,2],...,[5]]
good_order = {tuple(range(5, 5 - (i + 1), -1)) for i in range(5)}


def h(new_node):
    rod_3 = new_node.state.rods[2]
    return -len(rod_3) if tuple(rod_3) in good_order else 0


def f(new_node):
    return new_node.path_cost + h(new_node)

pq = PriorityQueue(order='min', f=f)
pq.append(NodeHanoi(problem.initial))

while len(frontier) != 0:
    node = pq.pop()
    explored.add(node.state)

    if problem.goal_test(node.state):
        last_node = node
        print("Encontramos la solución")
        break
    for next_node in node.expand(problem):
        if next_node.state not in explored:
            pq.append(next_node)
            frontier.insert(0, next_node)
end = time.time()
print(len(explored), "nodos se expandieron y", len(frontier), "nodos quedaron en la frontera")
print(end - start)