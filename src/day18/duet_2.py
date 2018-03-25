from day18.duet_1 import *
from collections import deque


class SendReceiveProcessor(Processor):
    def __init__(self, id_, commands, pipe):
        super().__init__(commands)
        self.queue = deque()
        self.pipe = pipe
        pipe.register(self)
        self.id_ = id_
        self.regs['p'] = id_
        self.snd_count = 0

    def receive(self, msg):
        self.queue.appendleft(msg)

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
            self.pipe.receive(self, resolve(self.regs, self.get_cmd()[1]))
            self.snd_count += 1
            self.state = Processor.INC_PTR
        elif self.state == Processor.RCV:
            if len(self.queue) != 0:
                val = self.queue.pop()
                self.regs[self.get_cmd()[1]] = val
                self.state = Processor.INC_PTR
        elif self.state == Processor.JMP:
            self.c_ptr += resolve(self.regs, self.get_cmd()[2])
            self.state = Processor.DECIDE
            if self.check_oob():
                self.state = Processor.DONE

    def is_done(self):
        return super().is_done() or self.state == Processor.RCV


class Pipe:
    def __init__(self):
        self.first = None
        self.second = None
        self.from_to = {}

    def register(self, p):
        if self.first is None:
            self.first = p
        else:
            self.second = p
            self.from_to = {
                self.first: p,
                p: self.first
            }

    def receive(self, from_, msg):
        self.from_to[from_].receive(msg)
