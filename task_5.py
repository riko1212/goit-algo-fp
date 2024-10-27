import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="#000000"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Колір вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def build_tree_from_heap(heap):
    if not heap:
        return None

    nodes = [Node(val) for val in heap]

    for i in range(len(heap)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(heap):
            nodes[i].left = nodes[left_index]
        if right_index < len(heap):
            nodes[i].right = nodes[right_index]

    return nodes[0]  

def generate_colors(n):
    colors = []
    for i in range(n):
        intensity = int(255 * (i / (n - 1)))
        color = f'#{intensity:02x}{intensity:02x}ff' 
        colors.append(color)
    return colors

def depth_first_search(tree_root):
    stack = [tree_root]
    visited_nodes = []
    
    while stack:
        node = stack.pop()
        if node:
            visited_nodes.append(node)
            stack.append(node.right)
            stack.append(node.left)
    
    return visited_nodes

def breadth_first_search(tree_root):
    queue = deque([tree_root])
    visited_nodes = []

    while queue:
        node = queue.popleft()
        if node:
            visited_nodes.append(node)
            queue.append(node.left)
            queue.append(node.right)
    
    return visited_nodes

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, visited_nodes, colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    for i, node in enumerate(visited_nodes):
        node.color = colors[i] 

    node_colors = [tree.nodes[node.id]['color'] if node.id in pos else '#000000' for node in visited_nodes]
    labels = {node.id: node.val for node in visited_nodes}

    plt.figure(figsize=(10, 7))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=node_colors)
    plt.show()

heap = [10, 5, 3, 2, 4, 1]
tree_root = build_tree_from_heap(heap)

# Обхід в глибину
visited_dfs = depth_first_search(tree_root)
colors_dfs = generate_colors(len(visited_dfs))
draw_tree(tree_root, visited_dfs, colors_dfs)

# Обхід в ширину
visited_bfs = breadth_first_search(tree_root)
colors_bfs = generate_colors(len(visited_bfs))
draw_tree(tree_root, visited_bfs, colors_bfs)
