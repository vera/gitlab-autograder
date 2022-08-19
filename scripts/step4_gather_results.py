import sqlite3
import requests
import sys
from collections import Counter

SUBMISSION_GROUP_ID = <YOUR_SUBMISSION_GROUP_ID>
GITLAB_TOKEN = "<YOUR_GITLAB_TOKEN>"
GITLAB_URL = "https://<YOUR_GITLAB_URL>"
DATABASE_FILE_PATH = "<YOUR_DB_FILE_PATH>"

if len(sys.argv) < 2:
	sys.stderr.write("Usage: python3 step4_gather_results.py EXERCISE_NUMBER\n")
	sys.exit(1)

EXERCISE = int(sys.argv[1])

conn = sqlite3.connect(DATABASE_FILE_PATH)
cur = conn.cursor()
try:
	# cur.execute("DROP TABLE results")
	cur.execute("CREATE TABLE results (student_name text, student_username text, exercise integer, passed integer, failed_job text)")
except sqlite3.OperationalError as e:
	print("ERROR creating table: %s" % e)

results = []
total = 0
total_passed = 0
total_attempted = 0
failed_jobs = Counter()

page = 1
while True:
	r1 = requests.get(GITLAB_URL + "/api/v4/groups/%d/subgroups?page=%d" % (SUBMISSION_GROUP_ID, page), headers = { "PRIVATE-TOKEN": GITLAB_TOKEN })

	for student_group in r1.json():
		student_name = student_group["name"]
		student_username = student_group["path"]
		if "." not in student_username:
			continue
		total += 1

		while True:
			try:
				r2 = requests.get(GITLAB_URL + "/api/v4/groups/%d/projects" % student_group["id"], headers = { "PRIVATE-TOKEN": GITLAB_TOKEN })
				for project in r2.json():
					exercise_num = int(project["path"].split("-")[0])
					if exercise_num != EXERCISE:
						continue
					result_exists = (cur.execute("SELECT COUNT(*) FROM results WHERE student_name = ? AND exercise = ?", (student_name, exercise_num)).fetchone()[0] > 0)
					if not result_exists:
						r3 = requests.get(GITLAB_URL + "/api/v4/projects/%d/pipelines?status=success" % project["id"], headers = { "PRIVATE-TOKEN": GITLAB_TOKEN })
						passed = (len(r3.json()) > 0)
						failed_job_name = None
						if not passed:
							jobs_page = 1
							while True:
								r4 = requests.get(GITLAB_URL + "/api/v4/projects/%d/jobs?scope=failed&per_page=1&page=%d" % (project["id"], jobs_page), headers = { "PRIVATE-TOKEN": GITLAB_TOKEN })
								if len(r4.json()) > 0:
									failed_job_name = r4.json()[0]["name"]
									if not (failed_job_name == "Versuchsanzahl-Check" or failed_job_name == "Deadline-Check"):
										failed_jobs.update({ failed_job_name: 1 })
										total_attempted += 1
										break

								if r4.headers["X-Next-Page"] == "":
									break

								jobs_page += 1
						else:
							total_passed += 1
							total_attempted += 1
						result = (student_name, student_username, exercise_num, passed, failed_job_name)
						cur.execute("INSERT INTO results VALUES (?, ?, ?, ?, ?)", result)
						print(result)
			except requests.exceptions.ConnectionError:
				continue
			break

	if r1.headers["X-Next-Page"] == "":
		break
	page += 1

print("Attempted: %d/%d" % (total_attempted, total))
print("Passed: %d/%d" % (total_passed, total))
print("Failed jobs: %s" % (failed_jobs))

conn.commit()
conn.close()
