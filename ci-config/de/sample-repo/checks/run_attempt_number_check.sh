commitCount=$(git rev-list --count $CI_COMMIT_SHA)
attemptCount=$(expr $commitCount - 1)
attemptsLeft=$(expr 3 - $attemptCount)

if [ $attemptCount -gt 3 ]; then
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Sie haben bereits alle drei Versuche aufgebraucht!"
	echo "Diese Abgabe wird daher nicht gezählt."
	echo "Es zählt das Ergebnis Ihrer dritten Abgabe."
	echo "	"
	echo "###############################################################################"
	exit 1
else

	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Sie haben nach dieser Abgabe noch $attemptsLeft Versuche übrig."
	echo "	"
	echo "###############################################################################"
fi
