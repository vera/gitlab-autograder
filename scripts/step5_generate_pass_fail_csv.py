import sqlite3

DATABASE_FILE_PATH = "<YOUR_DB_FILE_PATH>"
EXERCISES_REQUIRED_TO_PASS = <YOUR_NUMBER>
EMAIL_SUFFIX = "<YOUR_SUFFIX>"

conn = sqlite3.connect(DATABASE_FILE_PATH)
cur = conn.cursor()

try:
	res = cur.execute("SELECT student_username, SUM(passed) AS exercises_passed FROM results GROUP BY student_username")
	rows = res.fetchall()
	for row in rows:
		print(row[0] + EMAIL_SUFFIX + "," + ("1" if row[1] >= EXERCISES_REQUIRED_TO_PASS else "0"))
except sqlite3.OperationalError as e:
	print("ERROR querying table: %s" % e)
