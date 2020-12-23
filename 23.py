from collections import defaultdict


class DLList(object):
    class Node(object):
        def __init__(self, value, previous=None, next=None):
            self.value = value
            self.previous = previous
            self.next = next

    def __init__(self):
        self.head = None
        self.nodes = defaultdict(self.Node)

    def read_input(self, numbers):
        self.head = self.Node(numbers[0])
        previous = self.head
        self.nodes[previous.value] = previous
        for value in numbers[1:]:
            node = self.Node(value, previous)
            previous.next = node
            previous = node
            self.nodes[previous.value] = previous
        self.head.previous = previous
        previous.next = self.head

    def run(self, moves, length, first_part=True):
        move = 0
        current = self.head
        while move != moves:
            next_node = current.next
            third_next_node = next_node.next.next
            picked = {next_node.value, next_node.next.value, third_next_node.value}
            current.next = third_next_node.next
            current.next.previous = current
            destination = None
            while destination is None or destination in picked:
                if destination is None:
                    destination = (current.value - 1)
                    destination %= length
                else:
                    destination -= 1
                    destination %= length
                destination = length if destination == 0 else destination
            destination_node = self.nodes[destination]
            third_next_node.next = destination_node.next
            destination_node.next.previous = third_next_node
            destination_node.next = next_node
            current = current.next
            move += 1
        if first_part:
            solved_current = self.nodes[1]
            result = ""
            for i in range(length-1):
                result += str(solved_current.next.value)
                solved_current = solved_current.next
            return result
        return self.nodes[1].next.value * self.nodes[1].next.next.value


def solve():
    #inputo = [3, 8, 9, 1, 2, 5, 4, 6, 7]
    inputo = [1, 8, 6, 5, 2, 4, 9, 7, 3]
    moves = 100
    dllist = DLList()
    dllist.read_input(inputo)
    print(dllist.run(moves, len(inputo)))
    inputo += [val for val in range(max(inputo) + 1, 1000001)]
    moves = 10000000
    dllist = DLList()
    dllist.read_input(inputo)
    print(dllist.run(moves, len(inputo), False))


solve()

