import time
from hanoi_states import StatesHanoi, ProblemHanoi
from tree_hanoi import NodeHanoi
import heapq

initial_state = StatesHanoi([5, 4, 3, 2, 1], [], [], max_disks=5)
goal_state = StatesHanoi([], [], [5, 4, 3, 2, 1], max_disks=5)

problem = ProblemHanoi(initial=initial_state, goal=goal_state)

frontier = []
explored = set()

# good_order = {(5,4,3,2,1),(5,4,3,2),...,(5)}
good_order = {tuple(range(5, 5 - (i + 1), -1)) for i in range(5)}

def h(node):
    rod_3 = node.state.rods[2]
    return -len(rod_3) if tuple(rod_3) in good_order else 0

def f(new_node):
    return new_node.path_cost + h(new_node)

heapq.heappush(frontier, (f(NodeHanoi(problem.initial)), NodeHanoi(problem.initial)))
end = 0
start = time.time()
while frontier:
    _, node = heapq.heappop(frontier)
    explored.add(node.state)

    if problem.goal_test(node.state):
        end = time.time()
        print("Llegamos a la solucion")
        last_node = node
        break

    for next_node in node.expand(problem):
        if next_node.state not in explored:
            heapq.heappush(frontier, (f(next_node), next_node))
            explored.add(next_node.state)  # Add to explored to avoid re-expanding

print(len(explored), "nodos se expandieron y", len(frontier), "nodos quedaron en la frontera")
print(end - start)
# nuestro ( con cola de prioridad + heuristica) => 0.11039423942565918
# original => 0.09908318519592285