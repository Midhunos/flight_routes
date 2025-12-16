
def find_nth_node(root, direction, n):
    current = root

    for _ in range(n):
        next_node = current.children.filter(position=direction).first()
        if not next_node:
            return None
        current = next_node

    return current
