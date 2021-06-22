import parso
from data.function import Function


def parse_file(path: str):
    with open(path, "r") as code_file:
        return parso.parse(code_file.read(), version="3.9")


def analyze_function(node):
    my_function = Function(node)
    my_function.analyze_parameters()
    return my_function
