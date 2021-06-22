from analyze import parse_file, analyze_function
from render.render import write_render_output, render_function, render_file
from parso.python.tree import Function, Class, PythonNode
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("files", type=str, nargs='+')
parser.add_argument("--html", type=str)
arguments = parser.parse_args()

for input_file in arguments.files:
    result = []
    render_file(input_file)
    code = parse_file(input_file)
    for node in code.children:
        if isinstance(node, Class):
            for node in node.iter_funcdefs():
                result.append(analyze_function(node))
        if isinstance(node, Function):
            result.append(analyze_function(node))
    [render_function(function) for function in result]
write_render_output(arguments.html)
