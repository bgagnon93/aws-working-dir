from function.algorithms.postfix import postfix

def test_postfix_1():
    # FactSet Prompt
    expression = "7+8-3*2"
    assert postfix(expression) == "7 8 + 3 2 * -"

def test_postfix_2():
    # Algebra instead of numbers
    expression = "A+B*C/E"
    assert postfix(expression) == "A B C * E / +"

def test_postfix_3():
    # Exponents
    expression = "A+B*C/E^F"
    assert postfix(expression) == "A B C * E F ^ / +"

def test_postfix_4():
    # Increasing then decreasing order of operations
    expression = "A+B*C^D/E-F"
    assert postfix(expression) == "A B C D ^ * E / + F -"

def test_postfix_5():
    # Simple expression
    expression = "A+B"
    assert postfix(expression) == "A B +"

def test_postfix_6():
    # No operation
    expression = "A"
    assert postfix(expression) == "A"
