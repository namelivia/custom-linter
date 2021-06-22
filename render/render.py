from yattag import Doc

doc, tag, text = Doc().tagtext()


def render_file(path):
    with tag('div'):
        with tag('h3'):
            text(path)


def render_function(function):
    with tag('div'):
        with tag('p'):
            with tag('b'):
                text(function.get_name())
        with tag('p'):
            text(f"Number of params: {len(function.params)}")

        if function.warnings:
            with tag('p'):
                with tag('b'):
                    text("WARNINGS")
            for warning in function.warnings:
                render_warning(warning)

        for param in function.params:
            render_param(param)


def render_param(param):
    with tag('p'):
        text(f"Name: {param.name}")
    with tag('p'):
        text(f"Position: {param.position_index}")
    with tag('p'):
        text(f"Star count: {param.star_count}")
    with tag('p'):
        text(f"Annotation: {param.annotation}")
    with tag('p'):
        text(f"Default: {param.default}")

    if param.warnings:
        with tag('p'):
            with tag('b'):
                text("WARNINGS")
        for warning in param.warnings:
            render_warning(warning)


def render_warning(contents: str):
    with tag('p'):
        with tag('b'):
            text(contents)


def write_render_output(path: str):
    with open(path, "w") as result_file:
        result_file.write(doc.getvalue())
