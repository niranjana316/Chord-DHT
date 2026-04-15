import random
import math

class Node:
    def __init__(self, id, m):
        self.id = id
        self.m = m
        self.finger = []

class Chord:
    def __init__(self, n, m=4):
        self.m = m
        self.nodes = sorted([random.randint(0, 2**m - 1) for _ in range(n)])
        self.node_objs = [Node(i, m) for i in self.nodes]

    def successor(self, id):
        for n in self.nodes:
            if n >= id:
                return n
        return self.nodes[0]

    def build_finger_table(self):
        for node in self.node_objs:
            node.finger = []
            for i in range(self.m):
                start = (node.id + 2**i) % (2**self.m)
                node.finger.append(self.successor(start))

def lookup(self, start, key):
    path = [start]
    current = start

    while True:
        # find closest node using finger table
        node_obj = next(n for n in self.node_objs if n.id == current)

        next_node = None
        for finger in reversed(node_obj.finger):
            if current < finger <= key or (key < current and (finger > current or finger <= key)):
                next_node = finger
                break

        if next_node is None:
            next_node = self.successor(key)

        path.append(next_node)

        if next_node == self.successor(key):
            break

        current = next_node

    return path
