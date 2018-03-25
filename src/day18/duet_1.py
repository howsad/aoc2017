def factory(f):
    def arithmetic_function(regs, x, y):
        regs[x] = f(regs.get(x, 0), resolve(regs, y))

    return arithmetic_function


def resolve(regs, x):
    if x.isalpha():
        return regs.get(x, 0)
    return int(x)


arithmetic = {
    'set': factory(lambda x, y: y),
    'add': factory(lambda x, y: x + y),
    'mul': factory(lambda x, y: x * y),
    'mod': factory(lambda x, y: x % y)
}


class Processor:
    DECIDE = -1
    ARITHMETIC = 0
    INC_PTR = 1
    SND = 2
    RCV = 3
    JMP = 4
    DONE = 5

    def __init__(self, commands):
        self.commands = commands
        self.c_ptr = 0
        self.state = Processor.DECIDE
        self.regs = {}
        self.freq = 0

    def get_cmd(self):
        return self.commands[self.c_ptr]

    def check_oob(self):
        return self.c_ptr < 0 or self.c_ptr >= len(self.commands)

    def decide(self):
        cmd = self.get_cmd()
        cmd_name = cmd[0]
        if cmd_name in arithmetic.keys():
            return Processor.ARITHMETIC
        if cmd_name == 'snd':
            return Processor.SND
        if cmd_name == 'rcv':
            return Processor.RCV
        if cmd_name == 'jgz':
            if resolve(self.regs, cmd[1]) > 0:
                return Processor.JMP
            else:
                return Processor.INC_PTR

    def nxt(self):
        if self.state == Processor.DECIDE:
            self.state = self.decide()
        elif self.state == Processor.ARITHMETIC:
            cmd = self.get_cmd()
            arithmetic[cmd[0]](self.regs, cmd[1], cmd[2])
            self.state = Processor.INC_PTR
        elif self.state == Processor.INC_PTR:
            self.c_ptr += 1
            self.state = Processor.DECIDE
            if self.check_oob():
                self.state = Processor.DONE
        elif self.state == Processor.SND:
            self.freq = resolve(self.regs, self.get_cmd()[1])
            self.state = Processor.INC_PTR
        elif self.state == Processor.RCV:
            if resolve(self.regs, self.get_cmd()[1]) != 0 and self.freq != 0:
                self.state = Processor.DONE
            else:
                self.state = Processor.INC_PTR
        elif self.state == Processor.JMP:
            self.c_ptr += resolve(self.regs, self.get_cmd()[2])
            self.state = Processor.DECIDE
            if self.check_oob():
                self.state = Processor.DONE

    def is_done(self):
        return self.state == Processor.DONE


def read_input():
    import sys
    return [line.strip().split() for line in sys.stdin.readlines()]
