from DATA_STRUCTURES.Stack.stack import Stack


def check_balanced_parentheses(s):
    if len(s) % 2 != 0:
        return False

    stack = Stack()
    opening_parentheses = ['(', '[', '{']
    matches = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for item in s:
        if item in opening_parentheses:
            stack.push(item)
        elif not stack.is_empty() and stack.peek() == matches[item]:
            stack.pop()
        else:
            return False

    return stack.is_empty()


def check_balanced_parentheses_list(s):
    if len(s) % 2 != 0:
        return False

    stack = []
    opening_parentheses = ['(', '[', '{']
    matches = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for item in s:
        if item in opening_parentheses:
            stack.append(item)
        elif not len(stack) == 0 and stack[-1] == matches[item]:
            stack.pop()
        else:
            return False

    return len(stack) == 0
