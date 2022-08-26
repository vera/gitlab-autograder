pylint solution.py --disable=all --enable=syntax-error --score=no --msg-template="{path}, line {line}: {msg}" --output=linter_output.txt

if [ ! $? -eq 0 ]; then	
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Your code contains syntax errors:" | fold -s
	echo "	"
	cat linter_output.txt | fold -s
	echo "	"
	echo "If the error message is related to 'indentation', check again whether you have consistently used either only spaces or only tabs to indent your code." | fold -s
	echo "	"
	echo "###############################################################################"
	exit 1
fi

pylint solution.py --disable=all --enable=deprecated_builtins,forbid_import_token,forbid_internal_vars_and_funcs,wrong_program_structure --load-plugins=pylint.extensions.bad_builtin,forbid_import,structure_check,forbid_internal_vars_and_funcs --bad-functions=input,sorted,reversed,__import__,eval,exec,vars --score=no --msg-template="{path}, line {line}: {msg}" --output=linter_output.txt

if [ ! $? -eq 0 ]; then	
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Please read the general guidelines in the task description again. Your code does not adhere to these guidelines:" | fold -s
	echo "	"
	cat linter_output.txt | fold -s
	echo "	"
	echo "###############################################################################"
	exit 1
fi
