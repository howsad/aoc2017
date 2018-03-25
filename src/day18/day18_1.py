from day18.duet_1 import Processor, read_input

commands = read_input()
processor = Processor(commands)
while not processor.is_done():
    processor.nxt()
print(processor.freq)
