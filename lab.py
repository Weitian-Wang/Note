import fileinput

class Node:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next

# create in reverse order
# number input as string
def create_list(num_list):
    new_node = None
    for num in num_list:
        new_node = Node(data = ord(num)-48, next = new_node)
    return new_node

def print_list(head):
    stack = []
    while head:
        stack.append(head.data)
        head = head.next
    while stack:
        print(stack.pop(), end="")
    print()

def add(head1, head2):
    rst = Node()
    cur = rst
    carry = 0
    while head1 and head2:
        new_node = Node((head1.data + head2.data + carry)%10)
        carry = (head1.data + head2.data + carry)//10
        cur.next = new_node
        cur = cur.next
        head1, head2 = head1.next, head2.next
    while head1:
        new_node = Node((head1.data + carry)%10)
        carry = (head1.data + carry)//10
        cur.next = new_node
        cur = cur.next
        head1 = head1.next
    while head2:
        new_node = Node((head2.data + carry)%10)
        carry = (head2.data + carry)//10
        cur.next = new_node
        cur = cur.next
        head2 = head2.next
    if carry:
        cur.next = Node(carry)
    return rst.next

def multiply_step(head1, digit, offset):
    if digit == 0:
        return None
    rst = Node()
    cur = rst
    carry = 0
    while head1:
        new_node = Node((head1.data * digit + carry)%10)
        carry = (head1.data * digit + carry)//10
        cur.next = new_node
        cur = cur.next
        head1 = head1.next
    if carry:
        cur.next = Node(carry)
    rst = rst.next
    for _ in range(offset):
        rst = Node(0, rst)
    return rst

def multiply(head1, head2):
    rst, step_rst = Node(0), Node(0)
    offset = 0
    # loop n2 times
    while head2:
        # n1 complexity
        step_rst = multiply_step(head1, head2.data, offset)
        # n1 complexity
        rst = add(rst, step_rst)
        head2 = head2.next
        offset += 1
    return rst

def main():
    input_list = [None, None]
    for idx, line in enumerate(fileinput.input()):
        input_list[idx] = create_list(line.strip('\n'))
    head1, head2 = input_list[0], input_list[1]
    print_list(head1)
    print_list(head2)
    print_list(multiply(head1,head2))

if __name__ == "__main__":
    main()