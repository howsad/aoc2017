class StreamProcessor:
    READING = 1
    GARBAGE = 2
    IGNORE = 3
    FINISHED = 4
    ERROR = 5

    def __init__(self):
        self.stack = []
        self.state = StreamProcessor.READING
        self.position = 0
        self.score = 0
        self.garbage_count = 0

    def read(self, c):
        if c == '{':
            self.stack.append(c)
        elif c == '}':
            self.score += len(self.stack)
            if len(self.stack) == 0 or self.stack.pop() != '{':
                self.state = StreamProcessor.ERROR
                return
            if len(self.stack) == 0:
                self.state = StreamProcessor.FINISHED
        elif c == '<':
            self.stack.append(c)
            self.state = StreamProcessor.GARBAGE
        elif c == '!':
            self.state = StreamProcessor.IGNORE

    def ignore(self, c):
        self.state = {
            '{': StreamProcessor.READING,
            '<': StreamProcessor.GARBAGE
        }[self.stack[-1]]

    def garbage(self, c):
        if c == '>':
            if len(self.stack) == 0 or self.stack.pop() != '<':
                self.state = StreamProcessor.ERROR
            else:
                self.state = StreamProcessor.READING
        elif c == '!':
            self.state = StreamProcessor.IGNORE
        else:
            self.garbage_count += 1

    def process(self, stream):
        c = stream[self.position]
        {
            StreamProcessor.READING: self.read,
            StreamProcessor.GARBAGE: self.garbage,
            StreamProcessor.IGNORE: self.ignore,
        }[self.state](c)
        self.position += 1

    def can_process(self):
        return self.state != StreamProcessor.FINISHED \
               and self.state != StreamProcessor.ERROR


stream = input()
processor = StreamProcessor()
while processor.can_process():
    processor.process(stream)
if processor.state == StreamProcessor.ERROR:
    print("Error! Current position = %d, current stack = %s" %
          (processor.position, processor.stack))
else:
    print("Score = %d, garbage_count = %d" %
          (processor.score, processor.garbage_count))
