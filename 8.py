from copy import deepcopy

"""reformatting just in case of reocurring later, paranoid from last year"""

"""CODE FORMAT: [instruction, value, line_index]"""


class BootCode(object):
    def __init__(self, file):
        self.file = file
        self.instructions_set = {"nop", "jmp", "acc"}
        self.code, self.code_length = self.read_file()
        self.accumulator = 0

    def read_file(self):
        instruction_index = 0
        code = []
        with open(self.file, 'r') as file:
            for line in file:
                value = line.strip().split()
                code.append(value + [instruction_index])
                instruction_index += 1
        return code, instruction_index

    def find_instructions(self, instruction_set):
        result = []
        for index, line in enumerate(self.code):
            if line[0] in instruction_set:
                result.append(line)
        return result

    def run(self, stop_on_last=False, stop_on_reused=False, code=None):
        if code is None:
            code = self.code
        self.accumulator = 0
        index = 0
        used_indeces = set()
        normal_finish = False
        while 1:
            instruction, value, index = code[index]
            if index in used_indeces and stop_on_reused:
                break
            used_indeces.add(index)
            if instruction == "nop":
                index += 1
            elif instruction == "jmp":
                index += int(value)
            elif instruction == "acc":
                self.accumulator += int(value)
                index += 1
            else:
                if instruction not in self.instructions_set:
                    raise Exception("Instruction not yet discovered!")
                raise Exception("Missing instruction response!")
            if index == self.code_length and stop_on_last:
                normal_finish = True
                break
        return self.accumulator, normal_finish

    def eight_one(self):
        value, _ = self.run(False, True, None)
        self.print_result(value, "8.1")
        return value

    def eight_two(self):
        instructions = self.find_instructions({"jmp", "nop"})
        for instruction, _, line_index in instructions:
            new_code = deepcopy(self.code)
            if instruction == "jmp":
                new_code[line_index][0] = "nop"
            elif instruction == "nop":
                new_code[line_index][0] = "jmp"
            else:
                raise Exception("Badly found instructions!")
            value, finish = self.run(True, True, new_code)
            if finish:
                self.print_result(value, "8.2")
                return value
        raise Exception("Something went wrong!")

    def print_result(self, value, task):
        print()
        print(f"Result for task {task} is {value}")
        print()


if __name__ == "__main__":
    FILE_NAME = "input8.in"
    bc = BootCode(FILE_NAME)
    bc.eight_one()
    bc.eight_two()