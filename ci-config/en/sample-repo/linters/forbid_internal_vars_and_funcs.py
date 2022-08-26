from pylint import checkers, interfaces

class InternalVarsAndFuncsASTChecker(checkers.BaseChecker):
    __implements__ = interfaces.IAstroidChecker

    name = 'forbid_internal_vars_and_funcs'
    priority = -1
    msgs = {
        'C0003': (
            'Python-internal variables or functions (e.g. "__builtins__") are not allowed to be used',
            'forbid-internal-vars-and-funcs',
            'No code should use internal variables or functions.',
        ),
    }

    def visit_name(self, node):
        if node.name[:2] == '__' and node.name[-2:] == '__':
        	self.add_message('forbid-internal-vars-and-funcs', node=node)

def register(linter):
    linter.register_checker(InternalVarsAndFuncsASTChecker(linter))
