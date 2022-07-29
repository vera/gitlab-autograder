from astroid.nodes.scoped_nodes.scoped_nodes import FunctionDef, ClassDef
from astroid.nodes.node_classes import Assign
from pylint import checkers, interfaces

ALLOWED_GLOBAL_VARS = ["languagePopularity"]

class ProgramStructureASTChecker(checkers.BaseChecker):
	__implements__ = interfaces.IAstroidChecker

	name = 'wrong_program_structure'
	priority = -1
	msgs = {
		'C0002': (
			'Code außerhalb der Funktionen/Klassen',
			'wrong-program-structure',
			'The program structure must be according to the task description.',
		),
	}

	def visit_module(self, node):
		for subnode in node.body:
			if isinstance(subnode, Assign):
				if not (len(subnode.targets) == 1 and subnode.targets[0].name in ALLOWED_GLOBAL_VARS):
					self.add_message('wrong-program-structure', node=subnode)
			elif not (isinstance(subnode, FunctionDef) or isinstance(subnode, ClassDef)):
				self.add_message('wrong-program-structure', node=subnode)

def register(linter):
	linter.register_checker(ProgramStructureASTChecker(linter))
