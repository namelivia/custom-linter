class Parameter:
    def __init__(self, node, *, is_keyword):
        self.warnings = []
        self.node = node
        self.is_keyword = is_keyword
        if self.is_boolean() and not self.is_keyword:
            # TODO: I don't actually want this warning
            self.warnings.append("This parameter is boolean and not keyword")
        self.name = self.node.name.value
        self.position_index = self.node.position_index
        self.star_count = self.node.star_count
        try:
            self.annotation = self.node.annotation.value if self.node.annotation is not None else None
        except Exception:
            self.annotation = self.node.annotation.get_code()
        self.default = self.node.default.value if self.node.default is not None else None

    def is_boolean(self):
        try:
            return self.node.annotation.value == "bool"
        except Exception:
            return False
