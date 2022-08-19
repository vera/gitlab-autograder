import csv
import requests
import sys

GITLAB_TOKEN = "<YOUR_GITLAB_TOKEN>"
GITLAB_URL = "https://<YOUR_GITLAB_URL>"

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("Usage: python3 step3_create_forks.py SUBMISSION_GROUP_ID PROJECT_TO_FORK")
		sys.exit(1)

	SUBMISSION_GROUP_ID = sys.argv[1]
	PROJECT_TO_FORK = sys.argv[2]

	page = 1
	while True:
		r = requests.get(GITLAB_URL + "/api/v4/groups/" + str(SUBMISSION_GROUP_ID) + "/subgroups?page=" + str(page), headers = { "PRIVATE-TOKEN": GITLAB_TOKEN })

		for student_group in r.json():
			data = {
				"namespace_path": student_group["full_path"],
				"visibility": "private"
			}
			r2 = requests.post(GITLAB_URL + "/api/v4/projects/" + str(PROJECT_TO_FORK) + "/fork", headers = { "PRIVATE-TOKEN": GITLAB_TOKEN }, data = data)
			if r2.status_code == 201:
				print("Created fork for", student_group["name"])
			else:
				print("Failed to create fork for", student_group["name"])
				print(r2.text)

		if r.headers["X-Next-Page"] == "":
			break
		page += 1
