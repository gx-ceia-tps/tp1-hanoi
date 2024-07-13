import time
from Hanoi.aima import PriorityQueue
from hanoi_states import StatesHanoi, ProblemHanoi
from tree_hanoi import NodeHanoi

initial_state = StatesHanoi([5, 4, 3, 2, 1], [], [], max_disks=5)
goal_state = StatesHanoi([], [], [5, 4, 3, 2, 1], max_disks=5)

problem = ProblemHanoi(initial=initial_state, goal=goal_state)

explored = set()

good_order = {tuple(range(5, 5 - (i + 1), -1)) for i in range(5)}


def h(new_node):
    rod_3 = new_node.state.rods[2]
    return -len(rod_3) if tuple(rod_3) in good_order else 0


def f(new_node):
    return new_node.path_cost + h(new_node)


pq = PriorityQueue(order='min', f=f)
pq.append(NodeHanoi(problem.initial))
nodes_used = []

while len(pq) != 0:
    node = pq.pop()
    explored.add(node.state)
    nodes_used.append(node)
    if problem.goal_test(node.state):
        last_node = node
        print("Encontramos la solución")
        break
    for next_node in node.expand(problem):
        if next_node.state not in explored:
            pq.append(next_node)
        elif next_node in pq:
            if f(next_node) < pq[next_node]:
                del pq[next_node]
                pq.append(next_node)


print('nodes used: ', len(nodes_used))
last_node.generate_solution_for_simulator()

ans = []
node = last_node
while node.parent is not None:
    print(node.state)
    node = node.parent
    ans.append(node)

depth = len(ans)
print(depth)


