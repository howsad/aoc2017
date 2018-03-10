import re
import sys


class Firewall:
    def __init__(self, depths):
        self.depths = depths
        self.time = 0

    def next(self):
        self.time += 1

    def set_time(self, time):
        self.time = time

    def is_detected(self, layer):
        depth = self.depths.get(layer)
        if depth is None:
            return False
        return self.time % ((depth - 1) * 2) == 0

    def severity(self, layer):
        if self.is_detected(layer):
            return layer * self.depths[layer]
        return 0


def read_depths():
    lines = sys.stdin.readlines()
    depths = {}
    for line in lines:
        match = re.fullmatch('(\d+): (\d+)', line.strip())
        depths[int(match.group(1))] = int(match.group(2))
    return depths


depths = read_depths()
firewall = Firewall(depths)
total_severity = 0
max_depth = max(depths.keys()) + 1
for current_level in range(0, max_depth):
    total_severity += firewall.severity(current_level)
    firewall.next()
print("When going immediately total severity = %d" % total_severity)


def probe(firewall):
    for current_level in range(0, max_depth):
        if firewall.is_detected(current_level):
            return False
        firewall.next()
    return True


offset = 0
while True:
    firewall.set_time(offset)
    probe_result = probe(firewall)
    if probe_result:
        break
    else:
        offset += 1
print("In order to bypass unnoticed offset = %d" % offset)
