from Hanoi.aima import PriorityQueue
from hanoi_states import StatesHanoi, ProblemHanoi
from tree_hanoi import NodeHanoi
from math import log2, log

# disks = 6
print("Disks|b*|nodes_used")
for disks in [1,2,3,4,5,6,7,8,9, 10]:
    # print(f'-----Caso Disco: {disks}')
    initial_state = StatesHanoi(list(range(disks,0,-1)), [], [], max_disks=disks)
    goal_state = StatesHanoi([], [], list(range(disks,0,-1)), max_disks=disks)
    problem = ProblemHanoi(initial=initial_state, goal=goal_state)
    explored = set()
    good_order = {tuple(range(disks, disks - (i + 1), -1)) for i in range(disks)}

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
        nodes_used.append(node)
        if problem.goal_test(node.state):
            last_node = node
            # print("Encontramos la solución")
            break
        for next_node in node.expand(problem):
            if next_node.state not in explored:
                pq.append(next_node)
                explored.add(next_node.state)
            elif next_node in pq:
                if f(next_node) < pq[next_node]:
                    del pq[next_node]
                    pq.append(next_node)

    # print('nodes used: ', len(nodes_used))
    N = len(nodes_used)
    h = (2**disks) -1
    b_star = 2**(log2(N+2)/(h+1))

    # N+1 = (b^(h+1)) -1
    # logb(N+2) = h+1
    # logb(N+2)-1 = heff
    # h_star = logb((N+2))

    # print('b*: ', b_star)

    h_star= log(N+2,3)
    k_h = h-h_star
    # print('k_h: ', k_h)
    # print('new_depth = ', h-k_h)
    # print('2^(new_depth)', 2**(h-k_h))

    print(f'{disks}|{b_star:.4f}|{len(nodes_used)}')

    node = last_node
    path = [last_node.state]
    while node.parent is not None:
        node = node.parent
        path.append(node.state)

    # for p in path[::-1]:
    #     print(p)
    nodes_cnt = len(path)
    transitions = nodes_cnt - 1
    # print(f'Cantidad de movimientos: {transitions}')

    # la heuristica a medida q vas agergando discos mejora
