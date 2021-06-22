from parso.python.tree import Param, Operator
from .parameter import Parameter


class Function:
    def __init__(self, node):
        self.warnings = []
        self.node = node
        self.params = []
        self.name = node.name.value

    def is_param_a_bolean(self, param):
        if param.annotation is not None:
            return param.annotation.value == "bool"

    def add_warning(self, contents: str):
        self.warnings.append(contents)

    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

    def check_booleans_should_go_last(self, *, is_bool_already_found):
        if is_bool_already_found:
            self.warnings.append(
                "Warning, boolean arguments should go after non bool ones"
            )

    def check_parameter_number(self, num_params: int):
        if (num_params > 5):
            self.warnings.append("Warning, this function has too many params")

    def analyze_parameters(self):
        bool_already_found = False
        on_keyword_params = False

        for item in self.node.children[2].children:
            if isinstance(item, Param):
                param = Parameter(item, is_keyword=on_keyword_params)
                self.params.append(param)

                if (param.is_boolean()):
                    self.check_booleans_should_go_last(is_bool_already_found=bool_already_found)
                    bool_already_found = True

            if isinstance(item, Operator):
                if item.value == "*":
                    on_keyword_params = True

        self.check_parameter_number(len(self.params))
