from function.algorithms.evaluate import evaluate_postfix_expression

def test_postfix_1():
    # FactSet Prompt
    expression = "7 8 + 3 2 * -"
    assert evaluate_postfix_expression(expression) == 9


def test_postfix_2():
    # Algebra instead of numbers
    expression = "4 18 2 * 6 / +"
    assert evaluate_postfix_expression(expression) == 10

def test_postfix_3():
    # Exponents
    expression = "6 14 4 * 2 3 ^ / +"
    assert evaluate_postfix_expression(expression) == 13

def test_postfix_4():
    # Increasing then decreasing order of operations
    expression = "6 3 10 2 ^ * 5 / + 7 -"
    assert evaluate_postfix_expression(expression) == 59

def test_postfix_5():
    # Simple expression
    expression = "6 18 +"
    assert evaluate_postfix_expression(expression) == 24

def test_postfix_6():
    # No operation
    expression = "4"
    assert evaluate_postfix_expression(expression) == 4

    