import sys
import re


def read_instructions():
    return sys.stdin.readlines()


def create_registers(register_names, registers):
    for register in register_names:
        if not registers.__contains__(register):
            registers[register] = 0


def process_instruction(s, registers):
    match = re.fullmatch('([a-z]+) (inc|dec) (-?\d+) '
                         'if ([a-z]+) (<|<=|==|!=|>|>=) (-?\d+)', s)
    changed_register_name = match.group(1)
    compared_register_name = match.group(4)
    create_registers([changed_register_name, compared_register_name], registers)
    condition = {
        '<': lambda x, y: x < y,
        '<=': lambda x, y: x <= y,
        '==': lambda x, y: x == y,
        '!=': lambda x, y: x != y,
        '>': lambda x, y: x > y,
        '>=': lambda x, y: x >= y,
    }[match.group(5)](registers[compared_register_name], int(match.group(6)))
    if condition:
        addend = {
            'inc': lambda x: x,
            'dec': lambda x: -x
        }[match.group(2)](int(match.group(3)))
        registers[changed_register_name] += addend
        return registers[changed_register_name]
    else:
        return None


registers = {}
instructions = read_instructions()
register_value_history = [0]
for instruction in instructions:
    reg_value = process_instruction(instruction.strip(), registers)
    if reg_value is not None:
        register_value_history.append(reg_value)
print(max(register_value_history))
