from scipy import optimize

__all__ = ["run_calculation"]


INITIAL_GUESS = 2

_value_a = 0
_value_b = 0
_target = 0


def equation(x, a, b, target):
    return x**a + b**x - target


def equation_to_solve(x):
    return equation(x, _value_a, _value_b, _target)


def run_calculation(value_a, value_b, target, method="fsolve"):
    global _value_a
    global _value_b
    global _target
    _value_a = value_a
    _value_b = value_b
    _target = target

    value_x = None
    if method == "fsolve":
        _tmp = optimize.fsolve(equation_to_solve, INITIAL_GUESS)
        value_x = _tmp[0]
    elif method == "newton":
        value_x = optimize.newton(equation_to_solve, INITIAL_GUESS)

    if not value_x:
        raise ValueError("Something went wrong")

    return value_x
