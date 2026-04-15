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
            next_node = self.successor(key)
            if current == next_node:
                break
            path.append(next_node)
            break

        return path
