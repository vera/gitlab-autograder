if python3 -m unittest VerificationTestSuite.py &> /dev/null; then
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "SUPER!"
	echo "	"
	echo "Du hast alle Tests bestanden!"
	echo "	"
	echo "###############################################################################"
else
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Deine Lösung ist nicht korrekt, denn sie besteht nicht alle unsere Tests."
	echo "	"
	echo "Deine Lösung muss auch mit anderen Eingaben als mit denen aus der Aufgaben-"
	echo "stellung das richtige Ergebnis liefern!"
	echo "	"
	echo "TIPP: Überlege dir ein paar eigene weitere Testfälle und teste deine Lösung"
	echo "selbst damit."
	echo "	"
	echo "###############################################################################"
	exit 1
fi
