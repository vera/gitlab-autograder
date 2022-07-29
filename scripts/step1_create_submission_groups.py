import csv
import requests

STUDENTS_CSV = "<YOUR_CSV_FILE>"
SUBMISSION_GROUP_ID = <YOUR_SUBMISSION_GROUP_ID>
GITLAB_TOKEN = "<YOUR_GITLAB_TOKEN>"

with open(STUDENTS_CSV) as csv_file:
	csv_reader = csv.DictReader(csv_file, delimiter=',')
	for row in csv_reader:
		data = {
			"parent_id": SUBMISSION_GROUP_ID,
			"name": row["Vorname"] + " " + row["Nachname"],
			"path": row["E-Mail-Adresse"].split("@")[0],
			"default_branch_protection": 1,
			"project_creation_level": "maintainer",
			"visibility": "private"
		}
		r = requests.post("https://<YOUR_GITLAB_URL>/api/v4/groups", headers = { "PRIVATE-TOKEN": GITLAB_TOKEN }, data = data)
		if r.status_code == 201:
			print("Created group for", row["Vorname"], row["Nachname"])
		else:
			print("Failed to create group for", row["Vorname"], row["Nachname"])
			print(r.text)
