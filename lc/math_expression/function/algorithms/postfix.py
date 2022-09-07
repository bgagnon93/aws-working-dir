from data_structures.stack import Stack
from data_structures.queue import Queue

def postfix(expression):
    # In a postfix expression, whenever an operator is encountered, the previous two numbers in the expression are evaluated via that operator. 

    # First, create an operators dict. This dict contains the priority of each operator, so it will serve another purpose later. 
    operators = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2,
        "^": 3
    }

    # Split the expression into a linear array. Assume no spaces (unfortunately 😟)
    # TODO: Consider refactoring the below, I think I can do better, and combine it with the below while loop. 
    expression_queue = Queue()
    i = 0 # i will demark the start of a number. j will come to represent the location of a symbol, so i:j will be the index range for a number in the expression char array. 
    for j in range(0, len(expression)):
        if expression[j] in operators:
            expression_queue.enqueue(expression[i:j]) # number
            expression_queue.enqueue(expression[j]) # operator
            i = j + 1 # j is now indexed at the space one after the operator. 
    expression_queue.enqueue(expression[j:len(expression)]) # the last number must be appended to the array. 

    # The postfix_queue will contain the conditions for the postfix_expression. I am choosing a queue instead of a stack because I don't have to reverse the output of the stack when returning the postfix expression. 
    postfix_queue = Queue()

    # The operator_stack is a tool for managing the order of operations in the construction of the postfix expression. 
    operator_stack = Stack()

    # There is only one "dequeue" call per loop. This sounds obvious in hindsight, but if I update this to handle parenthesis, I should accept this fact as gospel. 
    while expression_queue.__len__() > 0:
        op = expression_queue.dequeue()

        # If the op is not an operator, then it should be added to the postfix_queue.
        if op not in operators:
            postfix_queue.enqueue(op)
        
        # Else, things get more complicated. The operator will always be added to the operator_stack, but before it does, a previously added operator in the operator_stack may be enqueued in the postfix_queue. This will happen for as many operators are of higher priority than the operator currently being evaluated. 
        # For example, if the current operator is '-', and the operator stack contains '*,^', the exponent '^' will be enqued to the postfix_queue first, followed by the multiplier '*'. Then, the subtractor '-' will be pushed to the operator stack. 
        else:
            while operator_stack.__len__() > 0:
                op0 = operator_stack.pop()
                if operators[op] <= operators[op0]:
                    postfix_queue.enqueue(op0)
                else:
                    operator_stack.push(op0)
                    break
            operator_stack.push(op)
            
    # All remaining operators in the operator stack must be enqueued in the postfix_queue. 
    while operator_stack.__len__() > 0:
        postfix_queue.enqueue(operator_stack.pop())

    # This is why I picked a queue instead of a stack, no reversal necessary. Just dequeue each operand/operator, and put a space between each one. 
    postfix_expression = postfix_queue.dequeue()
    while postfix_queue.__len__() > 0:
        postfix_expression += f" {postfix_queue.dequeue()}"

    return postfix_expression

