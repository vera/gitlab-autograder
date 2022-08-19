# GitLab Autograder: Skripte

## `step1_create_submission_groups.py`

Mit diesem Skript können automatisch die „Abgaben“-Untergruppen angelegt werden. Dafür wird eine CSV-Datei benötigt, die pro Gruppe eine Zeile enthält. Aktuell wird dabei Datei mit den Spalten „Vorname“, „Nachname“ und „E-Mail-Adresse“ erwartet, wie sie von Moodle erzeugt wird. Diese Spalten werden zur Benennung der Gruppe verwendet. Das Skript kann aber leicht angepasst werden, so dass es andere Spalten erwartet bzw. die Gruppen anders benennt.

Folgende Werte müssen im Skript ersetzt werden:

- `<YOUR_CSV_FILE>` (Pfad der CSV-Datei)
- `<YOUR_SUBMISSION_GROUP_ID>` (ID der Gruppe „Abgaben“)
- `<YOUR_GITLAB_TOKEN>` (GitLab-Token, das das Anlegen von Untergruppen erlaubt)
- `<YOUR_GITLAB_URL>` (URL der GitLab-Instanz)

## `step2_add_members_to_submission_groups.py`

Mit diesem Skript können automatisch Mitglieder zu den „Abgaben“-Untergruppen hinzugefügt werden. Das Skript ist aktuell dafür ausgelegt, dass jede Gruppe nur ein Mitglied erhält und der Name des Mitglieds im „path“-Attribut der Gruppe zu finden ist (das ist der Fall, wenn die Gruppe mit dem Skript von oben angelegt wurde). Da die verwendete GitLab-Instanz leider keine Möglichkeit bot, einen Nutzer eindeutig zu identifieren und zu suchen, gibt das Skript alle Kandidaten auf der Ausgabe aus und erwartet dann eine Eingabe. Der Nutzer wird nur hinzugefügt, wenn die Eingabe „y“ erfolgt. Ob es sich beim Nutzer um den korrekten handelt, muss manuell überprüft werden.

Folgende Werte müssen im Skript ersetzt werden:

- `<YOUR_SUBMISSION_GROUP_ID>` (ID der Gruppe „Abgaben“)
- `<YOUR_GITLAB_TOKEN>` (GitLab-Token, das das Anlegen von Untergruppen erlaubt)
- `<YOUR_GITLAB_URL>` (URL der GitLab-Instanz)

## `step3_create_forks.py` und `step3_create_forks.sh`

Mit diesem Python-Skript kann ein Aufgaben-Repository in alle „Abgaben“-Untergruppen geforkt werden. Die IDs der „Abgaben“-Gruppe und des zu forkenden Projekts werden dabei als Programmparameter erwartet (d.h. ein Aufruf soll so aussehen: `python3 create_forks.py <SUBMISSION_GROUP_ID> <PROJECT_TO_FORK>`).

Folgende Werte müssen im Skript ersetzt werden:

- `<YOUR_GITLAB_TOKEN>` (GitLab-Token, das das Anlegen von Untergruppen erlaubt)
- `<YOUR_GITLAB_URL>` (URL der GitLab-Instanz)

Das Skript kann in einem Cronjob verwendet werden, um Aufgaben zu einem bestimmten Termin automatisch freizuschalten. Dafür gibt es zusätzlich noch das Shell-Skript `step3_create_forks.sh`. Um dieses Skript mit cron zu nutzen, muss vorher ein virtuelles Environment in Python in `.venv` angelegt werden (`python3 -m venv .venv`) und darin das Paket `requests` installiert werden. Dann kann dieses Skript in Cronjobs verwendet werden, z.B. so:

```
00 00 19 05 * <YOUR_SCRIPT_PATH>/create_forks.sh <YOUR_SUBMISSION_GROUP_ID> <YOUR_PROJECT_TO_FORK>
```

Diese Zeile muss in die cron-Tabelle eingetragen werden. Die kann z.B. mit dem Befehl `crontab -e` bearbeitet werden. Uhrzeit, Datum, Pfad zur .sh-Datei und die Gruppen-IDs müssen natürlich angepasst werden.

Das Skript legt eine Log-Datei an.

Folgende Werte müssen im Shell-Skript ersetzt werden:

- `<YOUR_SCRIPT_PATH>` (Pfad des Python-Skripts und des venvs)
- `<YOUR_LOG_PATH>` (Pfad, unter dem die Log-Datei angelegt werden soll)

(Beide Pfade können übereinstimmen.)

## `step4_gather_results.py`

Mit diesem Skript können die Ergebnisse einer einzelnen Programmieraufgabe aus GitLab exportiert werden. Das Skript gibt die exportierten Ergebnisse auf der Standardausgabe aus und speichert sie außerdem für weitere Verwendung in einer SQLite3-Datenbank (einer SQL-Datenbank, die aus einer einzigen Datei besteht). Das Skript erwartet die Nummer der Aufgabe als Programmparameter. Außerdem wird erwartet, dass die Aufgaben-Repositories nach dem Schema „`<NUMMER>. <NAME>`“ benannt wurden, d.h. dass ihre Pfade „`<NUMMER>-<NAME>`“ lauten. Falls das nicht der Fall ist, muss Zeile 46 angepasst werden.

Folgende Werte müssen im Skript ersetzt werden:

- `<YOUR_GITLAB_TOKEN>` (GitLab-Token, das das Anlegen von Untergruppen erlaubt)
- `<YOUR_GITLAB_URL>` (URL der GitLab-Instanz)
- `<YOUR_DB_FILE_PATH>` (Pfad, unter dem die SQLite3-Datenbank angelegt werden soll)

## `step5_generate_pass_fail_csv.py`

Mit diesem Skript können die finalen Ergebnisse aller Programmieraufgaben ausgewertet werden. Es prüft, ob eine Mindestanzahl an Programmieraufgaben erfolgreich bearbeitet wurde. Dafür muss zunächst jede einzelne Programmieraufgabe mit dem oben beschriebenen Skript `step4_gather_results.py` ausgewertet worden sein. Das Skript gibt die Ergebnisse auf der Standardausgabe in CSV-Format aus. Sie können z.B. in eine CSV-Datei umgeleitet werden und dann bei Moodle importiert werden.

Folgende Werte müssen im Skript ersetzt werden:

- `<YOUR_DB_FILE_PATH>` (Pfad, unter dem die SQLite3-Datenbank mit den Ergebnissen der Aufgaben liegt)
- `<EXERCISES_REQUIRED_TO_PASS>` (Anzahl der Aufgaben, die für das Bestehen erfolgreich gelöst sein müssen)
- `<EMAIL_SUFFIX>` (Suffix, der an Nutzernamen angehängt werden soll (z.B. für Moodle-Import erforderlich); kann auch leer sein)
