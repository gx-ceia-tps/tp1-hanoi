import time

start = time.time()


from hanoi_states import StatesHanoi, ProblemHanoi
from tree_hanoi import NodeHanoi

initial_state = StatesHanoi([5, 4, 3, 2, 1], [], [], max_disks=5)
goal_state = StatesHanoi([], [], [5, 4, 3, 2, 1], max_disks=5)

problem = ProblemHanoi(initial=initial_state, goal=goal_state)

frontier = [NodeHanoi(problem.initial)]
explored = set()

# good_order = [[5,4,3,2,1],[5,4,3,2],...,[5]]
good_oder = [list(range(5,5-(i+1), -1)) for i in range(5)]

while len(frontier) != 0:
    node = frontier.pop()
    explored.add(node.state)

    if problem.goal_test(node.state):
        last_node = node
        print("Encontramos la solución")
        break

    priority_queue = []
    actions = problem.actions(node.state)
    for i, next_node in enumerate(node.expand(problem)):
        rod_3 = next_node.state.rods[2]
        h = -len(rod_3) if rod_3 in good_oder else 0
        curr_cost = problem.path_cost(h=h, state1=node.state, action=actions[i], state2=next_node.state)
        priority_queue.append([curr_cost, next_node])

    sorted_nodes_and_prio = sorted(priority_queue, key=lambda x: x[0])
    sorted_nodes = [x[1] for x in sorted_nodes_and_prio]

    for next_node in sorted_nodes:
        if next_node.state not in explored:
            frontier.insert(0, next_node)

print(len(explored), "nodos se expandieron y", len(frontier), "nodos quedaron en la frontera")

end = time.time()
print(end - start)
# nuestro ( con cola de prioridad + heuristica) => 0.11039423942565918
# original => 0.09908318519592285