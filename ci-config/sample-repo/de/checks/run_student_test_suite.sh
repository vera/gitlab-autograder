if ! python3 -m unittest StudentTestSuite.py &> /dev/null; then
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Deine Lösung ist nicht korrekt! Sie besteht nicht alle Tests aus der Student-"
	echo "Test-Suite, die euch zur Verfügung steht."
	echo "	"
	echo "TIPP: Teste deine Lösung *immer* zuerst selbst, bevor du sie hochlädst! Führe"
	echo "dafür in dem Verzeichnis, in dem die Test-Suite und deine Lösung liegen,"
	echo "den folgenden Befehl aus:"
	echo "	"
	echo "	python3 -m unittest StudentTestSuite.py"
	echo "	"
	echo "###############################################################################"
	exit 1
fi
