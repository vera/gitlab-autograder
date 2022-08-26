if python3 -m unittest VerificationTestSuite.py &> /dev/null; then
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "CONGRATULATIONS!"
	echo "	"
	echo "Your solution has passed all of the tests!"
	echo "	"
	echo "###############################################################################"
else
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Your solution is not correct. It doesn't pass all of our test cases."
	echo "	"
	echo "Your solution must also work with inputs other than the sample inputs from the task description!" | fold -s
	echo "	"
	echo "HINT: Think of a few new test cases yourself, add them to the test suite and use that to test your solution further." | fold -s
	echo "	"
	echo "###############################################################################"
	exit 1
fi
