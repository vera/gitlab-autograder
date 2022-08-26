if ! python3 -m unittest StudentTestSuite.py &> /dev/null; then
	echo "	"
	echo "###############################################################################"
	echo "	"
	echo "Your solution is not correct! It doesn't pass all test cases in the public student test suite." | fold -s
	echo "	"
	echo "HINT: *Always* test your solution yourself before uploading it! To do this, execute the following command in the directory that contains both the student test suite and your solution file:" | fold -s
	echo "	"
	echo "	python3 -m unittest StudentTestSuite.py"
	echo "	"
	echo "###############################################################################"
	exit 1
fi
