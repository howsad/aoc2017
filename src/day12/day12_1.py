import sys
import re


class Pipes:
    def __init__(self):
        self.graph = {}

    def add_node(self, p_id):
        if not self.graph.__contains__(p_id):
            self.graph[p_id] = set()

    def connect(self, in_id, out_ids):
        self.add_node(in_id)
        for out_id in out_ids:
            self.add_node(out_id)
            self.graph[in_id].add(out_id)
            self.graph[out_id].add(in_id)

    def get_connected_ids(self, p_id):
        s = set()
        self.fill_connected_ids(p_id, s)
        return s

    def fill_connected_ids(self, p_id, connected):
        connected.add(p_id)
        out_ids = self.graph[p_id]
        out_ids = out_ids.difference(connected)
        for out_id in out_ids:
            self.fill_connected_ids(out_id, connected)

    def count_groups(self):
        count = 0
        ids = set(self.graph.keys())
        while len(ids) > 0:
            count += 1
            group = self.get_connected_ids(next(iter(ids)))
            ids = ids.difference(group)
        return count


def read_line(line):
    match = re.fullmatch('(\d+) <-> ([0-9, ]+)', line)
    return match.group(1), match.group(2).split(', ')


pipes = Pipes()
for line in sys.stdin.readlines():
    pipes.connect(*read_line(line.strip()))
connected_to_0 = pipes.get_connected_ids('0')
print(len(connected_to_0))
print("groups count = %d" % pipes.count_groups())
