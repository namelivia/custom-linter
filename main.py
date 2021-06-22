from analyze import parse_file, analyze_function
from render.render import write_render_output, render_function, render_file
from parso.python.tree import Function
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("files", type=str, nargs='+')
parser.add_argument("--html", type=str)
arguments = parser.parse_args()

for input_file in arguments.files:
    render_file(input_file)
    code = parse_file(input_file)
    result = [analyze_function(node) for node in code.children if isinstance(node, Function)]
    [render_function(function) for function in result]
write_render_output(arguments.html)
