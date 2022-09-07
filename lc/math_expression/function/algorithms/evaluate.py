from data_structures.stack import Stack


# Evaluate the postfix expression, and return a number. 
# The request will be of the form: "14 3 10 2 ^ * 5 / + 1 -", with one space between each operand/operator.
# The response will be a number, but will not necessarily be an Integer. 
def evaluate_postfix_expression(postfix_expression):
    operators = ["+", "-", "*", "/", "^"]
    
    # Split the expression into an array, where each element is an operand or operator. 
    # "14 3 10 2 ^ * 5 / + 1 -" ==> [14,3,10,2,^,*,5,/,+,1,-]
    expression_arr = postfix_expression.split(" ")

    stack = Stack()
    
    # For each element in the array
    #   If the element is an operand, push the operand to the stack. 
    #   If the element is an operator, pop the most recent two operands from the stack and perform the designated operation on them. 
    for op in expression_arr:
        if op in operators:

            # The second operand pops first. This is a problem for division, because the second operand (which should be the denominator) will be used as the numerator. 
            # Although I could get creative (division is inverse multiplication, subtraction is inverse addition), I prefer to just create two new variables for these operands, so I may pass them in whichever order I choose for each operator. 
            op1 = stack.pop()
            op0 = stack.pop()
            
            if op == "+":
                stack.push(op0 + op1)
            elif op == "-":
                stack.push(op0 - op1)
            elif op == "*":
                stack.push(op0 * op1)
            elif op == "/":
                stack.push(op0 / op1)
            else: # op is "^"
                stack.push(op0 ** op1)
        else:
            stack.push(int(op))
    
    # After evaluating the for loop, the stack should be of size = 1 (the solution). Just return that value. 
    return stack.pop()
