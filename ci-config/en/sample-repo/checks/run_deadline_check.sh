deadlineSec=$(date --date "$DEADLINE_TIMESTAMP" +'%s')
nowSec=$(date --date "$CI_COMMIT_TIMESTAMP" +'%s')

if [ $nowSec -gt $deadlineSec ]; then
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Your submission is too late!"
	echo "The result of your last submission prior to the deadline is your final result."
	echo "	"
	echo "###############################################################################"
	exit 1
else
	secondsLeft=$(expr $deadlineSec - $nowSec)
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo -n "This submission was made "
	printf '%d days, %d hours, %d minutes and %d seconds prior to the \n' $((secondsLeft/86400)) $((secondsLeft%86400/3600)) $((secondsLeft%3600/60)) $((secondsLeft%60))
	echo "deadline."
	echo "	"
	echo "###############################################################################"
fi
