import sys
import re
from collections import Counter


class Program:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.children = []
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return "name = %s, weight = %s, children = %s" % \
               (self.name, self.weight, self.children)


def to_list(children_string):
    if children_string is None:
        return []
    return children_string.split(', ')


def read_program_definition(s):
    match = re.fullmatch('([a-z]+) \((\d+)\)(?: -> ([a-z, ]+))?', s)
    return Program(
        match.group(1),
        int(match.group(2))
    ), to_list(match.group(3))


def read_programs():
    programs = {}
    child_name_to_parent = {}
    lines = sys.stdin.readlines()
    for line in lines:
        program, children = read_program_definition(line.strip())
        programs[program.name] = program
        for child in children:
            child_name_to_parent[child] = program
    for child_name in child_name_to_parent:
        parent = child_name_to_parent[child_name]
        child = programs[child_name]
        parent.add_child(child)
        child.set_parent(parent)
    return programs

some_program = next(iter(read_programs().values()))
while some_program.parent is not None:
    some_program = some_program.parent


def dfs(root):
    children_dfs = [dfs(child) for child in root.children]
    bad_children = list(filter(lambda x: x[2] > 0, children_dfs))
    if len(bad_children) > 0:
        return bad_children[0]
    children_weights = [x[1] for x in children_dfs]
    weight_counter = Counter(children_weights)
    if len(weight_counter) < 2:
        return root, root.weight + sum(children_weights), 0
    common_weight = weight_counter.most_common(1)[0][0]
    bad_child = next(filter(
        lambda x: x[1] != common_weight, children_dfs)
    )
    desired_weight = common_weight - bad_child[1] + bad_child[0].weight
    return bad_child, bad_child[1], desired_weight

print(some_program)
print(dfs(some_program)[2])
