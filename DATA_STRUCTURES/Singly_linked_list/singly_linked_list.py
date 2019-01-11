class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def detect_cycle(head):
    seen = []
    node = head
    while node.next is not None:
        if node.next in seen:
            return True
        seen.append(node)
        node = node.next
    return False


def detect_cycle_2_pointers(head):
    pointer_1 = head
    pointer_2 = head
    while pointer_2.next is not None and pointer_2.next.next is not None:
        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.next.next
        if pointer_2 == pointer_1:
            return True
    return False
