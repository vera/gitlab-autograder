from pylint import checkers, interfaces

class ImportASTChecker(checkers.BaseChecker):
    __implements__ = interfaces.IAstroidChecker

    name = 'forbid_import_token'
    priority = -1
    msgs = {
        'C0001': (
            '\'import\'-Anweisungen dürfen nicht benutzt werden',
            'forbid-import-token',
            'No code should use "import" statements.',
        ),
    }

    def visit_import(self, node):
        self.add_message('forbid-import-token', node=node)

    def visit_importfrom(self, node):
        self.add_message('forbid-import-token', node=node)

def register(linter):
    linter.register_checker(ImportASTChecker(linter))
