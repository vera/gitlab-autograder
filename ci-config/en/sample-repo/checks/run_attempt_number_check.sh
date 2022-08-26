commitCount=$(git rev-list --count $CI_COMMIT_SHA)
attemptCount=$(expr $commitCount - 1)
attemptsLeft=$(expr 3 - $attemptCount)

if [ $attemptCount -gt 3 ]; then
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "You have already used up all three attempts!"
	echo "Therefore, this submission will be ignored."
	echo "The result of your third submission is your final result."
	echo "	"
	echo "###############################################################################"
	exit 1
else

	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "After this submission, you have $attemptsLeft attempts left."
	echo "	"
	echo "###############################################################################"
fi
