from tree import TreeNode, generate_tree

def print_tree(node, level=0):
    if node is not None:
        print('  ' * level + node.state + ' - Circle: ' +
              str(node.circle_points) + ', Cross: ' + str(node.cross_points))

        for child in node.children:
            print_tree(child, level + 1)

def generate_tree_graph(n, i=0, graph=''):
    if i == 0:
        graph += 'digraph {\n'
        graph += 'node [shape=record]\n'

    idx = n.changed_index

    if idx > -1:
        state = n.state[:idx] + f'<u>{n.state[idx]}</u>' + n.state[idx+1:]
    else:
        state= n.state

    label = f'{n.circle_points}|{state}|{n.cross_points}|@{n.player}'

    if type(n).__name__ == 'MinimaxNode':
        label += f'|{n.heuristic_value}'

    graph += f'n{i} [label=<{label}>]\n'

    ni = i + 1
    for c in n.children:
        graph += f'n{i} -> n{ni}\n'
        graph, ni = generate_tree_graph(c, ni, graph)

    if i == 0:
        graph += '}'
        return graph

    return graph, ni

def debug_heuristic1(node, opponent):
    circle_points = node.circle_points
    cross_points = node.cross_points

    if opponent == 'X':
        return circle_points - cross_points
    elif opponent == 'O':
        return cross_points - circle_points

def debug_heuristic2(node, opponent):
    return max(min(debug_heuristic1(node, opponent), 1), -1)

def run_example():
    root_state = 'XXOOXOOX'
    root_player_type = 'O'
    root_node = TreeNode(root_state, root_player_type)
    generate_tree(root_node, 1)
    print(generate_tree_graph(root_node))

if __name__ == '__main__':
    run_example()