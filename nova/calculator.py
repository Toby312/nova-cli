import ast
import operator


OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
}


def calculate(expression: str):
    """
    Safely evaluate a basic mathematical expression.
    """

    try:
        tree = ast.parse(expression, mode="eval")

        def evaluate(node):

            if isinstance(node, ast.Expression):
                return evaluate(node.body)

            elif isinstance(node, ast.Constant):
                if isinstance(node.value, (int, float)):
                    return node.value

                raise ValueError("Invalid number.")

            elif isinstance(node, ast.BinOp):
                operation = OPERATORS.get(type(node.op))

                if operation is None:
                    raise ValueError("Unsupported operation.")

                left = evaluate(node.left)
                right = evaluate(node.right)

                return operation(left, right)

            else:
                raise ValueError("Invalid expression.")

        return evaluate(tree)

    except ZeroDivisionError:
        return "You cannot divide by zero."

    except (SyntaxError, ValueError, TypeError):
        return "Invalid mathematical expression."