pylint solution.py --disable=all --enable=syntax-error --score=no --msg-template="{path}, Zeile {line}: {msg}" --output=linter_output.txt

if [ ! $? -eq 0 ]; then	
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Ihr Code enthält Syntax-Fehler:" | fold -s
	echo "	"
	cat linter_output.txt | fold -s
	echo "	"
	echo "Falls es sich um eine Fehlermeldung zur 'indentation' (Einrückung) handelt, prüfen Sie noch einmal, ob Sie entweder überall Tabs oder überall Leerzeichen zur Einrückung verwendet haben." | fold -s
	echo "	"
	echo "Um Fehler beim Kopieren in GitLab auszuschließen, stellen Sie sicher, dass Sie den kompletten Inhalt Ihrer lokal getesteten Datei markiert und kopiert haben. Alternativ verwenden Sie statt dem 'Edit'-Button den 'Replace'-Button, um Ihre lokal getestete Datei abzugeben." | fold -s
	echo "	"
	echo "###############################################################################"
	exit 1
fi

pylint solution.py --disable=all --enable=deprecated_builtins,forbid_import_token,forbid_internal_vars_and_funcs,wrong_program_structure --load-plugins=pylint.extensions.bad_builtin,forbid_import,structure_check,forbid_internal_vars_and_funcs --bad-functions=input,sorted,reversed,__import__,eval,exec,vars --score=no --msg-template="{path}, Zeile {line}: {msg}" --output=linter_output.txt

if [ ! $? -eq 0 ]; then	
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Lesen Sie noch einmal die allgemeinen Hinweise in der Aufgabenstellung genau durch. Ihr Code hält sich nicht an die Vorgaben:" | fold -s
	echo "	"
	cat linter_output.txt | fold -s
	echo "	"
	echo "###############################################################################"
	exit 1
fi
