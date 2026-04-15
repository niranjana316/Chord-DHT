def lookup(self, start, key):
    path = [start]
    current = start

    while True:
        node_obj = next(n for n in self.node_objs if n.id == current)

        next_node = None

        for finger in reversed(node_obj.finger):
            if current < key:
                if current < finger <= key:
                    next_node = finger
                    break
            else:
                if finger > current or finger <= key:
                    next_node = finger
                    break

        if next_node is None:
            next_node = self.successor(key)

        path.append(next_node)

        if next_node == self.successor(key):
            break

        current = next_node

    return path
