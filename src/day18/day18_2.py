from day18.duet_2 import SendReceiveProcessor, read_input, Pipe

commands = read_input()
pipe = Pipe()
p0 = SendReceiveProcessor(0, commands, pipe)
p1 = SendReceiveProcessor(1, commands, pipe)
current_p = p0
while True:
    current_p.nxt()
    if current_p.is_done():
        current_p = pipe.from_to[current_p]
        current_p.nxt()
        if current_p.is_done():
            break
    while not current_p.is_done():
        current_p.nxt()
    current_p = pipe.from_to[current_p]
print(p1.snd_count)
