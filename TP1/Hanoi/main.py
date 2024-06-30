import time
from hanoi_states import StatesHanoi, ProblemHanoi
from tree_hanoi import NodeHanoi
import heapq

initial_state = StatesHanoi([5, 4, 3, 2, 1], [], [], max_disks=5)
goal_state = StatesHanoi([], [], [5, 4, 3, 2, 1], max_disks=5)

problem = ProblemHanoi(initial=initial_state, goal=goal_state)

frontier = [NodeHanoi(problem.initial)]
explored = set()

# good_order = {(5,4,3,2,1),(5,4,3,2),...,(5)}
good_order = [tuple(range(5, 5 - (i + 1), -1)) for i in range(5)]
good_order_set = set(good_order) #Es mas rapido buscar en un set

end = 0
start = time.time()
while len(frontier) != 0:
    node = frontier.pop()
    explored.add(node.state)

    if problem.goal_test(node.state):
        end = time.time()
        last_node = node
        print("Encontramos la solución")
        break

    priority_queue = []
    actions = problem.actions(node.state)
    for i, next_node in enumerate(node.expand(problem)):
        rod_3 = next_node.state.rods[2]
        h = -len(rod_3) if rod_3 in good_order else 0
        curr_cost = h + actions[i].cost
        heapq.heappush(priority_queue, (curr_cost, next_node))

    sorted_nodes = [heapq.heappop(priority_queue)[1] for _ in range(len(priority_queue))]

    for next_node in sorted_nodes:
        if next_node.state not in explored:
            frontier.insert(0, next_node)

print(len(explored), "nodos se expandieron y", len(frontier), "nodos quedaron en la frontera")

end = time.time()
print(end - start)
# nuestro ( con cola de prioridad + heuristica) => 0.11039423942565918
# original => 0.09908318519592285