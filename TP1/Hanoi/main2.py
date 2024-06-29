import time

from Hanoi.aima import PriorityQueue

start = time.time()

from hanoi_states import StatesHanoi, ProblemHanoi
from tree_hanoi import NodeHanoi

initial_state = StatesHanoi([5, 4, 3, 2, 1], [], [], max_disks=5)
goal_state = StatesHanoi([], [], [5, 4, 3, 2, 1], max_disks=5)

problem = ProblemHanoi(initial=initial_state, goal=goal_state)

frontier = [NodeHanoi(problem.initial)]
explored = set()

# good_order = [[5,4,3,2,1],[5,4,3,2],...,[5]]
good_oder = [list(range(5, 5 - (i + 1), -1)) for i in range(5)]


def h(node):
    rod_3 = node.state.rods[2]
    h_ = -len(rod_3) if rod_3 in good_oder else 0
    return h_


def f(new_node):
    return new_node.path_cost + h(new_node)

priority_queue = PriorityQueue(order='min', f=f)


while len(frontier) != 0:
    node = frontier.pop()
    explored.add(node.state)

    if problem.goal_test(node.state):
        last_node = node
        print("Encontramos la solución")
        break

    priority_queue.extend(node.expand(problem))

    while len(priority_queue) != 0:
        next_node = priority_queue.pop()
        if next_node.state not in explored:
            frontier.insert(0, next_node)

print(len(explored), "nodos se expandieron y", len(frontier), "nodos quedaron en la frontera")

end = time.time()
print(end - start)