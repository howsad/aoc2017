import sys


def read_input():
    return [int(line.strip()) for line in sys.stdin.readlines()]


class Processor:
    JUMP = 1
    INCREMENT = 2
    CHECK_OOB = 3
    FINISH = 4

    def __init__(self):
        self.state = Processor.JUMP
        self.position = 0
        self.prev_position = 0
        self.jump_count = 0

    def jump(self, instructions):
        self.prev_position = self.position
        self.position += instructions[self.position]
        self.jump_count += 1
        self.state = Processor.CHECK_OOB

    def check_OOB(self, instructions):
        inbounds = 0 <= self.position < len(instructions)
        if inbounds:
            self.state = Processor.INCREMENT
        else:
            self.state = Processor.FINISH

    def increment(self, instructions):
        if self.position - self.prev_position > 2:
            instructions[self.prev_position] -= 1
        else:
            instructions[self.prev_position] += 1
        self.state = Processor.JUMP

    def step(self, instructions):
        {
            Processor.JUMP: self.jump,
            Processor.CHECK_OOB: self.check_OOB,
            Processor.INCREMENT: self.increment
        }[self.state](instructions)


instructions = read_input()
processor = Processor()
while processor.state != Processor.FINISH:
    processor.step(instructions)
print(processor.jump_count)