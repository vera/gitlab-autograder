import csv
import requests
import sys

SUBMISSION_GROUP_ID = <YOUR_SUBMISSION_GROUP_ID>
GITLAB_TOKEN = "<YOUR_GITLAB_TOKEN>"
GITLAB_URL = "https://<YOUR_GITLAB_URL>"

for group_id in SUBMISSION_GROUP_ID:
	found = 0
	found_new = 0
	print()
	page = 1
	while True:
		r = requests.get(GITLAB_URL + "/api/v4/groups/" + str(group_id) + "/subgroups?page=" + str(page), headers = { "PRIVATE-TOKEN": GITLAB_TOKEN })

		for student_group in r.json():
			if not "." in str(student_group["path"]):
				continue

			while True:
				try:
					r3 = requests.get(GITLAB_URL + "/api/v4/groups/" + str(student_group["id"]) + "/members", headers = { "PRIVATE-TOKEN": GITLAB_TOKEN })
				except requests.exceptions.ConnectionError:
					sys.stderr.write("Connection error occured when adding member to group %s\n" % student_group["name"])
					continue
				break

			if r3.status_code == 200 and len(r3.json()) > 1:
				found += 1
				sys.stderr.write("Student user already added to group %s\n" % student_group["name"])
				continue

			while True:
				try:
					r2 = requests.get(GITLAB_URL + "/api/v4/users?search=" + str(student_group["path"]).replace(".", "+"), headers = { "PRIVATE-TOKEN": GITLAB_TOKEN })
				except requests.exceptions.ConnectionError:
					sys.stderr.write("Connection error occured when finding user for %s\n" % student_group["name"])
					continue
				break

			users = r2.json()
			if users == []:
				sys.stderr.write("Failed to find user for %s\n" % student_group["name"])
			else:
				for u in users:
					data = {
						"user_id": u["id"],
						"access_level": 30 # Developer
					}
					print("Candidate user for %s: %s" % (student_group["name"], u))
					answer = input("Add this user? (yN) ")
					if answer == "y":
						found += 1
						while True:
							try:
								r3 = requests.post(GITLAB_URL + "/api/v4/groups/" + str(student_group["id"]) + "/members", headers = { "PRIVATE-TOKEN": GITLAB_TOKEN }, data = data)
							except requests.exceptions.ConnectionError:
								sys.stderr.write("Connection error occured when adding member to group %s\n" % student_group["name"])
								continue
							break

						if r3.status_code == 201:
							found_new += 1
							print("Added member to group", student_group["name"])
						elif not ("message" in r3.json() and r3.json()["message"] == "Member already exists"):
							sys.stderr.write("Failed to add member to group %s: %s\n" % (student_group["name"], r3.text))

		if r.headers["X-Next-Page"] == "":
			break
		page += 1

	print("Found users: %d (%d new)" % (found, found_new))
