deadlineSec=$(date --date "$DEADLINE_TIMESTAMP" +'%s')
nowSec=$(date --date "$CI_COMMIT_TIMESTAMP" +'%s')

if [ $nowSec -gt $deadlineSec ]; then
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Ihre Abgabe ist zu spät!"
	echo "Es zählt Ihre letzte Abgabe vor der Deadline."
	echo "	"
	echo "###############################################################################"
	exit 1
else
	secondsLeft=$(expr $deadlineSec - $nowSec)
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo -n "Diese Abgabe wurde "
	printf '%d Tage, %d Stunden, %d Minuten und %d Sekunden vor der\n' $((secondsLeft/86400)) $((secondsLeft%86400/3600)) $((secondsLeft%3600/60)) $((secondsLeft%60))
	echo "Deadline gemacht."
	echo "	"
	echo "###############################################################################"
fi
